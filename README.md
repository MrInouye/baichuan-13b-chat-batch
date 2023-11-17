# baichuan-13b-chat-batch
baichuan-13b-chat的批量生成demo

1. 先将baichuan-13b-chat模型文件夹里面的generation_utils.py和modeling_baichuan.py这两个文件，替换成我目录中的。
2. 原始的model.chat()方法主要是三步(见modeling_baichuan.py文件)：
   1) 将messages转成token；
   2) 调用generate()方法；
   3) 返回第一个结果；
   ![企业微信截图_17002045405547](https://github.com/MrInouye/baichuan-13b-chat-batch/assets/73767263/a83f40b0-db0d-4077-9257-f266071c574b)
3. generate()方法是支持批量的，所主要的修改就在于将批量的messages转成token并进行padding(见generation_utils.py文件)：
   ![企业微信截图_17002044406983](https://github.com/MrInouye/baichuan-13b-chat-batch/assets/73767263/bfe0e812-5f77-40a5-a95b-8f5dd2507369)
4. 运行infer.py文件进行批量生成(暂不支持stream方式)
