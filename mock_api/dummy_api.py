from flask import Flask, jsonify, request
import json
import os

data_path = os.getenv("DOCKER_DATA_PATH", "mock_api/dummy_data")

app = Flask(__name__)

@app.route('/locations')
def get_locations():

    local_authority = request.args.get('localAuthority')
    
    if local_authority != 'Oldham':
        return jsonify({"error": "Unsupported local authority"}), 400
    
    with open (os.path.join(data_path, 'locations.json'), 'r') as f:
        locations = json.load(f)
    return jsonify(locations)
    
@app.route('/locations/<location_id>')
def get_location_details(location_id):
    with open (os.path.join(data_path, f'location_details/location_{location_id}.json'), 'r') as f:
        location_details = json.load(f)
    return jsonify(location_details)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
