import streamlit as st

def main():
    st.title('내 앱 대시보드')

    name = st.text_input('이름을 입력하세요!', max_chars = 10)

    st.text('입력하신 이름은 ' + name)

    message = st.text_area('메시지를 입력하세요!', height=1) # height ; 몇 줄만 표시해주세요.

    st.text(message)

    # 숫자 입력

    number = st.number_input('숫자 입력하세요~',1,100) # 정수, 실수 형변환 가능
    st.text(number * 3) 

    number2 = st.number_input('숫자 입력하세요~',1.0,100.0) # 정수, 실수 형변환 가능
    st.text(number2 * 3)

    # 날짜 입력
    my_date = st.date_input('약속 날짜 입력')
    print(my_date)
    print(type(my_date))
    st.text(my_date)

    # 시간 입력
    my_time = st.time_input('시간 선택')
    print(my_time)
    print(type(my_time))
    st.text(my_time)

    # 비밀번호 처리방법
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)

    # 색 입력
    color = st.color_picker('색을 선택하세요.')
    st.text(color)


if __name__ == '__main__':
    main() 