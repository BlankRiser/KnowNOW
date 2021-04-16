import numpy as np
import pandas as pd
import requests


def numericalValues(rawData):
    columnsNeeded = []
    for i in rawData.columns:
        if rawData[i].dtype == np.dtype("float64") or rawData[i].dtype == np.dtype("int64"):
            columnsNeeded.append(rawData[i])

    columnsNeededData = pd.concat(columnsNeeded, axis=1)

    return(list(columnsNeededData.columns))
