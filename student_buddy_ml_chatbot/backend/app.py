from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("question")
    if not query:
        return jsonify({"response": "Please enter a question."})
    answer = get_response(query)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)