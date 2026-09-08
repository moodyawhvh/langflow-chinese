# 中文注释:列出指定 Flow 已上传的文件(v1 API)
# 使用前请设置环境变量:LANGFLOW_URL(Langflow 服务器地址)、FLOW_ID(flow ID)、LANGFLOW_API_KEY(API key)
import os

import requests

# 拼接列出文件的 API 端点地址:/api/v1/files/list/{FLOW_ID}
url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/files/list/{os.getenv('FLOW_ID', '')}"

# 请求头:声明接收 JSON,并附带 Langflow API key 做认证
headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

# 发送 GET 请求查询文件列表
response = requests.request("GET", url, headers=headers)
# 状态码非 2xx 时抛出异常,便于及早发现认证或参数错误
response.raise_for_status()

# 打印原始 JSON 响应内容
print(response.text)
