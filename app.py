from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import google.generativeai as genai
import os

app = Flask(__name__)
cors = CORS(app)
CORS(app, resources={r"/*": {"origins": ["https://anamenbala.netlify.app"]}})
model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key='AIzaSyC4IfeZfDy-ZgsgGp9od8Xf3jBKmLjtut8')
@app.route('/api/answer', methods=['POST'])
def answer():
    data = request.get_json()
    print(data)
    prompt = data['prompt']
    response = model.generate_content(prompt)
    result = jsonify({'response': response.text})
    result.headers.add('Access-Control-Allow-Origin', 'https://anamenbala.netlify.app')
    result.headers.add('Access-Control-Allow-Credentials', 'true')
    return result

if __name__ == '__main__':
    app.run(debug=True)
