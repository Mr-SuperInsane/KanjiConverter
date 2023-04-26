from urllib.request import urlopen
from urllib.parse import urlencode
import json

message = "ここにげんぶんをにゅうりょく"

url = "http://www.google.com/transliterate?"
param = {'langpair':'ja-Hira|ja','text':message}
paramStr = urlencode(param)
print(url + paramStr)
readObj = urlopen(url + paramStr)
response = readObj.read()
datas = json.loads(response)
result_message = ''
for data in datas:
    fixed_data = json.loads(json.dumps(data[1][0], ensure_ascii=False))
    result_message += fixed_data

print(result_message)
