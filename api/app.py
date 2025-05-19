from flask import Flask, request, jsonify
import tempfile, os, subprocess, shutil

app = Flask(__name__)

@app.route("/hello-world", methods=['GET'])
def helloWorld():
    return jsonify({
        "message":"hello world"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)