


Despite the many attractive properties of PFs, they require an ensemble size that increases
exponentially with the dimension of the system. Serval strategies for overcoming the dimensionality challenges of PFs have been proposed recently.  The equal-weigts PF and the
implicit PF are drawing particles from a proposal density conditioned on the current observations. Another strategy, introduced in Reich, is to avoid the random sampling aspect of PFs by solving an optimal transportation problem for transforming prior particles into posterior particles.


One means of achieving localization is to extend the original weights from scalars to vectors of length <img src="http://www.forkosh.com/mathtex.cgi?N_x"> which will denoted by <img src="http://www.forkosh.com/mathtex.cgi? \omega_n">. The resulting vectors form the columns of a  <img src="http://www.forkosh.com/mathtex.cgi? N_x \times N_e"> weighting matrix, and are constructed to reflect the local influence of observations on the posterior estimation.  This form of localization is achieved by including the function,  <img src="http://www.forkosh.com/mathtex.cgi?l[y,x_j,r] ">, in the calculation of the jth elements of each <img src="http://www.forkosh.com/mathtex.cgi? \omega_n"> and their normalization vector


<img src="http://www.forkosh.com/mathtex.cgi? \omega_{n,j} = [p(y|x_{n,j}) - 1]l[y,x_j,r] + 1">

and

<img src="http://www.forkosh.com/mathtex.cgi? \Omega_j = \sum_{m=1}^N_e \omega_{m,j}">

The localization function has a maximum value of 1 when the Euclidean distance between y and x_j is zeros, and decays to y and x_j are far apart; the rate of this decay is controlled by the parameter r. 

# A non-parametric ensemble transform method for Bayesian inference






<img src="http://www.forkosh.com/mathtex.cgi? \Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}">
