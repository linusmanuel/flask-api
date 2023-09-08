from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
  return jsonify({'message': 'To fodaa'})