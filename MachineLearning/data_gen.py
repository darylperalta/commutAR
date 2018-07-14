import numpy as np
from random import shuffle
# 1 day
#Monday
"""
Input:
        Station In [0-19] One hot vector
        Station Out [0-19] One hot vector
        Time [0-17] continuous in hrs (5:00 am to 10:00 pm)
        Day [M T W Th F Sat Sun] discrete one hot vector
        Month [0-11] discrete one hot vector (Jan to Dec)
        Weather (0-100) continuous 100 amount of rain

Output:
        Labels:  Mins
"""

stations = ['Roosevelt','Balintawak','Monumento','5th Avenue','R. Papa', 'Abad Santos', 'Blumentritt', 'Tayuman', 'Bambang', 'Doroteo Jose','Carriedo', 'Central Terminal', 'United Nations', 'Pedro Gil', 'Quirino', 'Vito Cruz','Gil Puyat','Libertad','EDSA','Baclaran']
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov','Dec']
days = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

def synthetic_dataLoader(batch_size = 4, person_per_hr = 10, max_hrs=10):
    total_stations=20
    input_batch = np.zeros((batch_size,6), dtype= np.float32)
    ETA_batch = np.zeros((batch_size,1), dtype= np.float32)
    ctr = 0
    # text_file = open("Output.txt", "w")

    while True:
        for month in range(12):
            for day in range(7):
                for time_in in range(17):
                    for s_in in range(total_stations):
                        for s_diff in range(total_stations-s_in-1):
                                s_out = s_in+s_diff+1
                                for batch_i in range(batch_size):
                                    rain_factor = np.random.uniform()
                                    ETA = (2.5*(s_out-s_in))+(2.0*rain_factor)
                                    day_factor = np.random.uniform()

                                    if (day == 7):

                                        ETA = ETA - (day_factor*0.5)
                                    elif (day==6):
                                        ETA = ETA - (day_factor*0.2)
                                    month_factor = np.random.uniform()
                                    if (month==12):
                                        ETA = ETA + (month_factor*2)
                                    if (month==1):
                                        ETA = ETA + (month_factor*1)

                                    time_factor = np.random.uniform()
                                    if (1<=time_in<=2): # 6-7 am
                                        ETA = ETA + (time_factor*3.0)
                                    elif (2<time_in<4): # 8 am
                                        ETA = ETA + (time_factor*2.0)
                                    elif (time_in==4): # 9 am
                                        ETA = ETA + (time_factor*1.0)

                                    elif (time_in==11): # 4 pm
                                        ETA = ETA + (time_factor*1.0)
                                    elif (time_in==12): # 5 pm
                                        ETA = ETA + (time_factor*2.0)
                                    elif (12<time_in<=14): # 6 - 7 pm
                                        ETA = ETA + (time_factor*3.0)
                                    elif (14<time_in<=15): # 8 pm
                                        ETA = ETA + (time_factor*1.0)

                                    var = np.random.uniform(low=-0.2,high=0.2)
                                    ETA = ETA +var

                                    input_batch[batch_i,:] = np.array([float(s_in/19), float(s_out/19), float(time_in/16), float(day/6), float(month/11), float(rain_factor)],dtype=np.float32)
                                    ETA_batch[batch_i,:] = np.array([float(ETA/(max_hrs*60))])
                                    # print('month: ', month, 'day: ', day, 'time: ', time_in, 's_in: ', s_in, 's_out: ', s_out,'rain_factor: ', rain_factor*100, 'ETA: ', ETA)
                                    text = 'Month: ',  months[month],' day: ',days[day], ' time: %d station_in: ',stations[s_in], ' station_out: ',stations[s_out], ' rain: %.4f: ETA: %f' % (month,day,time_in,s_in,s_out,rain_factor*100,ETA)
                                    # text_file.write(text)
                                yield input_batch, ETA_batch
                                ctr = ctr+1


