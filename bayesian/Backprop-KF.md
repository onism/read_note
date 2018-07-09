# Backprop-KF

    Backprop KF: Learning Discriminative Deterministic State Estimators
    https://arxiv.org/pdf/1605.07148.pdf

Generative models have limited capacity to handle rich sensory observations. This paper presents an alternative approach where the parameters of the latent state distribution are directly optimized as a deterministic computation graph, resulting in a simple and effective gradient descent algorithm for training discriminative state estimators. This model can be viewed as a type of recurrent neural network, and the connection to probabilistic fitering allows us to design a network architecture that is particularly well suited for state estimation.

## Introduction

They propose an efficient and scalable method for discriminative training of state estimators. Instead of performing inference in a probabilistic latent variable model, they instead construct a deterministic computation graph with equivalent representational power.