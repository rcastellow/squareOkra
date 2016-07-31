import numpy
from numpy import unravel_index
from copy import copy
'''
Created on Apr 30, 2015

@author: RobCastellow
'''

class Matrix(object):
    '''
    classdocs
    '''
    currentDepth = 0
    maxDepthToSearchAllLeaves = 1

    def __init__(self):
        '''
        Constructor
        '''
    def findLargestSquares(self, matrix, solutionMatrix, numberOfRows, numberOfColumns):
        
        scanMatrix = numpy.zeros(shape=(numberOfRows, numberOfColumns), dtype=numpy.int16)
        
        # Find the largest squares in the matrix
        for y in xrange(numberOfRows - 1, -1, -1):
            for x in xrange(numberOfColumns - 1, -1, -1):
                if matrix[y][x] != 0:
                    if (x < numberOfColumns - 1 and y < numberOfRows - 1):
                        currentSquareSize = (1 + min(scanMatrix[y][x + 1], scanMatrix[y + 1, x + 1], scanMatrix[y + 1, x]))
                        scanMatrix[y][x] = currentSquareSize
                    else:
                        scanMatrix[y][x] = 1      
        return scanMatrix
 
    # Zero out the cells in the scanMatrix after finding the max       
    def zeroOutSquare(self, maxLocation, scanMatrix, maxValue):
        for y in xrange(maxLocation[0], maxLocation[0] + maxValue):
            scanMatrix[y][maxLocation[1]:(maxLocation[1] + maxValue)] = 0 
        return scanMatrix      
    
    
    def recurseScanMatrix(self, maxValue, maxLocation, scanMatrix, solutionMatrix, numberOfRows, numberOfColumns):   
        self.currentDepth += 1
        if (maxValue > 1) :
            solutionMatrix[maxLocation[0]][maxLocation[1]] = maxValue
            solutionMatrix = self.findSquares(scanMatrix, solutionMatrix, numberOfRows, numberOfColumns)
        else:
            solutionMatrix += scanMatrix
         
        self.currentDepth -= 1  
        return solutionMatrix
        
    # Find the max and location of the max                
    # Update logic here to choose the first N levels of maxes
    # Pass in mxLocation over the entire matrixes
    # If maxLocation is passed in do not call the find Largest Squares in Matrix
    def findSquares(self, matrix, solutionMatrix, numberOfRows, numberOfColumns):
        
        scanMatrix = self.findLargestSquares(matrix, solutionMatrix, numberOfRows, numberOfColumns)        
        maxValue = scanMatrix.max()

        if (self.currentDepth < self.maxDepthToSearchAllLeaves):
            maxX, maxY = numpy.where(scanMatrix == scanMatrix.max())
            minNumberOfSquares = numberOfRows * numberOfColumns
            minSolutionMatrix = copy(solutionMatrix)  # Reset matrix each time
            for maxXLocation in xrange(0, maxX.size):
                tempScanMatrix = copy(scanMatrix)  # Reset matrix
                tempSolutionMatrix = copy(solutionMatrix)
                maxLocation = (maxX[maxXLocation], maxY[maxXLocation])
                if (maxValue > 1):
                    tempSolutionMatrix[maxLocation[0]][maxLocation[1]] = maxValue
                else:
                    tempSolutionMatrix = tempSolutionMatrix + scanMatrix  # If we are at max 1 just copy the remainder cels over
                tempScanMatrix = self.zeroOutSquare(maxLocation, tempScanMatrix, maxValue)
                tempSolutionMatrix = self.recurseScanMatrix(maxValue, maxLocation, tempScanMatrix, tempSolutionMatrix, numberOfRows, numberOfColumns)
                numberOfSquares = (tempSolutionMatrix > 0).sum()
                print "Number of squares found: {} at depth {} with max {} located at {}".format(numberOfSquares, self.currentDepth, maxValue, maxLocation)
                if (numberOfSquares < minNumberOfSquares):
                    minNumberOfSquares = numberOfSquares
                    minSolutionMatrix = copy(tempSolutionMatrix)
            solutionMatrix = copy(minSolutionMatrix)                  
        else:
            maxLocation = unravel_index(scanMatrix.argmax(), scanMatrix.shape)
            solutionMatrix[maxLocation[0]][maxLocation[1]] = maxValue
            scanMatrix = self.zeroOutSquare(maxLocation, scanMatrix, maxValue)
            solutionMatrix = self.recurseScanMatrix(maxValue, maxLocation, scanMatrix, solutionMatrix, numberOfRows, numberOfColumns)
            
        return solutionMatrix
        

        
        
