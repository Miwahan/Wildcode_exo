import streamlit as st
import pandas as pd
import plotly.express as px

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df= pd.read_csv(link)

# Menu
st.sidebar.title("Navigation")
options = st.sidebar.radio("Menu", options=['Df exercice', 'Heatmap', 'Distribution'])

# Graph heatmap 
def heatmap_def(df):
    st.title("Afficher une heatmap")
    df_corr = round(df.select_dtypes("number").corr(),2)
    heatmap = px.imshow(df_corr,  text_auto=True, color_continuous_scale="oranges")
    st.plotly_chart(heatmap, theme="streamlit", use_container_width=True)

# Graph dynamique sur la distribution
def interactive_plot(df):
    st.title("Afficher la distribution")
    x_axis_val = st.selectbox("Selectionnner l'abscisse", options=df.columns)
    y_axis_val = st.selectbox("Selectionnner l'ordonnée", options=df.columns)
    
    plot = px.histogram(df, x=x_axis_val, y=y_axis_val, color='continent')
    
    st.plotly_chart(plot)

# Navigation avec boutons radios
if options == 'Heatmap':
    heatmap_def(df)
elif options == 'Distribution':
    interactive_plot(df)
elif options == 'Df exercice':
    st.header("Le dataframe de l'exercice")
    st.write(df.head(5))



