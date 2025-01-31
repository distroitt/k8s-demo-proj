from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis-service', port=6379, decode_responses=True)

@app.route('/set/<key>', methods=['POST'])
def set_value(key):
    value = request.form['value']
    redis_client.set(key, value)
    return jsonify({"message" : f"Set key {key} with value {value}"}), 200

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = redis_client.get(key)
    if value:
        return jsonify({key: value}), 200
    else:
        return jsonify({"message": "Key not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)