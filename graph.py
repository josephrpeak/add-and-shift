import addshift
import time
import random
from matplotlib import pyplot as plt

results = []
accuracy = int(input("Enter accuracy: "))

def generateBinaryNumber(length):
	n = ""
	for i in range(length):
		n+=str(random.randrange(0,2))

	print(n)
	return n 

for i in range(4, 16):
	total = 0
	for j in range(accuracy):
		start = time.time()

		addshift.main(generateBinaryNumber(i),generateBinaryNumber(i))

		end = time.time()

		elapsed = end - start
		total += elapsed

	results.append(total/accuracy)

	print(f"Elapsed Time: {elapsed}")

y_data1 = results
x_data1 = range(4, 16)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x_data1, y_data1)
ax1.set_xlabel('# of Bits')
ax1.set_ylabel('Avg. Elapsed Time')
ax1.set_title(f'Avg. Elapsed Time vs # of Bits ({accuracy} Samples)')

fig.tight_layout()

plt.show()