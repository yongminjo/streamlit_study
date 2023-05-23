import streamlit as st  # 스트림릿 라이브러리(앱 대시보드) 임포트.

def main():
    st.title('내 앱 대시보드')
    st.text('데이터 분석 앱입니다.')
    st.text('테스트 앱입니다.')

if __name__ == '__main__':     ## 스트림릿 가장 기본적인 형태
    main()     #서버를 끌땐 컨트롤키 + C