# 1700 - 1917 Julian calendar
# since 1919 - now Gregorian calendar

# Feb has 29 days during leap year and 28 during all other years

class Calendar:

	def __init__(self, year):
		self.year = year
		self.year_is_leap = False
		self.is_gregorian = False
		self.is_julian = False
		self.total_days = int()
		self.programer_days = 256
		self.eight_months = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30,
							'may': 31, 'jun': 30, 'jul': 31, 'aug': 31 }

	def time_period(self):
		if self.year == 1918:
			print("oopsie woopsie")
			print("In 1918, February 14th was the 32nd day of the year in Russia")
			print("13 days extra days granted.")

		if self.year <= 1917:
			print(f"Julian calender was used in {self.year}")
			self.is_julian = True

		elif self.year > 1918:
			print(f"Gregorian calender was used in {self.year}")
			self.is_gregorian = True


	def check_leap_year(self):

		if self.year % 4 == 0 and self.is_julian == True:
			print("By Julian calender:")
			print(f"leap february of {self.year} has 29 days")
			self.year_is_leap = True

		elif self.is_gregorian == True:

			if self.year % 400 == 0:
				print("By Gregorian Calendar:")
				print(f"leap(400)february of {self.year} has 29 days")
				self.year_is_leap = True
				

			if self.year % 4 == 0 and self.year % 100 != 0:
				print("By Gregorian Calendar:")
				print(f"leap(4) february of {self.year} has 29 days")
				self.year_is_leap = True

			else:
				print("Not a leap year. 28 days in february")

		elif self.year != 1918:
			print("Not a leap year. February has 28 days.")

	def calculate_total_days(self):
		if self.year_is_leap == True:
			self.eight_months['feb'] = 29

		return sum(self.eight_months.values())
		
	def determine_day(self):

		if self.year == 1918:
			programmers_day = self.programer_days - self.calculate_total_days() + 13
		else:
			programmers_day = self.programer_days - self.calculate_total_days()
		
		print(f"{programmers_day}.09.{self.year}")


if __name__ == "__main__":

	calender = Calendar(1918)
	calender.time_period()
	calender.check_leap_year()
	calender.calculate_total_days()
	calender.determine_day()
	


