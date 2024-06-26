from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# 環境変数からAPIキーを取得
openai_api_key = os.getenv('OPENAI_API_KEY')

# APIキーを設定
openai.api_key = openai_api_key

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify_review():
    data = request.json
    review = data.get('review')
    
    if not review:
        return jsonify({'error': 'No review provided'}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"このレビューはサクラレビューですか？： {review}\n\n1. サクラレビュー\n2. 正常なレビュー"}
        ]
    )

    result_text = response.choices[0].message['content'].strip()
    is_sakura = "サクラレビュー" in result_text

    return jsonify({'is_sakura': is_sakura})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)