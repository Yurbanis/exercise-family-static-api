from flask import Flask, jsonify, request
from datastructures import FamilyStructure

app = Flask(__name__)

jackson_family = FamilyStructure('Jackson')

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({'error': 'Member not found'}), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    jackson_family.add_member(data)
    return jsonify(), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({'done': True}), 200

if __name__ == '__main__':
    app.run()