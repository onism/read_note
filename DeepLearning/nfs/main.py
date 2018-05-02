import numpy as np
from dataloader import load_data
from sklearn_rfs import rfs_fit


def neural_random_forest(dataset_name='mpg'):
    data = load_data(dataset_name)
    ntrees = 30
    depth = 6
    rf, rf_results = rfs_fit(data, ntrees, depth)

if __name__ == '__main__':
    neural_random_forest()