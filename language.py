import streamlit as st
import plotly.graph_objects as go
from PIL import Image

st.title('l')

# 왼쪽 사이드바에 캐릭터 선택 옵션
st.sidebar.header('캐릭터 선택')
character = st.sidebar.radio(
    "분석가를 선택하세요:",
    ['유비 (친절한 분석)', '관우 (엄격한 분석)', '장비 (과격한 분석)']
)

# 음식 선택 (오른쪽 상단)
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

# 음식 분석 결과 표시
st.header(f'🍜 {food} 분석 결과')

# 음식 설명
st.subheader("💭 분석가의 한마디")
st.write(food_info[food]['설명'][character_name])

# 칼로리 그래프
st.subheader("📊 일일 권장 칼로리 대비 섭취량")
calories = food_info[food]['칼로리']
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = calories,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "칼로리"},
    gauge = {
        'axis': {'range': [None, 2000]},
        'bar': {'color': "darkblue"},
        'steps': [
            {'range': [0, 800], 'color': "lightgray"},
            {'range': [800, 1500], 'color': "gray"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': calories
        }
    }
))

st.plotly_chart(fig)

# 추가 정보
st.info(f'💡 일일 권장 칼로리 2000kcal 기준, {food}({calories}kcal)는 약 {(calories/2000*100):.1f}%를 차지합니다.')