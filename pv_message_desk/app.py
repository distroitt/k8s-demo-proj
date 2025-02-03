from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FILE_PATH = "/data/messages.txt"

os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        f.write("")

@app.route('/messages', methods=['GET', 'POST'])
def handle_message():
    if request.method == 'POST':
        data = request.json.get("message", "")
        with open(FILE_PATH, "a") as f:
            f.write(data + "\n")
        return {"status": "Message added"}, 201
    elif request.method == 'GET':
        with open(FILE_PATH, "r") as f:
            messages = f.readlines()
        return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)