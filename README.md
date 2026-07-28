# 动手学深度学习笔记

[![在线阅读](https://img.shields.io/badge/在线阅读-Quartz-2563eb?style=for-the-badge&logo=github)](https://lan-007.github.io/Notes-of-Dive-into-DeepLearning/)
[![Markdown 链接检查](https://github.com/Lan-007/Notes-of-Dive-into-DeepLearning/actions/workflows/markdown-links.yml/badge.svg)](https://github.com/Lan-007/Notes-of-Dive-into-DeepLearning/actions/workflows/markdown-links.yml)

基于 PyTorch 的《动手学深度学习》学习笔记，涵盖基础知识、神经网络训练、注意力机制、Transformer 与 NLP 预训练应用。

> [!TIP]
> 推荐访问 **[在线阅读版](https://lan-007.github.io/Notes-of-Dive-into-DeepLearning/)**，可使用全文搜索、章节目录和公式渲染。

## 学习路线

路线：PyTorch 基础 → 神经网络训练 → 深度学习 → Transformer → NLP 预训练 → NLP 应用

### 第 1 章：引言

 传统机器学习、深度学习、数据、模型、损失函数、优化算法、回归、分类、监督学习。

### 第 2 章：预备知识

- [2.1 数据操作](<content/02. 预备知识/02.1数据操作.md>)

  关键词：Tensor、shape、numel、reshape、广播、索引、切片、内存。

- [2.2 数据预处理](<content/02. 预备知识/02.2 数据预处理.md>)

  关键词：CSV、pandas、DataFrame、缺失值、均值填充、独热编码。

- [2.3 线性代数](<content/02. 预备知识/02.3 线性代数.md>)

  关键词：点积、矩阵—向量乘法、矩阵乘法、范数、维度。

- [2.4 微积分与自动微分](<content/02. 预备知识/02.4 微积分与自动微分.md>)

  关键词：梯度、自动求导、`requires_grad`、`backward`、`grad`、计算图分离。

- [2.5 概率论](<content/02. 预备知识/02.5 概率论.md>)

  关键词：大数定律、贝叶斯定理。

### 第 3 章：线性神经网络

#### 3.1 线性回归

- [3.1.1 线性回归](<content/03.1 线性神经网络/01. 线性回归.md>)

  关键词：回归模型、均方误差、梯度下降、批量、训练流程。

- [3.1.2 从零开始实现](<content/03.1 线性神经网络/02. 从零开始实现.md>)

  关键词：合成数据、DataLoader、模型函数、损失函数、SGD、手写训练循环。

- [3.1.3 简洁实现](<content/03.1 线性神经网络/03. 简洁实现.md>)

  关键词：`nn.Sequential`、`nn.Linear`、`MSELoss`、优化器、标准训练流程。

#### 3.2 Softmax 回归

- [3.2.1 Softmax 回归](<content/03.2 softmax回归/01. softmax回归.md>)

  关键词：多分类、类别分数、概率、softmax、交叉熵、独热编码。

- [3.2.2 从零开始实现](<content/03.2 softmax回归/02. 从零开始实现.md>)

  关键词：Fashion-MNIST、图像张量、softmax、交叉熵、分类准确率、训练函数。

- [3.2.3 简洁实现](<content/03.2 softmax回归/03. 简洁实现.md>)

  关键词：`Flatten`、`Linear`、`CrossEntropyLoss`、SGD、分类训练。

### 第 4 章：多层感知机

- [4.1 多层感知机](<content/04. 多层感知机/01. 多层感知机.md>)

  关键词：隐藏层、非线性、ReLU、MLP、通用近似。

- [4.2 从零实现](<content/04. 多层感知机/02. 从零实现.md>)

  关键词：手写参数、ReLU、前向传播、交叉熵、Fashion-MNIST。

- [4.3 简洁实现](<content/04. 多层感知机/03. 简洁实现.md>)

  关键词：`nn.Sequential`、参数初始化、MLP 训练。

- [4.4 模型选择、欠拟合和过拟合](<content/04. 多层感知机/04. 模型选择、欠拟合和过拟合.md>)

  关键词：训练误差、泛化误差、验证集、测试集、模型复杂度、超参数。

- [4.5 权重衰减](<content/04. 多层感知机/05. 权重衰减.md>)

  关键词：L2 正则化、`weight_decay`、参数惩罚、过拟合。

- [4.6 Dropout](<content/04. 多层感知机/06. 暂退法（dropout）.md>)

  关键词：随机失活、保留概率、训练模式、推理模式、正则化。

- [4.7 前向传播、反向传播和计算图](<content/04. 多层感知机/07.前向传播、反向传播和计算图.md>)

  关键词：forward、loss、backward、梯度、optimizer、计算图。

- [4.8 数值稳定性和模型初始化](<content/04. 多层感知机/08. 数值稳定性和模型初始化.md>)

  关键词：梯度消失、梯度爆炸、Xavier 初始化、数值稳定性、NaN。

- [4.9 环境和分布偏移](<content/04. 多层感知机/09. 环境和分布偏移.md>)

  关键词：协变量偏移、标签偏移、概念偏移、线上效果、数据分布。

- [4.10 Kaggle 房价预测](<content/04. 多层感知机/10. 实战Kaggle比赛：预测房价.md>)

  关键词：表格数据、标准化、缺失值、K 折交叉验证、训练、预测、submission。

### 第 5 章：深度学习计算

- [5.1 层和块](<content/05. 深度学习计算/01. 层和块.md>)

  关键词：`nn.Module`、自定义模型、层、块、`forward`、模型组合。

- [5.2 参数管理](<content/05. 深度学习计算/02.参数管理.md>)

  关键词：`parameters`、`named_parameters`、参数访问、参数初始化、共享参数。

- [5.3 延后初始化](<content/05. 深度学习计算/03. 延后初始化.md>)

  关键词：`LazyLinear`、输入维度推断、首次前向传播、参数初始化。

- [5.4 读写文件与模型参数](<content/05. 深度学习计算/04. 读写文件（模型参数）.md>)

  关键词：`torch.save`、`torch.load`、`state_dict`、模型保存、checkpoint、恢复训练。

- [5.5 GPU](<content/05. 深度学习计算/05. GPU.md>)

  关键词：device、CUDA、`.to(device)`、张量迁移、模型迁移、多 GPU 基础。

### 第 10 章：注意力机制

- [10.1 注意力提示](<content/10. 注意力机制/01. 注意力提示.md>)

  关键词：Query、Key、Value、注意力权重、加权求和。

- [10.2 注意力汇聚与核回归](<content/10. 注意力机制/02. 注意力汇聚：Nadaraya-Watson 核回归.md>)

  关键词：Nadaraya-Watson、核函数、相似度、非参数注意力、带参数注意力。

- [10.3 注意力评分函数](<content/10. 注意力机制/03. 注意力评分函数.md>)

  关键词：masked softmax、加性注意力、缩放点积注意力、有效长度、批量矩阵乘法。

- [10.4 Bahdanau 注意力](<content/10. 注意力机制/04. Bahdanau 注意力.md>)

  关键词：Encoder—Decoder、上下文向量、解码器查询、编码器隐藏状态。

- [10.5 多头注意力](<content/10. 注意力机制/05. 多头注意力.md>)

  关键词：多个 head、线性投影、维度变换、并行注意力、拼接。

- [10.6 自注意力和位置编码](<content/10. 注意力机制/06. 自注意力和位置编码.md>)

  关键词：self-attention、QKV 同源、计算复杂度、正弦位置编码、序列顺序。

- [10.7 Transformer](<content/10. 注意力机制/07. Transformer.md>)

  关键词：Encoder、Decoder、FFN、AddNorm、残差连接、LayerNorm、因果掩码、训练、预测、BLEU。

### 第 14 章：NLP 预训练

- [14.1 词嵌入](<content/14. NLP预训练/01. 词嵌入.md>)

  关键词：one-hot、Word2Vec、CBOW、Skip-gram、静态词向量。

- [14.2 近似训练](<content/14. NLP预训练/02. 近似训练.md>)

  关键词：负采样、层序 softmax、计算复杂度、正负样本。

- [14.3 词嵌入数据集](<content/14. NLP预训练/03. 用于预训练词嵌入的数据集.md>)

  关键词：PTB、词表、下采样、中心词、上下文词、负采样、batch。

- [14.4 预训练 Word2Vec](<content/14. NLP预训练/04. 预训练word2vec.md>)

  关键词：Embedding、Skip-gram、负采样损失、掩码、训练、相似词。

- [14.5 GloVe](<content/14. NLP预训练/05. 全局向量的词嵌入（GloVe）.md>)

  关键词：共现矩阵、全局统计、加权最小二乘、词向量。

- [14.6 子词嵌入](<content/14. NLP预训练/06. 子词嵌入.md>)

  关键词：fastText、字符 n-gram、Byte Pair Encoding、BPE、未登录词。

- [14.7 词相似性和类比](<content/14. NLP预训练/07. 词的相似性和类比任务.md>)

  关键词：余弦相似度、KNN、近义词、向量类比、词向量评价。

- [14.8 BERT](<content/14. NLP预训练/08. 来自Transformers的双向编码器表示（BERT）.md>)

  关键词：上下文表示、Transformer Encoder、token/segment/position embedding、MLM、NSP、BERTModel。

- [14.9–14.10 BERT 数据与预训练](<content/14. NLP预训练/09. 预训练BERT.md>)

  关键词：WikiText-2、MLM 数据、NSP 数据、有效长度、预测位置、损失函数、小型 BERT、训练、句子编码。

### 第 15 章：NLP 应用

- [15.1–15.3 情感分析](<content/15. NLP微调/01. 情感分析.md>)

  关键词：IMDb、tokenize、词表、截断、padding、DataLoader、GloVe、BiLSTM、TextCNN、二分类、迁移学习。
