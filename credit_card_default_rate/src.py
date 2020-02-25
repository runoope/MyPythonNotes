import pandas as pd

# data read
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('./UCI_Credit_Card.csv')

# data explore/fearture selection
data.drop('ID', axis=1, inplace=True)
target = data['default.payment.next.month']
columns = data.columns.tolist()
columns.remove('default.payment.next.month')
features = data[columns].values
train_x, test_x, train_y, test_y = train_test_split(features, target, test_size=0.33)

rf = RandomForestClassifier()
pipeline = Pipeline(
    [('scaler', StandardScaler()),
     ('randomforestclassifier', rf)]
)

paragrams = {'randomforestclassifier__n_estimators': range(1, 11)}
clf = GridSearchCV(estimator=pipeline, param_grid=paragrams)
clf.fit(train_x, train_y)
print(clf.best_score_)
print(clf.best_params_)
predict_y = clf.predict(test_x)
print("准确率 %0.4lf" % accuracy_score(test_y, predict_y))
