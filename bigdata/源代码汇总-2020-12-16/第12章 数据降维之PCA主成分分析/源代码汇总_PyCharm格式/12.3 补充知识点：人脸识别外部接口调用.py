# # 12.3 补充知识点：人脸识别外部接口调用
from aip import AipFace
import base64
APP_ID = '16994639'
API_KEY = 'L9XnkKQEMnHhB5omF2P8D9OM'
SECRET_KEY = 'nnOZDoruZ6AjVglBs6ecvUjFRIAKrn9T'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
filePath = r'王宇韬.jpg'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')
imageType = "BASE64"

options = {}
options["face_field"] = "age,gender,beauty"

result = aipFace.detect(get_file_content(filePath), imageType, options)
print(result)

age = result['result']['face_list'][0]['age']
print('年龄预测为：' + str(age))
gender = result['result']['face_list'][0]['gender']['type']
print('性别预测为：' + gender)
beauty = result['result']['face_list'][0]['beauty']
print('颜值评分为：' + str(beauty))

