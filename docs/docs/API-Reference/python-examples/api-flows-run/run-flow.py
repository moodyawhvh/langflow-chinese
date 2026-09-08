# 中文注释:通过 /run 端点运行指定 Flow 并打印结果
# 使用前请设置环境变量:LANGFLOW_URL(或 LANGFLOW_SERVER_URL)、FLOW_ID、LANGFLOW_API_KEY
import os

import requests

# 从环境变量读取服务器地址、flow ID 和 API key
base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

# 运行 flow 的 API 端点:/api/v1/run/{FLOW_ID}
url = f"{base}/api/v1/run/{flow_id}"

# 请求头:JSON 请求体 + x-api-key 认证
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

# 请求负载:input_value 为用户输入文本;
# session_id 用于保持会话记忆;input_type/output_type 指定聊天模式;
# output_component 留空表示使用 flow 的默认输出组件
payload = {
    "input_value": "Tell me about something interesting!",
    "session_id": "chat-123",
    "input_type": "chat",
    "output_type": "chat",
    "output_component": "",
}

# 发送 POST 请求,60 秒超时,防止请求无限挂起
response = requests.post(url, headers=headers, json=payload, timeout=60)
# 状态码非 2xx 时抛出异常
response.raise_for_status()
# 打印 flow 运行结果的原始 JSON
print(response.text)
