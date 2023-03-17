import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
import numpy as np
from data import *
from text import *

st.set_page_config(layout='wide',initial_sidebar_state="expanded")



chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

nav = option_menu(
        menu_title=None,
        options=['Introduction','Methodology','Charts','Conclusion','About'],
        icons=['book','stack','graph-up','award','exclamation-diamond-fill'],
        orientation='horizontal'
    )


if nav == 'Introduction':
  st.markdown(INTRODUCTION_1)
  st.markdown(INTRODUCTION)

if nav == 'Methodology':
  st.markdown(METHODOLOGY)

if nav == 'Charts':
  options = ['Overall Weekly Metrics', 'Daily Metrics', 'Liquidity Pool Actions', 'Stake Activity','Swap Activity','User Retention']
  st.markdown('#### Select one or more subjects from the box below')
  chart_nav = st.multiselect(label='',options=options,default=['Overall Weekly Metrics'])
  
  #Overall Weekly Metrics'
  if options[0] in chart_nav:
    op = options[0]
    charts = get_charts(op)
    st.title(op)
    col1,col2 = st.columns(2)
    with col1:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[0])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[2])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[4])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[6])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[8])

    with col2:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[1])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[3])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[5])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[7])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[9])
    st.markdown(Overall_Weekly_Metrics)


  #Daily Metrics
  if options[1] in chart_nav:
    op = options[1]
    charts = get_charts(op)
    st.title(op)
    col1,col2 = st.columns(2)

    with col1:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[0])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[2])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[4])

    with col2:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[1])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[3])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[5])

    st.markdown(Daily_Metrics)


  #Liquidity Pool Actions
  if options[2] in chart_nav:
    op = options[2]
    st.title(op)
    charts = get_charts(op)
    cont1 = st.container()
    cont2 = st.container()
    with cont1:
      col1,col2 = st.columns(2)
      with col1:
        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[0])

        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[2])

      with col2:
        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[1])


        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[3])
      st.markdown(Liquidity_Pool_Actions_1)

    with cont2:
      col1,col2 = st.columns(2)
      with col1:
        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[4])


        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[6])


      with col2:
        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[5])
      st.markdown(Liquidity_Pool_Actions_2)


  #Stake Activity
  if options[3] in chart_nav:
    op = options[3]
    st.title(op)
    charts = get_charts(op)
    cont1 = st.container()
    cont2 = st.container()
    with cont1:
      col1,col2 = st.columns(2)
      with col1:
        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[0])

        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[2])


        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[4])

      with col2:
        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[1])

        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[3])


        st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
        st.plotly_chart(charts[5])
      st.markdown(Stake_Activity_1)


    with cont2:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[6])


      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[7])
      st.markdown(Stake_Activity_2)


  #Swap Activity
  if options[4] in chart_nav:
    op = options[4]
    charts = get_charts(op)
    st.title(op)
    col1,col2 = st.columns(2)
    with col1:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[0])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[2])


    with col2:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[1])

      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[3])
    
    st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
    st.plotly_chart(charts[4])
    st.markdown(Swap_Activity)



  #User Retention
  if options[5] in chart_nav:
    op = options[5]
    st.title(op)
    charts = get_charts(op)
    cont1 = st.container()
    cont2 = st.container()
    with cont1:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[0])
      st.markdown(User_Retention_1)

    with cont2:
      st.markdown("[source code](https://app.flipsidecrypto.com/dashboard/2JCfzm)")
      st.plotly_chart(charts[1])
      st.markdown(User_Retention_2)



if nav == 'Conclusion':
  st.markdown(Conclusion)

if nav == 'About':
  st.markdown(About)