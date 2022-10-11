package main

import "fmt"

func maxSubArray(nums []int) int {
	localMax := nums[0]
	globalMax := nums[0]
	fmt.Println("index: 0", ",local max:", localMax, ",globalMax:", globalMax)

	for i := 1; i < len(nums); i++ {
		currentNum := nums[i]
		localMax = max(localMax+currentNum, currentNum)
		globalMax = max(globalMax, localMax)
		fmt.Println("index:", i, ",local max:", localMax, ",globalMax:", globalMax)
	}
	return globalMax
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	array := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println("the maximum subarray sum:", maxSubArray(array))
}

/*
output:
index: 0 ,local max: -2 ,globalMax: -2
index: 1 ,local max: 1 ,globalMax: 1
index: 2 ,local max: -2 ,globalMax: 1
index: 3 ,local max: 4 ,globalMax: 4
index: 4 ,local max: 3 ,globalMax: 4
index: 5 ,local max: 5 ,globalMax: 5
index: 6 ,local max: 6 ,globalMax: 6
index: 7 ,local max: 1 ,globalMax: 6
index: 8 ,local max: 5 ,globalMax: 6
the maximum subarray sum: 6
*/
