# time conversion

time = '12:01:00AM'

def convert(time):

	meridian = time[-2:]
	time_without_meridian = time[:-2]
	hour = int(time[:2])

	if meridian == 'AM':
		hour = (hour+1) % 12 - 1
	elif meridian == "PM":
		hour = hour % 12 + 12

	time = str(hour) + time_without_meridian[2:]
	print(time)

convert(time)