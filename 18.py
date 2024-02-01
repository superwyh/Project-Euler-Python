from typing import List

def max_path_sum(triangle: List[List[int]]) -> int:
    n = len(triangle)
    partial_sum_to = [0] * n
    
    for i in range(n):
        temp_partial_sum = partial_sum_to.copy()
        temp_partial_sum[0] = partial_sum_to[0] + triangle[i][0]
        
        for j in range(1, i):
            temp_partial_sum[j] = max(partial_sum_to[j - 1], partial_sum_to[j]) + triangle[i][j]
            
        temp_partial_sum[i] = partial_sum_to[i - 1] + triangle[i][i]
        partial_sum_to = temp_partial_sum

    return max(partial_sum_to)

def solve():
    triangle = [
        [75],
	    [95,64],
	    [17,47,82],
	    [18,35,87,10],
	    [20, 4,82,47,65],
	    [19, 1,23,75, 3,34],
	    [88, 2,77,73, 7,63,67],
	    [99,65, 4,28, 6,16,70,92],
	    [41,41,26,56,83,40,80,70,33],
	    [41,48,72,33,47,32,37,16,94,29],
	    [53,71,44,65,25,43,91,52,97,51,14],
	    [70,11,33,28,77,73,17,78,39,68,17,57],
	    [91,71,52,38,17,14,91,43,58,50,27,29,48],
	    [63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	    [ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
    ]
    return max_path_sum(triangle)

if __name__ == "__main__":
    print(solve())
