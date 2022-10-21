# -*- coding: utf-8 -*-
"""
@file     : CSV Handler
@brief   : Handles CSV and TXT file conversion and plotting.
@date    : 2022/08/12
@version : 1.0.0
@author  : Lucas Cortés.
@contact : lucas.cortes@lanek.cl
@bug     : None.
"""

from PIL import Image
import streamlit as st
from source.plot import csv_plot
from source.welcome import welcome


def main():

    im = Image.open("assets/logos/favicon.png")

    st.set_page_config(
        page_title="Agrosuper",
        page_icon=im,
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    if csv_plot():
        st.markdown("#### ¡Proceso finalizado con éxito! 🥳🎉🎊🎈")

    # functions = {
    #     "Plot": csv_plot,
    #     #"Principal": welcome,
        
    # }

    # selected_function = st.sidebar.selectbox(
    #     "Hola Nicco! ¿Que quieres hacer hoy?", functions.keys()
    # )

    # if functions[selected_function]():
    #     st.markdown("#### ¡Proceso finalizado con éxito! 🥳🎉🎊🎈")


if __name__ == "__main__":
    main()
