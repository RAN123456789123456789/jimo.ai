# -*- coding: utf-8 -*-
import requests
import json
import sys
import os

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 从config.json读取api_key
config_path = r'E:\Desktop\经理的批量化操作\config.json'
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)
    api_key = config.get('api_key', '')

url = "https://jimoai-bot-api.xiaohuodui.cn/v2/datasets/documents"

payload = json.dumps({
   "name": "string",
   "segments": [{"content": "string", "indexNo": "string", "index_1": "string", "index_2": "string"}],
   "datasetId": 0  # 需要替换为实际的数据集ID
})

headers = {
   'Authorization': api_key,  # 直接使用api_key，不需要Bearer前缀
   'Content-Type': 'application/json'
}

print("发送请求...")
response = requests.post(url, headers=headers, data=payload)
print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")
