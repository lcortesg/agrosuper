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
from datetime import date



def agro_locations():

    st.markdown("# Agrosuper Locations 🐷")
    #st.sidebar.markdown("# Agrosuper Plot 🐖")

    truck_id = st.selectbox(
        'Truck to read',
        (["Wilson", "Triel"])
        )

    #with col_truck1:
    st.markdown(f"## Camión {truck_id}")
    for sensor_id in Config.sensor_ids:
        if Config.sensor_ids[sensor_id]["Truck"] == truck_id:
            Sensors.sensor_show(sensor_id)
    


    
