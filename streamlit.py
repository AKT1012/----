import streamlit as st
import requests

# タイトルと説明の設定
st.title("レビューチェッカー")
st.write("商品ページのURLを入力すると、レビューにサクラが存在するかをチェックします。")

# 商品URLの入力フォーム
product_url = st.text_input("商品ページのURLを入力してください:")

# チェックボタン
if st.button("サクラをチェック"):
    if product_url:
        st.write("商品URL:", product_url)
        st.write("レビューを解析中...")
        
        # レビュー取得のシンプルな例
        reviews = [
            "この商品は素晴らしいです！また購入したいです。",
            "この商品は最悪です。お金の無駄です。",
        ]
        
        # モデルAPIにリクエストを送信
        response = requests.post('http://localhost:5001/classify', json={'reviews': reviews})
        
        if response.status_code == 200:
            results = response.json()
            for review, result in zip(reviews, results):
                if "サクラレビュー" in result:
                    st.error(f"サクラレビューが見つかりました！: {review}")
                else:
                    st.success(f"サクラレビューは見つかりませんでした: {review}")
        else:
            st.warning("レビューの解析に失敗しました。")
    else:
        st.warning("商品ページのURLを入力してください。")

# フッター
st.write("このアプリはサクラレビュー検出のためのデモンストレーションです。")

