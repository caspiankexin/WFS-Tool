# -*- coding:utf-8 -*-
'''
@作者：caspian，github：@caspiankexin
制作日期：2021年6月21
请合法使用，作者对此工具产生的结果不负责任
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import gui界面
import os
import jieba
import csv
from matplotlib import cm
from matplotlib import font_manager as fm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl


'''
读取，模式一选项下，项目地址
'''
def projectpath (ui):
    input = ui.lineEdit.text()
    path = str (input)
    return path

'''
读取，模式二选项下，项目地址
'''
def projectpath2 (ui):   #模式二的项目地址文本框
    input = ui.lineEdit.text()
    path = str (input)
    return path

'''
读取，模式二选项下，关键词内容
'''
def keywords1 (ui):   #模式二的项目地址文本框
    input = ui.lineEdit_2.text()
    keywords = str(input)
    return keywords


def run_first ():
    print("模式一启动")

    fuji = projectpath(ui)  # 例如我的项目地址：E:\onedrive\project\语象观察人民日报

    xuhebing = fuji + "\\实际操作\\需合并文件的列表.txt"

    with open(xuhebing, 'r', encoding='UTF-8') as f:
        lines1 = [line1.strip() for line1 in f.readlines()]

    for line1 in lines1:
        a = len(line1)
        b = line1[0:5]
        yuefen = fuji + "\\原始数据\\" + b + "\\" + line1
        nianfen = fuji + "\\原始数据\\" + line1
        if a > 5:
            newstr = yuefen
        else:
            newstr = nianfen

        newstr = newstr  # 需要合并的每一个文件夹
        newfile = fuji + "\\实际操作\\合并后的文件\\" + line1 + "合并后文档.txt"  # 输入合并后文件的存储路径
        paths = []  # 存放文件夹（含子文件夹）下所有文件的路径及名称
        for root, dirs, files in os.walk(newstr):
            for file in files:
                paths.append(os.path.join(root, file).encode('utf-8'))  # 支持中文名称

        # 创建新的文件
        f = open(newfile, 'w', encoding='utf-8')
        # 将之前获取到的文件夹（含子文件夹）下所有文件的路径及名称里的内容写进新建的文件里
        for i in paths:
            for line in open(i, encoding='utf-8'):
                f.writelines(line)
        f.close()  # 保存并关闭新建的文件

    print("所有文件夹都已合并完成。")

    # 打开需要统计的已经合并后的txt文件的汇总好的文件地址的txt列表
    with open(xuhebing, 'r', encoding='UTF-8') as f:  # 这里的open的使用方式看对不对，对比下面na g
        lines = [line.strip() for line in f.readlines()]

    guanjianci = fuji + "\\实际操作\\关键词名单列表.txt"
    with open(guanjianci, 'r', encoding='UTF-8') as f:
        lines2 = [line2.strip() for line2 in f.readlines()]

    guanjiancifuji = fuji + "\\关键词名单"  # 关键词文件父级地址
    xutongjiwenjianfuji = fuji + "\\实际操作\\合并后的文件"  # 需要统计的文件所在的文件夹地址
    cunchuwenjianfuji = fuji + "\\实际操作\\统计后输出"  # 统计后输出的文件所在的文件夹地址

    for line in lines:  # 例如：2020年1月、2020年2月、
        dateline = line
        line = line + "合并后文档"  # 注意这里的，看是否会有问题
        for line2 in lines2:  # 例如：中国政要名单、世界政要名单、

            keyword_lists = []
            values = []

            with open(file=guanjiancifuji + "\\" + line2 + ".txt", encoding='UTF-8') as f:
                nameList = f.read().split('\n')

            newaddress = xutongjiwenjianfuji + "\\" + line + ".txt"
            newfileaddress = cunchuwenjianfuji + "\\" + dateline + line2 + ".csv"  # 输入合并后文件的存储路径
            paths = []  # 存放文件夹（含子文件夹）下所有文件的路径及名称
            oldfile = newaddress  # 输入需要统计的文档的路径
            newfile = newfileaddress  # 统计后数据的保存路径
            with open(file=oldfile, encoding='UTF-8') as f:
                txt = f.read()

            # 向jieba库中加入人名，防止jieba在分词时将人名当作两个词拆分掉
            for name in nameList:
                jieba.add_word(name)

            # 打开表格文件，若表格文件不存在则创建
            # 输出的文件路径也是可以设置的，和之前的修改估计一样
            # 直接输入要存入的路径即可，不过路径中不是“\”而是“/”
            Excel = open(newfile, 'w', newline='')
            writ = csv.writer(Excel)  # 创建一个csv的writer对象用于写每一行内容
            writ.writerow(['名称', '出现次数'])  # 写表格表头

            # 分词
            txt = jieba.lcut(txt)

            # 创建一个字典，用于对词出现次数的统计，键表示词，值表示对应的次数
            counts = {}
            for item in txt:
                for name in nameList:
                    if item == name:
                        counts[name] = counts.get(name, 0) + 1  # 在字典中查询若该字返回次数加一
            # 排序并输出结果
            count = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
            for item in count[:15]:  # 选择打印输出前多少的数据
                print(item)  # 会显示在控制面板上，但不会保存到本地

            item = list(counts.items())  # 将字典转化为列表格式
            item.sort(key=lambda x: x[1], reverse=True)  # 对列表按照第二列进行排序
            for i in item:  # 要确保设置导出的数小于等于可以导出数的最大值！！！！！！这个得解决！！！
                writ.writerow(i)  # 将前几名写入表格，

                keyword_list = i[0]
                num_list = i[1]

                keyword_lists.append(keyword_list)
                values.append(num_list)
            print(dateline + line2 + '统计结果输出成功')
        print(dateline + "的所有选定关键词目录已经统计完成")

        # 以下为可视化，扇形图部分

        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['axes.unicode_minus'] = False

        s = pd.Series(values, index=keyword_lists)  # 修改参数为程序中的两列数据

        labels = s.index
        sizes = s.values

        # explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)  # 突出展示某一部分内容,如果需要启用的话，需要在patches, texts,...这一行的shadow前面加上“explode=explode”

        fig, axes = plt.subplots(figsize=(10, 6), ncols=2)
        # 设置绘图区域大小，

        ax1, ax2 = axes.ravel()

        colors = cm.rainbow(np.arange(len(sizes)) / len(sizes))
        # 让颜色为渐变色样式。colormaps: Paired, autumn, rainbow, gray,spring,Darks
        patches, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.0f%%', shadow=False,
                                            startangle=170, colors=colors,
                                            labeldistance=1.24, pctdistance=1.13, radius=0.4)
        # labeldistance: 控制labels显示的位置
        # pctdistance: 控制百分比显示的位置
        # radius: 控制切片突出的距离

        ax1.axis('equal')

        # 重新设置字体大小
        proptease = fm.FontProperties()
        proptease.set_size(10)
        # 设置字体大小：‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
        plt.setp(autotexts, fontproperties=proptease)
        plt.setp(texts, fontproperties=proptease)

        ax1.set_title(dateline + "内关键词出现的次数", loc='center')

        # ax2 只显示图例（legend）
        ax2.axis('off')
        ax2.legend(patches, labels, loc='center left')

        plt.tight_layout()
        # plt.savefig("pie_shape_ufo.png", bbox_inches='tight')
        plt.savefig(fuji + "\\" + "实际操作/统计后输出/" + dateline + "中关键词出现次数的扇形图.png")
        plt.show(block=False)
        plt.pause(3)  # 3 seconds, I use 1 usually
        plt.close("all")

    '''
    以下部分为，设置散点图，实现“结束弹窗”的功能。
    '''
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.unicode_minus'] = False

    pop_up_x = [14, 1, 1, 14, 2, 2, 2, 2, 2, 2.5, 2.5, 3, 3.5, 4, 4.5, 3, 3.5, 4, 4.5, 4.7, 5, 5, 5, 5, 5, 8, 8, 8, 8,
                8, 8, 8,
                8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
    pop_up_y = [14, 1, 14, 1, 6, 6.5, 7, 7.5, 8, 5.3, 8.5, 5, 5, 5, 5, 9, 9, 9, 8.5, 5.3, 6, 6.5, 7, 7.5, 8, 3, 4, 5, 6,
                7, 8,
                9, 10, 11, 6.5, 7.5, 6, 8, 5.5, 8.5, 5, 9]

    plt.plot(pop_up_x, pop_up_y, 'o')
    plt.title("程序运行完完毕，请关闭所有窗口，查看结果", size=17)  # 给整个图表加上标题
    plt.show()
    print("模式一运行完成，请查看数据")


def run_second ():
    print("模式二启动")
    project = projectpath2(ui)
    keywords = keywords1(ui)
    klist = keywords.split(" ")
    klist = [str(klist[i]) for i in range(len(klist))]

    mergalist = project + "\\实际操作\\需合并文件的列表.txt"

    with open(mergalist, 'r', encoding='UTF-8') as f:
        lines1 = [line1.strip() for line1 in f.readlines()]

    for line1 in lines1:
        a = len(line1)
        b = line1[0:5]
        yuefen = project + "\\原始数据\\" + b + "\\" + line1
        nianfen = project + "\\原始数据\\" + line1
        if a > 5:
            newstr = yuefen
        else:
            newstr = nianfen

        newstr = newstr  # 需要合并的每一个文件夹
        newfile = project + "\\实际操作\\合并后的文件\\" + line1 + "合并后文档.txt"  # 输入合并后文件的存储路径
        paths = []  # 存放文件夹（含子文件夹）下所有文件的路径及名称
        for root, dirs, files in os.walk(newstr):
            for file in files:
                paths.append(os.path.join(root, file).encode('utf-8'))  # 支持中文名称

        # 创建新的文件
        f = open(newfile, 'w', encoding='utf-8')
        # 将之前获取到的文件夹（含子文件夹）下所有文件的路径及名称里的内容写进新建的文件里
        for i in paths:
            for line in open(i, encoding='utf-8'):
                f.writelines(line)
        f.close()  # 保存并关闭新建的文件

    print("所有文件夹都已合并完成。")

    for keyword in klist:  # 输入的多个关键词，循环进行统计。

        # 打开需要统计的已经合并后的txt文件的汇总好的文件地址的txt列表
        with open(project + "\\实际操作\\需合并文件的列表.txt", 'r', encoding='UTF-8') as f:
            lines = [line.strip() for line in f.readlines()]

            firstdata = lines[0]
            lastdata = lines[-1]
            newfpath = project + "\\" + "实际操作/统计后输出/" + firstdata + "-" + lastdata + "中“" + keyword + "”的出现次数.csv"

        Excel = open(newfpath, 'w', newline='')
        writ = csv.writer(Excel)  # 创建一个csv的writer对象用于写每一行内容
        writ.writerow(['日期', '出现次数'])  # 写表格表头
        Excel2 = open(newfpath, 'a+', newline='')
        writ2 = csv.writer(Excel2)  # 创建一个csv的writer对象用于写每一行内容

        date_lists = []
        num_lists = []

        for lines1 in lines:  # 2021年1月，2021年2月。。。。。
            with open(file=project + "\\" + "实际操作" + "\\" + "合并后的文件" + "\\" + lines1 + "合并后文档.txt",
                      encoding='UTF-8') as f:
                txt = f.read()
                nameList = f.read().split('\n')
                jieba.add_word(keyword)

            # 分词
            txt = jieba.lcut(txt)

            # 创建一个字典，用于对词出现次数的统计，键表示词，值表示对应的次数
            counts = {}
            for item in txt:
                if item == keyword:
                    counts[keyword] = counts.get(keyword, 0) + 1  # 在字典中查询若该字返回次数加一
            # 排序并输出结果
            count = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
            for item in count[:15]:  # 选择打印输出前多少的数据
                print(item)  # 会显示在控制面板上，但不会保存到本地

            item = list(counts.items())  # 将字典转化为列表格式
            #    item.sort(key=lambda x: x[1], reverse=True)  # 对列表按照第二列进行排序
            for one in item:  # 要确保设置导出的数小于等于可以导出数的最大值！！！！！！这个得解决！！！
                two = [lines1 if i == keyword else i for i in one]
                writ2.writerow(two)  # 将前几名写入表格，
                date_list = two[0]
                num_list = two[1]
                date_lists.append(date_list)
                num_lists.append(num_list)
            print(keyword + lines1 + '统计结果输出成功')
        print(keyword + "选定时间段内的次数已经成功统计并保存到csv")

        '''
        以下为折线图可视化部分
        '''

        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['axes.unicode_minus'] = False

        x = np.arange(20, 350)
        # l1 = plt.plot(date_lists, num_lists, 'r--', label=keyword)
        # l2 = plt.plot(x2, y2, 'g--', label='type2')
        # l3 = plt.plot(x3, y3, 'b--', label='type3')
        plt.plot(date_lists, num_lists, 'ro-')

        for a, b in zip(date_lists, num_lists):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=13)

        plt.xticks(rotation=20)  # 有时候x轴标签比较长，就会重叠在一起，这里旋转一定角度就能更方便显示，如下图
        plt.xlabel(u'时间段', size=10)  # 设置x轴名
        plt.ylabel(u'出现次数', size=10)  # 设置y轴名
        plt.title(keyword + "在" + firstdata + "-" + lastdata + "人民日报中出现的次数", size=10)  # 给整个图表加上标题
        #plt.legend()
        plt.savefig(project + "\\" + "实际操作/统计后输出/" + keyword + "在" + firstdata + "-" + lastdata + "中次数的折线图.png")

        print(keyword + "选定月份内的数据已成功生成折线图并保存")
        # plt.show()
        plt.show(block=False)
        plt.pause(3)  # 3 seconds, I use 1 usually
        plt.close("all")

    '''
    以下部分为，设置散点图，实现“结束弹窗”的功能。
    '''

    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.unicode_minus'] = False

    pop_up_x = [14, 1, 1, 14, 2, 2, 2, 2, 2, 2.5, 2.5, 3, 3.5, 4, 4.5, 3, 3.5, 4, 4.5, 4.7, 5, 5, 5, 5, 5, 8, 8, 8, 8, 8, 8, 8,
         8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
    pop_up_y = [14, 1, 14, 1, 6, 6.5, 7, 7.5, 8, 5.3, 8.5, 5, 5, 5, 5, 9, 9, 9, 8.5, 5.3, 6, 6.5, 7, 7.5, 8, 3, 4, 5, 6, 7, 8,
         9, 10, 11, 6.5, 7.5, 6, 8, 5.5, 8.5, 5, 9]

    plt.plot(pop_up_x, pop_up_y, 'o')
    plt.title("程序运行完完毕，请关闭所有窗口，查看结果", size=17)  # 给整个图表加上标题
    plt.show()
    print("模式二运行完成，请查看数据")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui界面.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(projectpath, ui))   #点模式一，读取项目地址
    ui.pushButton.clicked.connect(run_first)                  #点模式一启动，运行模式一内容
    ui.pushButton_2.clicked.connect(partial(projectpath2, ui))  #点模式二，读项目地址
    ui.pushButton_2.clicked.connect(partial(keywords1, ui))      #点模式二，读关键词内容
    ui.pushButton_2.clicked.connect(run_second)                #点模式二启动，运行模式二内容
    sys.exit(app.exec_())





