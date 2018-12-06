from operator import sub, mul

def make_anonymous_factorial():
    '''
    Return the value of an expression that computes factorial.
    '''
    return (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1))))