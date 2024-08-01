
# ایجاد API با فریم‌ورک Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'علی'},
        {'id': 2, 'name': 'مریم'}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
