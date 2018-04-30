#  Transport methodology

## Standard Approach

The basic principle of the transport methodology is to determine a mapping $T$ relating a base distribution $\eta$ to a target distribution $\tilde{\pi}$. Given the map $T$, we can obtain samples from $\tilde{\pi}$ by simply mapping samples from $\eta$ via $T$. More precisely,
$$
T_{\sharp} \eta(x) = \eta(T^{-1}(x))|det \nabla T^{-1}(x)| = \tilde{\pi}(x)
$$