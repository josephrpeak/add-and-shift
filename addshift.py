import sys

def add(A, B):
	result = bin(int(A,2) + int(B,2))[2::]

	if(len(result) > len(max(A,B))):
		result = result[1::]

	return result.zfill(len(max(A,B)))

def shift(A, Q):
	AQ = list(A + Q)
	shifted = []

	for i in range(len(AQ)):
		shifted.append(AQ[i-1])

	shifted[0] = '0'

	return "".join(shifted)

def graph():

	x_data1 = list_avg_hash_power
	y_data1 = range(4,16)

	fig = plt.figure()
	ax1 = fig.add_subplot(1, 2, 1)
	ax1.plot(x_data1, y_data1)
	ax1.set_xlabel('Difficulty Bits')
	ax1.set_ylabel('Avg. Elapsed Time')
	ax1.set_title('Avg. Elapsed Time vs Difficulty Bits')

	fig.tight_layout()

	plt.show()


def main(x,y):

	#x = str(sys.argv[1])
	#y = str(sys.argv[2])

	n = len(max(x,y))
	A = "0"*len(max(x,y))
	B = x 
	Q = y
	AQ = A + Q

	print()
	print(n, A, Q, B, "INITIALIZATION")

	while(n > 0):
		if(AQ[-1] == '0'):
			print(n, A, Q, B, "SHIFT")
			AQ = shift(A,Q)
		elif(AQ[-1] == '1'):
			print(n, A, Q, B, "ADD")
			A = add(A,B)
			print(n, A, Q, B, "SHIFT")
			AQ = shift(A,Q)

		A = AQ[0:len(AQ)//2]
		Q = AQ[(len(AQ)//2)::]
		n-=1

	print(n, A, Q, B)

	print(f"\nResult: {AQ}")


if __name__=="__main__":
	main()