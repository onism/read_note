## Inverse Transport

Let $\{x_i\}_{i=1}^{\infty}$ be a MC sample of a random variable $\mathbf{X}$ with unknown distribution $v_{\pi}$. Our goal is to characterize this distribution, given a finite sample $\{x_i\}_{i=1}^n$ from $\mathbf{X}$ . We then look for the map $\hat{S}$ such that 
$$
\hat{S} = \arg \min_{S \in \mathcal{T}_{\Delta}} D_{KL}(S_{\sharp}v_{\pi}|v_{\rho})
$$
For the sake of this sythetic example we enforce $X \sim \text{Gumbel}(\mu,\beta)$ with $\mu=3$ and $\beta = 4$. 

