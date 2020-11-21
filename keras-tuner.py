import keras
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Activation
from keras.optimizers import Adam
from kerastuner.tuners import RandomSearch
from sklearn.model_selection import train_test_split
import numpy as np
import glob

dataset = None  # 사진
labels = None  # 레이블

### 데이터 전처리 ###
dataset = dataset.atype('float32') / 255.0
dataset = np.asarray(dataset)

### train, test set 나누기 ###
(X_train, y_train), (X_test, y_test) = train_test_split(dataset, labels, test_size=0.2, random_state=1)


### Sequential 방식으로 architecture 만들기 ### min_valu, max_value, step 은 알맞게 고르시면 됩니다.
def build_model(hp):
    model = keras.models.Sequential()

    model.add(
        Conv2D(hp.Int("input_units", min_value=32, max_value=512, step=32), (3, 3), input_shape=X_train.shape[1:])) # min_value 는 최소 값, max_value 는 최댓값, step 은 최소값에서 최댓값까지 얼마나 건너쮤지.
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    for i in range(hp.Int("n_layers", min_value=1, max_value=4)): # step이 없을때는 +1
        model.add(Conv2D(hp.Int("conv_%d_units" % i, min_value=32, max_value=512, step=32), (3, 3)))
        model.add(Activation('relu'))

    model.add(Flatten())

    model.add(Dense(10))
    model.add(Activation("softmax"))

    model.compile(optimizer=Adam(learning_rate=hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])), # learning_rate 를 values 안에 있는 것중 랜덤하게 고른다.
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    return model


tuner = RandomSearch(
    build_model, # 위에 def build_model 만들겁니다.
    objective="val_accuracy",
    max_trials=10,  # 몇번이나 랜덤하게 모델을 학습시킬지
    executions_per_trial=1  # 같은 모델을 몇번이나 학습시킬지
)

tuner.search(x=X_train,
             y=y_train,
             epochs=5,
             batch_size=64,
             validation_data=(X_test, y_test))

best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]  # val_accuracy 가 가장 높았을때의 hyperparameters 를 저장한다.


print("The hyperparameter search is complete. The optimal number of units in the first densely-connected layer is %d, "
      "the number of layers is %d and the optimal learning rate for the optimizer is %f." % (
      best_hps.get('input_units'),
      best_hps.get('learning_rate'),
  best_hps.get('n_layers'))) #

model = tuner.hypermodel.build(best_hps) # 위에서 bext_hps 에 저장한 높은 정확성이 있는 모델을 model에 저장한다.

model.fit(X_train, y_train, batch_size=64, epochs=5, validation_data = (X_test, y_test))
