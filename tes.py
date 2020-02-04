from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
import pickle

bootstrap = 0
for i in range(5):
    bootstrap += 25
    model = BaggingClassifier(base_estimator=LogisticRegression(), n_estimators=bootstrap, bootstrap=True)
    model.fit(X_train,y_train)
    #clf.fit(X_train,y_train)
    model_path = "model"
    pickle.dump(clf,open(model_path+"/bagging_logistic_%s.sav" % bootstrap, "wb"))