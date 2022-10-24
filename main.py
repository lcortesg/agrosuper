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
from source.plot import agro_plot
from source.location import agro_locations
from source.welcome import welcome


def main():

    im = Image.open("assets/logos/favicon.png")

    st.set_page_config(
        page_title="Agrosuper",
        page_icon=im,
        layout="wide",
        initial_sidebar_state="expanded"
    )

    #if agro_plot():
    #    st.markdown("#### ¡Proceso finalizado con éxito! 🥳🎉🎊🎈")

    functions = {
        "Plot": agro_plot,
        "Locations": agro_locations,
        #"Principal": welcome,
        
    }

    selected_function = st.sidebar.selectbox(
        "Seleccionar función", functions.keys()
    )

    if functions[selected_function]():
        st.markdown("#### ¡Proceso finalizado con éxito! 🥳🎉🎊🎈")


if __name__ == "__main__":
    main()
