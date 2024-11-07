"""
Algorithm complexity expressed as `O(f(n))` e.g. O(1)

## Constant Time: O(1)
Will always take the same amount of time and space regardless of size of the input.
Fastest, most efficient.

## Logarithmic Time: O(log n)
Runtime grows logarithmically with size of input.
Pretty fast.

## Linear Time: O(n)
Runtime grows directly proportional to the input size.
Moderate efficiency.

## Quadratic Time: O(n^2)
Runtime grows with the square of the input size.
Slow.

## Exponential Time: O(2^n)
Runtime grows exponentially with the input size.
Very slow.

## Factorial Time: O(n!)
Runtime grows by a factor of input size. Worst case scenario.
Slowest -- practically unusable for large problems.


"""

# O(1) example
def accessEl(arr, index):
	return arr[index]

# O(n) example
def linearSearch(arr, value):
	for item in arr:
		if item == value:
			return item
	return False

# O(n^2) example
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j+1], arr[j]

# O(log n)
def binarySearch(arr, value):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == value:
			return mid
		elif arr[mid] < value:
			left = mid + 1
		else: 
			right = mid - 1
	return -1