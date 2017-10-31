# Grading Comments 

- Overall good, though a few suggestions below.
- In your notebook, you define long tuples with `(1,2,3)`. Since you want to use arrays anyway, it's better to simply define them as arrays: `np.array([1,2,3])`
- Once you have arrays, you can simply vectorize operations over them. For example, if you have the domain points `x = np.linspace(0,1,100)`, then you can define the square of the domain as `y = x**2`. Since the `**` operation is vectorized over arrays, this just works, without any additional for loop.
- In your matrix definitions in the notebook, you forgot the important factor of `1/dx`
