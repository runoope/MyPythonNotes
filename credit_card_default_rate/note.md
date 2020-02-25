# 信用卡违约率分析：

这两个问题作为数据挖掘核心的问题：选择哪个分类算法？如何选择分类算法的参数？

## 随机森林分类器

随机森林的英文名字叫做RandomForest（简称RF），它是一个包含多个决策树的分类器，每一个分类器都是一颗CART分类回归树。因此随机森林既可以做分类，又可以做回归。

RandomForestClassifier()

参数为：n_estimators 随机森林里决策树的个数，默认为10

criterion 决策树分裂的标准，默认为基尼指数，也可以选择entropy

max_depth
决策树的最大深度，默认是None，也就是不限制决策树的深度，亦可以是一个整数，限制决策的最大深度。

n_jobs 拟合和预测的时候CPU的核数，默认为1，当为-1时则代表CPU的核数。

## GridSearchCV工具

它是python的参数自动搜索模块。

它来自 sklearn.model_selection

它常用的有四个参数，estimator 想要采用的分类器

param_grid代表我们想要优化的参数及取值

cv,scoring 

## Pipeline管道机制进行流水线作业

管道机制就是让我们把每一步都按顺序列下来，从而创建 Pipeline 流水线作业。每一步都采用 (‘名称’, 步骤) 的方式来表示。