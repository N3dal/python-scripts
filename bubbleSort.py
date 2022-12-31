numbers = [18, 40, 35, 12, 30]

for i in range(0, len(numbers)-1):
	for j in range(len(numbers)-1, 0, -1):
		if numbers[j-1] > numbers[j]:
			temp = numbers[j-1]
			numbers[j-1] = numbers[j]
			numbers[j] = temp
			
			
print(numbers)