# Bayesian Quadrature in Nonlinear Filtering

This paper deals with the state estimation of nonlinear stochastic discrete-time systems by means of quadrature-based filtering algorithms. The aim is at evaluation of the integral by Bayesian quadrature. **The Bayesian quadrature perceives the integral itself as a random variable, on which inference is to be performed by conditioning on the function evaluations.**


A limitation of classical integral approximations, such as the Gaussian-Hermite quadrature, is that they are specifically designed to perform with zero error on a narrow class of functions.

The BQ treats numerical integration as a problem of Bayesian inference and thus it is able to provide an additional information. The goal of this paper is to augment to the current $\sigma-$point algorithms so that the uncertainty associated with the integral approximations is also reflected in their estimates.


## Gaussian Process Priors

Gaussian process is a collection of random variables indexed by elements of an index set, any finite number of which has a joint Gaussian density. That is, for any finite set of indicies, it holds that 

$$
(g(x_1),g(x_2),...,g(x_m)^T \sim \mathcal{N}(0,K)
$$

where the kernel matrix $K$ is made up of pair-wise evaluations of the kernel function.  

## Bayesian Quadrature

If GP prior density is used, then the value of the integral of the function will also be Gaussian distributed. This follows from the fact that integral is a linear operator acting on the GP distributed random function $g(x)$.

## Incorporating Integral Uncertainty

