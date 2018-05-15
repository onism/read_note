# CNN-SVM

    An Architecture Combining Convolutional Neural Network (CNN) and Support Vector Machine (SVM) for Image Classification

Some studeis havec claimed that the use of SVM in an ANN architecture produces better results than the use of the conventional softmax function. **There is a drawbck to this approach, and tthat is the restriction to binary classification.**


## SVM
Its objective is to find the optimal hyperplane $f(w,x) = w \cdot x + b$ to separate two classes in a given dataset, with features $x$.

SVM learns the parameters $w$ by solving an optimization problem:

\[
\min \frac{1}{p} w^T w + C \sum_{i=1}^p \max(0,1-y^{'}(w^Tx_i +b))    
\]

## CNN

The distinction of CNN from a plain MLP is its usage of convoluntional layers, pooling, and non-linearities such as tanh, sigmoid, and ReLU.

Intuitively speaking, the CONV layer is used to slide through the width and height of an input image, and compute the dot product of the input's region and the weight learning parameters.  This in turn will produce a 2-d activation map that consists of responses of the filter at given regions.

