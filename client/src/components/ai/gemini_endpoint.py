from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()
api_key = os.environ.get("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/generate-quiz', methods=['GET'])
def generate_quiz():
    # Print incoming request data
    print("\n=== Incoming Request ===")
    print("Arguments:", request.args)
    print("Prompt:", request.args.get('prompt'))
    print("Number of Questions:", request.args.get('num_questions'))
    print("Difficulty:", request.args.get('difficulty'))
    
    prompt = request.args.get('prompt', '')
    num_questions = request.args.get('num_questions', '5')
    difficulty = request.args.get('difficulty', 'medium')
    
    prompt_template = f"""Generate a {difficulty}-difficulty quiz about {prompt}. 
    Please create {num_questions} questions."""
    
    # Print what we're sending to Gemini
    print("\n=== Sending to Gemini ===")
    print(prompt_template)
    
    response = model.generate_content(prompt_template)
    
    # Print Gemini's response
    print("\n=== Gemini Response ===")
    print(response.text)
    
    return jsonify({"quiz": response.text})

if __name__ == '__main__':
    app.run(port=5000, debug=True) 