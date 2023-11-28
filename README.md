# Clothing Color Matching

[Download Project Requirement](./requirement_zh-CN.pdf)

[Download Report](./report_zh-CN.pdf)

**File List:**

| Dir                          | FileName                       | Description                                                                                                                                                                                                   |
| ---------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                         | generate_json.py               | Run to generate json folder and two auxiliary json files                                                                                                                                                      |
|                              | process_balance_data.ipynb     | Run to generate tensor format data                                                                                                                                                                            |
|                              | resnet18.py                    | Run to train ResNet18 model                                                                                                                                                                                   |
|                              | resnest50.py      **BEST**     | Run to train ResNeSt50 model                                                                                                                                                                                  |
|                              | densenet161.py                 | Run to train DenseNet161 model                                                                                                                                                                                |
|                              | inference.ipynb                | Run to infer json results, stored in the json folder of this directory                                                                                                                                        |
|                              | dataset.py                     | Defines DataSet class                                                                                                                                                                                         |
|                              | get_label.py                   | Defines get_label function, input Chinese word output label                                                                                                                                                   |
|                              | train_model.py                 | Defines train_model function                                                                                                                                                                                  |
|                              | count_appearance.py            | Auxiliary function, used to analyze the dataset, not necessary for training                                                                                                                                   |
|                              | my_test_data_ResNeSt50....json | The best json result, not necessary for training                                                                                                                                                              |
|                              | README.md                      |                                                                                                                                                                                                               |
| data                         | medium folder                  | Need to pre-place medium size image data [https://cloud.tsinghua.edu.cn/d/27849370d8774de3a2e2/files/?p=%2Fmedium.zip&dl=1](https://cloud.tsinghua.edu.cn/d/27849370d8774de3a2e2/files/?p=%2Fmedium.zip&dl=1) |
| model (empty directory)      |                                | Place the generated model                                                                                                                                                                                     |
| tensor_data(empty directory) |                                | Place the generated tensor format data                                                                                                                                                                        |



**My Training Environment:**

Ubuntu 16.04.7 LTS,  264G ram,  4*1080Ti

python3.7.11, torch 1.8.1+cu101, torchvision 0.9.1+cu101



**How to Use:**

- Follow the steps below to process data, train models, and generate inference results
- Note, this project uses the method of directly loading all images at once, please ensure that the running memory is not less than 128G
- Note, this project directly stores the original model, and uses multi-GPU training, you need to ensure that the available graphics card number during training is consistent with the inference

1. According to the table above, create all the empty directories

2. cd to the code directory, run generate_json.py

   This will generate a json folder in the code directory (containing color2label.json, word2color.json)

3. Run process_balance_data.ipynb, generate unbalanced and balanced tensor format data in turn, stored in the tensor_data directory (takes 1h)

4. Choose a model, run the file, each epoch's model will be stored in the model directory. If you use ResNeSt50, please install first:

```bash
pip install resnest --pre
```

5. Modify the parameters in inference.ipynb (specify the model path), run, the inference results are saved in the json directory in the code folder



Directly download the best model (this model requires GPU0,1,2,3 to be available for inference): https://cloud.tsinghua.edu.cn/f/2f6d3723c1b743cda0b4/