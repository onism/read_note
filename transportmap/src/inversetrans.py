import logging
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import SpectralToolbox.Spectral1D as S1D
import TransportMaps as TM
import TransportMaps.Functionals as FUNC
import TransportMaps.Maps as MAPS
import TransportMaps.Distributions as DIST
TM.setLogLevel(logging.INFO)

class GumelDistribution(DIST.Distribution):
    """docstring for GumelDistribution"""
    def __init__(self, mu,beta):
        super(GumelDistribution, self).__init__(1)
        self.mu  = mu
        self.beta = beta
        self.dist = stats.gumbel_r(loc=mu,scale=beta)
    def pdf(self,x,params = None):
        return self.dist.pdf(x).flatten()
    def quadrature(self,qtype,qparams,*args,**kwargs):
        if qtype == 0:
            x = self.dist.rvs(qparams)[:,np.newaxis]
            w = np.ones(qparams)/float(qparams)
        else:
            raise ValueError("Quadrature not defined")
        return (x,w)


mu = 3
beta = 4
pi = GumelDistribution(mu,beta)
x,w = pi.quadrature(0,5000)
plt.figure()
plt.hist(x,bins = 20)
plt.savefig("quadratureGumel.pdf")

