def is_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return 0
	return 1

def find_prime(beg, end):
	if beg == 1:
		print("1 is not prime number")
	for itr in range(2, end + 1):
		if is_prime(itr):
			print("%d is prime number" % itr)

def main():
	find_prime(2, 10)

if __name__ == "__main__":
	main()
