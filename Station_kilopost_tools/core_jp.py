#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BveTs Map ファイル Station コマンド抽出ツール
ファイルを本スクリプトにドラッグ＆ドロップすると、Station コマンドとその距離程を自動抽出します
出力ファイルはスクリプトと同じディレクトリに保存されます
"""

import sys
import os


def extract_stations(filepath):
    """
    BveTs Map ファイルから Station コマンドとその距離程を抽出する
    """
    results = []
    current_distance = None

    # 文字コード試行順序：UTF-8（BOM 含む）を優先して試行。BveTs Map ファイルは通常 shift-jisとUTF-8
    # utf-16-le/be は「成功」するが文字化けする可能性があるため後方に配置
    encodings = ['utf-8-sig', 'utf-8', 'shift-jis', 'gbk', 'utf-16', 'utf-16-le', 'utf-16-be']
    content = None

    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            # 追加検証："Station" キーワードが含まれているか確認
            # 含まれない場合は文字化けの可能性があるため、次の文字コードを試行
            if "Station" in content:
                break
        except (UnicodeError, UnicodeDecodeError):
            continue

    if content is None:
        raise ValueError(f"ファイルをデコードできません: {filepath}")

    lines = content.splitlines()

    for line in lines:
        stripped = line.strip()

        # 距離程マーカーかどうかを確認（純粋な数字、またはセミコロンで終わる数字）
        if stripped and stripped.rstrip(';').isdigit():
            current_distance = int(stripped.rstrip(';'))

        # Station['xxx'].Put を含むかどうかを確認
        if "Station['" in stripped and "].Put(" in stripped:
            results.append((current_distance, stripped))

    return results


def main():
    # スクリプトのあるディレクトリ
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # ドラッグ＆ドロップされたファイルパスを取得（複数ファイル対応）
    files = sys.argv[1:]

    if not files:
        print("BveTs Map ファイルを本スクリプトにドラッグ＆ドロップしてください")
        input("Enter キーを押して終了...")
        sys.exit(1)

    for filepath in files:
        filepath = filepath.strip()

        if not os.path.exists(filepath):
            print(f"エラー: ファイルが存在しません: {filepath}")
            continue

        try:
            results = extract_stations(filepath)
        except Exception as e:
            print(f"ファイルの処理に失敗しました [{filepath}]: {e}")
            continue

        # 出力ファイル名：元のファイル名 + _stations.txt、スクリプトのディレクトリに保存
        basename = os.path.splitext(os.path.basename(filepath))[0]
        output_path = os.path.join(script_dir, basename + '_stations.txt')

        # 結果を書き込み
        with open(output_path, 'w', encoding='utf-8') as f:
            for distance, line in results:
                f.write(f"{distance}: {line}\n")

        print(f"[{os.path.basename(filepath)}] -> {len(results)} 件のレコードを抽出")
        print(f"結果を保存しました: {output_path}")

    input("\nEnter キーを押して終了...")


if __name__ == '__main__':
    main()