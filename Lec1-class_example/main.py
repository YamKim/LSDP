class GetAverage:
	def __init__(self):
		# when instance is created
		print("class constructor")
	def __del__(self):
		# when instance is eliminated
		print("class destructor")
	def calculate_average(self, val1, val2):
		average = (val1 + val2) / 2.0
		print("The average of two vals:", average) 

def main():
	avg = GetAverage()
	input_msg = "enter two values seperated by comma: "
	num1,num2 = map(float, input(input_msg).split(','))
	avg.calculate_average(num1, num2)

if __name__ == "__main__":
	main()
