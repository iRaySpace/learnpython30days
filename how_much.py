def how_much(money, years):
	"""Compute how much can you save in year, 5 years, 10 years"""
	return money * (years * 365)

money = input("Input money per day: ")
years = input("Year(s): ")

calculated = how_much(int(money), int(years))

print("In %d year(s), you will have a projected money of P%d" % (int(years), calculated))