def synthetic_dataLoader_shuffle(batch_size = 4, person_per_hr = 10, max_hrs=10):
    total_stations=20
    input_batch = np.zeros((batch_size,6), dtype= np.float32)
    ETA_batch = np.zeros((batch_size,1), dtype= np.float32)
    ctr = 0

    month_shuffle = list(range(12))
    # print('month shuff ', month_shuffle)
    shuffle(month_shuffle)
    #
    day_shuffle = list(range(7))
    shuffle(day_shuffle)
    time_shuffle = list(range(17))
    shuffle(time_shuffle)
    stations_shuffle = list(range(total_stations))
    shuffle(stations_shuffle)
    # print('month shuff ', month_shuffle)
    # print('day shuff ', day_shuffle)
    # print('time shuff ', time_shuffle)
    # print('stations shuff ', stations_shuffle)
    # text_file = open("Output.txt", "w")
    # print('start loop: ')
    while True:
        # break
        for m in range(12):
            month = month_shuffle[m]
            for d in range(7):
                day = day_shuffle[d]
                for t in range(17):
                    time_in = time_shuffle[t]
                    for s in range(total_stations):
                        s_in = stations_shuffle[s]
                        for s_diff in range(total_stations-s_in-1):

                                for batch_i in range(batch_size):
                                    s_out = s_in+s_diff+1
                                    rain_factor = np.random.uniform()
                                    ETA = (2.5*(s_out-s_in))+(2.0*rain_factor)
                                    day_factor = np.random.uniform()

                                    if (day == 7):

                                        ETA = ETA - (day_factor*0.5)
                                    elif (day==6):
                                        ETA = ETA - (day_factor*0.2)
                                    month_factor = np.random.uniform()
                                    if (month==12):
                                        ETA = ETA + (month_factor*2)
                                    if (month==1):
                                        ETA = ETA + (month_factor*1)

                                    time_factor = np.random.uniform()
                                    if (1<=time_in<=2): # 6-7 am
                                        ETA = ETA + (time_factor*3.0)
                                    elif (2<time_in<4): # 8 am
                                        ETA = ETA + (time_factor*2.0)
                                    elif (time_in==4): # 9 am
                                        ETA = ETA + (time_factor*1.0)

                                    elif (time_in==11): # 4 pm
                                        ETA = ETA + (time_factor*1.0)
                                    elif (time_in==12): # 5 pm
                                        ETA = ETA + (time_factor*2.0)
                                    elif (12<time_in<=14): # 6 - 7 pm
                                        ETA = ETA + (time_factor*3.0)
                                    elif (14<time_in<=15): # 8 pm
                                        ETA = ETA + (time_factor*1.0)

                                    var = np.random.uniform(low=-0.2,high=0.2)
                                    ETA = ETA +var

                                    input_batch[batch_i,:] = np.array([float(s_in/19), float(s_out/19), float(time_in/16), float(day/6), float(month/11), float(rain_factor)],dtype=np.float32)
                                    ETA_batch[batch_i,:] = np.array([float(ETA/(max_hrs*60))])
                                    # text = 'Month: ',  months[month],' day: ',days[day], ' time: %d station_in: ',stations[s_in], ' station_out: ',stations[s_out], ' rain: %.4f: ETA: %f' % (rain_factor*100,ETA)
                                    # print('Month: ',  months[month],' Day: ',days[day], ' Time: %d:00 Station_in: ' % (time_in),stations[s_in], ' Station_out: ',stations[s_out], ' Rain: %.4f: ETA: %f' % (rain_factor*100,ETA))
                                    # print('month: ', month, 'day: ', day, 'time: ', time_in, 's_in: ', s_in, 's_out: ', s_out,'rain_factor: ', rain_factor*100, 'ETA: ', ETA)
                                    # text = 'month: %d day: %d time: %d s_in: %d s_out: %d rain: %f: ETA: %f' % (month,day,time_in,s_in,s_out,rain_factor*100,ETA)
                                    # text_file.write(text)
                                yield input_batch, ETA_batch
                                ctr = ctr+1

        # print('1 epoch')
        # print('month shuff ', month_shuffle)
        # print('day shuff ', day_shuffle)
        # print('time shuff ', time_shuffle)
        # print('stations shuff ', stations_shuffle)
        # break
        # text_file.close()
        # print('created:   ', str(ctr), ' samples')
        # break


