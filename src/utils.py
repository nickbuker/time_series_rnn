# standard library imports
from typing import Tuple
# third party imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential


def make_training_data(
        series: pd.Series,
        n_x: int,
        n_y: int,
) -> Tuple[np.array, np.array]:
    """TODO

    Parameters
    ----------
    series
        full time series
    n_x
        number of observations to include in x
    n_y
        number of observations to include in y

    Returns
    -------
    Union[np.array, np.array]
        data to be ingested by and estimated by the model
    """
    x = None
    y = None
    i = 0
    while i + n_x + n_y < series.shape[0]:
        if i == 0:
            x = series[i: i + n_x].values
            y = series[i + n_x: i + n_x + n_y].values
        else:
            x = np.vstack([x, series[i: i + n_x].values])
            y = np.vstack([y, series[i + n_x: i + n_x + n_y]])
        i += 1
    return x, y


def plot_rnn_output(
    x: np.array,
    y: np.array,
    i: int,
    model: Sequential,
) -> None:
    """TODO

    Parameters
    ----------
    x
        validation data ingested by model
    y
        validation data to be estimated by model
    i
        index of data to be plotted
    model
        model used to estimate y

    Returns
    -------
    None
    """
    # TODO: add subplot titles
    fig, axs = plt.subplots(
        nrows=1,
        ncols=2,
        sharey=True,
        figsize=(16, 8))
    axs[0].set_xlim((0, x.shape[1] + y.shape[1] - 1))
    axs[1].set_xlim(0, y.shape[1] - 1)
    axs[0].plot(
        x[0],
        label='Input data',
        color='dodgerblue',
        linewidth=1)
    axs[0].plot(
        range(x.shape[1], x.shape[1] + y.shape[1]),
        model.predict(x[i].reshape(1, x[i].shape[0], 1))[0],
        label='Estimated result',
        color='orange',
        linewidth=1)
    axs[0].plot(
        range(x.shape[1], x.shape[1] + y.shape[1]),
        y[i],
        label='True result',
        color='limegreen',
        linewidth=1)
    axs[1].plot(
        model.predict(x[i].reshape(1, x[i].shape[0], 1))[0],
        label='Estimated result',
        color='orange')
    axs[1].plot(
        y[i],
        label='True result',
        color='limegreen')
    return
