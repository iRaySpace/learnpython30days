# generator function
# def square_numbers(nums):
# 	for i in nums:
# 		yield (i*i)

# my_nums = square_numbers([1, 2, 3])

# list
# my_nums = [ x*x for x in [1, 2, 3]]

# generators
my_nums = (x*x for x in [1, 2, 3])

print(my_nums)

for i in my_nums:
	print(i)