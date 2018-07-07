# Symmetric Measurement Equation filter

## Kernel-SME filter

The kernel-SME filter removes the data association uncertainty of the original measurement equation with the help of a symmetric transformation. The basic idea is to define a symmetric transformation that maps the set of measurements to a function, i.e., a Gaussian mixture, and deterministic sampling of this function gives the symmetric transformation.


### Problem Formulation

1. The number of targets is known and fixed
2. Each target gives rise to exactly one single measurement per time instant
3. There are no false measurements.

### SME filter

**Definition 1.** A transformation $S(y_k)$ of the measurement vector $y_k$ with $S$ is called symmetric if 
$$
S(y_k) = S(P_{\pi}(y_k))
$$
for all $\pi \in \prod_N$.


**Example 1:** The sum-of-powers transformation for two targets and one-dimensional measurements $y_k^1, y_k^2$ is given by
$$
S([y_k^1,y_k^2]^T) = [y_k^1+y_k^2, (y_k^1)^2 + (y_k^2)^2]^T
$$

Symmetric means that the value S is unchanged for any permutation of the $y$.

Although the SME approach is very neat way for dealing with data association uncertainties, it comes with some challenges:

1. The generalization of existing symmetric transformations to states with dimension larger than 1 is nontrivial due to the so-called ghost target probelm resulting from non-injective transormations.
2. Due to 1., the resulting nonlinear estimation problem is very difficult.

### Kernel-SME filter

The basic idea of the Kernel-SME filter is to interpret the measurements as the parameters of a function, where the function is a sum of kernel functions that are placed at the measurement locations.


**Definition 2:** (Kernel Transformation). Let $H_n^N$ denote the space of all n-dimensional Gaussian mixtrues with $N$ components. The kernel transformation $S^K$, which maps $y_k$ to a function $F_{y_k}$, is defined as
$$
S^K (y_k) = F_{y_k}
$$
with
$$
F_{y_k} = \sum_{l=1}^N \mathcal{N}(z - y_k^l; \Sigma^K)
$$

**Theorem 1.** The expected kernel transformation of the stacked measurements $y_k$ coincides with the convolution of the PHD with kernel.

**Example 2.**
