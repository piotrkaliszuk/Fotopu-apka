import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from labels import zbiorX, Y
from sklearn.model_selection import train_test_split
from keras.layers import LSTM, Dense
from sklearn.preprocessing import OneHotEncoder


print(np.array(Y).shape)
print(np.array(zbiorX).shape)
#print(zbiorX)
ohe = OneHotEncoder(sparse=False)
one_hot_Y = ohe.fit_transform(Y)
#print(one_hot_Y)

X_train, X_test, y_train, y_test = train_test_split(np.array(zbiorX),one_hot_Y, train_size=0.9)

"""
print(np.array(X_train).shape)
print(np.array(y_train).shape)
print(np.array(X_test).shape)
print(np.array(y_test).shape)
"""

model = Sequential()
model.add(LSTM(units = 3, input_shape = (120, 3),return_sequences=True))
model.add(LSTM(units = 3,return_sequences=True))
model.add(LSTM(units = 3,return_sequences=False))
model.add(Dense(units = 3))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
history = model.fit(X_train, y_train, epochs = 100, validation_split = 0.30, batch_size = 32, verbose = 1)

plt.plot(np.array(history.history['loss']), "r--", label = "Train loss")
plt.plot(np.array(history.history['accuracy']), "g--", label = "Train accuracy")
plt.plot(np.array(history.history['val_loss']), "r-", label = "Validation loss")
plt.plot(np.array(history.history['val_accuracy']), "g-", label = "Validation accuracy")
plt.title("Training session's progress over iterations")
plt.legend(loc='lower left')
plt.ylabel('Training Progress (Loss/Accuracy)')
plt.xlabel('Training Epoch')
plt.ylim(0)
plt.show()

loss, accuracy = model.evaluate(X_test, y_test, batch_size = 32, verbose = 1)
print("Test Accuracy :", accuracy)
print("Test Loss :", loss)