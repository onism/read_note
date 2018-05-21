# CEDAS

    ref: Fully Online Clustering of Evolving Data Streams into Arbitrarily Shaped Clusters

In this paper, the authors present a fully online technique for clustering evolving data streams into arbitrary shaped clusters. **It is a two stage technique that is accurate, robust to noise, computationally and memory efficient, with a low time penalty as the number of data dimensions increases.**

The first stage of the technique produces micro-clusters and the second stage combines these micro-clusters into macro-clusters.

The first adds data to current micro-clusters and adjust their information, or creates micro-clusters when data samples occur in un-clustered data space. The radius of the micri-clusters is fixed and should be as small as practical. When no data is received the micro-clusters lose some Energy, gradually fading out. If no data is received for a long time the micro-cluster Energy will reach zero and they are discared.

The second state searches for overlapping micro-clusters. Each macro-cluster consists of the graph of intersecting micro-clusters; the adjacency relations for each micro-cluster are stored as a property of that micro-cluster.


New data from the data stream will fall in to one of 3 regions:

1. empty space, where it will form a new, outlier-micro-cluster
2. a micro-cluster shell region, where it will be assigned to the cluster, the cluster count updated and the micro-cluster centre recursively updated to the mean of its samples
3. a micro-cluster kernel region, where it will be assigned to the micro-cluster and the cluster count updated.