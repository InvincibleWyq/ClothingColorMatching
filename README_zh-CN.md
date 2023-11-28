### 衣物颜色匹配大作业 自93王逸钦 2019010850

[Download Project Requirement](./requirement_zh-CN.pdf)

[Download Report](./report_zh-CN.pdf)

**文件列表：**

| Dir                 | FileName                       | Description                                                                                                                                                                                           |
| ------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                | generate_json.py               | 运行以生成json文件夹和两个辅助json文件                                                                                                                                                                |
|                     | process_balance_data.ipynb     | 运行以生成tensor格式的数据                                                                                                                                                                            |
|                     | resnet18.py                    | 运行以训练ResNet18模型                                                                                                                                                                                |
|                     | resnest50.py      **BEST**     | 运行以训练ResNeSt50模型                                                                                                                                                                               |
|                     | densenet161.py                 | 运行以训练DenseNet161模型                                                                                                                                                                             |
|                     | inference.ipynb                | 运行以推理json结果，存于本目录json文件夹                                                                                                                                                              |
|                     | dataset.py                     | 内定义DataSet类                                                                                                                                                                                       |
|                     | get_label.py                   | 内定义get_label函数，输入中文词输出标号                                                                                                                                                               |
|                     | train_model.py                 | 内定义train_model函数                                                                                                                                                                                 |
|                     | count_appearance.py            | 辅助函数，用于分析数据集，对训练不必需                                                                                                                                                                |
|                     | my_test_data_ResNeSt50....json | 最优的json结果，对训练不必需                                                                                                                                                                          |
|                     | README.md                      |                                                                                                                                                                                                       |
| data                | medium文件夹                   | 需要预先放置medium尺寸的图片数据 [https://cloud.tsinghua.edu.cn/d/27849370d8774de3a2e2/files/?p=%2Fmedium.zip&dl=1](https://cloud.tsinghua.edu.cn/d/27849370d8774de3a2e2/files/?p=%2Fmedium.zip&dl=1) |
| model (空目录)      |                                | 放置生成的模型                                                                                                                                                                                        |
| tensor_data(空目录) |                                | 放置生成的tensor格式的数据                                                                                                                                                                            |



**我的训练环境：**

Ubuntu 16.04.7 LTS,  264G ram,  4*1080Ti

python3.7.11, torch 1.8.1+cu101, torchvision 0.9.1+cu101



**使用方法：**

- 按以下步骤可进行数据处理、模型训练、推理生成结果
- 注意，本项目采用直接把所有图片一次性load的方式，请保证运行内存不低于128G
- 注意，本项目直接存储原始model，且使用多GPU训练，需保证训练时的可用显卡编号和推理时一致

1. 按照上表所示，建立出所有的空目录

2. cd到code目录下，运行generate_json.py

   这将在code目录下生成json文件夹(内含有color2label.json, word2color.json)

3. 运行process_balance_data.ipynb，依次产生未经平衡和经平衡的tensor格式数据，存于tensor_data目录 (耗时1h)

4. 选择一种模型，运行该文件，每个epoch的模型均会存储在model目录。若使用ResNeSt50，请先安装：

```bash
pip install resnest --pre
```

5. 修改inference.ipynb中的参数（指定模型的路径），运行，推理结果保存在code文件夹下的json目录中



直接下载模型最优模型 (该模型推理时需要GPU0,1,2,3均可用)：https://cloud.tsinghua.edu.cn/f/2f6d3723c1b743cda0b4/

