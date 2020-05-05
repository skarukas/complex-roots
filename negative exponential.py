import math
import cmath

def power(a, b, max_num_roots=10):
    """Computes a set of solutions for `a**b` for real numbers `a, b` by
    finding ALL complex solutions (roots of `x**(1/b) = a`). 
    
    Whee!!"""
    pi = cmath.pi
    isclose = lambda x, y: cmath.isclose(x, y, abs_tol=1e-10)
    roots = []

    # normie math.pow
    pos_result = math.pow(abs(a), b)

    # the start angle of the exponential but including j
    first_pwr = 1j * b * pi

    # 1 if a is negative, 0 otherwise
    # determines whether we rotate all solutions by pi
    phase_shift = a < 0

    #   |a|^b * sign(a)^b
    # = |a|^b * e^(j * b * pi * (2k + [a < 0]? )) 
    #    for k in range [0, max_num_roots) or until all 
    #    solutions are already found (e.g. the roots become periodic)
    
    for k in range(0, max_num_roots):

        # calculate complex root according to above expression
        root = pos_result * cmath.exp(first_pwr * (2 * k + phase_shift))

        # stop if the exponential has completed a period
        if k != 0 and isclose(roots[0], root):
            break

        # round off purely imag or real nums
        if isclose(root.real, 0):
            root = complex(0, root.imag)
        if isclose(root.imag, 0):
            root = complex(root.real, 0)
        
        print(k, ":", root)
        roots.append(root)

    return roots

power(7, 2)
power(-7, 2)
power(-2, 0.3333333333333)