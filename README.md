# TIMS生成器
[日本語readme](Readme_JP.md "日本語readme")

[下载地址](https://github.com/njfdCRH1A/TIMS-Excel/raw/refs/heads/main/TIMS_tool_v2.xlsx "下载地址")
## 2026/6/15更新
vibe coding（？）了个[python脚本文件](Station_kilopost_tools/ "python脚本文件")提取车站里程
将这个文件夹中的所有内容下载后将线路文件（以BVETS MAP 2.00开头的文件）拖放至bat文件即可自动提取，支持批量提取，结果保存在bat同目录下以“源文件名+stations.txt”命名。

运行环境准备：你需要安装[python](https://www.python.org/ "python")并设置好环境变量
原理：bat文件负责把文件丢给core.py，由core.py处理好文件后输出结果，至于core.py是怎么实现的我没仔细看（）反正是vibecoding出来的东西能跑就行（（（
如果车站里程另存于其它的文件，以及车站里程包括变量的话，程序无法提取这类车站里程，用@zbx1425制作的[QMV](https://www.zbx1425.cn/nautilus/quickmap/index.zh-CN.html "QMV")查看车站里程罢（逃
## 文件概览
M电时刻表编辑区
![](readme/M_Staff.png)
(时刻表为那須野氏制作的JR宇都宮線3523M快速ラピット)
E电时刻表编辑区
![](readme/E_Staff.png)
(时刻表为822sty氏制作的JR中央線1160T特別快速)
## 使用方法：
**无论使用M电还是E电，车站里程、车站TIMS图像编号、到达时间、发车（通过时间）都是必填项，否则结果将会出错**
### I、编辑M电时刻表（列车时刻表）
#### 1、输入数据
![](readme/M_Necessary.png)
图中所有用红框圈起来的地方都是必填项，注意到除了上述提到的必填项外，还必须填入通过站（时间栏显示“↓”）、停车站（时间栏显示“停”）、终到站（时间栏显示“=”）对应的图像编号，以及显示0点/0时/0分时时/分/秒各自对应的图像编号
![](readme/ME_Staname_Time.png)
时间和站名可以直接从stationlist文件复制，表格可以自动提取时间并转换为TIMS显示格式，站名不影响相关数据的计算，仅起到方便对照的作用。

此外还可以根据需要填写车站股道，进出站限速，站间用时。站间用时如果不填写，则将自动计算当前行的发车时间和下一行的到达时间之差，如果需要可以在站间用时一栏按照hh: mm: ss的格式填写
#### 2、生成结果
观察下面的书签选项，第一个表格为M电时刻表输入，第二个表格为E电时刻表输入，在第二个表格之后就是表格自动计算生成的结果。标签带(M)的即M电时刻表生成结果。选中生成的结果复制到你正在编辑的TIMS时刻表中。
![书签选项](readme/ME_INPUT_OUTPUT.png "书签选项")

以M电站名表示为例，首先选中下图所示表格

![](readme/copy1.png)

选择生成结果

![](readme/copy2.png)

复制到正在编辑的TIMS文件中即可

![](readme/copy3.png)

同理，车站时刻、股道等也如法炮制复制到正在编辑的TIMS文件中
最终TIMS文件应该是这样的：
```
BveTs Map 2.00
#TIMS駅名表示						
#列車スタフ						
3790;	Beacon.Put(110,0,1050);	Beacon.Put(110,0,2051);	Beacon.Put(110,0,3052);	Beacon.Put(110,0,4053);	Beacon.Put(110,0,5065);	Beacon.Put(110,0,6066);
6875+25;	Beacon.Put(110,0,1051);	Beacon.Put(110,0,2052);	Beacon.Put(110,0,3053);	Beacon.Put(110,0,4065);	Beacon.Put(110,0,5066);	Beacon.Put(110,0,6067);
8460+25;	Beacon.Put(110,0,1052);	Beacon.Put(110,0,2053);	Beacon.Put(110,0,3065);	Beacon.Put(110,0,4066);	Beacon.Put(110,0,5067);	Beacon.Put(110,0,6069);
13240+25;	Beacon.Put(110,0,1053);	Beacon.Put(110,0,2065);	Beacon.Put(110,0,3066);	Beacon.Put(110,0,4067);	Beacon.Put(110,0,5069);	Beacon.Put(110,0,6070);
15880+25;	Beacon.Put(110,0,1065);	Beacon.Put(110,0,2066);	Beacon.Put(110,0,3067);	Beacon.Put(110,0,4069);	Beacon.Put(110,0,5070);	Beacon.Put(110,0,6072);
24240+25;	Beacon.Put(110,0,1066);	Beacon.Put(110,0,2067);	Beacon.Put(110,0,3069);	Beacon.Put(110,0,4070);	Beacon.Put(110,0,5072);	Beacon.Put(110,0,6073);
（下略）
#TIMS時刻設定												
#列車スタフ												
3790;	Beacon.Put(111,0,1075660);	Beacon.Put(111,0,2250000);	Beacon.Put(111,0,3250000);	Beacon.Put(111,0,4000760);	Beacon.Put(111,0,5250000);	Beacon.Put(111,0,6001660);	Beacon.Put(112,0,1075860);	Beacon.Put(112,0,2080130);	Beacon.Put(112,0,3000245);	Beacon.Put(112,0,4000745);	Beacon.Put(112,0,5000945);	Beacon.Put(112,0,6001630);
6875+25;	Beacon.Put(111,0,1250000);	Beacon.Put(111,0,2250000);	Beacon.Put(111,0,3000760);	Beacon.Put(111,0,4250000);	Beacon.Put(111,0,5001660);	Beacon.Put(111,0,6250000);	Beacon.Put(112,0,1080130);	Beacon.Put(112,0,2000245);	Beacon.Put(112,0,3000745);	Beacon.Put(112,0,4000945);	Beacon.Put(112,0,5001630);	Beacon.Put(112,0,6001945);
8460+25;	Beacon.Put(111,0,1250000);	Beacon.Put(111,0,2000760);	Beacon.Put(111,0,3250000);	Beacon.Put(111,0,4001660);	Beacon.Put(111,0,5250000);	Beacon.Put(111,0,6002260);	Beacon.Put(112,0,1000245);	Beacon.Put(112,0,2000745);	Beacon.Put(112,0,3000945);	Beacon.Put(112,0,4001630);	Beacon.Put(112,0,5001945);	Beacon.Put(112,0,6002360);
13240+25;	Beacon.Put(111,0,1000760);	Beacon.Put(111,0,2250000);	Beacon.Put(111,0,3001660);	Beacon.Put(111,0,4250000);	Beacon.Put(111,0,5002260);	Beacon.Put(111,0,6250000);	Beacon.Put(112,0,1000745);	Beacon.Put(112,0,2000945);	Beacon.Put(112,0,3001630);	Beacon.Put(112,0,4001945);	Beacon.Put(112,0,5002360);	Beacon.Put(112,0,6002545);
15880+25;	Beacon.Put(111,0,1250000);	Beacon.Put(111,0,2001660);	Beacon.Put(111,0,3250000);	Beacon.Put(111,0,4002260);	Beacon.Put(111,0,5250000);	Beacon.Put(111,0,6250000);	Beacon.Put(112,0,1000945);	Beacon.Put(112,0,2001630);	Beacon.Put(112,0,3001945);	Beacon.Put(112,0,4002360);	Beacon.Put(112,0,5002545);	Beacon.Put(112,0,6002715);
24240+25;	Beacon.Put(111,0,1001660);	Beacon.Put(111,0,2250000);	Beacon.Put(111,0,3002260);	Beacon.Put(111,0,4250000);	Beacon.Put(111,0,5250000);	Beacon.Put(111,0,6002945);	Beacon.Put(112,0,1001630);	Beacon.Put(112,0,2001945);	Beacon.Put(112,0,3002360);	Beacon.Put(112,0,4002545);	Beacon.Put(112,0,5002715);	Beacon.Put(112,0,6003015);
（下略）
#TIMS到着番線						
#列車スタフ						
3790;	Beacon.Put(113,0,100);	Beacon.Put(113,0,200);	Beacon.Put(113,0,300);	Beacon.Put(113,0,400);	Beacon.Put(113,0,500);	Beacon.Put(113,0,600);
6875+25;	Beacon.Put(113,0,100);	Beacon.Put(113,0,200);	Beacon.Put(113,0,300);	Beacon.Put(113,0,400);	Beacon.Put(113,0,500);	Beacon.Put(113,0,600);
8460+25;	Beacon.Put(113,0,100);	Beacon.Put(113,0,200);	Beacon.Put(113,0,300);	Beacon.Put(113,0,400);	Beacon.Put(113,0,500);	Beacon.Put(113,0,600);
13240+25;	Beacon.Put(113,0,100);	Beacon.Put(113,0,200);	Beacon.Put(113,0,300);	Beacon.Put(113,0,400);	Beacon.Put(113,0,500);	Beacon.Put(113,0,600);
15880+25;	Beacon.Put(113,0,100);	Beacon.Put(113,0,200);	Beacon.Put(113,0,300);	Beacon.Put(113,0,400);	Beacon.Put(113,0,500);	Beacon.Put(113,0,600);
24240+25;	Beacon.Put(113,0,100);	Beacon.Put(113,0,200);	Beacon.Put(113,0,300);	Beacon.Put(113,0,400);	Beacon.Put(113,0,500);	Beacon.Put(113,0,600);
（下略）
#TIMS次駅設定					
#列車スタフ					
3790;				Beacon.Put(106,0,050053);	Beacon.Put(107,0,000760);
6875;	$dis=distance;$dis-500;	Beacon.Put(30,0,-1);	Beacon.Put(105,0,-498);	Beacon.Put(106,0,051053);	Beacon.Put(107,0,000760);
8460;	$dis=distance;$dis-500;	Beacon.Put(30,0,-1);	Beacon.Put(105,0,-498);	Beacon.Put(106,0,052053);	Beacon.Put(107,0,000760);
13240;	$dis=distance;$dis-500;	Beacon.Put(30,0,500);	Beacon.Put(105,0,498);	Beacon.Put(106,0,053066);	Beacon.Put(107,0,001660);
15880;	$dis=distance;$dis-500;	Beacon.Put(30,0,-1);	Beacon.Put(105,0,-498);	Beacon.Put(106,0,065066);	Beacon.Put(107,0,001660);
24240;	$dis=distance;$dis-500;	Beacon.Put(30,0,500);	Beacon.Put(105,0,498);	Beacon.Put(106,0,066069);	Beacon.Put(107,0,002260);
（下略）
#TIMS制限速度&駅間時間																		
#列車スタフ																		
3790;	Beacon.Put(114,0,100);	Beacon.Put(114,0,200);	Beacon.Put(114,0,300);	Beacon.Put(114,0,400);	Beacon.Put(114,0,500);	Beacon.Put(114,0,600);	Beacon.Put(115,0,130);	Beacon.Put(115,0,260);	Beacon.Put(115,0,300);	Beacon.Put(115,0,400);	Beacon.Put(115,0,500);	Beacon.Put(115,0,600);	Beacon.Put(116,0,10330);	Beacon.Put(116,0,20115);	Beacon.Put(116,0,30415);	Beacon.Put(116,0,40200);	Beacon.Put(116,0,50615);	Beacon.Put(116,0,60315);
6875+25;	Beacon.Put(114,0,100);	Beacon.Put(114,0,200);	Beacon.Put(114,0,300);	Beacon.Put(114,0,400);	Beacon.Put(114,0,500);	Beacon.Put(114,0,600);	Beacon.Put(115,0,160);	Beacon.Put(115,0,200);	Beacon.Put(115,0,300);	Beacon.Put(115,0,400);	Beacon.Put(115,0,500);	Beacon.Put(115,0,600);	Beacon.Put(116,0,10115);	Beacon.Put(116,0,20415);	Beacon.Put(116,0,30200);	Beacon.Put(116,0,40615);	Beacon.Put(116,0,50315);	Beacon.Put(116,0,60215);
8460+25;	Beacon.Put(114,0,100);	Beacon.Put(114,0,200);	Beacon.Put(114,0,300);	Beacon.Put(114,0,400);	Beacon.Put(114,0,500);	Beacon.Put(114,0,645);	Beacon.Put(115,0,100);	Beacon.Put(115,0,200);	Beacon.Put(115,0,300);	Beacon.Put(115,0,400);	Beacon.Put(115,0,500);	Beacon.Put(115,0,600);	Beacon.Put(116,0,10415);	Beacon.Put(116,0,20200);	Beacon.Put(116,0,30615);	Beacon.Put(116,0,40315);	Beacon.Put(116,0,50215);	Beacon.Put(116,0,60245);
13240+25;	Beacon.Put(114,0,100);	Beacon.Put(114,0,200);	Beacon.Put(114,0,300);	Beacon.Put(114,0,400);	Beacon.Put(114,0,545);	Beacon.Put(114,0,600);	Beacon.Put(115,0,100);	Beacon.Put(115,0,200);	Beacon.Put(115,0,300);	Beacon.Put(115,0,400);	Beacon.Put(115,0,500);	Beacon.Put(115,0,600);	Beacon.Put(116,0,10200);	Beacon.Put(116,0,20615);	Beacon.Put(116,0,30315);	Beacon.Put(116,0,40215);	Beacon.Put(116,0,50245);	Beacon.Put(116,0,60130);
15880+25;	Beacon.Put(114,0,100);	Beacon.Put(114,0,200);	Beacon.Put(114,0,300);	Beacon.Put(114,0,445);	Beacon.Put(114,0,500);	Beacon.Put(114,0,600);	Beacon.Put(115,0,100);	Beacon.Put(115,0,200);	Beacon.Put(115,0,300);	Beacon.Put(115,0,400);	Beacon.Put(115,0,500);	Beacon.Put(115,0,600);	Beacon.Put(116,0,10615);	Beacon.Put(116,0,20315);	Beacon.Put(116,0,30215);	Beacon.Put(116,0,40245);	Beacon.Put(116,0,50130);	Beacon.Put(116,0,60230);
24240+25;	Beacon.Put(114,0,100);	Beacon.Put(114,0,200);	Beacon.Put(114,0,345);	Beacon.Put(114,0,400);	Beacon.Put(114,0,500);	Beacon.Put(114,0,600);	Beacon.Put(115,0,100);	Beacon.Put(115,0,200);	Beacon.Put(115,0,300);	Beacon.Put(115,0,400);	Beacon.Put(115,0,500);	Beacon.Put(115,0,600);	Beacon.Put(116,0,10315);	Beacon.Put(116,0,20215);	Beacon.Put(116,0,30245);	Beacon.Put(116,0,40130);	Beacon.Put(116,0,50230);	Beacon.Put(116,0,60300);
（下略）
```
### II、编辑E电时刻表（电车时刻表）
操作方法和M电时刻表大致相同，只需注意必须填写红框内的参数即可。
![](readme/E_Necessary.png)
