#!/usr/bin/env python3
import numpy as np
import array_calculus as ac

def test_array_calculus():
    actual = [1,1,1,1,1,1]
    trial = ac.derivative(0,10,6) @ np.array([0,2,4,6,8,10])
    np.testing.assert_allclose(actual,trial)
    