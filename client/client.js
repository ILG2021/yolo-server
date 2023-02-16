import fetch from "node-fetch";

var url = "https://ultralytics.com/images/zidane.jpg"
var type = 'jpg'
var imgData = await fetch(url).then(r => r.buffer()).then(buf => `data:image/${type};base64,`+buf.toString('base64'));

var response = await fetch('http://127.0.0.1:1235/persons',
    {method: 'POST', body: JSON.stringify({
        "img": [
          imgData
        ]
      }),
      "headers": {
        "content-type": "application/json"
       }
    }
);
var data = await response.json();

console.log("persons:" , data);

response = await fetch('http://127.0.0.1:1235/objects',
    {method: 'POST', body: JSON.stringify({
        "img": [
          imgData
        ]
      }),
      "headers": {
        "content-type": "application/json"
       }
    }
);
data = await response.json();

console.log("objects:" , data);