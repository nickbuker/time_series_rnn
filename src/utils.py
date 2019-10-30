# standard library imports
from typing import Tuple
# third party imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential


def make_samples(
        series: pd.Series,
        n_in: int,
        n_out: int,
) -> Tuple[np.array, np.array]:
    """TODO

    Parameters
    ----------
    series
        full time series
    n_in
        number of observations to include in the model input
    n_out
        number of observations to include in the model output

    Returns
    -------
    Union[np.array, np.array]
        data to be ingested by and estimated by the model
    """
    data_in = None
    data_out = None
    i = 0
    while i + n_in + n_out < series.shape[0]:
        if i == 0:
            data_in = series[i: i + n_in].values
            data_out = series[i + n_in: i + n_in + n_out].values
        else:
            data_in = np.vstack([data_in, series[i: i + n_in].values])
            data_out = np.vstack([data_out, series[i + n_in: i + n_in + n_out]])
        i += 1
    return data_in, data_out


def plot_rnn_output(
    data_in: np.array,
    data_out: np.array,
    i: int,
    model: Sequential,
) -> None:
    """Plots the input data, output data, and estimated data from the model

    Parameters
    ----------
    data_in
        validation data ingested by model
    data_out
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
    axs[0].set_xlim((0, data_in.shape[1] + data_out.shape[1] - 1))
    axs[1].set_xlim(0, data_out.shape[1] - 1)
    axs[0].plot(
        data_in[i],
        label='Input data',
        color='dodgerblue',
        linewidth=1)
    axs[0].plot(
        range(data_in.shape[1], data_in.shape[1] + data_out.shape[1]),
        model.predict(data_in[i].reshape(1, data_in[i].shape[0], 1))[0],
        label='Estimated result',
        color='orange',
        linewidth=1)
    axs[0].plot(
        range(data_in.shape[1], data_in.shape[1] + data_out.shape[1]),
        data_out[i],
        label='True result',
        color='limegreen',
        linewidth=1)
    axs[1].plot(
        model.predict(data_in[i].reshape(1, data_in[i].shape[0], 1))[0],
        label='Estimated result',
        color='orange')
    axs[1].plot(
        data_out[i],
        label='True result',
        color='limegreen')
    plt.show()
    return
