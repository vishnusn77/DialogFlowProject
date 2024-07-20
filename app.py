from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"student_number": "200557136"})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = 'This is a sample response from your webhook!'
    return jsonify({'fulfillmentText': fulfillmentText})

if __name__ == '__main__':
    app.run(debug=True)
