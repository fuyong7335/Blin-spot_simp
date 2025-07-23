import streamlit as st
import openai

# --- APIキーの設定（streamlit secretsを利用） ---
openai.api_key = st.secrets["openai_api_key"]

# --- タイトルと説明 ---
st.set_page_config(page_title="アナタの知らないあなたを診断・簡易版", layout="centered")
st.title("アナタの知らないあなたを診断・簡易版")
st.markdown("5つの問いに直感で答えるだけで、“アナタの知らないあなた”を分析します。")

# --- 質問リスト ---
questions = [
    "他人からの評価に、ふりまわされてしまうと感じる",
    "つい頑張りすぎて、疲れることが多い",
    "本音を言うのが少し怖いと感じる",
    "誰かと比べて、自分を責めてしまうことがある",
    "感情を抑えてしまうクセがある"
]

# --- ユーザー入力 ---
responses = []
with st.form("shadow_quiz"):
    for idx, q in enumerate(questions):
        response = st.radio(q, ["はい", "いいえ", "どちらともいえない"], key=f"q{idx}")
        responses.append(response)
    submitted = st.form_submit_button("診断する")

# --- 診断ロジック（AIによるつぶやきコメント） ---
if submitted:
    prompt = """
あなたは人の心の奥深くを見つめる心理学者です。
次に紹介するユーザーの回答を読んで、その人自身も気づいていないかもしれない一面について、コメントをしてください。
思わず心に響くような、読み手が「深読み」したくなる内容だとうれしいです。
ただし、事実と異なることは言わず、理解しやすい言葉を使ってください。
難しい表現やわかりにくい単語は避けて、親しみやすい話し方でお願いします。
また、自然な日本語で回答してください。
ユーザーの中に見えるもう一人のユーザーを見つけ出し指摘してその性質を生かすためのヒントを丁寧にかつ端的に答えてください。

【回答】
"""
    import openai

client = openai.OpenAI(api_key=st.secrets["openai_api_key"])

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "あなたは優秀な心理学者でユーザーの持つ力を信じている人です"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.9,
    max_tokens=100
)


    result = response.choices[0].message.content
    st.markdown("---")
    st.subheader("診断結果")
    st.markdown(f"🌀 {result}")
    st.markdown("---")
    st.caption("アナタの知らないあなたはどんなアナタでしたか？ 明日へのヒントが見つかりますように。")
