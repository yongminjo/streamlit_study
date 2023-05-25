import streamlit as st
import pandas as pd

def main():
    st.title('앱 대시보드')

    df = pd.read_csv('data/iris.csv')

    # 버튼 만들기
    if st.button('데이터 보기'):  #버튼을 누를때 (버튼을 누를때 True)
        st.dataframe(df)

    name = 'Mike'
    # 대문자 버튼을 누르면, 대문자로 표기하고
    # 소문자 버튼을 누르면, 소문자로 나오게 하자!
    if st.button('대문자'):
        st.text(name.upper())
    if st.button('소문자'):
        st.text(name.lower())

    st.dataframe(df)

    # petal_length 컬럼을 정렬하고 싶다.
    # 오름차순 정렬, 내림차순 정렬 두가지 옵션을 선택토록

    status = st.radio('정렬을 선택하세요.', ['오름차순', '내림차순'])
    
    print(status)  # 메모리의 값을 확인 -> 프린트함수로 찍어본다.

    if status == '오름차순':

        st.dataframe(df.sort_values('petal_length'))
    
    elif status == '내림차순':
        
        st.dataframe(df.sort_values('petal_length', ascending=False))

    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다.')

    # 여러개 중에 1개를 선택
    language = ['Python', 'Java', 'C', 'Go', 'PHP']

    selected_lang = st.selectbox('선호하는 언어를 선택!',language)

    if selected_lang == 'Python':
        st.text('파이썬이 최고지!')

    elif selected_lang == 'Java':
        st.text('클래스가 좀 어렵지ㅜㅜ')

    # 데이터 프레임의 컬럼 이름을 보여주고,
    # 유저가 컬럼을 선택하면
    # 해당 컬럼만 가져와서 데이터프레임을 보여주고 싶다.
    
    

    column_list = st.multiselect('컬럼을 선택하세요.', df.columns)
    ## 리스트로 리턴.

    print(column_list)  # 메모리의 상황을 확인할 수 있다.

    # 선택한 컬럼으로 데이터프레임을 보여주기!
    st.dataframe(df[column_list])

    age = st.slider('나이', min_value = 10, max_value=110, value=50)

    st.text('나이는 ' + str(age) + ' 입니다.')

    with st.expander('hello'):
        st.text('안녕하세요!')

if __name__ == '__main__':    
    main() 