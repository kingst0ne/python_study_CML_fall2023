from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
import pandas as pd


# digits = datasets.load_iris()

# n_samples = len(digits.images)

# data = np.load('water_potability.csv', delimiter=',')

data = pd.read_csv('water_potability.csv')
data = data.dropna()
data = data.to_numpy()


model = svm.SVC()
model.gamma = 3

# X_train, X_test, Y_train, Y_test = train_test_split(
#     data[:,:-1], data[:,9], shuffle=True
# )
X_train, X_test, Y_train, Y_test = train_test_split(
    data[:,:-1], data[:,9], shuffle=True
)

model.fit(X_train,Y_train)

predicted = model.predict(X_test[0:5])
Y_test = Y_test[:5]

print('Предсказания сети')
print(predicted)
print('\nПравильные ответы')
print(Y_test)