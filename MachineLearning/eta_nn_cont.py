from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from keras.callbacks import ModelCheckpoint
from data_gen import synthetic_dataLoader_shuffle, synthetic_dataLoader_oa
import numpy as np

"""
Input:
        Station In [0-19] cont normalized
        Station Out [0-19] cont normalized
        Time [0-17] continuous in hrs
        Day [M T W Th F Sat Sun] cont normalized
        Month [0-11] cont normalized
        Weather (0-100) continuous 100 amount of rain

Output:
        Labels:  Mins
"""


def build_model(input_size = 6):


    model = Sequential()
    model.add(Dense(128, input_dim=input_size, activation='relu'))
    model.add(Dense(256, activation='relu'))
    # model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    return model

def main():


    train = True
    cont = False
    init_epoch = 0

    person_per_day = 2000

    data_size = person_per_day * 365
    data_size = 271320
    print('data_size: ', data_size)
    input_size = 6 # Station_in, day, month, station, destination station, tap in, tap out

    model = build_model()
    model.compile(loss='mse', optimizer = Adam(lr=0.00005))
    model.summary()
    plot_model(model, to_file = 'eta_nn_cont.png', show_shapes=True)



    if train == True:
        epochs = 15
        checkpt_path = '/home/daryl/HackaTren/checkpoints/'
        checkpointer = ModelCheckpoint(filepath=checkpt_path + 'cont_nn_model_oa2-{epoch:02d}.hdf5', verbose=1)

        batch_size = 4
        save_path = 'eta_nn_cont_oa2.h5'
        cont_path = '/home/daryl/HackaTren/checkpoints/cont_nn_model_oa-04.hdf5'
        if cont == True:
            model.load_weights(cont_path)


        # model.fit_generator(synthetic_dataLoader_shuffle(batch_size=batch_size), steps_per_epoch = data_size, epochs=epochs, callbacks=[checkpointer], initial_epoch = init_epoch)
        model.fit_generator(synthetic_dataLoader_oa(batch_size=batch_size), steps_per_epoch = data_size, epochs=epochs, callbacks=[checkpointer], initial_epoch = init_epoch)

        model.save_weights(save_path)
    else:
        test_input = np.zeros((1,6), dtype= np.float32)
        s_in = 0
        s_out = 4
        time_in = 3
        day = 0
        month = 4
        rain_factor = 0.2
        test_input[0,:] = np.array([float(s_in/19), float(s_out/19), float(time_in/16), float(day/6), float(month/11), float(rain_factor)],dtype=np.float32)

        print('input: ', test_input)
        pred_path = 'eta_nn_cont2.h5'
        model.load_weights(pred_path)

        eta_pred = model.predict(test_input)

        max_eta_hrs = 10
        eta = eta_pred[0]
        eta *= max_eta_hrs
        eta_min,eta_hrs = np.modf(eta)
        eta_hrs = eta_hrs.astype('int')
        print('out: ', eta_pred)
        eta_min = (eta_min*60).astype('int')
        print('eta: %d hours and %d minutes' % (eta_hrs,eta_min))


if __name__ == "__main__":
    main()
