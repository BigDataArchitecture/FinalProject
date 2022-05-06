from itertools import count
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import plost


def analytics(user1):


#data_load_state = st.text('Loading data...')
    placeholder = st.empty()
    #create three columns
    # kpi1, kpi2, kpi3 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    # kpi1.metric(
    #     label="Total Page Hits ⏳",
    #     value=count(user_data['user_id']==user)
    #     #delta=round(avg_age) - 10,
    # )

    # kpi2.metric(
    #     label="Time Spent"
    #     # value=int(count_married),
    #     # delta=-10 + count_married,
    # )

    # kpi3.metric(
    #     label="Temp",
    #     # value=f"$ {round(balance,2)} ",
    #     # delta=-round(balance / count_married) * 100,
    # )
    # create two columns for charts

    fig_col1, fig_col2 = st.columns((7,3))

    with fig_col1:
        st.markdown("#### Keywords Searched")
        fig2 = px.histogram(user1, x="keywords")
        st.write(fig2)
    
    st.markdown('##### Sentiments of keywords searched')
    fig = px.line(user1, 
    x = "sentiment", y = "count", title = user)
    st.plotly_chart(fig)
        
    st.markdown('#### Location of tweets')
    plost.donut_chart(
            data=user1 ,
            theta='location',
            color='location')

st.title('User Analytics dashboard')
user_data = pd.read_csv('users.csv')

clist=user_data['user_id'].unique()
user = st.sidebar.selectbox("Select a user:",clist)
user1 = user_data[user_data['user_id'] ==user]
analytics(user1)
    
