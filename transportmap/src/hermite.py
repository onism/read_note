import numpy as np
from scipy.special import eval_hermitenorm

class Hermite(object):
    """docstring for Hermite"""
    def __init__(self):
        return

    def hermite_value(self,x,order):
        '''
            return the hermite polynomial value
        '''
        return eval_hermitenorm(order,x)
    def grad_value(self,x,order):
        '''
            return the first derivate of hermite polynomial evaluated at x
        '''
        return order*eval_hermitenorm(order-1,x)


if __name__ == '__main__':
    '''
        test
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    hermite = Hermite()
    x = np.linspace(-5,5)
    fig,axes = plt.subplots(5,1)
    for i in xrange(0,5):
        y = hermite.hermite_value(x,i)
        axes[i].plot(x,y,label = "order{0}".format((i)))
    plt.show()


    plt.legend(loc="best")
    plt.savefig('figs/hermite_poly.pdf')




