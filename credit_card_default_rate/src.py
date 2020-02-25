from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris

rf = RandomForestClassifier()
parameters = {'n_estimators': range(1, 11)}

clf = GridSearchCV(estimator=rf, param_grid=parameters)
iris = load_iris()
clf.fit(iris.data, iris.target)
print(clf.best_score_)
print(clf.best_params_)
