from app import app
from flask import jsonify, make_response, request
from app.service.database.interaction_with_bd import Interaction as Interaction_DB
from app.marshmallow.marshmallow import TaskSchema


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'code': '404', 'error': 'Not found'}), 404)


@app.route('/api/v1.0/tasks/getAll', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': TaskSchema(many=True).dump(Interaction_DB.get_all(named=request.args.get('title', default=False))).data or 'Title not found'})


@app.route('/api/v1.0/tasks/get', methods=['GET'])
def get_task():
    return jsonify({'task': TaskSchema().dump(Interaction_DB.get_one_by_title(request.args.get('title', type=str))).data}), 200


@app.route('/api/v1.0/tasks/create', methods=['POST'])
def create_task():
    try:
        data, errors = TaskSchema().load(request.get_json())
        Interaction_DB.post(**data)
        return jsonify({'task': TaskSchema().dump(Interaction_DB.get_one_by_title(data['title'])).data}), 201
    except Exception as e:
        return jsonify({'errors': e.messages}), 400


@app.route('/api/v1.0/tasks/update', methods=['PUT'])
def update_task():
    response = Interaction_DB.update_one_by_title(request.args.get('title'), request.json.get('title', request.args.get('title')),
                                       request.json['description'], request.json.get('done', False))
    return jsonify({'task': TaskSchema().dump(response).data}), 200


@app.route('/api/v1.0/tasks/delete', methods=['DELETE'])
def delete_task():
    return jsonify({'result': 'Success', 'deleted task': TaskSchema().dump(
        Interaction_DB.delete_one_by_title(request.args.get('title'))).data}), 200
