import streamlit as st

# 페이지 레이아웃 설정
st.set_page_config(
    page_title="Language 모듈",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS로 스타일 조정
st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    .stProgress > div > div > div > div {
        background-color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

st.title('Language 모듈')

# 메인 컨테이너
with st.container():
    # 캐릭터 선택을 상단에 배치
    st.subheader('분석가 선택')
    character = st.radio(
        "분석 스타일을 선택하세요:",
        ['유비 (친절한 분석)', '관우 (엄격한 분석)', '장비 (과격한 분석)'],
        horizontal=True  # 가로로 배치
    )

    # 구분선 추가
    st.divider()

    # 두 컬럼으로 레이아웃 구성
    col1, col2 = st.columns([2, 3])

    with col1:
        # 음식 선택
        food = st.selectbox(
            '분석할 음식을 선택하세요:',
            ['짜장면', '칼국수', '메밀국수']
        )

    # 음식별 정보 딕셔너리
    food_info = {
        '짜장면': {
            '칼로리': 800,
            '설명': {
                '유비': "짜장면은 균형 잡힌 한 끼 식사입니다. 면과 야채가 적절히 어우러져 있네요.",
                '관우': "짜장면의 탄수화물 함량이 다소 높습니다. 운동을 병행하시는 것을 추천드립니다.",
                '장비': "이 정도는 기본이지! 양념장 더 넣고 곱배기로 가자고!"
            }
        },
        '칼국수': {
            '칼로리': 600,
            '설명': {
                '유비': "칼국수는 정성이 가득 담긴 음식입니다. 국물이 깔끔하네요.",
                '관우': "면의 양을 조절하면 더 건강한 식사가 될 수 있습니다.",
                '장비': "국물까지 원샷! 수제비 추가하면 더 맛있을텐데!"
            }
        },
        '메밀국수': {
            '칼로리': 400,
            '설명': {
                '유비': "메밀국수는 깔끔하고 건강한 선택입니다. 좋은 선택이에요!",
                '관우': "저칼로리 식사로 적합합니다. 단백질 보충을 고려해보세요.",
                '장비': "이걸로 배가 찰까? 고기 추가 필수다!"
            }
        }
    }

    # 선택된 캐릭터의 스타일 표시
    character_name = character.split(' ')[0]

    with col2:
        # 음식 분석 결과 표시
        st.header(f'🍜 {food} 분석 결과')

        # 음식 설명
        st.subheader("💭 분석가의 한마디")
        st.write(food_info[food]['설명'][character_name])

        # 칼로리 표시
        st.subheader("📊 일일 권장 칼로리 대비 섭취량")
        calories = food_info[food]['칼로리']
        progress = calories / 2000  # 2000칼로리 기준
        
        # 프로그레스 바와 텍스트를 컨테이너로 묶기
        with st.container():
            st.progress(progress)
            st.write(f"섭취 칼로리: {calories}kcal (권장량의 {progress*100:.1f}%)")

        # 추가 정보
        st.info(f'💡 일일 권장 칼로리 2000kcal 기준, {food}({calories}kcal)는 약 {(calories/2000*100):.1f}%를 차지합니다.')