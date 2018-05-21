# A New Online Clustering Approach for Data in Arbitrary Shaped Clusters

CODAS is a two stage process using a simple local density to initiate micro-clusters which are then combined into clusters. The micro-clusters divide the data space into sub-spaces with a core region and a non-core region. Core regions which intersect define the clusters. A threshold value is used to identify outlier micro-clusters separately from small clusters of unusual data.

The first creates micro-clusters when the number of data samples within a given initial radius of any data sample reaches a specified value.  Each cluster consists of a centre point, an outer cluster radius and an inner core cluster radius which is fixed proportion of the outer radius. Data samples are considered to be members of a cluster if they lie within the outer cluster radius. The radius of the cluster is adjusted according to the mean distance of the data samples from the cluster centers. Data samples which have a low density do not form clusters but remain as outliers.

The second stage combines any of these micro-clusters that overlap into global clusters.