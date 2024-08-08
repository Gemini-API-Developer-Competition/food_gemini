from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import requests
import re
import config

app = Flask(__name__)

# Gemini API 키 설정
genai.configure(api_key=config.GEMINI_API_KEY)

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
    return render_template('api_index.html')

@app.route('/gemini')
def gemini_index():
    return render_template('gemini_index.html')

@app.route('/api/gemini', methods=['POST'])
def summarize():
    input_text = request.form['input_text']
    
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(input_text)
    summarized_text = convert_to_bold(response.text)
    
    return render_template('gemini_result.html', input_text=input_text, summarized_text=summarized_text)

@app.route('/verify')
def verify_index():
    return render_template('api_index.html')

@app.route('/api/verify', methods=['POST'])
def verify():
    business_number = request.form['business_number']
    
    if not business_number:
        return jsonify({"error": "No business number provided"}), 400
    
    data = {
        "b_no": [business_number]
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.post(f"{config.PUBLIC_DATA_API_URL}/status?serviceKey={config.PUBLIC_DATA_API_KEY}", json=data, headers=headers)
    if response.status_code == 200:
        verification_result = response.json()
    else:
        verification_result = f"Error: {response.text}"
    
    return render_template('api_result.html', business_number=business_number, verification_result=verification_result)

@app.route('/validate')
def validate_index():
    return render_template('validate_index.html')

@app.route('/api/validate', methods=['POST'])
def validate():
    business_number = request.form['business_number']
    start_date = request.form['start_date']
    p_nm = request.form['p_nm']
    p_nm2 = request.form['p_nm2']
    b_nm = request.form['b_nm']
    corp_no = request.form['corp_no']
    b_sector = request.form['b_sector']
    b_type = request.form['b_type']
    b_adr = request.form['b_adr']
    
    if not business_number:
        return jsonify({"error": "No business number provided"}), 400
    
    data = {
        "businesses": [
            {
                "b_no": business_number,
                "start_dt": start_date,
                "p_nm": p_nm,
                "p_nm2": p_nm2,
                "b_nm": b_nm,
                "corp_no": corp_no,
                "b_sector": b_sector,
                "b_type": b_type,
                "b_adr": b_adr
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.post(f"{config.PUBLIC_DATA_API_URL}/validate?serviceKey={config.PUBLIC_DATA_API_KEY}", json=data, headers=headers)
    if response.status_code == 200:
        validation_result = response.json()
    else:
        validation_result = f"Error: {response.text}"
    
    return render_template('validate_result.html', business_number=business_number, validation_result=validation_result)

if __name__ == '__main__':
    app.run(debug=True)
