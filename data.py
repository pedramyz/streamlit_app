import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from text import *


# def get_url(x,y):
#     url_dict = {
#         'Overall Weekly Metrics' : {
#             '1-3':"https://app.flipsidecrypto.com/velocity/queries/ccf1153e-a4a0-4dd7-9439-36d15bf98d97",
#             '4' : "https://app.flipsidecrypto.com/velocity/queries/7159ad22-cb22-4d34-b42f-75e470d1c76b",
#             '5-7' : "https://app.flipsidecrypto.com/velocity/queries/b25071a0-9702-4be2-8975-fb189c019966",
#             '8-10' : "https://app.flipsidecrypto.com/velocity/queries/5a94ac82-8780-442a-bc95-2069f9f3a229"
#         },
#         'Daily Metrics' : {
#             '1-3' : "https://app.flipsidecrypto.com/velocity/queries/7f637c72-ce0e-49d1-acfe-808bc02e77aa",
#             '4' : "https://app.flipsidecrypto.com/velocity/queries/3d143cd2-d202-40da-b4b6-d066ec039a0a",
#             '5-6' : "https://app.flipsidecrypto.com/velocity/queries/7f637c72-ce0e-49d1-acfe-808bc02e77aa"
#         },
#         'Liquidity Pool Actions':{
#             '1-4' : "https://app.flipsidecrypto.com/velocity/queries/93e032f9-0ac0-4281-87de-3a8dcdf01693",
#             '5-7' : "https://app.flipsidecrypto.com/velocity/queries/93e032f9-0ac0-4281-87de-3a8dcdf01693"   
#         },
#         'Stake Activity' : {
#             '1-6' : "https://app.flipsidecrypto.com/velocity/queries/b5ba353a-b718-4626-8469-b75a7f93526d",
#             '7' : "https://app.flipsidecrypto.com/velocity/queries/6fdef755-d24d-4c84-aaa2-4281108eed56",
#             '8' : "https://app.flipsidecrypto.com/velocity/queries/397457eb-b07a-4b08-96ea-f8731b25ff52"
#         },
#         'Swap Activity' : {
#             '1-2' :  "https://app.flipsidecrypto.com/velocity/queries/189ba7fa-ba32-41b1-9c29-5881980d316d",
#             '3': "https://app.flipsidecrypto.com/velocity/queries/6a6bbe9e-5394-4a31-a0ff-d55f113e7511",
#             '4': "https://app.flipsidecrypto.com/velocity/queries/1478c91c-55f9-4961-b710-d00c17d42e39",
#             '5':"https://app.flipsidecrypto.com/velocity/queries/eb17da4d-502f-4980-b5ed-ed8cd76db5fd"
#         },
#         'User Retention' : {
#             '1' : "https://app.flipsidecrypto.com/velocity/queries/c3710dd7-5480-4667-bc03-a20233aaa725",
#             '2' : "https://app.flipsidecrypto.com/velocity/queries/902ffc17-c9fc-402a-b802-81e9ad6ee544"
#         }
#     }
#     return url_dict[x][y]




def get_df(x,y):
    df_dict = {
        'Overall Weekly Metrics' : {
            '1-3':pd.read_csv('csv_files/Overall_Weekly_Metrics/1_3.csv'),
            '4' : pd.read_csv('csv_files/Overall_Weekly_Metrics/4.csv'),
            '5-7' : pd.read_csv('csv_files/Overall_Weekly_Metrics/5_7.csv'),
            '8-10' : pd.read_csv('csv_files/Overall_Weekly_Metrics/8_10.csv')
        },
        'Daily Metrics' : {
            '1-3' : pd.read_csv('csv_files/Daily_Metrics/1_3.csv'),
            '4' : pd.read_csv('csv_files/Daily_Metrics/4.csv'),
            '5-6' : pd.read_csv('csv_files/Daily_Metrics/5_6.csv')
        },
        'Liquidity Pool Actions':{
            '1-4' : pd.read_csv('csv_files/Liquidity_Pool_Actions/1_4.csv'),
            '5-7' : pd.read_csv('csv_files/Liquidity_Pool_Actions/5_7.csv')   
        },
        'Stake Activity' : {
            '1-6' : pd.read_csv('csv_files/Stake_Activity/1_6.csv'),
            '7' :  pd.read_csv('csv_files/Stake_Activity/7.csv'),
            '8' :  pd.read_csv('csv_files/Stake_Activity/8.csv')
        },
        'Swap Activity' : {
            '1-2' :  pd.read_csv('csv_files/Swap_Activity/1_2.csv'),
            '3': pd.read_csv('csv_files/Swap_Activity/3.csv'),
            '4': pd.read_csv('csv_files/Swap_Activity/4.csv'),
            '5': pd.read_csv('csv_files/Swap_Activity/5.csv')
        },
        'User Retention' : {
            '1' : pd.read_csv('csv_files/User_Retention/1.csv'),
            '2' : pd.read_csv('csv_files/User_Retention/2.csv')
        }
    }
    return df_dict[x][y]


