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

from config.config import Config
import numpy as np
import pandas as pd
import streamlit as st
import requests
import datetime  
from datetime import date


headers = {'APIKeyID': st.secrets["API_KEY"], 'APISecretKey': st.secrets["API_SECRET"]}
url_get = Config.url_get
url_data = Config.url_data

class Sensors:

    def get_sensor(sensor_id):
        try:
            req = requests.get(url_get+'?sensorID='+sensor_id, headers=headers)
            data_raw = req.json()
            data = data_raw['Result']
            #st.write(data)
            time = int(data["LastCommunicationDate"].split('(')[1].split(')')[0])/1000
            last_date = datetime.datetime.fromtimestamp(time)
            #st.write(last_date)
            sensor_type = data["SensorName"].split()[0]
            #st.write(sensor_type)
            sensor_name = data["SensorName"].split()[-1]
            #st.write(sensor_name)
            out_data = {
                "Name": sensor_name,
                "Type": sensor_type,
                "Truck": Config.sensor_ids[sensor_name]["Truck"],
                "Location": Config.sensor_ids[sensor_name]["Location"],
                "Last": last_date,
            }
            return out_data
        except Exception as e:
            print(e)  

    def get_data(sensor_id, sensor_type, from_date, to_date):
        dates = []
        temps = []
        hums = []
        x = []
        y = []
        z = []
        m = []
        try:
            req = requests.get(url_data+'?SensorID='+sensor_id+'&fromDate='+from_date+'&toDate='+to_date, headers=headers)
            data_raw = req.json()
            data = data_raw['Result']
            for i in data:
                time = int(i['MessageDate'].split('(')[1].split(')')[0])/1000
                date = datetime.datetime.fromtimestamp(time)
                dates.append(str(date.day)+'-'+str(date.month)+'-'+str(date.year)+'/'+str(date.hour)+':'+str(date.minute)+':'+str(date.second))

                if sensor_type == "Temperature":
                    temps.append(float(i['Data']))

                if sensor_type == "Humidity":
                    data_sensor = i['Data'].split(",")
                    hums.append(float(data_sensor[0]))
                    temps.append(float(data_sensor[1]))
                
                if sensor_type == "G-force":
                    data_sensor = i['Data'].split("|")
                    x.append(float(data_sensor[0]))
                    y.append(float(data_sensor[1]))
                    z.append(float(data_sensor[2]))
                    m.append(float(data_sensor[3]))

            if sensor_type == "Temperature":    
                variables = {
                    "Fecha": dates,
                    "Temperatura": temps,
                }

            if sensor_type == "Humidity":    
                variables = {
                    "Fecha": dates,
                    "Temperatura": temps,
                    "Humedad": hums,
                }
            
            if sensor_type == "G-force":    
                variables = {
                    "Fecha": dates,
                    "X": x,
                    "Y": y,
                    "Z": z,
                    "Magnitud": m,
                }

            df = pd.DataFrame(variables)
            df = df.set_index('Fecha')
            return df
        except Exception as e:
            print(e)
        
    def plot_data(df):
        st.line_chart(df)

    def epoch_to_date(epoch):
        st.write(epoch)
        time = int(epoch.split('(')[1].split(')')[0])/1000
        st.write(time)
        date = datetime.datetime.fromtimestamp(time)
        return date
    
    def sensor_show(sensor_id):
        data = Sensors.get_sensor(sensor_id)
        #st.write(data)
        
        var_list = str(date.today()-data["Last"].date()).split()
        if var_list[0] == "0:00:00":
            var = "Today"
            delta_color = "normal"
        else:
            var = f'{var_list[0]} {var_list[1][0:-1]}'
            delta_color="inverse"
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Nombre", data["Name"])
        col2.metric("Tipo", data["Type"])
        col3.metric("Ubicación", data["Location"])
        col4.metric("Última Actividad", str(data["Last"]).split()[0], var, delta_color=delta_color)


