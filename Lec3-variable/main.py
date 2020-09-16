def main():
	num_base10 = 2010
	num_base8  = 3733
	num_base16 = 0x708
	print("type of num_base10:", type(num_base10))
	print("base10: %d" % num_base10)
	print("base8 : %d" % num_base8)
	print("base16: %d" % num_base16)
	print()

	complex1 = complex(1, 2)
	complex2 = 3 + 4j
	print("type of complex1:", type(complex1))
	print("complex1:", complex1)
	print("real part of complex1:", complex1.real)
	print("complex2:", complex2)
	print("imag part of complex2:", complex2.imag)

if __name__ == "__main__":
	main()
