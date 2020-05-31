import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop

dt = pd.read_csv('dataset.csv')

y = dt['Exited']
dt.columns

X = dt[['CreditScore','Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary']]
sc = StandardScaler()
X = sc.fit_transform(X)

X = pd.concat([pd.DataFrame(X) , pd.get_dummies(dt['Geography'],drop_first = True), pd.get_dummies(dt['Gender'],drop_first = True)],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = Sequential()

model.add(Dense(units=6,input_dim=11,activation='relu',kernel_initializer='he_normal'))

model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=32,activation='relu'))

model.add(Dense(units=1,activation='sigmoid'))

model.compile(optimizer=RMSprop(learning_rate=0.001),loss='binary_crossentropy',metrics=['accuracy'])

acc = model.fit(X_train, y_train, verbose = 2, validation_data = (X_test, y_test),epochs=5)
model.save('churn_model.hd5')

accuracy = acc.history['accuracy'][-1]

import os

if int(accuracy) > 0.85:

     print('accuracy is: ',accuracy*100)
     os.system('curl --user admin:b@8788 http://192.168.43.57:8080/job/Mt3_job3/build?token=success')

else:

     print('accuracy is: ',accuracy*100)
     os.system('curl --user admin:b@8788 http://192.168.43.57:8080/job/Mt3_job4/build?token=failure')