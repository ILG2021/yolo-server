# yolo-server
Yolo的flask服务端封装，默认端口1235。

node_client.js是测试客户端。

请求使用POST方法，body中用raw格式，img字段中放base64数据数组，返回这组图片中包含人物的个数。详细用法见node_client.js。

返回数据格式：
```json
[ 2, 2 ]
```

依赖:
```bash
pip install -r requirements.txt
pip install flask
npm install node-fetch
```

服务器启动：
```bash
python api.py
```

客户端运行：
```bash
node node_client.js
```
