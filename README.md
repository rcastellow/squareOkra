Name: SquareOkra Algorithm

Submitted By: Robert Castellow 2015/05/20

Description: The squareOkra algorithm is a modified largest to smallest best fit method of solving how to fit the fewest  
number of squares into the provided puzzle.  The following procedure is executed to cover the the provided puzzle.

1. Download the puzzle and convert to a matrix of 1's and 0's
2. Loop thru all x, y coordinates of the matrix to find the max square size using the formula to :
	 1 + min(scanMatrix[y][x + 1], scanMatrix[y + 1, x + 1], scanMatrix[y + 1, x])
3. Find the coordinates of the maxes of the largest square (the depth of maxes to search is configurable)
4. Use the first max square size as the first entry to the solution
5. Zero out the max square found and repeat 2-4 until the max =1
6. Once max = 1 combine the remaining entries into the final solution
7. Repeat steps 3-6 and find the minimum number of square solution
8. Submit solution
