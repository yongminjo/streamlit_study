import streamlit as st  
import pandas as pd

def main():
    st.title('내 앱 대시보드')

    df = pd.read_csv('data/iris.csv')
    # print(df)  ## 터미널창에만 보임

    st.dataframe(df) # 데이터 프레임을 표현

    species = df['species'].unique()

    st.text('아이리스 꽃은' + species + '으로 되어있다.')

    st.write( df.head() )

if __name__ == '__main__':
    main() 