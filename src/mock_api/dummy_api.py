from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/providers')
def get_providers():

    local_authority = request.args.get('localAuthority')  # capture query param
    
    if local_authority != 'Oldham':
        return jsonify({"error": "Unsupported local authority"}), 400
    
    with open ('src/mock_api/dummy_data/providers.json', 'r') as f:
        providers = json.load(f)
    return jsonify(providers)
    
@app.route('/providers/<provider_id>')
def get_provider_details(provider_id):
    with open (f'src/mock_api/dummy_data/provider_details/provider_{provider_id}.json', 'r') as f:
        provider_details = json.load(f)
    return jsonify(provider_details)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    