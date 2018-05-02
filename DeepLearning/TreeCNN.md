# Tree-CNN

    ref: Tree-CNN: A Deep Convolutional Neural Network for Lifelong Learning

Tree-CNN network grows in a tree like manner to accomodate the new classes of data without losing the ability to identify the previously trained classes.

## Issues of CNN

1. Modifying one part of the parameter space immediately affects the model globally.
2. **catastrophic foregetting**. When new data is fed into a DCNN, it results in the destruction of existing features learned from earlier data.
3. hyper-parameter tuning

## feature of Tree-CNN

1. When an image belonging to a new class is shown to the network, the network grows to accommodate the new class.
2. The network grows by adding a new branch or a new leaf node to the current structure. **The decision is based on how closely the new class resembles a particular superclass and its sub-classes**
3. The objective is to reduce the training effort
4. The updates are localized to a section of the tree, while majority of the Tree-CNN is left untouched, therefore reducing the cost of learning new classes.

## Lifelong learning model


### Algorithm

At each node, begining with the top node, the image is fed to the DCNN associated with that node. The output node with the highest classification probability is the next node the algorithm moves to. If it is a leaf node, then the class associated with that node is the predicted class. Else, the algorithm feeds the image to the DCNN of that node.


#### Detail

The tree-CNN is already trained to classify $N$ classes. Now, data belonging to $M$ new classes have been acquired and the network needs to learn to classify them while trying to minimize the change in network structure, and having a low training effort. A small sample of images is selected from the training set of the new classes. At the root node these images are fed to the DCNN, one class at a time.

1. Add the new class to an existing child node
2. Combine one or more child nodes and the new class to form a new child node.
3. Add the new class as a new child node