'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-03-12 08:28:35
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-03-12 09:03:01
FilePath: /wangchenkang/ES/test_upload/pdf_parsing.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from elasticsearch import Elasticsearch
import os
import json

# 创建 Elasticsearch 客户端连接
es = Elasticsearch(
    "https://172.16.2.51:165",
    basic_auth=("elastic", "C-pa1WxXoF2U1FkpSK_i"),
    verify_certs=False  # 在生产环境中应该设置为True并配置proper证书
)

# 1. 加载 PDF 文档
loader = PyPDFLoader("uploads/2._csdn_sty945.pdf")
documents = loader.load()

# 2. 文本切分
text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

print(texts[3].page_content)