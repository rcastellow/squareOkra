import numpy
from com.pac.squareo.Matrix import Matrix
from com.pac.squareo.Cimpress import Cimpress
import json


'''
Created on Apr 30, 2015

@author: RobCastellow
'''

def executeSquareOkra():
    
    data = {}
    data['key'] = 'value'
    global totalNumberOfSquares
    global totalScore
    global totalPenalty
    global totalNumberOfErrors
    
    # Main program
    print 'Using API key: {0}'.format(Cimpress.API_KEY)
    s = Cimpress()
    
    # Step 1 - Get a puzzle, and convert the returned JSON to a Python dictionary
    grouping = Matrix()
    jsonResult = s.getPuzzle()
    incomingMatrix = json.loads(jsonResult)
    
    matrixHeight = incomingMatrix['height']
    matrixWidth = incomingMatrix['width']

    # Step 2 - Start scan to find largest matrix
    solutionMatrix = numpy.zeros(shape=(matrixHeight,matrixWidth),dtype=numpy.int16)
    solutionMatrix = grouping.findSquares(incomingMatrix['puzzle'], solutionMatrix, matrixHeight, matrixWidth)
    
    # Step 3 - Convert solution to the JSON format required by Cimpress
    jsonSolution = []
    for y in xrange(0,matrixHeight):
        for x in xrange(0,matrixWidth):
            if (solutionMatrix[y][x]>0):
                sizeOfSquare = numpy.asscalar(solutionMatrix[y][x])
                jsonSolution.append({'X': x, 'Y': y, 'Size': sizeOfSquare})
  
  
    # Step 4 - Submit solution
    print 'Submitting solution'
    jsonResult = s.submitSolution(incomingMatrix['id'], jsonSolution)
    response = json.loads(jsonResult);

    # Step 5 - Report Status **************************
    print 'Incoming Matrix:' 
    for y in xrange(0,matrixHeight):
        print map(lambda x: 1 if x else 0, incomingMatrix['puzzle'][y] )
    print 'You retrieved a puzzle with {0} width x {1} height and ID={2}'.format(
    matrixWidth,
    matrixHeight, 
    incomingMatrix['id'])
    if len(response['errors']) > 0:
        print 'Your solution failed with {0} problems and used {1} squares.'.format(
               len(response['errors']),
               response['numberOfSquares'])
        totalNumberOfErrors += len(response['errors'])
    else:
        print 'Your solution succeeded with {0} squares, for a score of {1}, with a time penalty of {2}.'.format(
               response['numberOfSquares'],
               response['score'],
               response['timePenalty'])
        totalScore += (response['score'])
        totalPenalty += response['timePenalty']
          
    print 'Solution Matrix:'
    for y in xrange(0,matrixHeight):
        print solutionMatrix[y] 


if __name__ == '__main__':

    totalNumberOfSquares = 0
    totalScore = 0
    totalPenalty = 0
    totalNumberOfErrors = 0
    
    totalRuns = 2

    for i in xrange(1,totalRuns):
        executeSquareOkra()
        print 'Avg Score: {}'.format(totalScore / i)
        print 'Total Penalty: {}'.format(totalPenalty)
        print 'Number of Errors: {}'.format(totalNumberOfErrors)
        

    # End STATUS **************************       
    