# 【v2.0 优化版】后端用户接口：增加长度校验拦截
from flask import Flask, jsonify, request
app = Flask(__name__)

users_db = {
    1: {
        "id": 1, 
        "name": "张三", 
        "role": "normal_user", 
        "email": "zhangsan@company.com",
        "bio": "热爱编程与产品设计"
    }
}

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({"code": 404, "msg": "用户不存在"}), 404
    return jsonify({"code": 200, "data": user})

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({"code": 404, "msg": "用户不存在"}), 404
    
    data = request.json
    # 规则1：昵称限制
    if "name" in data:
        name = data["name"].strip()
        if len(name) < 2 or len(name) > 10:
            return jsonify({"code": 400, "msg": "昵称必须在2-10字之间"}), 400
        user["name"] = name
        
    # 规则2：签名限制
    if "bio" in data:
        bio = data["bio"].strip()
        if len(bio) > 50:
            return jsonify({"code": 400, "msg": "签名不能超过50字"}), 400
        user["bio"] = bio

    return jsonify({"code": 200, "msg": "更新成功", "data": user})

if __name__ == '__main__':
    app.run(port=5000)
