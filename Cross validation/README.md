# Cross validation
Types:-
##  K Fold Cross Validation 
`from sklearn.model_selection import KFold,cross_val_score
k = KFold(5)
result = cross_val_score(model,X,Y,cv = k)
print(result)
print()
print(np.mean(result))`

##  Stratified K Fold Cross Validation
- Every fold has equal proportion of all the classes/categories.



## Leave One Out Cross Validation 
- Preferved on short datasets
- take first sample of dataset as testing sample and train model with remaining. Repear this until every sample was cosidered as testing sample.
- Every sample considered as testing once
- take average of all the accuracy.
