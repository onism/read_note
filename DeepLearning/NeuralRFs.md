# Neural Random Forests

On the one hand, the many parameters of neural networks make thme a versatile and expressively rich tool for complex data modeling. However, their expressive power comes with the downside of increased **overfitting risk**, especially on small data sets. Conversely, random forests have fewer parameters to tune, but the greedy feature space separation by orthogonal hyperplanes results in typical stair or box-like decision surfaces, which may be advantageous for some data but suboptimal for other.

## Trees, forests, and networks

The general framework is nonparametric regression estimation, in which an input random vector $X$ is observed and the goal is to predict the square integrable random response $Y$ by estimating the regression function $r(x) = E[Y|X=x]$.

A regression tree is a regression function estimate that uses a hierarchical segmentation of the input space, where each tree node corresponds to one of the segmentation subsets.

Assume that a regression tree $t_n$, which takes constant values on each of $K >=2$ terminal nodes. **It turns out that this estimate may be reinterpreted as a three layer neural network estimate with two hidden layers and one output layer.**