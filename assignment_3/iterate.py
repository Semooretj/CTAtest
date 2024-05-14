import numpy

def iterate(c,max_iter=100,epsilon=1e3):
    """Carrys out iteration 
    Parameters
    c ---- complex number in form x+iy
    max_iter --- max number of iterations carried out
    epsilon --- large number to signify divergence
    
    Returns
    n --- number of loops before divergence (if n=max_iter, point does not diverge)
    """
    n = 0
    values = [0]
    
    while n < max_iter:
        # Implementing recurssive expression
        c_i = values[-1]**2+c
        modulus = numpy.sqrt(c_i.real**2+c_i.imag**2)
        # Increases counter
        n += 1
        # Ends loop if absolute value gets very large
        if modulus < epsilon:
            values.append(c_i)
        else:
            break
    return n
