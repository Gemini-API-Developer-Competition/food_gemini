# AIzaSyCHNkjeXb8TNnXT4DKlIbI4GMdP0y_AHWo


from flask import Flask, request, render_template
import google.generativeai as genai
import re

app = Flask(__name__)

# Gemini API 키 설정
genai.configure(api_key="AIzaSyCHNkjeXb8TNnXT4DKlIbI4GMdP0y_AHWo")

# 모델 생성
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def convert_to_bold(text):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['input_text']
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(input_text)
    summarized_text = convert_to_bold(response.text)
    return render_template('result.html', input_text=input_text, summarized_text=summarized_text)

if __name__ == '__main__':
    app.run(debug=True)
