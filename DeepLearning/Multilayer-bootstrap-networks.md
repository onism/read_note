# Multilayer Bootstrap Networks

Multilayer Bootstrap networks builds a gradually narrowed multilayer nonlinear network from bottom up for unsupervised nonlinear dimensionality reduction.

MBN is composed of two novel components:
1. each layer of MBN is a nonparametric density estimator by random resampling
2. The network is a deep ensemble model. It essentially reduces the nonlinear variations of data by building a vast number of hierarchical trees on the data space.

## Introduction
Dimensionality reduction has two core steps. The first step finds a suitable feature space where the density of data the new feature representation can be well discovered. The second step discards the noise componenets or small variations of the data with the new feature representation.

The density of a local region of a probability distribution can be approximated by counting the events that fall into the local region.


## MBN