from flask import request
from bp import chatpdf

# 基于chatpdf的路由
@chatpdf.route('/chatpdf', methods=['GET', 'POST'])
def chat1():
    if request.method == 'POST':
        # 获取前端传来的数据
        data = request.get_json()
        # print(data)
        # print(data['url'])
        # print(data['name']) 
        # print(data['type'])
        # print(data['page'])
        # print(data['time'])
        # print(data['ip'])
        # print(data['ua'])
    else:
        params=request.args
        print(params)
    return 'chatpdf'
        

@chatpdf.route('/additional', methods=['GET', 'POST'])
def additional():
    if request.method == 'POST':
        # 获取前端传来的数据
        data = request.get_json()
        # print(data)
        # print(data['url'])
        # print(data['name'])
        # print(data['type'])
        # print(data['page'])
        # print(data['time'])
        # print(data['ip'])
        # print(data['ua'])
    else:
        params=request.args
        print(params)
    return 'additional'
