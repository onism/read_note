Second-order accurate ensemble transform particle filters

    ref: Second-order accurate ensemble transform particle filters

The ensemble transform particle filter (ETPF) requires the solution of a linear transport problem in each assimilation step, which renders the methods substantially more expensive than an EnKF.
A ensemble filter is called second-order accurate if the posterior mean and covariance matrix of the ensemble are in agreement with their importance sampling estimates from a Bayesian inference step.