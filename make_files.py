import pandas as pd
import numpy as np
import time
import logging
import os
from utils import COUNTRIES, _make_filename

logging.basicConfig(level=logging.DEBUG)

logging.info("Starting ...")
app_update_freq = int(os.environ["APP_UPDATE_FREQ"])
logging.info(f"App update freq: {app_update_freq}")

n = 30
columns = ["x"]
n_columns = len(columns)
index = pd.period_range("01-01-2022", periods=n, freq="M")
data = {}
files = {}
for country in COUNTRIES:
    data[country] = pd.DataFrame(
        np.random.normal(loc=10, size=n),
        columns=columns,
        index=index,
    )
    files[country] = _make_filename(country)

while True:
    for country in COUNTRIES:
        logging.info(f"Updating {country} ...")
        d = data[country]
        d = d + np.random.normal(loc=0, scale=0.2, size=(n, 1))
        d.to_csv(files[country], header=True, index=True)
    time.sleep(app_update_freq)
