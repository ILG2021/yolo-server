# yolo-server
Yolo v5的flask服务端封装，提供了三个接口。

/，返回hello world，可以通过它来测试服务是否运行

/persons，返回图片中人的个数

/objects，返回图片中所有对象

## 依赖:
```bash
pip install yolov7detect
pip install flask
```

## 运行
```bash
python yolo.py
```

## windows打包
```bash
./pyinstaller.bat
```

## node客户端
客户端运行：
```bash
cd client
node install
node client.js
```

请求使用POST方法，body中用raw格式，img字段中放base64数据数组，详细用法见client.js。

返回数据格式：

/ 接口

```json
<h1>Hello, yolo v5!</h1>
```

/persons接口
```json
[ 2, 2 ]
```

/objects接口
```json
[
  [
    {
      "xmin": 140.561706543,
      "ymin": 200.3346862793,
      "xmax": 1040.3491210938,
      "ymax": 719.0960693359,
      "confidence": 0.867138803,
      "class": 0,
      "name": "person"
    },
    {
      "xmin": 742.5676269531,
      "ymin": 34.279876709,
      "xmax": 1168.8041992188,
      "ymax": 718.5871582031,
      "confidence": 0.844445169,
      "class": 0,
      "name": "person"
    },
    {
      "xmin": 397.8048400879,
      "ymin": 442.6307373047,
      "xmax": 501.1861877441,
      "ymax": 709.9008789062,
      "confidence": 0.2953968346,
      "class": 27,
      "name": "tie"
    }
  ],
  [
    {
      "xmin": 140.561706543,
      "ymin": 200.3346862793,
      "xmax": 1040.3491210938,
      "ymax": 719.0960693359,
      "confidence": 0.867138803,
      "class": 0,
      "name": "person"
    },
    {
      "xmin": 742.5676269531,
      "ymin": 34.279876709,
      "xmax": 1168.8041992188,
      "ymax": 718.5871582031,
      "confidence": 0.844445169,
      "class": 0,
      "name": "person"
    },
    {
      "xmin": 397.8048400879,
      "ymin": 442.6307373047,
      "xmax": 501.1861877441,
      "ymax": 709.9008789062,
      "confidence": 0.2953968346,
      "class": 27,
      "name": "tie"
    }
  ]
]
```

