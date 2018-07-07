# Relational recurrent neural networks 
https://arxiv.org/pdf/1806.01822.pdf

## Abstract

Memory-based neural networks model temporal data by leveraging an ability to remember information for long periods. It is unclear, however, whether they also have an ability to perform complex relational reasoning with the information they remember. This paper proposed a new networks that it is fruitful to cosider memory interactions along with storage and retrieval.

## Introduction

Using a new Relational Memory Core (RMC), wich uses multi-head dot product attention to allow memories to interact with each other.

## Relational Reasoning
Some previous approaches make the relational inductive bias more explicit: in message passing neural networks, the nodes comprise the entities and the relaations are computed using learnable functions applied to nodes connected with an edge, or sometimes reducing the relational function to a weighted sum of the source entities.

In the temporal domain relational reasoning could comprise a capacity to compare and contrast information seen at different points in time.