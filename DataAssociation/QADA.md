##Multitarget Tracking Performance based on the Quality Assessment of Data Association

The $m \times n$ reward matrix $\Omega = [w(i,j)]$  is defined by its elements $w(i,j) > 0$ , representing the gian of the association of target $T_i$ with the measurement $z_j$. Thes values are usually homogeneous to the likelihood ratios. In our case $w(i,j)$ represents the normalized distances between the measurement $Z_j$ and target $T_i$. In this case the DA problem consists in finding the best assignment, minimizing the overall cost.

The optimal DA problem consists in finding the $m \times n$ binary association matrix $A = [a(i,j)]$ with $a(i,j) \in \left\{0,1 \right\}$  maximizing the global reward $R(\Omega,A)$, given by:
$$
R(\Omega,A) = \sum_{i=1}^m \sum_{j=1}^n w(i,j)a(i,j)
$$
The best optimal assignment solution is not necessarily unique, as well as the second best one.



### Quality Assessment of Pairings in DA

The main idea behind it is to compare the values $a_1(i,j)$ in $A_1$ with the corresponding values $a_2(i,j)$ in $A_2$, and to identify if there is a change of the optimal pairing $(i,j)$ .  The construction of the quality indicator is based on BF theory and Proportional Conflict depends on the type of the pairing matching.

Several cases are possible:

1. Case1: $a_1(i,j) = a_2(i,j) = 0$: Agreement on non-association of $T_i$ with $z_j$.
2. Case 2: $a_1(i,j) = a_2(i,j) = 1$ Agreement on association $T_i,z_j$

http://www.onera.fr/sites/default/files/297/SlidesYBSWorkshopFusion2017-QADA-PDAversusJPDA.pdf