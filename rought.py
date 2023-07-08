from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main_route():
    data = request.get_json()
    if "'Sage'" in data or "Claude+" in data or "Claude_instant" in data:
        response = requests.post('https://', json=data)
    else:
        response = requests.post('https://api.openai-sb.com', json=data)

    # 构造一个 Flask 的 Response 对象，将上游的状态码、头部信息和内容全部返回给原请求者
    return Response(response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(port=9091)
