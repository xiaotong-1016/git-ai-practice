# 【v1.0 初始版本】后端用户接口
from flask import Flask, jsonify, request
app = Flask(__name__)

users_db = {
    1: {"id": 1, "name": "张三", "role": "normal_user", "email": "zhangsan@company.com"}
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
    if "name" in data:
        user["name"] = data["name"]
    return jsonify({"code": 200, "msg": "更新成功", "data": user})

if __name__ == '__main__':
    app.run(port=5000)
