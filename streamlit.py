import streamlit as st
import requests
import os

# サーバーのURLを環境変数から取得
API_URL = os.getenv('API_URL', 'http://localhost:5001/classify')

# タイトルと説明の設定
st.title("レビューチェッカー")
st.write("レビューを入力すると、サクラレビューかどうかをチェックします。")

# レビューの入力フォーム
review_text = st.text_area("レビューを入力してください:")

# チェックボタン
if st.button("サクラをチェック"):
    if review_text:
        if len(review_text) < 10:
            st.warning("レビューは10文字以上入力してください。")
        else:
            try:
                # サクラ検出APIの呼び出し
                response = requests.post(API_URL, json={'review': review_text})
                response.raise_for_status()
                
                # サクラ検出結果の表示
                result = response.json()
                if result.get('is_sakura'):
                    st.error("⚠️ サクラレビューが見つかりました！")
                else:
                    st.success("✅ サクラレビューは見つかりませんでした。")
            except requests.exceptions.HTTPError as http_err:
                st.error(f"HTTPエラーが発生しました: {http_err}\nサーバーの設定を確認してください。")
            except requests.exceptions.ConnectionError:
                st.error("接続エラーが発生しました。サーバーが動作しているか確認してください。")
            except requests.exceptions.Timeout:
                st.error("リクエストがタイムアウトしました。後でもう一度お試しください。")
            except requests.exceptions.RequestException as err:
                st.error(f"予期しないエラーが発生しました: {err}")
    else:
        st.warning("レビューを入力してください。")

st.write("このアプリはサクラレビュー検出のためのデモンストレーションです。")

# 環境変数の設定例
# API_URL=http://localhost:5001/classify
