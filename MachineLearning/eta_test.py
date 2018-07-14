import numpy as np
from eta_nn_cont import build_model
import matplotlib.pyplot as plt
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from keras.callbacks import ModelCheckpoint


def arrival_demo():
    test_input = np.zeros((19,6), dtype= np.float32)

    # station = input('Enter where you are: 1-Roosevelt, 2-Balintawak, 3-Monumento, 4-5th. Ave, 5-R.Papa, 6-Abad.Santos, 7-Tayuman, 8-Bluementritt,...20-Baclaran. \n')
    # s_in = int(station)
    s_in = 0

    # station_out = input('Enter where you are: 1-Roosevelt, 2-Balintawak, 3-Monumento, 4-5th. Ave, 5-R.Papa, 6-Abad.Santos, 7-Tayuman, 8-Bluementritt,...20-Baclaran. \n')
    # s_out = int(station_out)
    # s_out -= 1
    s_out = 19

    # month = input('Enter month: (1 for Jan, 2 for Feb, ... 12 for Dec.) \n')
    # month = int(month)
    month = 6


    # day = input('Enter day: (1 for Mon, 2 for Tues, ... 7 for Sun.) \n')
    # day = int(day)
    day = 6

    # time = input('Enter hour: 5 for 5:00am - 22 for 10:00pm. \n')
    # time_in = int(time)
    time_in =11
    # rain = input('Enter prob of raining: \n')
    rain = float(1.0)

    for i in range(1,20):
        print('i ', i)
        test_input[i-1,:] = np.array([float(s_in/19), float(i/19), float(time_in/16), float(day/6), float(month/11), float(rain)],dtype=np.float32)

    print('test input: ', test_input)
    model = build_model()
    pred_path = '/home/daryl/HackaTren/checkpoints/cont_nn_model_oa-04.hdf5'
    model.load_weights(pred_path)
    eta_pred = model.predict(test_input)
    # print('month: ', int(month))
    # print('day: ', int(day))
    # print('time: ', time)
    # print('station_loc: ', station)
    # print(station_out)
    # print(rain)

    # test_input[0,:] = np.array([float(s_in/19), float(s_out/19), float(time_in/16), float(day/6), float(month/11), float(rain)],dtype=np.float32)
    # print(test_input)

    max_eta_hrs = 10
    stations = ['Roosevelt','Balintawak','Monumento','5th Avenue','R. Papa', 'Abad Santos', 'Blumentritt', 'Tayuman', 'Bambang', 'Doroteo Jose','Carriedo', 'Central Terminal', 'United Nations', 'Pedro Gil', 'Quirino', 'Vito Cruz','Gil Puyat','Libertad','EDSA','Baclaran']
    print('len: ', len(stations))
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov','Dec']
    days = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    #hours = ['5:00',]
    for i in range(1,20):
        print('          ')
        print('Estimated time from ', stations[s_in],' to ', stations[i], ' at %.2d:00 '%(time_in+5), ' ', days[day], ' ', months[month] )
        print('          ')
        eta = eta_pred[i-1]
        # print()
        eta *= max_eta_hrs
        eta_min,eta_hrs = np.modf(eta)
        eta_hrs = eta_hrs.astype('int')
        print('out: ', eta)
        eta_min = (eta_min*60).astype('int')
        print('eta: %d hours and %d minutes' % (eta_hrs,eta_min))



    # eta = eta_pred[0]
