from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an empty list to store points
points = []

# Endpoint to create a new point


@app.route('/points', methods=['POST'])
def create_point():
    data = request.json
    points.append(data)
    return jsonify({'message': 'Point crée avec succès'}), 201

# Endpoint to get all points


@app.route('/points', methods=['GET'])
def get_points():
    return jsonify(points)

# Endpoint to update a point by ID


@app.route('/points/<int:point_id>', methods=['PUT'])
def update_point(point_id):
    if point_id < len(points):
        data = request.json
        points[point_id] = data
        return jsonify({'message': 'Point mis a jour avec succès'})
    else:
        return jsonify({'error': 'Point introuvable'}), 404

# Endpoint to delete a point by ID


@app.route('/points/<int:point_id>', methods=['DELETE'])
def delete_point(point_id):
    if point_id < len(points):
        del points[point_id]
        return jsonify({'message': 'Point supprimer avec succès'})
    else:
        return jsonify({'error': 'Point introuvable'}), 404


if __name__ == '__main__':
    app.run(debug=True)
