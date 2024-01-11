#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import pandas as pd


# In[5]:


df = pd.read_csv("merged_data(project).csv")


# In[6]:

# In[8]:


df.drop('Unnamed: 0',axis = 1, inplace = True)


# In[9]:


# In[10]:


st.sidebar.title('Oil Prediction')


# In[ ]:
df['Date'] = pd.to_datetime(df['Date'])

def main():
    st.title('Predicted Price Viewer')

    # Create a slider for date selection
    start_date = st.date_input('Select Start Date', min_value=df['Date'].min().date(), max_value=df['Date'].max().date())
    end_date = st.date_input('Select End Date', min_value=df['Date'].min().date(), max_value=df['Date'].max().date())

    # Convert date input values to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the dataset based on the selected date range
    filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    st.subheader('Selected Data')
    st.write(filtered_data)

    # Create a line chart to display the selected data
    st.subheader('Price Over Time')
    #import plotly.express as px
    #px.lineplot(filtered_data.set_index('Date')['Price'])
    st.line_chart(filtered_data.set_index('Date')['Price'])

if __name__ == '__main__':
    main()



