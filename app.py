import streamlit as st
import pandas as pd
from utils import _make_filename
import logging
import time
import os
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.DEBUG)
logging.info("Running app ...")

app_update_freq = int(os.environ["APP_UPDATE_FREQ"])
logging.info(f"App update freq: {app_update_freq}")

valid_countries = ("DE", "NL")
valid_markets = ("gas", "power")
country = st.selectbox("country", valid_countries)
market = st.selectbox("market", valid_markets)

file = _make_filename(country, market)

st.title("Live curves")

# st.subheader("Curve")
data = pd.read_csv(file, index_col=0, header=0)
# st.dataframe(data)

fig, ax = plt.subplots(1, figsize=(15, 5))
for column in data.columns:
    data[column].plot(ax=ax)

ax.set(xlabel="Time", ylabel="Price")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

st.pyplot(fig)

# TODO replace with file watcher
time.sleep(app_update_freq)
st.experimental_rerun()