def varying_time():
    label = ['5a', '6a', '7a','8a','9a','10a','11a','12p','1p','2p','3p','4p','5p','6p','7p','8p','9p']
    values = list()
    values2 = list()
    values3 = list()
    s_in = 0
    s_out = 19
    month = 6
    day = 5
    test_input = np.zeros((17,6), dtype= np.float32)
    rain = 0.1
    for i in range(17):
        test_input[i,:] = np.array([float(s_in/19), float(s_out/19), float(i/16), float(day/6), float(month/11), float(rain)],dtype=np.float32)

    model = build_model()
    pred_path = '/home/daryl/HackaTren/checkpoints/cont_nn_model_shuff-09.hdf5'
    model.load_weights(pred_path)
    eta_pred = model.predict(test_input)
    max_eta_hrs = 10

    for i in range(17):
        eta = eta_pred[i]
        eta *= max_eta_hrs
        eta = float(eta)*60
        print(type(eta))
        values.append(eta)

    rain = 0.5
    for i in range(17):
        test_input[i,:] = np.array([float(s_in/19), float(s_out/19), float(i/16), float(day/6), float(month/11), float(rain)],dtype=np.float32)

    eta_pred2 = model.predict(test_input)

    for i in range(17):
        eta2 = eta_pred2[i]
        eta2 *= max_eta_hrs
        eta2 = float(eta2)*60
        print(type(eta2))
        values2.append(eta2)

    rain = 0.9
    for i in range(17):
        test_input[i,:] = np.array([float(s_in/19), float(s_out/19), float(i/16), float(day/6), float(month/11), float(rain)],dtype=np.float32)

    eta_pred3 = model.predict(test_input)

    for i in range(17):
        eta3 = eta_pred3[i]
        eta3 *= max_eta_hrs
        eta3 = float(eta3)*60
        print(type(eta3))
        values3.append(eta3)

    # values = list(range(len(label)))
    print('values ', values)
    print(len(values))
    print(len(label))
    index = np.arange(len(label))
    plt.plot(index, values, color='y')
    plt.plot(index, values2, color='g')
    plt.plot(index, values3, color='b')

    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Travel time (mins)', fontsize=15)
    plt.xticks(index, label, fontsize=10, rotation=30)
    plt.title('Travel Time from Roosevelt to Baclaran Station')
    plt.legend(['10% chance of rain', '50% chance of rain', '90% chance of rain'], loc = 'upper center')
    plt.show()


def main():
    test_input = np.zeros((1,6), dtype= np.float32)

    station = input('Enter where you are: 1-Roosevelt, 2-Balintawak, 3-Monumento, 4-5th. Ave, 5-R.Papa, 6-Abad.Santos, 7-Tayuman, 8-Bluementritt,...20-Baclaran. \n')
    s_in = int(station)
    s_in -= 1

    station_out = input('Enter where you are: 1-Roosevelt, 2-Balintawak, 3-Monumento, 4-5th. Ave, 5-R.Papa, 6-Abad.Santos, 7-Tayuman, 8-Bluementritt,...20-Baclaran. \n')
    s_out = int(station_out)
    s_out -= 1

    month = input('Enter month: (1 for Jan, 2 for Feb, ... 12 for Dec.) \n')
    month = int(month)
    month -= 1


    day = input('Enter day: (1 for Mon, 2 for Tues, ... 7 for Sun.) \n')
    day = int(day)
    day = day-1

    time = input('Enter hour: 5 for 5:00am - 22 for 10:00pm. \n')
    time_in = int(time)
    time_in -=5
    rain = input('Enter prob of raining: \n')
    rain = float(rain)


    # print('month: ', int(month))
    # print('day: ', int(day))
    # print('time: ', time)
    # print('station_loc: ', station)
    # print(station_out)
    # print(rain)

    test_input[0,:] = np.array([float(s_in/19), float(s_out/19), float(time_in/16), float(day/6), float(month/11), float(rain)],dtype=np.float32)
    print(test_input)
    stations = ['Roosevelt','Balintawak','Monumento','5th Avenue','R. Papa', 'Abad Santos', 'Blumentritt', 'Tayuman', 'Bambang', 'Doroteo Jose','Carriedo', 'Central Terminal', 'United Nations', 'Pedro Gil', 'Quirino', 'Vito Cruz','Gil Puyat','Libertad','EDSA','Baclaran']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov','Dec']
    days = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    #hours = ['5:00',]
    print('          ')
    print('Estimated time from ', stations[s_in],' to ', stations[s_out], ' at %.2d:00 '%(time_in+5), ' ', days[day], ' ', months[month] )
    print('          ')
    pred_path = '/home/daryl/HackaTren/checkpoints/cont_nn_model_shuff-09.hdf5'

    model = build_model()
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


if __name__ == '__main__':
    # main()
    # arrival_demo()
    varying_time()
