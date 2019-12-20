# standard library imports
from typing import Tuple
# third party imports
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler


class DataPrep:

    def __init__(self, feature_range: Tuple[int, int] = (0, 1)):
        """TODO

        Parameters
        ----------
        feature_range
            new min and max for scaled data
        """
        self.lr = LinearRegression(fit_intercept=True, normalize=False)
        self.mms = MinMaxScaler(feature_range=feature_range)

    def detrend(self, ts: np.ndarray) -> np.ndarray:
        """Ingests timeseries data and removes linear trend

        Parameters
        ----------
        ts
            timeseries data to be detrended TODO: specify dimensionality

        Returns
        -------
        np.ndarray
            detrended timeseries data TODO: specify dimensionality
        """
        x = np.arange(0, ts.shape[0]).reshape(-1, 1)
        self.lr.fit(X=x, y=ts)
        ts_hat = self.lr.predict(X=x)
        return ts - ts_hat

    def rev_detrend(self, ts: np.ndarray) -> np.ndarray:
        """Ingests detrended timeseries data and retrends it

        Parameters
        ----------
        ts
            timeseries data to be detrended TODO: specify dimensionality

        Returns
        -------
        np.ndarray
            retrended timeseries data TODO: specify dimensionality
        """
        x = np.arange(0, ts.shape[0]).reshape(-1, 1)
        ts_hat = self.lr.predict(X=x)
        return ts + ts_hat

    def scale(self, ts: np.ndarray) -> np.ndarray:
        """TODO

        Parameters
        ----------
        ts
            detrended data to be scaled

        Returns
        -------
        np.ndarray
            min max scaled data
        """
        return self.mms.fit_transform(ts)

    def rev_scale(self, scaled_ts: np.ndarray) -> np.ndarray:
        """TODO

        Parameters
        ----------
        scaled_ts
            detrended scaled data to be unscaled

        Returns
        -------
        np.ndarray
            detrended data that has been unscaled
        """
        return self.mms.inverse_transform(scaled_ts)

    @staticmethod
    def _validate_input(ts: np.ndarray) -> None:
        """TODO

        Parameters
        ----------
        ts
            input data to be validated

        Returns
        -------
        None
        """
        if not isinstance(ts, np.ndarray):
            raise TypeError('Input must be instance of numpy ndarray')
        if len(ts.shape) != 2 or ts.shape[1] != 1:
            raise IndexError('Input array must be 2-dimensional (use numpy reshape(-1, 1)')
        return
