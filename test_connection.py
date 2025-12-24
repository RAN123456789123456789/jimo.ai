# -*- coding: utf-8 -*-
import requests
import sys

# 设置UTF-8编码输出
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 测试网络连接
print("测试网络连接...")
try:
    response = requests.get("https://jimoai-bot-api.xiaohuodui.cn", timeout=5)
    print(f"[成功] 网络连接成功，状态码: {response.status_code}")
except Exception as e:
    print(f"[失败] 网络连接失败: {e}")
    exit(1)

# 测试API端点
print("\n测试API端点...")
url = "https://jimoai-bot-api.xiaohuodui.cn/v2/datasets/documents"
try:
    response = requests.get(url, timeout=5)
    print(f"[成功] API端点可访问，状态码: {response.status_code}")
except Exception as e:
    print(f"[失败] API端点访问失败: {e}")

print("\n提示: 需要提供有效的Authorization token才能发送POST请求")

