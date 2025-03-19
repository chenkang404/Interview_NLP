'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-03-12 08:03:56
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-03-12 09:21:50
FilePath: /wangchenkang/ES/test_upload/client_upload.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests

url = 'http://127.0.0.1:5000/upload'  # 替换为你的服务地址
file_path = '2.计算机网络_csdn_sty945.pdf'  # 替换为你要上传的文件路径
idx = "121212"
with open(file_path, 'rb') as f:
    data = {'idx': idx}
    files = {'file': (file_path, f)} # file_path, f 组成元组，这样可以指定上传的文件名称。
    response = requests.post(url, files=files,data=data)

print(response.json())