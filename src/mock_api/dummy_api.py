from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/locations')
def get_locations():

    local_authority = request.args.get('localAuthority')  # capture query param
    
    if local_authority != 'Oldham':
        return jsonify({"error": "Unsupported local authority"}), 400
    
    with open ('src/mock_api/dummy_data/locations.json', 'r') as f:
        locations = json.load(f)
    return jsonify(locations)
    
@app.route('/locations/<location_id>')
def get_location_details(location_id):
    with open (f'src/mock_api/dummy_data/location_details/location_{location_id}.json', 'r') as f:
        location_details = json.load(f)
    return jsonify(location_details)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
