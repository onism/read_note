# Point Mass Filter

For numerical integration of the real line, or in the plane, there exists a variety of methods to construct efficient quadratures for general integrands. These methods determine the quadrature points adaptively given the integrand and integration region.

The curse of dimensionality implies that theses uniform mesh approximations cannot be applied in very high dimensions without adaptively choosing the grid points.

## Point-Mass Approximation

In the PMF we utilize a simple numerical integration method with quadrature points given in a grid mesh of uniform resolution. The posterior density is approximately described by point-mass values located in the nodes of this grid.

### Grid Adaption

The grid should remove values with low probability from the grid and increse the grid support through the time update. The resolution should be increased when enough grid point have been removed from the meash and when measurements with low information content are received, the grid resolution should be decreased again so that the computational requirements stay inside some predefined limits.