## Top-down particle filtering for Bayesian decision trees

Decision tree learning is a popular approach for classification and regression im ML and statistics. Unlike classic decision tree learning algorithms, which work in a top-down manner, existing Bayesian algorithms produce an approximation to the posterior distribution by evolving a complete tree iteratively via local MC modifications to the structure of the tree,e.g, using MCMC.



Bayesian approaches start by placing a prior distribution on the decision tree itself. To complete the specification of the model, it is common to associate each leaf node with a parameter indexing a family of likelihoods. The lables are then assumed to be conditionally independent draws from their respective likelihoods. Then Bayesian approach has a number of useful properties:

the posterior distribution on the decision tree can be interpreted as reflecting residual uncertainty and can be used to produce point and interval estimate.



In this article, we present such an adaption, proposing a SMC method for approximate inference in Bayeisna decision trees that works by sampling a collection of trees in a top-down manner. Unlike classical methods, there is no pruning state after the top-down learning stage to prevent over-fitting, as the prior  combines with the likelihood to automatically cut short the growth of the trees, and resampling focues attention on those trees that better fit the data.



### Model 

In this section, we present the decision tree model for the distribution of the labels $Y=\{ y_n\}$  corresponding to input vectors  $X=\{x_n \}_{n=1}^N$.





## Divide-and-Conquer with Sequential Monte Carlo