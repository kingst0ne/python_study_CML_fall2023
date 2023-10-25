from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_iris()

# n_samples = len(digits.images)
data = digits.data

model = svm.SVC()

X_train, X_test, Y_train, Y_test = train_test_split(
    data, digits.target, shuffle=True
)

model.fit(X_train,Y_train)

predicted = model.predict(X_test[0:5])
Y_test = Y_test[:5]

print('Предсказания сети')
print(predicted)
print('\nПравильные ответы')
print(Y_test)