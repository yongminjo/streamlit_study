import streamlit as st 
from PIL import Image  # 파이썬에서 이미지를 처리하는 유명한 라이브러리

def main():
    st.title('내 앱 대시보드')

    # 사진과 영상을 보여주는 방법

    img = Image.open('data/image_03.jpg')

    # 이미지 URL로 불러와서 보여주기

    print(img)

    st.image(img)

    st.image(img, use_column_width=True) #use_column_width ; 옆으로 꽉차게 보여주세요

    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')

    video_file = open('data/video1.mp4', 'rb') # 'rb' ; 바이너리 파일을 읽어주세요.
    st.video(video_file)

if __name__ == '__main__':
    main() 