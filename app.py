from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app, resources={r"/api/answer*": {"origins": "*"}})
model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key='AIzaSyC4IfeZfDy-ZgsgGp9od8Xf3jBKmLjtut8')
@app.route('/api/answer', methods=['POST'])
def answer():
    data = request.get_json()
    print(data)
    prompt = data['prompt']
    response = model.generate_content(prompt)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)