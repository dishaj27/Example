from flask import Blueprint, request, jsonify # type: ignore
from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')

    if not name or not email or not role:
        return jsonify({'error': 'Missing data'}), 400
    
    print("mongo instance:", mongo)
    print("mongo.db:", mongo.db)
    
    mongo.db.users.insert_one({
        'name': name,
        'email': email,
        'role': role
    })

    return jsonify({'message': 'User registered successfully!'})
