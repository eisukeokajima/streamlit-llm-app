from dotenv import load_dotenv

load_dotenv()

import streamlit as st
st.title("旅行プランを聞きたい！深掘りたい！")

st.write("##### ツアーコンダクター")
st.write("ツアーコンダクターの専門家として、希望に沿った旅行プランをご提案")
st.write("##### 歴史博士　～旅先の魅力発見～")
st.write("歴史博士として旅先の質問に返答し、旅の魅力を引き出すお手伝い")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["ツアーコンダクター", "歴史博士"]
)

st.divider()

if selected_item == "ツアーコンダクター":
    input_message = st.text_input(label="旅行プランのご要望を入力してください。")

else:
    input_message = st.text_input(label="訪れる予定のスポットやイベントについて質問を入力してください。")
    
if st.button("実行"):
    st.divider()
    # ここで即時にメッセージを表示
    status = st.empty()
    status.info("AIが解答を準備中です...")

    from langchain_openai import ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if selected_item == "ツアーコンダクター":
        if input_message:
            messages = [
                SystemMessage(content="あなたはプロのツアーコンダクターです。ユーザーの要望に沿った最適な旅行プランを日本語で丁寧に提案してください。"),
                HumanMessage(content=input_message),
            ]

            with st.spinner("AIが旅行プランを作成中です..."):
                result = llm(messages)
            status.empty()  # ステータスメッセージを消す
            st.write(f"提案された旅行プラン: **{result.content}**")

        else:
            status.empty()
            st.error("要望を入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            messages = [
                SystemMessage(content="あなたは日本の歴史学者です。ユーザーが訪れる予定のスポットやイベントについての質問に、専門的かつ分かりやすく日本語で回答してください。"),
                HumanMessage(content=input_message),
            ]

            with st.spinner("AIが回答を作成中です..."):
                result = llm(messages)
            status.empty()
            st.write(f"歴史学者の回答: **{result.content}**")

        else:
            status.empty()
            st.error("ご質問を入力してから「実行」ボタンを押してください。")