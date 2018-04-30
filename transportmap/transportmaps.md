 # Parameters of TM
 The basic principle of the transport methodology is to determine a mapping $T$ relating a base distribution $\eta$ to a potentially target distribution $\tilde{\pi}$. More precisely, the considered mapping $T$ is characterised by

 $$
T_{\sharp} \eta(x) = \eta(T^{-1}(x))|det \nabla T^{-1}(x)| = \tilde{\pi}
 $$

The problem at time $p$ can be solved by introducing a mapping $T_p$ of the form

$$
T_p(x_p, x_{p+1}) = \begin{bmatrix} T_p^0(x_p, x_{p+1}) \\ T_p^1(x_{p+1}) \end{bmatrix}
$$
 
which will transform the 2D base distrbution $\eta_{2d}$ into a target distribution related to the considered HMM. This target distribution can be expressed as 

$$
\tilde{\pi}(x_p,x_{p+1}) \propto \eta_d (x_p) f(T^1_{p-1}(x_p), x_{p+1}) g(x_{p+1},y_{p+1})
$$