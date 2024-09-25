import streamlit as st
import pandas as pd

st.header('Supermarket Dashboard')
data = pd.read_csv('mentornow/superSales.csv')

product = st.sidebar.selectbox('Select an Item',data['Product_line'].unique())

df = data[data['Product_line']==product]
with st.expander("Show Data"):
    st.write(df)


col1,col2 = st.columns(2)
cont1 = col1.container(border=True)
cont1.metric('Total Invoices',len(df))
cont2 = col2.container(border=True)
cont2.metric('Avg Rating',round(df['Rating'].mean(),2))

col1,col2 = st.columns(2)
cont1 = col1.container(border=True)
cont1.metric('Profit',df['gross_income'].sum())
cont2 = col2.container(border=True)
cont2.metric('Total Income',df['costs'].sum())

df1 = df[pd.to_datetime(df['Order_date']).dt.month==3]

# with st.expander("Show Data"):
#     st.write(df1)
result = df1.groupby(pd.to_datetime(df['Order_date']).dt.day)['gross_income'].sum().reset_index()
# st.write(result)
st.line_chart(result,x='Order_date',y='gross_income')