def decorator_function(original_function):
	def wrapper_function():
		print("Decorating the function")
		return original_function()
	return wrapper_function

@decorator_function
def display():
	print("Display function ran")

display()