def clean(fig,wide):
    if wide:
        return fig.update_layout(xaxis_title=None,yaxis_title=None,width=1200)
    return fig.update_layout(xaxis_title=None,yaxis_title=None,width=570)
    


def get_charts(subject):
    if subject == 'Overall Weekly Metrics':
        charts = []

        df = get_df('Overall Weekly Metrics','1-3')
        charts.append(px.bar(df,x='TIMELINE',y='DAILY_USER',color='TIMELINE',title='Number Of Users'))
        charts.append(px.bar(df,x='TIMELINE',y='DAILY_TRANSACTION',color='TIMELINE',title='Number Of Transactions'))
        charts.append(px.bar(df,x='TIMELINE',y='DAILY_AVG_FEE',color='TIMELINE',title='Average Transaction Fees'))

        df = get_df('Overall Weekly Metrics','4')
        charts.append(px.bar(df,x='TIMELINE',y='DAILY_NEW_WALLET',color='TIMELINE',title='New Wallets Created'))

        df = get_df('Overall Weekly Metrics','5-7')
        charts.append(px.bar(df,x='TIMELINE',y='LP_TRANSACTION_COUNT',color='TIMELINE',title='Number Of LP Transactions'))
        charts.append(px.bar(df,x='TIMELINE',y='USER_COUNT',color='TIMELINE',title='Number Of LP Users'))
        charts.append(px.bar(df,x='TIMELINE',y='TOTAL_ACTION_AMOUNT',color='TIMELINE',title='Volume Of LP Transactions'))

        df = get_df('Overall Weekly Metrics','8-10')
        charts.append(px.bar(df,x='TIMELINE',y='USERS_COUNT',color='TIMELINE',title='Number Of Staking Transactions'))
        charts.append(px.bar(df,x='TIMELINE',y='STAKE_COUNT',color='TIMELINE',title='Number Of Staking Users'))
        charts.append(px.bar(df,x='TIMELINE',y='TOTAL_AMOUNT',color='TIMELINE',title='Total Volume$ Of Staking Transactions'))

        charts = [clean(chart,False) for chart in charts]
        return charts

    if subject == 'Daily Metrics':
        charts = []

        df = get_df('Daily Metrics','1-3')
        charts.append(px.bar(df,x='DATE',y='DAILY_TRANSACTION',color='TIMELINE',title='Number Of Transactions'))
        charts.append(px.bar(df,x='DATE',y='DAILY_USER',color='TIMELINE',title='Number Of Users'))
        charts.append(px.bar(df,x='DATE',y='DAILY_AVG_FEE',color='TIMELINE',title='Daily Average Transaction Fees'))

        df = get_df('Daily Metrics','4')
        charts.append(px.bar(df,x='DATE',y='DAILY_NEW_WALLET',color='TIMELINE',title='Daily New Wallets Created On Terra Since Jan 1'))

        df = get_df('Daily Metrics','5-6')
        charts.append(px.area(df,x='DATE',y='DAILY_USER',color='TIMELINE',title='Cumulative Number Of Users Since Jan 1'))
        charts.append(px.area(df,x='DATE',y='DAILY_TRANSACTION',color='TIMELINE',title='Cumulative Number Of Transactions Since Jan 1'))

        charts = [clean(chart,False) for chart in charts]
        return charts

    if subject == 'Liquidity Pool Actions':
        charts = []

        df = get_df('Liquidity Pool Actions','1-4')
        l1 =  px.bar(df,x='DATE',y='LP_TRANSACTION_COUNT',color='TIMELINE')
        b1 =  px.line(df.groupby('DATE',as_index=False)['USER_COUNT'].sum(),x='DATE',y='USER_COUNT',color=px.Constant("LP_TRANSACTION_COUNT"))
        charts.append(go.Figure(data=b1.data + l1.data).update_layout(title='Daily Number Of Liquidity Pool Transactions In Correlation With Users'))
        charts.append(px.bar(df,x='DATE',y='USER_COUNT',color='TIMELINE',title='Daily Number Of Liquidity Pool Users'))
        charts.append(px.bar(df,x='DATE',y='TOTAL_ACTION_AMOUNT',color='TIMELINE',title='Daily Volume$ Of Liquidity Pool Transactions'))
        charts.append(px.bar(df,x='DATE',y='AVG_ACTION_AMOUNT',color='TIMELINE',title='Average Volume$ Of Liquidity Pool Transactions'))

        df = get_df('Liquidity Pool Actions','5-7')
        charts.append(px.bar(df,x='DATE',y='LP_TRANSACTION_COUNT',color='ACTION',title='Number Of LP Transactions Specified by Action Since Jan 1'))
        charts.append(px.bar(get_df('Liquidity Pool Actions','5-7'),x='DATE',y='USER_COUNT',color='ACTION',title='Number Of LP Users Specified By Action Since Jan 1'))
        charts.append(px.bar(get_df('Liquidity Pool Actions','5-7'),x='DATE',y='TOTAL_ACTION_AMOUNT',color='ACTION',title='Volume$ Of Liquidity Pool Transactions Specified By Action Since Jan 1'))

        charts = [clean(chart,False) for chart in charts]
        return charts
    
    if subject == 'Stake Activity':
        charts = []

        df = get_df('Stake Activity','1-6')
        df.columns = ['STAKED','TIMELINE','DATE','STAKE_COUNT','USERS_COUNT','TOTAL_AMOUNT','AVG_AMOUNT','NAN']        
        l = px.line(df.groupby("DATE",as_index=False)['USERS_COUNT'].sum(),x="DATE",y='USERS_COUNT')
        b1 = px.bar(df,x="DATE",y='STAKE_COUNT',color='TIMELINE')
        b2 = px.bar(df,x="DATE",y='STAKE_COUNT',color='STAKED')
        charts.append(go.Figure(data=b1.data + l.data ))
        charts.append(go.Figure(data=b2.data + l.data ))
        charts.append(px.bar(df,x="DATE",y='USERS_COUNT',color='TIMELINE'))
        charts.append(px.bar(df,x="DATE",y='USERS_COUNT',color='STAKED'))
        charts.append(px.bar(df,x="DATE",y='TOTAL_AMOUNT',color='TIMELINE'))
        charts.append(px.bar(df,x="DATE",y='TOTAL_AMOUNT',color='STAKED'))

        df = get_df('Stake Activity','7')
        charts.append(px.bar(df,x="TOTAL_AMOUNT",y='USERS',orientation='h'))

        df = get_df('Stake Activity','8')
        charts.append(px.bar(df,x="TOTAL_AMOUNT",y='USERS',orientation='h'))

        charts = [clean(chart,False) for chart in charts]
        charts[6] = charts[6].update_layout(width=1200)
        charts[7] = charts[7].update_layout(width=1200)
        return charts

    if subject == 'Swap Activity':
        charts = []

        df = get_df('Swap Activity','1-2')
        df.columns = ['TIMELINE','DATE','SWAPPER_COUNT','SWAP_COUNT','NAN']
        line_fig_df = df.groupby('DATE',as_index=False)['SWAPPER_COUNT'].sum()
        l1 =  px.line(line_fig_df,x='DATE',y='SWAPPER_COUNT',color=px.Constant('swaper count'))
        b1 = px.bar(df,x='DATE',y='SWAP_COUNT',color='TIMELINE')
        charts.append(go.Figure(data=b1.data + l1.data))
        charts.append(px.bar(df,x='DATE',y='SWAPPER_COUNT',color='TIMELINE',title='Number of Swappers'))

        df = get_df('Swap Activity','3')
        charts.append(px.pie(values=df['SWAPS_COUNT'],names=df['PRICE_RANGE'],title='Distribution Of Swap Volumes$ The Week Before Station Launch',hole=0.3))

        df = get_df('Swap Activity','4')
        charts.append(px.pie(values=df['SWAPS_COUNT'],names=df['PRICE_RANGE'],title='Distribution Of Swap Volume$ During the Week Of Station Launch',hole=0.3))

        df = get_df('Swap Activity','5')
        charts.append(px.area(df,x='DATE',y='SWAPS_COUNT',color='PRICE_RANGE',title='Normalized Share of Swap Volume$ On A Daily Basis Since Jan 1'))

        charts = [clean(chart,False) for chart in charts]
        charts[4] = charts[4].update_layout(width=1200)
        return charts

    if subject == 'User Retention':
        charts = []

        df = get_df('User Retention','1')
        charts.append(px.line(df,x='DATE',y='STICKINESS_RATIO',markers=True))

        df = get_df('User Retention','2')
        charts.append(px.bar(df,x='Date',y=['Existing Users','New Users','New User Percentage']))

        charts[0] = charts[0].update_layout(width=1200)
        charts[1] = charts[1].update_layout(width=1200)
        return charts


