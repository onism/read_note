import numpy as np
from sklearn.ensemble import RandomForestRegressor

#  ref : http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html

def rfs_fit(data, ntrees=30, depth=6, random_state=777):


    rf = RandomForestRegressor(ntrees, 'mse', depth, min_samples_split=2,
                            min_samples_leaf=1, min_weight_fraction_leaf=0.0,
                            max_features ='auto', max_leaf_nodes = None,
                            bootstrap = False, oob_score=False,
                            n_jobs =1, random_state = random_state, warm_start=False)

    X_Train, X_Valid, X_Test, Y_Train, Y_Valid, Y_Test = data
    rf.fit(X_Train, np.ravel(Y_Train))

    # generate predictions
    RF_predictions_train = rf.predict(X_Train)
    RF_predictions_valid = rf.predict(X_Valid)
    RF_predictions_test = rf.predict(X_Test)

    # compute RMSE metrics for predictions
    RF_score_train = np.sqrt( np.mean (np.square(RF_predictions_train-np.squeeze(Y_Train) ) )  )
    RF_score_valid = np.sqrt( np.mean (np.square(RF_predictions_valid-np.squeeze(Y_Valid) ) )  )
    RF_score_test = np.sqrt( np.mean (np.square(RF_predictions_test-np.squeeze(Y_Test) ) )  )

    print ("RF score (RMSE) train: ", RF_score_train)
    print ("RF score (RMSE) valid: ", RF_score_valid)
    print ("RF score (RMSE) test: ", RF_score_test)
    rf_results = (RF_score_train, RF_score_valid, RF_score_test)
    return rf, rf_results