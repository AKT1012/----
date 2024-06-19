import streamlit as st
import requests

# タイトルと説明の設定
st.title("レビューチェッカー")
st.write("レビューを入力すると、サクラレビューかどうかをチェックします。")

# レビューの入力フォーム
review_text = st.text_input("レビューを入力してください:")

# チェックボタン
if st.button("サクラをチェック"):
    if review_text:
        # サクラ検出APIの呼び出し
        response = requests.post('http://localhost:5001/classify', json={'review': review_text})
        
        # サクラ検出結果の表示
        if response.status_code == 200:
            result = response.json()
            if result.get('is_sakura'):
                st.error("サクラレビューが見つかりました！")
            else:
                st.success("サクラレビューは見つかりませんでした。")
        else:
            st.error("エラーが発生しました。サーバーが動作しているか確認してください。")
    else:
        st.warning("レビューを入力してください。")


st.write("このアプリはサクラレビュー検出のためのデモンストレーションです。")
