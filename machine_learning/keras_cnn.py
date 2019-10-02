import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from skelearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Convolution2D # 2D=images, 3D=video
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense # fully connected layers
from keras.layers import Dropout # helps to reduce overfitting


# ALWAYS Normalise/Standardise X. 
X_normalised = X / X.max()
X_scaled = StandardScaler().fit_transform(X)

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_normalised, y, test_size=0.2, shuffle=True)


# Create an instance on the model
clf = Sequential()

# Step 1 
# Convolution2D(filters, rowsInFilter, colsInFilter, 
#   input_shape=img_width, img_height, 3/2) 3=FullColor, 2=Blk&Wht
clf.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2
# Pool size of 2,2 works in most cases
clf.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer for peformance
clf.add(Convolution2D(32, 3, 3, activation = 'relu'))
clf.add(MaxPooling2D(pool_size = (2, 2)))

# Add dropout to reduce overfitting
clf.add(Dropout(0.5))

# Step 3 
# Flatten before sending to a normal NN
# Flattens feature maps to a single vector 2b using in input layer of ANN
clf.add(Flatten())

# Step 4 
# Fully connected layer
# Acts as the input & first hidden layer for the ANN
clf.add(Dense(output_dim = 128, activation = 'relu'))

# Step 5
# ANN Output Layer
# output_dim=1 for binary classification
clf.add(Dense(output_dim = 1, activation = 'sigmoid'))

# Compiling the CNN
# loss='categorical_crossentropy' for multiclass classification
clf.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the model
clf.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# Predicting test labels
y_pred = clf.predict(X_test)
y_pred = (y_pred>0.5) # Assuming a 50% threshold

# Check the classification accuracy
confusion_matrix(y_test, y_pred)
classification_report(y_test, y_pred)

# Saving the model
model_json = clf.to_json()
with open("model_v1.json", "w") as json_file:
    json_file.write(model_json)
    
# Saving the model weights
clf.save_weights('model_weights_v1.h5')