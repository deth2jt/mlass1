import csv
import sys
import random
import math




def getRecords(filename):
    records = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            
            if(line_count > 0 and line_count < 100):
            #if(line_count > 0 ):
                #print("leng", len(next(csv_reader)) )
                numoFColums = len(next(csv_reader))
                cell = []
                #if()
                #print("columncolumncolumncolumn",numoFColums)
                for column in range(numoFColums):
                    #print("row[column]",row[column])
                    cell += [float(row[column])]
                    
                records += [cell]
            line_count += 1
                    #print("cell", cell)
            #if(line_count % 100 == 0):
                #print("reading line ", line_count)

        #line_count=line_count-1
    return records

    
def featureExtract(records, intensity):
    arraySize = len(records[0])
    #print("arraySize", arraySize)

    array = []
    for index in range(arraySize):
        array += [0]

    for row in range(len(records)):
        for column in range(arraySize):
            if(records[row][column] != 0):
                array[column] += 1
    imp = []
    for column in range(arraySize):
        if(array[column] > intensity and column > 0):
            imp += [column]
    #print("imp", imp, len(imp))
    return imp


def createFixedSizedArray(features):
    array = []
    for index in range(features):
        array += [0]
    return array

def getSumCount(records, features):
    sumValue = createFixedSizedArray(features)

    for count in range(len(records)):
        for row in range(len(features)):

            cell = records[count][features[row]]
            sumValue[row] += cell

    return sumValue


    



def normalize(records, features):
    low = 0
    high = 255
    for count in range(len(records)):
        #cell = records[count]
        for column in range(len(features)):
        #for column in range(1,784):

            records[count][features[column]] = (records[count][features[column]] - low) / (high-low)
            #records[count][column] = (records[count][column] - low) / (high-low)

        
    return records

def printRecords(records):  
    for count in range(len(records)):
        print(count, ": ", records[count])

def setTrainValidateTestRecords(records):

    line_count= len(records)
    testValSize = .10*line_count

    #print("line_count", line_count)
    #print("testValSize", int(testValSize))

    testData = []
    validateData = []
    trainData = []

    for count in range(line_count):
        #row = 0
        if(count < testValSize):
            testData = testData + [records[count]]
            #row = row + 1
        elif(count < 2*testValSize):
            validateData = validateData + [records[count]]
        else:
            trainData = trainData + [records[count]]
    return(testData,validateData,trainData)
    

def distanceFrom(records, item1, feature):
    item = []
    for count in range(len(records)):
        if(item1[0] == records[count][0]):
            item = records[count]
    value = 0
    for featurelen in (range(len(feature))):
            pos = feature[featurelen]
            distanceMetric = pow(item[pos] - item1[pos], 2)
            value = value + (distanceMetric)
    return value

def knn(records, item, feature, k):
    #print("item", item)
    #print("distance",distanceFrom(records,item, feature))
    distance = []
    for count in range(len(records)):
        value = 0
        
        for featurelen in (range(len(feature))):
            pos = feature[featurelen]
            distanceMetric = (records[count][pos] - item[pos])**2
            value = value + (distanceMetric)
        #value = abs(records[count][1] - item[1] ) **2

        distance = distance + [(value, count, records[count][1])]
    #printRecords(distance)
    #print("records[1]", records[1])
    # print("Distance before sorting: ", distance[:k])

    distance.sort()
    # print("Distance after sorting: ", distance[:k])


    #printRecords(distance[0:k+1])
    distanceList = distance[0:k]
    neightbours = []
    for count in range(len(distanceList)):
        neightbours += [records[distanceList[count][1]]]
    #printRecords(neightbours)
    return neightbours



def voting(listOfNeighbours, item, feature):
    voteDict = dict()
    for count in range(len(listOfNeighbours)):
        #print("listOfNeighbourslistOfNeighbours", listOfNeighbours[count])
        vote = listOfNeighbours[count][0]
        if(voteDict.has_key(vote)):
            count = voteDict.get(vote)
            voteDict.update( {vote: count+1}  )
        else:
            voteDict.update( {vote: 1}  )

    #majorityPrev = sorted(voteDict.items(), key = lambda kv:(kv[1], kv[0]))[-2][0]  
    majorityPrev = sorted(voteDict.items(), key = lambda kv:(kv[1], kv[0]))[-1][0]        
    majority = sorted(voteDict.items(), key = lambda kv:(kv[1], kv[0]))[-1][0]

    #print("sorted",sorted(voteDict.items(), key = lambda kv:(kv[1], kv[0])))  

    val1 = voteDict.get(majority)
    val2 = voteDict.get(majorityPrev)
    dist1 = 0
    dist2 = 0

    if(val1 == val2):
        for count in range(len(listOfNeighbours)):
            
            #if(listOfNeighbours[count][0] == majority):
            if(listOfNeighbours[count][0] == majority):
                #dist1 = 
                mipmap=listOfNeighbours[count]
                for featurelen in (range(len(feature))):
                    pos = feature[featurelen]
                    distanceMetric = pow(mipmap[pos] - item[pos],2)
                    dist1 = dist1 + distanceMetric

            if(listOfNeighbours[count][0] == majorityPrev):
                #dist1 = 
                mipmap=listOfNeighbours[count]
                for featurelen in (range(len(feature))):
                    pos = feature[featurelen]
                    distanceMetric = pow(mipmap[pos] - item[pos],2)
                    dist2 = dist2 + distanceMetric

    if(dist1 < dist2):
        majority = majorityPrev
    

    #print("itemitem", item[0])
    #print("majority", majority)
    return majority

def bin(records, digit):
    value = 0
    for count in range(len(records)):
        if( records[count][0] == digit):
            value += 1
    return count 



def accuracy(records, outcomes, confusion):
    value = 0
    #confusion = dict()
    for count in range(len(records)):
        if( records[count][0] == outcomes[count]):
            value += 1
        pair=(outcomes[count], records[count][0])
        if(confusion.has_key(pair)):
            count = confusion.get(pair)
            confusion.update( {pair: count+1}  )
        else:
            confusion.update( {pair: 1}  )
            
    #occurance = 

    return ((value/float(len(records))) * 100, confusion)

if __name__ == '__main__':
    records = getRecords('../digit-recognizer/train copy.csv')
    features = featureExtract(records, 11)

    #normalize(records,features)
    #47
    #69
    #146
    random.seed(19)
    random.shuffle(records)

    testData, validateData, trainData = setTrainValidateTestRecords(records)

    knnCount = 11

    learnedOutcomes = []
    #print("len(testData)", len(testData) )
    confused = dict()
    for index in range(0,len(testData)):
    #for index in range(1):
        classOfData = voting(knn(trainData, testData[index], features, knnCount), testData[index], features)
        #print("testData[1]",testData[1])
        #print("class",classOfData)
        learnedOutcomes += [classOfData]
        if(index % 100 == 0):
            print("index",index)
    print("learnedOutcomes",learnedOutcomes)
    print("accuracy",accuracy(testData, learnedOutcomes,confused)[0])
    print("confusion",accuracy(testData, learnedOutcomes, confused)[1])
    
    #printRecords(records)

    #sum = getSumCount(records)[0]
    #countMat = getSumCount(records)[1]

        
    