# This is a python file! The '#' character indicates that the following line is a comment.

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print "hello world!"
    print name
    return

#Implement the Riemann Sum approximation for integrals.
def riemann(func, bounds, nb = 10):
    s = 0.0
    a, b = bounds
    step = (b - a) / float(nb)
    x = a + step
    while x < b:
        s += func(x) * step
        x += step
    return s

# test
def quadratic(x):
    return 3*(x**2) + 2*x + 3

print riemann(quadratic, (1, 2), nb = 100)
