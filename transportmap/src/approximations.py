import logging
import warnings
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import SpectralToolbox.Spectral1D as S1D
# import TransportMaps as TM
# import TransportMaps.Functionals as FUNC
# import TransportMaps.Maps as MAPS
# warnings.simplefilter("ignore")
# TM.setLogLevel(logging.INFO)

import TransportMaps.Distributions as DIST
class GumbelDistribution(DIST.Distribution):
    """docstring for GumbelDistribution"""
    def __init__(self, mu,beta):
        super(GumbelDistribution, self).__init__(1)
        self.mu = mu
        self.beta = beta
        self.dist = stats.gumbel_r(loc=mu,scale = beta)
    def pdf(self,x,params = None):
        return self.dist.pdf(x).flatten()
    def log_pdf(self,x,params = None):
        return self.dist.logpdf(x).flatten()
    def grad_x_log_pdf(self,x,params = None):
        m = self.mu
        b = self.beta
        z = (x - m)/b
        return (np.exp(-z)-1.)/b
    def hess_x_log_pdf(self,x,params=None):
        m = self.mu
        b = self.beta
        z = (x - m)/b
        return (-np.exp(-z)/b**2.)[:,:,np.newaxis]

mu = 3
beta = 4
pi = GumbelDistribution(mu,beta)


class GumbelTransportMap(object):
    """docstring for GumbelTransportMap"""
    def __init__(self, mu,beta):
        self.tar = stats.gumbel_r(loc=mu,scale = beta)
        self.ref = stats.norm(0.,1.)
    def evaluate(self,x,params=None):
        if isinstance(x,float):
            x = np.array([[x]])
        if x.ndim == 1:
            x = x[:,NAX]
        out = self.tar.ppf(self.ref.cdf(x))
        return out
    def __call__(self,x):
        return self.evaluate(x)
Tstar = GumbelTransportMap(mu,beta)

x_tm = np.linspace(-4,4,100).reshape((100,1))
def plot_mapping(tar_star, Tstar, tar=None, T=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax_twx = ax.twinx()
    ax_twy = ax.twiny()
    ax.plot(x_tm, Tstar(x_tm), 'k-', label=r"$T^\star$") # Map
    n01, = ax_twx.plot(x_tm, stats.norm(0.,1.).pdf(x_tm), '-b') # N(0,1)
    g, = ax_twy.plot(tar_star.pdf(Tstar(x_tm)), Tstar(x_tm), '-r') # Gumbel
    if T is not None:
        ax.plot(x_tm, T(x_tm), 'k--', label=r"$\hat{T}$") # Map
    if tar is not None:
        ax_twy.plot(tar.pdf(Tstar(x_tm)), Tstar(x_tm), '--r') # Gumbel
    ax.set_ylabel(r"Map")
    ax_twx.set_ylabel('N(0,1)')
    ax_twx.yaxis.label.set_color(n01.get_color())
    ax_twy.set_xlabel('Gumbel')
    ax_twy.xaxis.label.set_color(g.get_color())
    ax.legend(loc = (0.1, 0.8))
    plt.savefig('figs/GumbelTransportMap.pdf')
plot_mapping(pi, Tstar)




