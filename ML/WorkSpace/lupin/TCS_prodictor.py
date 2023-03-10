#Moving Average Convergence Divergence (MACD)
#The MACD is calculated by subtracting the 26-period Exponential Moving Average from the 12-period EMA
#EMA = (price(t) * K) + (EMA(y) * (1-K))
import keras
import tensorflow as tf
from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras import optimizers
import numpy as np
np.random.seed(4)
import tensorflow
tensorflow.random.set_seed(4)
from ML.WorkSpace.lupin.util_Low import csv_to_dataset, history_points


test_set_name = 'C:/Users/Antarix/Documents/StockData/KWALITY.csv'

ohlcv_histories = 0
technical_indicators = 0
next_day_open_values = 0
csv_file_path = ''
#for csv_file_path in list(filter(lambda x : x.endswith('daily.csv'), os.listdir('./'))):
if not csv_file_path == test_set_name:
    print("enterrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    print(csv_file_path)
    if type(ohlcv_histories) == int:
        print("ohlcv_historiesohlcv_historiesohlcv_historiesohlcv_historiesohlcv_histories")

        csv_to_dataset(test_set_name)

    #     ohlcv_histories, technical_indicators, next_day_open_values, _, _ = csv_to_dataset(test_set_name)
    # else:
    #     a, b, c, _, _ = csv_to_dataset(csv_file_path)
        # print(a)
        # ohlcv_histories = np.concatenate((ohlcv_histories, a), 0)
        # technical_indicators = np.concatenate((technical_indicators, b), 0)
        # next_day_open_values = np.concatenate((next_day_open_values, c), 0)

# ohlcv_train = ohlcv_histories
# print(ohlcv_train)
# tech_ind_train = technical_indicators
# print("ttttttttttttttttttttttttttttttttt")
# print(tech_ind_train)
# y_train = next_day_open_values
# #
# #
#
#
#
# # dataset
#
# ohlcv_histories, technical_indicators, next_day_open_values, unscaled_y, y_normaliser = csv_to_dataset('C:/Users/Antarix/Documents/StockData/KWALITY.csv')
# print("<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>??????????????????????????")
# print(ohlcv_histories)
# test_split = 0.9
# #take 90 percent of the total elements of the array
# n = int(ohlcv_histories.shape[0] * test_split)
# print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
# print("--3907--: ", n)
#
# ohlcv_train = ohlcv_histories[:n]
# tech_ind_train = technical_indicators[:n]
# y_train = next_day_open_values[:n]
#
# ohlcv_test = ohlcv_histories[n:]
# tech_ind_test = technical_indicators[n:]
# y_test = next_day_open_values[n:]
#
# unscaled_y_test = unscaled_y[n:]
#
# print(ohlcv_train.shape)
# print(ohlcv_test.shape)
#
#
# # model architecture
#
# # define two sets of inputs
# lstm_input = Input(shape=(history_points, 11), name='lstm_input')
# dense_input = Input(shape=(technical_indicators.shape[1],), name='tech_input')
#
# # the first branch operates on the first input
# x = LSTM(50, name='lstm_0')(lstm_input)
# x = Dropout(0.2, name='lstm_dropout_0')(x)
# lstm_branch = Model(inputs=lstm_input, outputs=x)
#
# # the second branch opreates on the second input
# y = Dense(20, name='tech_dense_0')(dense_input)
# y = Activation("relu", name='tech_relu_0')(y)
# y = Dropout(0.2, name='tech_dropout_0')(y)
# technical_indicators_branch = Model(inputs=dense_input, outputs=y)
#
# # combine the output of the two branches
# combined = concatenate([lstm_branch.output, technical_indicators_branch.output], name='concatenate')
#
#
# z = Dense(64, activation="sigmoid", name='dense_pooling')(combined)
# z = Dense(1, activation="linear", name='dense_out')(z)
#
# # our model will accept the inputs of the two branches and then output a single value
# model = Model(inputs=[lstm_branch.input, technical_indicators_branch.input], outputs=z)
#
# adam = optimizers.Adam(lr=0.0005)
#
# model.compile(optimizer=adam, loss='mse')
# print("ohlcv_trainohlcv_trainohlcv_trainohlcv_train")
# print(ohlcv_train)
# print("tech_ind_traintech_ind_traintech_ind_train")
# print(tech_ind_train)
#
# model.fit(x=[ohlcv_train, tech_ind_train], y=y_train, batch_size=32, epochs=1, shuffle=True, validation_split=0.1)
# y_test_predicted = model.predict([ohlcv_test, tech_ind_test])
# evaluation = model.evaluate([ohlcv_test, tech_ind_test], y_test)
# print(evaluation)
#
#
# y_test_predicted = y_normaliser.inverse_transform(y_test_predicted)
# y_predicted = model.predict([ohlcv_histories,technical_indicators])
# # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# # print(y_predicted)
# y_predicted = y_normaliser.inverse_transform(y_predicted)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(y_predicted[-1])
#
# assert unscaled_y_test.shape == y_test_predicted.shape
# real_mse = np.mean(np.square(unscaled_y_test - y_test_predicted))
# scaled_mse = real_mse / (np.max(unscaled_y_test) - np.min(unscaled_y_test)) * 100
# print("------------*******______141.56__________",scaled_mse)
#
# import matplotlib.pyplot as plt
#
# plt.gcf().set_size_inches(22, 15, forward=True)
#
# start = 0
# end = -1
#
# real = plt.plot(unscaled_y_test[start:end], label='real')
# pred = plt.plot(y_test_predicted[start:end], label='predicted')
#
# # real = plt.plot(unscaled_y[start:end], label='real')
# # pred = plt.plot(y_predicted[start:end], label='predicted')
#
# plt.legend(['Real', 'Predicted'])
#
# plt.show()
