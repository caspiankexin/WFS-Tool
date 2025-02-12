# 禾金词频统计工具—WFS

2025年2月12日更新

* 更新个人主页：idreams.cc   邮箱：a@idreams.cc
* 重新审视这个项目，处理问题逻辑和方法都很落后，今年心血来潮用ai重写了个程序。有针对海量的人民日报文本文件词频统计需求的，可以移步新项目了解：[觅影词频统计工具（ 一款针对大量文本数据进行词频统计的工具）](https://github.com/caspiankexin/MiYing)

---

**2022年更新**

Github下载地址：

https://github.com/caspiankexin/WFS-Tool/releases

## 项目说明

项目作者  Github用户 @caspiankexin  个人主页：www.cckeke.top 

如需人民日报数据，可访问另一个github仓库：

[https://github.com/caspiankexin/people-daily-crawler-date](https://github.com/caspiankexin/people-daily-crawler-date)

禾金词频统计工具（WFS），是看过钱钢的语象观察后的灵感的实现，目的就是为了方便普通人也可以搞语象观察的研究。

软件使用python编写，已在github开源，适用于大批量文档大批量关键词搜索使用。

软件完全免费，但禁止使用本软件做违法的事情和不利于社会发展的研究，作者只提供工具，不为产生的研究内容负责。如有相关改进需求，可以github上私信我

## 功能描述

本软件有两种统计分析模式。

模式一：指定一个范围段，对多批次的关键词进行统计，生成关键词词频数据，生成扇形图。

模式二：指定多个范围段，输入一些关键词，分别统计关键词在各个范围内的词频，生成折线图。

## 使用步骤

### 前期准备

软件使用需在相关文件夹下进行，确保程序能准确识别路径。

①检查文件路径是否准确

![](https://cors.zme.ink/http://cdn.idreams.cc/20250212a01cd383a7f27c3c00d36a380421efaf.webp)

②在原始数据文件夹内，存入需要统计的文件资料，如上图分类整理好；将整理好的关键词名单命名存放在【关键词名单】文件夹下。

③修改相关参数

Ⅰ 实际操作➡️需合并文件的列表.txt：输入需要统计的范围段    （必需操作，年份月份都可）

Ⅱ 实际操作➡️关键词名单列表.txt：输入需调用的关键词名单文件的名称   （模式一必选操作）

`PS：修改的内容，都参照模板里的格式来进行修改，不然无法识别`

<img src="https://cors.zme.ink/http://cdn.idreams.cc/20250212e764f8b4c906658f0d3274bd0dbb8e03.webp" alt="%E7%A6%BE%E9%87%91%E8%AF%8D%E9%A2%91%E7%BB%9F%E8%AE%A1%E5%B7%A5%E5%85%B7%E2%80%94WFS%20e6330b952a7740a084547b72d778b177/Untitled.png" style="zoom: 67%;" />

<img src="https://cors.zme.ink/http://cdn.idreams.cc/2025021284be7c9b57b39e756661004e73993e36.webp" style="zoom:67%;" />

<img src="https://cors.zme.ink/http://cdn.idreams.cc/20250212b400b3af8581dbae6bebe9bc6d9b6576.webp" style="zoom:67%;" />

### 操作环节

双击【禾金词频统计（WFS）.exe】（反应缓慢，捎等一会），出现两个窗口。一个信息显示界面，一个操作界面。如下图

![](https://cors.zme.ink/http://cdn.idreams.cc/20250212acbc472466a94b688d9a53c540a72661.webp)

![](https://cors.zme.ink/http://cdn.idreams.cc/2025021280ce0949fcec85aea9a8990122de47fc.webp)

输入项目文件夹地址，例如E:\禾金词频统计（WFS）

通过信息显示界面查看程序运行情况，运行完毕后会有弹窗提醒，运行时间取决于电脑性能。

### 运行结束

程序运行结束后，在【实际操作】➡️【统计后输出】文件夹中查看统计数据。

## 后记

作为我第一个编写的软件，还很简陋，还有很多可以优化的地方，这都是之后可以努力的方向。这个软件的实现用了将近三年的时间，想法在脑海里，一段一段时间去突破一个个困难，最终让我这个编程小白，把整出来了，功能实现也比之前要多很多。这个过程中看了无数的文章，学了很多东西。虽说是我编的程序，其实也是将许多人代码拼凑魔改而已。
