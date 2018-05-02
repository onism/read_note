import numpy as np
import pandas as pd
def mpg_load():
    filename = 'auto-mpg.data'
    data = pd.read_csv(filename, header=None, delim_whitespace=True)
    data.replace('?', np.NaN, inplace=True)
    data.dropna(inplace=True)
    X =  data.iloc[:,1:-1].values
    Y =  data.iloc[:,0].values
    return X,Y


def split_data(X,Y, seed):
    np.random.seed(seed)
    n_samples = X.shape[0]
    permutation = np.random.permutation(n_samples)
    X_perm = X[permutation,:]
    Y_perm = Y[permutation]
    split1 = int(0.5*n_samples) # train sets
    split2 = int(0.75*n_samples) #validation sets

    X_Train = X_perm[:split1,:]
    X_Valid = X_perm[split1+1:split2,:]
    X_Test  = X_perm[split2+1:,:]

    Y_Train = Y_perm[:split1]
    Y_Valid = Y_perm[split1+1:split2]
    Y_Test = Y_perm[split2+1:]

    return X_Train, X_Valid, X_Test, Y_Train, Y_Valid, Y_Test


def load_data(dataset_name, seed=777):
    if dataset_name == 'mpg':
        X,Y = mpg_load()
        return split_data(X,Y,seed)

    else:
        raise Exception('unknown dataset')


if __name__ == '__main__':
    load_data('mpg')