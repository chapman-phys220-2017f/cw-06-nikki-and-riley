import numpy as np
import array_calculus
import nose

def test_derivative():
    """test_derivative()
    Tests for the first derivative accuracy
    """
    a=0
    b=3
    n=3
    f=np.array([2.0,2.0,2.0])
    answer=np.empty(n)
    D1 = array_calculus.derivative(a,b,n)
    answer= D1@f
    desired = np.array([0.0, 0.0, 0.0])
    np.testing.assert_almost_equal(answer,desired)


#trial with x^2 just to check my test functions from the Jupyter notebook
def test_derivative_2():
    """test_derivative_2()
    Tests for the first derivative accuracy specifically for function x^2
    """
    a=0
    b=5
    n=5
    #f(x)=x^2 and x_array=[(0,1,2,3,4)], which is why the f array is defined this way
    f=np.array([0.0, 1.0, 4.0, 9.0, 16.0])
    answer=np.empty(n)
    D1 = array_calculus.derivative(a,b,n)
    #D2 = array_calculus.second_derivative(a,b,n)
    answer= D1@f
    desired = np.array([0.8, 1.6, 3.2, 4.8, 5.6])
    np.testing.assert_almost_equal(answer,desired)


def test_second_derivative():
    """test_second_derivative()
    Tests for the second derivative accuracy
    """
    a=0
    b=5
    n=5
    #f(x)=2x and x_array=[(0,1,2,3,4)], which is why the f array is defined this way
    f=np.array([0.0,2.0,4.0,6.0,8.0])
    answer=np.empty(n)
    D2 = array_calculus.second_derivative(a,b,n)
    answer= D2@f
    desired = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    np.testing.assert_almost_equal(answer,desired)
