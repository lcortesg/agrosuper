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
from source.sensors import Sensors
import numpy as np
import pandas as pd
import streamlit as st
import requests
import datetime  
from datetime import datetime, timedelta


def agro_plot():

    st.markdown("# Agrosuper Plot 🐖")
    #st.sidebar.markdown("# Agrosuper Plot 🐖")

    sensor_id = st.selectbox(
        'Sensor to read',
        (Config.sensor_ids)
        )
    
    data = Sensors.get_sensor(sensor_id)
    Sensors.sensor_show(sensor_id)
    sensor_name = data["Name"]
    sensor_type = data["Type"]
    last_date = data["Last"]
    last_day = str(last_date).split()[0]
    last_days = last_day.split("-")
    start_date = datetime(2022,10,8)
    full_start_date = "2022/10/08"

    window_time = st.slider(
        'Select a range of values',
        start_date, datetime(int(last_days[0]), int(last_days[1]), int(last_days[2])), (datetime(int(last_days[0]), int(last_days[1]), int(last_days[2]))))
        #datetime(2022,10,8), datetime(int(last_days[0]), int(last_days[1]), int(last_days[2])), (datetime(int(last_days[0]), int(last_days[1]), int(last_days[2])-6), datetime(int(last_days[0]), int(last_days[1]), int(last_days[2]))))
    
    #window_time = st.slider(
    #    "When do you start?",
    #    value=(datetime(int(last_days[0]), int(last_days[1]), int(last_days[2])-6), datetime(int(last_days[0]), int(last_days[1]), int(last_days[2]))),
    #    format="YYYY/MM/DD")
    #d = st.date_input(
    #    "When's your birthday",
    #    datetime(int(last_days[0]), int(last_days[1]), int(last_days[2])))
    full_date = str(window_time).split()[0].split("-")
    to_date = f'{full_date[0]}/{full_date[1]}/{full_date[2]}'
    from_date = f'{full_date[0]}/{full_date[1]}/{int(full_date[2])-7}'
    d = datetime.date(window_time) - timedelta(days=7)
    if not (d>start_date.date()):
        from_date =  full_start_date
    data = Sensors.get_data(sensor_id, sensor_type, from_date, to_date)
    Sensors.plot_data(data)
