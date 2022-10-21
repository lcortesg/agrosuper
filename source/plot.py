# -*- coding: utf-8 -*-
"""
@file    : CSV Plotter
@brief   : Handles CSV file plotting.
@date    : 2022/08/12
@version : 1.0.0
@author  : Lucas Cortés.
@contact : lucas.cortes@lanek.cl
@bug     : None.
"""

import numpy as np
import pandas as pd
import streamlit as st
import requests
import datetime  

def csv_plot():

    st.markdown("# Agrosuper Plot 🐖")
    #st.sidebar.markdown("# Agrosuper Plot 🐖")

    url = 'https://www.imonnit.com/json/SensorDataMessages?sensorID='
    headers = {'APIKeyID': 'MYz5Ya4utYKM' , 'APISecretKey': '1pqfIKdabjKTCYHYwG5raUGowa7KqTeq'}
    from_date = '10/20/22'
    to_date = '10/21/22'

    sensor_id = st.selectbox(
        'Sensor to read',
        ('355862', '406588'))
    
    d = st.date_input(
        "Date selector",
        datetime.date(2019, 7, 6))
    #auth = HTTPBasicAuth('apikey', 'MYz5Ya4utYKM')
    #files = {'sensors': open('filename', 'rb')}

    temps = []
    dates = []

    try:
        req = requests.get(url+sensor_id+'&fromDate='+from_date+'&toDate='+to_date, headers=headers)
        data_raw = req.json()
        data = data_raw['Result']
        for i in data:
            temps.append(float(i['Data']))
            time = int(i['MessageDate'].split('(')[1].split(')')[0])/1000
            date = datetime.datetime.fromtimestamp(time)
            dates.append(str(date.day)+'-'+str(date.month)+'-'+str(date.year)+'/'+str(date.hour)+':'+str(date.minute)+':'+str(date.second))
        variables = {
            "Fecha": dates,
            "Temperatura": temps,
        }
        df = pd.DataFrame(variables)
        df = df.set_index('Fecha')
        st.line_chart(df)
        return True
    
    except Exception as e:
        print(e)
        return False
