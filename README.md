# fast20-yang
## 运行步骤
1. `cd OptaneStudy/src/testscript`
2. `sudo /mount.sh [RepFS] [LatFS]`
3. 运行 script.py
4. dmesg -T > logdat.txt 裁剪只保留之前运行的结果
5. 运行 plot.py绘图