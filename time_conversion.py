#! /usr/bin/env python3

def convert_some_time(string_o_timey):

    am_pm_thingy_wingy = string_o_timey[-2:]
    timey_without_am_pm_thingy = string_o_timey[:-2] 
    chnaging_this = int(timey_without_am_pm_thingy[:2])

    if am_pm_thingy_wingy == 'AM':
        print(timey_without_am_pm_thingy[:2])
        if timey_without_am_pm_thingy[:2] == '12':
            print('#', timey_without_am_pm_thingy)
        new_timey = timey_without_am_pm_thingy

        print(timey_without_am_pm_thingy)
        print('I AM')
    
    elif am_pm_thingy_wingy == 'PM':
        new_timey = str(int(timey_without_am_pm_thingy[:2]) + 12)
        if chnaging_this > 11:
            new_timey = '00'
        new_time = new_timey + timey_without_am_pm_thingy[2:]
        print(new_time)
         
        print(timey_without_am_pm_thingy)
        print('IPM')

    print(am_pm_thingy_wingy, '\n' )
    return 'Happy timing\n'



if __name__ == "__main__":

    timey_string = '12:01:00AM'
    timey_string_2 = '12:00:00PM'

    testies = [timey_string, timey_string_2, '09:03:02PM', '12:45:54PM', '12:00:00AM']

    for testie_westie in testies:

        print(convert_some_time(testie_westie))
