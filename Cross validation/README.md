# Cross validation
**Types:-**
##  1)  K Fold Cross Validation 

`from sklearn.model_selection import KFold,cross_val_score`

`k = KFold(5)`

`result = cross_val_score(model,X,Y,cv = k)`

`np.mean(result)`

##  2)  Stratified K Fold Cross Validation
- Every fold has equal proportion of all the classes/categories.
- 
`from sklearn.model_selection import StratifiedKFold`

`skfold= StratifiedKFold(n_splits=5)`

`result = cross_val_score(model,X,Y,cv=skfold)`

`np.mean(result)`


## 3) Leave One Out Cross Validation 
- Preferved on short datasets
- take first sample of dataset as testing sample and train model with remaining. Repear this until every sample was cosidered as testing sample.
- Every sample considered as testing once
- take average of all the accuracy.

`from sklearn.model_selection import LeaveOneOut`

`lc = LeaveOneOut()`

`result = cross_val_score(model,X,Y,cv=lc)`

`np.mean(result)`
