# third party imports
import numpy as np
import pytest
# custom imports
from ..src.data_prep import DataPrep


# set random seed
np.random.seed(97)
# instantiate DataPrep object
dp = DataPrep(feature_range=(-1, 1))
# generate some data for testing
norm_arr = np.random.normal(loc=0.0, scale=1.0, size=72000).reshape(-1, 1)
trend_arr = np.add(norm_arr, np.linspace(-10, 10, 72000).reshape(-1, 1))
# create outputs to avoid object state resets
detrend_arr = dp.detrend(trend_arr)
rev_detrend_arr = dp.rev_detrend(detrend_arr)
scaled_arr = dp.scale(norm_arr)
rev_scaled_arr = dp.rev_scale(scaled_arr)


def test_detrend_dim():
    assert detrend_arr.shape == trend_arr.shape


def test_detrend_vals():
    assert np.allclose(detrend_arr, norm_arr, atol=0.01)


def test_rev_detrend_dim():
    assert rev_detrend_arr.shape == detrend_arr.shape


def test_rev_detrend_vals():
    assert np.allclose(rev_detrend_arr, trend_arr)


def test_scale_dims():
    assert scaled_arr.shape == norm_arr.shape


def test_scale_vals():
    test_list = [
        abs(scaled_arr.mean()) <= 0.01,
        scaled_arr.min() == -1.0,
        scaled_arr.max() == 1.0,
    ]
    assert all(test_list)


def test_rev_scale_dims():
    assert rev_scaled_arr.shape == scaled_arr.shape


def test_rev_scale_vals():
    assert np.allclose(rev_scaled_arr, norm_arr)


def test_validate_input_type():
    with pytest.raises(TypeError, match='Input must be instance of numpy ndarray'):
        dp._validate_input([1, 2, 3])


def test_validate_input_shape():
    with pytest.raises(IndexError, match='Input array must be 2-dimensional*'):
        dp._validate_input(np.zeros(5))