def synthetic_dataLoader_oa(batch_size = 4, person_per_hr = 10, max_hrs=10):
    total_stations=20
    input_batch = np.zeros((batch_size,6), dtype= np.float32)
    ETA_batch = np.zeros((batch_size,1), dtype= np.float32)
    ctr = 0

    month_shuffle = list(range(12))
    # print('month shuff ', month_shuffle)
    shuffle(month_shuffle)
    #
    day_shuffle = list(range(7))
    shuffle(day_shuffle)
    time_shuffle = list(range(17))
    shuffle(time_shuffle)
    stations_shuffle = list(range(total_stations))
    shuffle(stations_shuffle)
    # print('month shuff ', month_shuffle)
    # print('day shuff ', day_shuffle)
    # print('time shuff ', time_shuffle)
    # print('stations shuff ', stations_shuffle)
    # text_file = open("Output.txt", "w")
    # print('start loop: ')
    while True:
        # break
        for m in range(12):
            month = month_shuffle[m]
            for d in range(7):
                day = day_shuffle[d]
                for t in range(17):
                    time_in = time_shuffle[t]
                    for s in range(total_stations):
                        s_in = stations_shuffle[s]
                        for s_diff in range(total_stations-s_in-1):

                                for batch_i in range(batch_size):
                                    s_out = s_in+s_diff+1
                                    rain_factor = np.random.uniform()
                                    ETA = (2.5*(s_out-s_in))+(5.0*rain_factor)
                                    day_factor = np.random.uniform()

                                    if (day == 7):

                                        ETA = ETA - (day_factor*0.5)
                                    elif (day==6):
                                        ETA = ETA - (day_factor*0.2)
                                    month_factor = np.random.uniform()
                                    if (month==12):
                                        ETA = ETA + (month_factor*2)
                                    if (month==1):
                                        ETA = ETA + (month_factor*1)

                                    time_factor = np.random.uniform()
                                    if (1<=time_in<=2): # 6-7 am
                                        ETA = ETA + (time_factor*6.0)
                                    elif (2<time_in<4): # 8 am
                                        ETA = ETA + (time_factor*7.5)
                                    elif (time_in==4): # 9 am
                                        ETA = ETA + (time_factor*5.0)
                                    elif (time_in==5): # 10 am
                                        ETA = ETA + (time_factor*2.0)
                                    elif (time_in==11): # 4 pm
                                        ETA = ETA + (time_factor*4.0)
                                    elif (time_in==12): # 5 pm
                                        ETA = ETA + (time_factor*6.0)
                                    elif (12<time_in<=14): # 6 - 7 pm
                                        ETA = ETA + (time_factor*5.5)
                                    elif (14<time_in<=15): # 8 pm
                                        ETA = ETA + (time_factor*1.0)

                                    var = np.random.uniform(low=-0.2,high=0.2)
                                    ETA = ETA +var

                                    input_batch[batch_i,:] = np.array([float(s_in/19), float(s_out/19), float(time_in/16), float(day/6), float(month/11), float(rain_factor)],dtype=np.float32)
                                    ETA_batch[batch_i,:] = np.array([float(ETA/(max_hrs*60))])
                                    # text = 'Month: ',  months[month],' day: ',days[day], ' time: %d station_in: ',stations[s_in], ' station_out: ',stations[s_out], ' rain: %.4f: ETA: %f' % (rain_factor*100,ETA)
                                    # print('Month: ',  months[month],' Day: ',days[day], ' Time: %d:00 Station_in: ' % (time_in),stations[s_in], ' Station_out: ',stations[s_out], ' Rain: %.4f: ETA: %f' % (rain_factor*100,ETA))
                                    # print('month: ', month, 'day: ', day, 'time: ', time_in, 's_in: ', s_in, 's_out: ', s_out,'rain_factor: ', rain_factor*100, 'ETA: ', ETA)
                                    # text = 'month: %d day: %d time: %d s_in: %d s_out: %d rain: %f: ETA: %f' % (month,day,time_in,s_in,s_out,rain_factor*100,ETA)
                                    # text_file.write(text)
                                yield input_batch, ETA_batch
                                ctr = ctr+1

        # print('1 epoch')
        # print('month shuff ', month_shuffle)
        # print('day shuff ', day_shuffle)
        # print('time shuff ', time_shuffle)
        # print('stations shuff ', stations_shuffle)
        # break
        # text_file.close()
        # print('created:   ', str(ctr), ' samples')
        # break

def main():
    some_gen = synthetic_dataLoader_shuffle()
    while True:
        try:
            next(some_gen)
        except:
            print('end')
            break

if __name__ == '__main__':
    main()
