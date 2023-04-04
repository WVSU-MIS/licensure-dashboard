#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from PIL import Image

def filterByCampus(df, campus):
    if campus=='All':
        return df
    else:  
        filtered_df = df[df['Campus'] == campus]  
        return filtered_df

def filterByYear(df, year): 
    filtered_df = df[df['Year'] == year]  
    return filtered_df
    

def loadcsvfile():
    csvfile = 'licensure-exams.csv'
    df = pd.read_csv(csvfile, dtype='str', header=0, sep = ",", encoding='latin') 
    return df

# Define the Streamlit app
def app():
    st.title("Welcome to the WVSU Licensure Examination Dashboard")      
    st.subheader("(c) 2023 WVSU Management Information System")
                 
    st.write("This dashboard is managed by: Dr. Wilhelm P. Cerbo \nDirector, University Planning Office, updo@wvsu.edu.ph")
                 
    st.write("A licensure examination report typically contains information on the results of a professional exam taken by individuals seeking to obtain a license to practice in a specific field. The report usually includes statistics on the number of candidates who took the exam and the unit pass rates.")

    #load the data from file
    df = loadcsvfile()
    
    st.subheader("Licensure Examination Results")
    year = '2019'
    options = ['2019','2021','2022']
    st.write('* no licensure exams were conducted in 2020')
    selected_option = st.selectbox('Select the year', options)
    if selected_option=='2019':
        year = selected_option
        df = filterByYear(df, year)
    else:
        year = selected_option
        df = filterByYear(df, year)
        
    campus = 'All'
    options = ['All']
    options.append(df['Campus'].unique())
    
    selected_option = st.selectbox('Select the campus', options)
    if selected_option=='All':
        df = loadcsvfile()
        df = filterByYear(df, year)
    else:
        campus = selected_option
        df = filterByCampus(df, campus)
        
    df['Passing Rate'] = round(df['Passers'] / df['Takers'] * 100, 2)
    new_df = df.loc[:, ['Exam', 'Date', 'Takers', 'Passers', 'Passing Rate']]  
    mean_rate = new_df['Passing Rate'].mean()
    
    if st.button('Show Licensure Exam Report'):
        st.write('Year: ' + year)
        st.write('Campus: ' + campus)
        st.write(new_df)
        st.write('Mean Passing Rate: ' + mean_rate)
        
#run the app
if __name__ == "__main__":
    app()
