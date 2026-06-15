#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BveTs Map 文件 Station 命令提取工具
拖动文件到本脚本上即可自动提取 Station 命令及其里程
输出文件保存在脚本所在目录
"""

import sys
import os


def extract_stations(filepath):
    """
    从 BveTs Map 文件中提取 Station 命令及其里程
    """
    results = []
    current_distance = None

    # 编码尝试顺序：优先尝试 UTF-8（含 BOM），因为 BveTs Map 文件通常是 UTF-8
    # utf-16-le/be 可能会"成功"读取但产生乱码，所以放在后面
    encodings = ['utf-8-sig', 'utf-8', 'shift-jis', 'gbk', 'utf-16', 'utf-16-le', 'utf-16-be']
    content = None

    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            # 额外验证：检查是否能找到预期的 Station 关键字
            # 如果找不到，可能是编码错误导致的乱码，继续尝试下一个编码
            if "Station" in content:
                break
        except (UnicodeError, UnicodeDecodeError):
            continue

    if content is None:
        raise ValueError(f"无法解码文件: {filepath}")

    lines = content.splitlines()

    for line in lines:
        stripped = line.strip()

        # 检查是否是里程标记（纯数字或以分号结尾的数字）
        if stripped and stripped.rstrip(';').isdigit():
            current_distance = int(stripped.rstrip(';'))

        # 检查是否包含 Station['xxx'].Put
        if "Station['" in stripped and "].Put(" in stripped:
            results.append((current_distance, stripped))

    return results


def main():
    # 脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取拖放的文件路径（支持多个文件）
    files = sys.argv[1:]

    if not files:
        print("请将 BveTs Map 文件拖动到本脚本上")
        input("按回车键退出...")
        sys.exit(1)

    for filepath in files:
        filepath = filepath.strip()

        if not os.path.exists(filepath):
            print(f"错误: 文件不存在: {filepath}")
            continue

        try:
            results = extract_stations(filepath)
        except Exception as e:
            print(f"处理文件失败 [{filepath}]: {e}")
            continue

        # 生成输出文件名：原文件名 + _stations.txt，保存在脚本目录
        basename = os.path.splitext(os.path.basename(filepath))[0]
        output_path = os.path.join(script_dir, basename + '_stations.txt')

        # 写入结果
        with open(output_path, 'w', encoding='utf-8') as f:
            for distance, line in results:
                f.write(f"{distance}: {line}\n")

        print(f"[{os.path.basename(filepath)}] -> 提取 {len(results)} 条记录")
        print(f"结果已保存: {output_path}")

    input("\n按回车键退出...")


if __name__ == '__main__':
    main()