import re

def example1():
	my_pattern = re.compile(r'\d{9}')
	my_number = my_pattern.search('In this text should be number and value is 997998778')
	print(my_number.group())

def example2():
	my_pattern = re.compile(r'(\d{2}) (\d{3})')
	my_number = my_pattern.search('Search number 33 345 in text')
	print(my_number.group(2))
	print(0)
	

example2()