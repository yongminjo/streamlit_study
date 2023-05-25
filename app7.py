import streamlit as st
from datetime import datetime # 날짜시간 관련 라이브러리!
import os 
import pandas as pd


# 디렉터리 이름과, 파일을 주면 해당 디렉터리에 파일을 저장해주는 함수
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉터리가 있는지 확인하고, 없으면 디렉터리를 먼저 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 디렉터리가 있으니, 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 저장 완료!')


def main():
    st.title('내 앱 대시보드')

    menu = ['Image Upload', 'CSV Upload', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        st.subheader('이미지 파일 업로드')

        img_file = st.file_uploader('이미지를 업로드 하세요!', type=['png', 'jpg', 'jpeg'])
        if img_file is not None:  # 이미지 파일이 있을때 동작해주세요.
            
            print(type(img_file))

            print(img_file.name)
            print(img_file.size)
            print(img_file.type)

            # 유저가 올린 파일을, 서버에서 유니크하게(중복되지 않게) 처리하기 위해서 
            # 파일명을 현재시간 조합으로 해서 만든다.

            current_time = datetime.now()
            print(current_time)
            print(current_time.isoformat().replace(':','_') + '.jpg')
            # 파이썬 형식을 사람의 형태(세계표준)으로 바꿔주세요. / 콜론(:)을 언더스코어(_)로 바꿔주세요.

            filename = current_time.isoformat().replace(':','_') + '.jpg'
            
            img_file.name = filename

            save_uploaded_file('image', img_file )

            st.image('image/' + filename)

    elif choice == menu[1]:
        st.subheader('CSV 파일 업로드')
        
        csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'])
        if csv_file is not None :
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':','_') + '.csv'
            csv_file.name = filename

            save_uploaded_file('csv', csv_file)
            df = pd.read_csv('csv/'+filename)
            st.dataframe(df)


    else :
        st.subheader('이 대시보드 설명')


    print(choice)





if __name__ == '__main__':
    main()  