"""A humorous spending-habit quiz built with Streamlit.

Run locally with:
    streamlit run streamlit_habit.py

Needs the three meme image files to sit next to this script:
    이재용 쉿.jpeg, dja.jpeg, 다운로드 (1).jpeg
"""

import streamlit as st


st.set_page_config(
    page_title="소비습관 테스트",
    page_icon="💸",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    .stApp, .stApp p, .stApp span, .stApp label,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4,
    .stApp div, .stMarkdown, .stCaption {
        color: #000000 !important;
    }
    div[data-testid="stButton"] button {
        border-radius: 14px;
        border: 2px solid #eaeaea;
        background-color: #fafafa;
        color: #000000 !important;
        text-align: left;
        justify-content: flex-start;
        white-space: normal;
        padding: 14px 16px;
        transition: all 120ms ease;
    }
    div[data-testid="stButton"] button:hover {
        border-color: #000000;
        background-color: #f2f2f2;
    }
    div[data-testid="stButton"] button[kind="primary"] {
        background-color: #000000;
        border-color: #000000;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


QUESTIONS = [
    {
        "prompt": "월급(혹은 용돈)이 들어온 당일, 당신의 심리 상태는?",
        "options": [
            ("일단 고정비·저축부터 자동이체 걸어놓고 숨 쉰다", 4),
            ("조금은 쓰지만 큰 틀에서 계획대로 쓴다", 3),
            ("일단 먹고 싶은 거부터 시킨다, 계획은 내일의 나에게", 2),
            ("통장이 숨 쉴 틈도 안 주고 바로 '텅장'행 급행열차 탑승", 1),
        ],
    },
    {
        "prompt": "장바구니에 담아둔 물건, 며칠 뒤 다시 보면?",
        "options": [
            ("3일 이상 지나도 필요하면 산다 (쿨타임 지킴이)", 4),
            ("할인할 때만 산다", 3),
            ("이미 '구매완료' 문자가 와있다", 1),
            ("장바구니는 그냥 거쳐가는 정류장이다, 바로 결제", 1),
        ],
    },
    {
        "prompt": "배달 앱 / 카페 앱 알림이 뜨면?",
        "options": [
            ("알림 끈 지 오래, 내 눈엔 안 보인다", 4),
            ("가끔 보긴 하는데 참을 때가 많다", 3),
            ("'오늘만 특별히'를 거의 매일 외친다", 2),
            ("손이 먼저 앱을 열고 있다, 이미 주문 완료", 1),
        ],
    },
    {
        "prompt": "지금 당장 '이번 달 구독 서비스'가 몇 개인지 말할 수 있나요?",
        "options": [
            ("정확히 몇 개, 얼마 나가는지까지 외우고 있다", 4),
            ("대충은 안다, 큰 것들만", 3),
            ("글쎄... 넷플릭스는 있는 것 같다", 2),
            ("모른다, 그리고 알고 싶지도 않다", 1),
        ],
    },
    {
        "prompt": "친구가 '이거 요즘 핫하대' 하면서 뭔가를 추천하면?",
        "options": [
            ("필요한지 따져보고 안 필요하면 패스", 4),
            ("찜해두고 한번 검색은 해본다", 3),
            ("'오 그래?' 하면서 바로 검색창에 입력", 2),
            ("말 끝나기도 전에 이미 결제 중", 1),
        ],
    },
    {
        "prompt": "비상금(예상치 못한 지출 대비 자금)에 대해 솔직히 말하면?",
        "options": [
            ("3~6개월치 생활비는 따로 모아놨다", 4),
            ("적지만 조금은 있다", 3),
            ("비상금... 그게 뭔가요? 먹는 건가요?", 2),
            ("비상금은커녕 다음 월급도 당겨써야 할 판", 1),
        ],
    },
    {
        "prompt": "이번 달 카드값 명세서를 보는 당신의 반응은?",
        "options": [
            ("예상한 범위 안이라 평온하다", 4),
            ("약간 놀라지만 바로 수긍한다 ('맞다 그거 샀지')", 3),
            ("'이게 다 뭐지?' 하며 식은땀이 난다", 2),
            ("명세서 확인을 미루고 있다, 무서워서 못 본다", 1),
        ],
    },
    {
        "prompt": "스트레스 받는 날, 당신의 셀프 처방은?",
        "options": [
            ("산책, 운동, 수면 등 돈 안 드는 방법을 먼저 찾는다", 4),
            ("소소한 간식 하나 사먹는 정도로 푼다", 3),
            ("'플렉스'가 필요해, 작은 지름으로 해소한다", 2),
            ("'힐링엔 역시 쇼핑'이라며 큰 결제가 들어간다", 1),
        ],
    },
]


RESULTS = {
    "good": {
        "emoji": "👑",
        "title": "소비습관 甲 (아주 좋음)",
        "badge": "미래의 이재용 🤫",
        "badge_color": "#2ecc71",
        "image": "이재용 쉿.jpeg",
        "desc": """
솔직히 말할게요. 당신 주변 사람들 통장 사정을 다 합쳐도 당신 혼자 이기는 레벨입니다. 😮

충동구매는 당신 사전에 없는 단어고, 비상금은 이미 비상 상황을 대비해 비상 대기 중이죠.
카드 명세서를 봐도 심장이 평온한 그 능력, 정말 아무나 가진 게 아닙니다.
이 정도면 "쉿, 비밀인데 나 사실 부자야" 해도 믿을 각.

**단 하나의 리스크:** 너무 안 쓰다가 가끔은 스스로에게도 작은 선물 하나쯤 해줘도 됩니다.
아낀 돈, 당신이 쓰라고 있는 거예요 😉
""",
    },
    "normal": {
        "emoji": "🙂",
        "title": "소비습관 보통 (평범)",
        "badge": "염.....",
        "badge_color": "#f5a623",
        "image": "dja.jpeg",
        "desc": """
극단적으로 아끼지도, 흥청망청 쓰지도 않는 딱 '중간' 라인입니다.
어떤 날은 계획적이고, 어떤 날은 배달앱 알림에 홀리는 그런 사람이죠. 😅

누가 "너 소비습관 어때?"라고 물으면 저 고양이처럼 "염.....( 침묵 )" 하고
눈만 깜빡이게 되는 애매~한 포지션. 나쁘지 않지만 '이번 달도 뭐 산 것도 없는데
왜 텅장이지?' 싶은 날이 가끔 있을 뿐입니다.

**한 줄 처방:** 가계부 앱 하나만 깔아도 등급업 가능성 충분합니다.
""",
    },
    "bad": {
        "emoji": "🔥",
        "title": "소비습관 적신호 (안 좋음)",
        "badge": "난가? 아... 😭",
        "badge_color": "#e74c3c",
        "image": "다운로드 (1).jpeg",
        "desc": """
축하합니다, 당신은 지름신의 총애를 받는 소수의 선택된 자입니다. 🙏

장바구니는 당신에게 '숙고의 시간'이 아니라 '결제 직전 정류장'이고,
월급날의 기쁨은 보통 3일 안에 소멸되는 걸로 유명하죠.
"가난을 거꾸로 읽으면?"이라는 질문에 저도 모르게 "난가...?"라고 답하게 되는
그 마음, 저희는 압니다.

**그래도 희망은 있어요.** 지금 이 순간 '아 나 좀 심한가?' 하고 자각했다는 것
자체가 큰 발전입니다. 일단 알림부터 끄고, 비상금 10만원부터 시작해봐요.
작게 시작하면 됩니다 💪
""",
    },
}


def initialize_state():
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "completed" not in st.session_state:
        st.session_state.completed = False


def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.answers = {}
    st.session_state.completed = False


def pick_result(total_score):
    if total_score >= 26:
        return RESULTS["good"]
    if total_score >= 16:
        return RESULTS["normal"]
    return RESULTS["bad"]


def show_result():
    total_score = sum(st.session_state.answers.values())
    max_score = len(QUESTIONS) * 4
    result = pick_result(total_score)

    st.progress(1.0, text="테스트 완료!")
    st.markdown(f"<div style='font-size:3.5rem;text-align:center;'>{result['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>{result['title']}</h2>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style='text-align:center;margin-bottom:16px;'>
            <span style='background:{result["badge_color"]};color:white !important;
            padding:6px 16px;border-radius:20px;font-weight:700;font-size:0.9rem;'>
            {result['badge']}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    img_col = st.columns([1, 2, 1])[1]
    with img_col:
        st.image(result["image"], use_container_width=True)

    st.caption(f"총점 {total_score} / {max_score}점")
    st.markdown(result["desc"])

    if st.button("🔄 다시 테스트하기", use_container_width=True, type="primary"):
        restart_quiz()
        st.rerun()


initialize_state()

st.title("💸 소비습관 테스트")
st.caption("당신은 저축왕? 지름신? 그냥 평범한 월급루팡?")

if st.session_state.completed:
    show_result()
else:
    current_index = st.session_state.current_index
    question = QUESTIONS[current_index]

    st.progress(current_index / len(QUESTIONS), text=f"진행률 · {current_index}/{len(QUESTIONS)}")
    st.caption(f"Q{current_index + 1} / {len(QUESTIONS)}")
    st.subheader(question["prompt"])

    for option_text, score in question["options"]:
        if st.button(option_text, key=f"q{current_index}_{option_text}", use_container_width=True):
            st.session_state.answers[current_index] = score
            if current_index < len(QUESTIONS) - 1:
                st.session_state.current_index += 1
            else:
                st.session_state.completed = True
            st.rerun()

    st.divider()
    nav_cols = st.columns(2)
    with nav_cols[0]:
        if st.button("← 이전 질문", disabled=current_index == 0, use_container_width=True):
            st.session_state.current_index -= 1
            st.rerun()
    with nav_cols[1]:
        if st.button("처음으로", use_container_width=True):
            restart_quiz()
            st.rerun()
