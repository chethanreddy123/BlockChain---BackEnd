import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Price Bar and Prediction")
st.sidebar.header("Plotting Demo")
st.write(
    """This tool gives you the current price exchange of 
    unit of power for every single second."""
)

import pandas as pd

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart_data = pd.DataFrame(
    last_rows,
    columns=['Price Per Unit'])
chart = st.line_chart()

for i in range(1, 10001):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i/1000)
    last_rows = new_rows
    time.sleep(1)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")