from tensorflow.keras import layers, models, callbacks, optimizers

from keyscraper.utils import TimeName

from sklearn.model_selection import train_test_split

import numpy, pickle

from matplotlib import pyplot

trainFile, trainData = "./mushroom_training_data_D-i082022_T-223114.json", []

with open(trainFile, "rb") as RF: trainData = pickle.load(RF)

print(len(trainData), len(trainData[0]))


# 53 - 2 = 51
# 91 - 2 = 89
# 46 - 2 = 44
model = models.Sequential([
    layers.Input(shape = (44,)), 
    layers.Dense(128, activation = "relu"),
    layers.Dropout(0.1),
    layers.Dense(64, activation = "relu"),
    layers.Dropout(0.1),
    layers.Dense(2, activation = "softmax")
])

model.summary()

model.compile(
    optimizer = optimizers.Adam(learning_rate = 0.00002),
    loss = "categorical_crossentropy",
    metrics = [ "Accuracy" ]        
)

train_data, test_data, train_label, test_label = train_test_split(
    trainData[:,2:], trainData[:,0:2], test_size = 0.1, stratify = trainData[:,0:2]
)

print("Train: ", type(train_data), type(train_label), len(train_data), len(train_data[0]), len(train_label))

print("Test: ", type(test_data), type(test_label), len(test_data), len(test_data[0]), len(test_label))

history = model.fit(
    train_data, train_label, validation_data = (test_data, test_label), epochs = 5000, batch_size = 64, 
    callbacks = [ callbacks.EarlyStopping(monitor = "val_loss", patience = 75, min_delta = 0.01) ]
)

pyplot.plot(history.history["Accuracy"])

pyplot.plot(history.history["val_Accuracy"])

pyplot.legend([ "acc", "val_acc" ])

pyplot.savefig(TimeName().get_name("test_acc", ".png"))

pyplot.show()

pyplot.plot(history.history["loss"])

pyplot.plot(history.history["val_loss"])

pyplot.legend([ "loss", "val_loss" ])

pyplot.savefig(TimeName().get_name("test_loss", ".png"))

pyplot.show()

model.save(TimeName().get_name("test_model", ".h5"))
