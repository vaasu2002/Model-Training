from sklearn.model_selection import StratifiedKFold
skfold= StratifiedKFold(n_splits=5)
result = cross_val_score(model,X,Y,cv=skfold)
print(np.mean(result))
