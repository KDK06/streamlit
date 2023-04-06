import streamlit as st

st.set_page_config(
    page_title="체육대회 종목 조사",
    page_icon='⚾'
)

st.sidebar.title('2023년 4월 25일까지 제출')


st.title('구암고 :red[체육대회] 종목 투표')



학년 = st.text_input('학년','')
반 = st.text_input('반','')
번호 = st.text_input('번호','')
이름 = st.text_input('이름','')



개인종목 = st.radio("원하는 개인 종목에 투표해주세요",('50m 계주', '티볼 멀리치기', '800m 이어달리기'),
                      horizontal=True)

if 개인종목 == '50m 계주':
    st.caption('50m 계주를 선택했습니다')
elif 개인종목 == '티볼 멀리치기':
    st.caption('티볼 멀리치기를 선택했습니다')
else:
    st.caption('800m 이어달리기를 선택했습니다.')

단체종목 = st.multiselect('원하는 단체 종목에 투표해주세요(중복 투표 가능)'
                       , ['줄다리기', '장기자랑', '8자 줄넘기', '파도타기'])

btn = st.button('제출하기')



if btn:
    if 학년:
        if 반:
            if 번호:
                if 이름:
                    if 개인종목:
                        if 단체종목:
                            st.header('제출하셨습니다.')
                            st.balloons()
                        else:
                            st.header('단체종목을 고르시오')
                else:
                    st.header('이름을 적으세요')
            else:
                st.header('번호를 적으세요')
        else:
            st.header('반을 적으세요')
    else:
        st.header('학년을 적으세요')











