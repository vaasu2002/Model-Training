from sklearn.model_selection import KFold,cross_val_score
k = KFold(5)
result = cross_val_score(model,X,Y,cv = k)
print(result)
print()
print(np.mean(result))
