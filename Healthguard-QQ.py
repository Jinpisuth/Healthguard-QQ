import streamlit as st
import numpy as np
import pandas as pd
#import plotly.express as px
#import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use("Agg")
import seaborn as sns
import os
import streamlit.components as stc

#Utils
import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

from PIL import Image
import altair as alt
#import plotly_express as px

from collections import Counter
from matplotlib import colors
#import cv2

#Fxn
def text_downloader(raw_text):
  b64 = base64.b64encode(raw_text.encode()).decode()
  new_filename = "new_text_file_{}_.txt".format(timestr)
  st.markdown("### Download File ###")
  href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
  st.markdown(href,unsafe_allow_html=True)

def load_image(image_file):
  img = Image.open(image_file)
  return img

def main():
  st.title("HealthGuard QQ")
  html_temp = """
  <div style = "background-color:tomato;"><p>⠀</p></div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.sidebar.header("About")
  activities = ["Fetal Health Classification","Pneumonia Detection"]
  choice = st.sidebar.selectbox("Please Select",activities)
  #st.sidebar.header("About")
  #st.sidebar.info("Fetal Health Classification")
  #st.sidebar.info("Lung cancer Detection")
  if choice == 'Fetal Health Classification':
    st.subheader("Exploratory Data Analysis")

    data = st.file_uploader("Upload Dataset",type=["csv","txt"])
    if data is not None:
      df1 = pd.read_csv(data)
      st.dataframe(df1.head())


  #def file_selector(folder_path='.'):
    #filenames = os.listdir(folder_path)
    #selected_filename = st.selectbox("Select A file",filenames)
    #return os.path.join(folder_path,selected_filename)
  
  #filename = file_selector()

  #Read Data
  #df1 = pd.read_csv(filename)

  #if st.checkbox("Show Dataset"):
    #number = int(st.number_input("Number of Rows to View"))
    #st.dataframe(df1.head(number))


  #if st.checkbox("Fetal Health Classification"):

    #result = st.radio(
     # "Select an option:",
      #['Normal','Suspect','Pathological'])
    #if result =="Normal":
     # st.dataframe(df1.head(fetal_health=1))

    #num_shown = st.slider("Fetal Health Data",0, 100, 5)
    all_columns = df1.columns.to_list()  
    multi_select = st.multiselect("Explore more",all_columns)
    new_df = df1[multi_select]
    st.dataframe(new_df)
#if select == "histogram_mean":
  #st.bar
  #print(multi_select)




## Load Data
  #st.cache_data(persist=True)
  #def load_data():
    #df_fetal = pd.read_csv('/Users/codium/Downloads/Fetal Health.csv')
    #return df_fetal

  #df_fetal = load_data()
  #st.table(df_fetal[:num_shown])

  #select = st.selectbox("Explore more", options=("histogram_mean","percentage of time with abnormal long term variability","mean value of short term variability","baseline value","prolongued_decelerations","abnormal short term variability"))


    st.subheader("Input Your Data")
    placeholder = st.empty()

    a = st.number_input("Please enter histogram_mean : ")
    b = st.number_input("Please enter percentage of time with abnormal long term variability : ")
    c = st.number_input("Please enter mean value of short term variability : ")
    d = st.number_input("Please enter baseline value : ")
    e = st.number_input("Please enter prolongued_decelerations : ")
    f = st.number_input("Please enter abnormal short term variability : ")

    if a > 107.500:
      if b > 68.500:
        if c > 0.497:
          if d > 134:
            result = "Pathological"
          else:
            result = "Normal"
        else:
          result = "Pathological"
      elif b <= 68.500:
        if f > 79.500:
          if c > 0.205:
            result =  "Pathological"
          elif c <= 0.205:
            if b > 50.500:
              result = "Pathological"
            else:
              result = "Normal"
        elif f <= 79.500:
          if e > 0.003:
            result = "Pathological"
          elif e <= 0.003:
            if e > 0.003:
              if b > 3:
                result = "Suspect"
              else:
                result = "Pathological"
            elif e <= 0.003:
              if c > 0.600:
                if e > 0.001:
                  if a > 122.500:
                    result = "Suspect"
                  elif a <= 122.500:
                    if f > 17.500:
                      result = "Pathological"
                    else:
                      result = "Normal"
                elif e <= 0.001:
                  if a > 108.500:
                    if e > 0.001:
                      result = "Suspect"
                    else:
                      result = "Normal"
                  elif a <= 108.500:
                    if d > 140:
                      result = "Normal"
                    else:
                      result = "Pathological"
                elif c <= 0.600:
                  if d > 117:
                    if a > 122.500:
                      if b > 0.500:
                        result = "Suspect"
                      else:
                        result = "Normal"
                    elif a <= 122.500:
                      if f > 64:
                          result = "Pathological"
                      else:
                        result = "Normal"
                  else:
                    result = "Normal"
    elif a <= 107.500:
      if f > 25.500:
        if e > 0.000:
          result = "Pathological"
        elif e <= 0.000:
          if d > 115:
            result = "Pathological"
          else:
            result = "Normal"
      elif f <= 25.500:
        if d > 124.500:
          result = "Suspect"
        elif d <= 124.500:
          if c > 1.499:
            result = "Normal"
          else:
            result = "Suspect"

#print("Your Fatal Health is :", result)

    if st.button("Submit"):
      if result == "Normal":
        placeholder.success("Your Fatal Health is Normal")
      elif result == "Suspect":
        placeholder.warning("Your Fatal Health is Suspect")
      else:
        placeholder.error("Your Fatal Health is Pathological")

    st.subheader("Customization Plot")
    all_columns_names = df1.columns.to_list()
    type_of_plot = st.selectbox("Select Type of Plot",["area","bar","hist","box","kde"])
    selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

    if st.button("Generate Plot"):
      st.success("Generating Customiazation Plot of {} for {}".format(type_of_plot,selected_columns_names))

      if type_of_plot == 'area':
        cust_data = df1[selected_columns_names]
        st.area_chart(cust_data)
      elif type_of_plot == 'bar':
        cust_data = df1[selected_columns_names]
        st.bar_chart(cust_data)
      elif type_of_plot == 'line':
        cust_data = df1[selected_columns_names]
        st.line_chart(cust_data)
      elif type_of_plot:
        cust_plot = df1[selected_columns_names].plot(kind=type_of_plot)
        st.write(cust_plot)
        st.pyplot

    my_text = st.text_area("Diagnosis of disease")
    if st.button("Save"):
      st.write(my_text)
      text_downloader(my_text)



#if st.checkbox("Lung cancer Detection"):
 # st.subheader("Input Your Data")
  if choice == 'Pneumonia Detection':
    st.subheader("Pneumonia Detection")

    image_file = st.file_uploader("Upload Image",type=["PNG","JPG","JPEG"])
    if image_file is not None:
      img = load_image(image_file)
      st.image(img)
    if st.button("Analyze"):
      st.warning("Pneumonia")
  #st.sidebar.header("About")
  #st.sidebar.info("Fetal Health Classification")
  #st.sidebar.info("Lung cancer Detection")

if __name__ == '__main__':
  main()

  
 
