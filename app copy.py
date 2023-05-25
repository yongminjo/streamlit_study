import streamlit as st 
from PIL import Image  # 파이썬에서 이미지를 처리하는 유명한 라이브러리

def main():
    st.title('내 앱 대시보드')

    # 사진과 영상을 보여주는 방법

    img = Image.open('data/image_03.jpg')

    print(img)

    st.image(img)

    st.image(img, use_column_width=True) #use_column_width ; 옆으로 꽉차게 보여주세요

if __name__ == '__main__':
    main() 