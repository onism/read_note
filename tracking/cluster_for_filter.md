cluster for filter (C4F)

    ref: Clustering for filtering: Multi-object detection and estimation using multiple/massive sensors


Challenges and opportunities for MODE in harsh environments with little prior information, an interesting question is whether we have other efficient solutions that can avoid the need to design a sophisticated, computationally intensive and model-sensitive filter in order to maximally meet the requirement for reliable and real time MODE.

The C4F comprises three major steps:
1. project all sensor observations from the observation space to the state space
2. cluster the detections according to their spatial distribution density and certain constraints
3. the detections that are identified as belonging to the same object will be fused in the manner of least squares estimation

Assumption:

All sensor work sunchronously, reporting massive conditionally independent detections in the observation space.

## Expected cluster size

\[E(n_a) = \sum_{s \in S_a} p \leq |S_a|\]
where $n_a$ is the number of detection reported at area $a$, $|S_a|$ gives the number of elements in set $S_a$.

## Decluttering via cluttering

The detections of a single object given by different sensors will cluster locally, while false alarms will not.

Criterion 1: The detections are of high density in the area containing objects and are of low density anywhere else.

constraint 1: the detections reported by the same sensor cannot be clustered into the same cluster.
constrain 2: the size of each cluster shall be determined is respected.

When multiple objects appear closely, their detections can be easily clustered into one cluster. Therefore, to partion the over-sized cluster, another threshold $\rho$ is needed to given the average number of detections in a single-object cluster.