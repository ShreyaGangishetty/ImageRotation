'''
The code works for Python 3 or above.
The code expects the "rotation.csv" file to be in the same location as of the python script
'''

import pandas as pd
import numpy as np
#import matplotlib.pylab as plt
import math

def find_correction_angle(binary_image):
        #reading the input csv
        matrix = binary_image.as_matrix()
        '''
        figure = plt.figure()
        ax = figure.add_subplot(1,1,1)
        ax.set_aspect('equal')
        plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,10.5,0.5,10.5))
        plt.show()
        '''
        rowColList =[]
        # getting all the rectangle points
        for rowNo,row in enumerate(matrix):
            for colNo, col in enumerate(row):
                if(col>0):
                    #print(rowNo,colNo)
                    rowColList.append([rowNo, colNo])
        #calculting the boundaries of rectangle minX,minY,maxX,maxY
        rowList = [item[0] for item in rowColList]
        colList = [item[1] for item in rowColList]
        min_row=min(rowList)
        max_row=max(rowList)
        min_col=min(colList)
        max_col=max(colList)
        #print("boundaries",min_row,max_row,min_col,max_col)

        rectanglecoordinateslist=[]
        for row in rowColList:
            if(min_row==row[0] or max_row ==row[0] or min_col==row[1] or max_col ==row[1]):
                rectanglecoordinateslist.append(row)

        #print (rectanglecoordinateslist)
        y1=max_col;
        y2=max_col;
        x1=min_row;
        x2=min_row;
        #calculating the 4 corner coordinates for the rectangle 
        for coordinate in rectanglecoordinateslist:
            if(coordinate[0]==min_row):
                if(y1>coordinate[1]):
                    y1=coordinate[1];
            if(coordinate[0]==max_row):
                if(y2>coordinate[1]):
                    y2=coordinate[1];
            if(coordinate[1]==min_col):
                if(x1<coordinate[0]):
                    x1=coordinate[0];
            if(coordinate[1]==max_col):
                if(x2<coordinate[0]):
                    x2=coordinate[0];
        coordinates={min_row:y1,max_row:y2,x1:min_col,x2:max_col}
        #print(coordinates)
        #print(rectanglecoordinateslist)
        
        #calculating the slope of rectangle
        slope = (coordinates[min_row]-coordinates[x1])/(min_row-x1)
        #print(slope)
        #print(math.atan(-1.4))
        #inverse tan of slope gives the radians and then converted to degrees
        correction_angle=math.degrees(math.atan(slope))
        ##returning the correction_angle in degrees
        return correction_angle

#reading the input csv
try:
    binary_image = pd.read_csv("rotated.csv")
    #calling the method
    print(find_correction_angle(binary_image))
except:
    print("File rotated.csv not f   ound")