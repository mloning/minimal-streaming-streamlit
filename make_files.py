import pandas as pd
import numpy as np
import time
import logging
import os
from utils import _make_filename

logging.basicConfig(level=logging.DEBUG)

country = "DE"
market = "gas"

file = _make_filename(country, market)
n = 30

logging.info("Starting ...")
app_update_freq = int(os.environ["APP_UPDATE_FREQ"])
logging.info(f"App update freq: {app_update_freq}")
columns = ["x"]
n_columns = len(columns)
index = pd.period_range("01-01-2022", periods=n, freq="M")
data = pd.DataFrame(
    np.random.normal(loc=10, size=n),
    columns=columns,
    index=index,
)
while True:
    logging.info("Updating ...")
    data = data + np.random.normal(loc=0, scale=0.1, size=(n, 1))
    data.to_csv(file, header=True, index=True)
    time.sleep(app_update_freq)
