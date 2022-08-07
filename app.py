import streamlit as st
import pandas as pd
import numpy as np
from utils import COUNTRIES, _make_filename
import logging
import time
import os
import matplotlib.pyplot as plt
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logging.info("Running app ...")

app_update_freq = int(os.environ["APP_UPDATE_FREQ"])
logging.info(f"App update freq: {app_update_freq}")

st.title("Live curves")
country = st.selectbox("country", COUNTRIES)

max_n_files = 10
n_files = st.slider("history length", 1, max_n_files)

fig, ax = plt.subplots(1, figsize=(15, 5))
color = "blue"

base = 100
alphas = np.logspace(0, 1, max_n_files + 1, base=base) / base
alphas = alphas[:-1][::-1]

file = _make_filename(country)
data = pd.read_csv(file, index_col=0, header=0)
for j, i in enumerate(range(1, n_files)):
    f = Path(str(file) + f".{i}")
    if f.exists():
        d = pd.read_csv(f, index_col=0, header=0)
        d.plot(ax=ax, alpha=alphas[j], color=color, legend=None)
data.plot(ax=ax, alpha=1, color=color, legend=None)

ax.set(xlabel="Time", ylabel="Price")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

st.pyplot(fig)

# update files
for i in range(n_files, 0, -1):
    path = Path(str(file) + f".{i}")
    if path.exists():
        new_i = i + 1
        if new_i < n_files:
            new_path = str(path).replace(path.suffix, f".{new_i}")
            print(f"renaming: {path} to {new_path}")
            os.rename(path, new_path)
data.to_csv(Path(str(file) + ".1"))

# TODO replace with file watcher
time.sleep(app_update_freq)
st.experimental_rerun()
