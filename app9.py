import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def main():
    st.title('내 앱 대시보드')
    
    df = pd.read_csv('data/iris.csv')


    st.dataframe(df)

    # sepal_length, sepal_width 의 관계를 차트로

    fig = plt.figure() # 차트의 영역을 잡아준다
    plt.scatter(data=df, x = 'sepal_length', y = 'sepal_width') # 산점도를 그려주세요!
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)


    fig2 = plt.figure() #차트의 영역을 잡아준다.
    sns.regplot(data=df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig2)

    correlation = df[['sepal_length','sepal_width']].corr() # 상관관계계수 출력
    st.dataframe(correlation)

    # sepal_length 로 히스토그램을 그리자
    # bin(범위)의 갯수는 20개로 제한

    fig3 = plt.figure(figsize=(10,4)) # 전체 차트 사이즈는 figsize에서 조절!
    plt.subplot(1,2, 1) #1행 2열중의 1번째 차트는~
    plt.hist(data= df, x='sepal_length', rwidth=0.8, bins=20) # rwidth ; 막대그래프의 간격 조정 / bin ; 막대 갯수
    
    plt.subplot(1,2, 2) #1행 2열중의 2번째 차트는~
    plt.hist(data= df, x='sepal_length', rwidth=0.8, bins=10)

    st.pyplot(fig3)


    # species 컬럼에는 종에 대한 정보가 들어있는데,
    # 각 종별로 몇개씩의 데이터가 있는지
    # 차트로 나타내시오.

    st.dataframe(df['species'].value_counts())

    fig4 = plt.figure()
    sns.countplot(data=df, x = 'species')
    st.pyplot(fig4)

    ## 데이터프레임의 차트 그리는 코드도 실행 가능!
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='barh') # kind ; ~~차트로 그려주세요~
    st.pyplot(fig5)

    # 데이터프레임 자체 plot함수는 스트림릿에서 안된다.
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7= plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)



if __name__ == '__main__':   
    main() 