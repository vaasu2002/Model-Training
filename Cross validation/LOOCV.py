from sklearn.model_selection import LeaveOneOut
lc = LeaveOneOut()
result = cross_val_score(model,X,Y,cv=lc)
np.mean(result)
