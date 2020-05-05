# complex-roots
Computes a set of solutions for `a**b` for real numbers `a, b` by finding all complex solutions (roots of `x**(1/b) = a`). For rational `b` (= a reduced fraction `n/d`), these will be `d` complex values equally spaced around a circle in the complex plane with radius `|a|**b`.

N.B. The returned complex values in rectangular form *won't* necessarily satisfy `x**(1/b) = a`, as converting from polar into rectangular form equates an angle with itself `mod 2pi`, and taking a complex exponential, `exp(j*theta)` to the power `1/b` is not usually equivalent to taking `exp(j*(theta % 2pi))` to the same power.
