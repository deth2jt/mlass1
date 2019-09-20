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
            if(line_count > 0):
                cell = [float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]) ]
                records += [cell]

            line_count += 1

            #if(line_count % 100 == 0):
                #print("reading line ", line_count)

        line_count=line_count-1
    return records

    
        
    
def getSumCount(records):
    countMat = [0,0,0,0,0,0,0,0]
    sum = [0,0,0,0,0,0,0,0, 0]

    for count in range(len(records)):
        cell = records[count]
        #print("sum[8]", sum[8])
        #print("cell[8]", cell[8])
        sum[8] = sum[8]  + (cell[8])
        if( (cell[1]) != 0):
            sum[1] = sum[1]  + (cell[1])
            countMat[1] = countMat[1] + 1

        if((cell[2]) != 0):
            sum[2] = sum[2] + (cell[2])
            countMat[2] = countMat[2] + 1

        if((cell[3]) != 0):
            sum[3] = sum[3]  + (cell[3])
            countMat[3] = countMat[3] + 1
        #print(cell[4] != 0)
        #print("len(records)", len(records))
        if(cell[4] != 0):
            sum[4] = sum[4] + cell[4]
            countMat[4] = countMat[4] + 1
            #print("countMat[4]", countMat[4])

        if((cell[5]) != 0 ):
            sum[5] = sum[5]  + (cell[5])
            countMat[5] = countMat[5] + 1
    return (sum, countMat)


    
def updateZeroValues(records,avg):
    for count in range(len(records)):
        cell = records[count]
        if( (cell[1]) == 0):
            records[count][1] = avg[1]

        if((cell[2]) == 0):
            records[count][2] = avg[2]

        if((cell[3]) == 0):
            records[count][3] = avg[3]

        if((cell[4]) == 0):
            records[count][4] = avg[4]

        if((cell[5]) == 0 ):
            records[count][5] = avg[5]
    return records
    
    
def getMinMaxValues(records):
    low = [sys.maxint,sys.maxint,sys.maxint,sys.maxint,sys.maxint,sys.maxint, sys.maxint, sys.maxint]
    high = [0,0,0,0,0,0,0,0]

    for count in range(len(records)):
        cell = records[count]
        if((cell[0]) < (low[0]) ):
            low[0] = cell[0]

        if( (cell[1]) < (low[1])):
            low[1] = cell[1]

        if((cell[2]) < (low[2])):
            low[2] = cell[2]

        if((cell[3]) < (low[3])):
            low[3] = cell[3]

        if((cell[4]) < (low[4])):
            low[4] = cell[4]

        if((cell[5]) < (low[5]) ):
            low[5] = cell[5]

        if((cell[6]) < (low[6])):
            low[6] = cell[6]

        if((cell[7]) < (low[7])):
            low[7] = cell[7]

        #high
        if((cell[0]) > (high[0])):
            high[0] = cell[0]

        if((cell[1]) > (high[1])):
            high[1] = cell[1]

        if((cell[2]) > (high[2])):
            high[2] = cell[2]

        if((cell[3]) > (high[3])):
            high[3] = cell[3]

        if((cell[4]) > (high[4])):
            high[4] = cell[4]

        if((cell[5]) > (high[5])):
            high[5] = cell[5]

        if((cell[6]) > (high[6])):
            high[6] = cell[6]

        if((cell[7]) > (high[7])):
            high[7] = cell[7]

    return (low, high)


def normalize(records,high,low):
    for count in range(len(records)):
        #cell = records[count]
        records[count][0] = (records[count][0] - low[0]) / (high[0]-low[0])

        records[count][1] = (records[count][1] - low[1]) / (high[1]-low[1])
        records[count][2] = (records[count][2] - low[2]) / (high[2]-low[2])
        records[count][3] = (records[count][3] - low[3]) / (high[3]-low[3])
        records[count][4] = (records[count][4] - low[4]) / (high[4]-low[4])
        records[count][5] = (records[count][5] - low[5]) / (high[5]-low[5])
        records[count][6] = (records[count][6] - low[6]) / (high[6]-low[6])
        records[count][7] = (records[count][7] - low[7]) / (high[7]-low[7])
    return records

def printRecords(records):  
    for count in range(len(records)):
        print(count, ": ", records[count])

def setTrainValidateTestRecords(records):
    line_count= len(records)
    testValSize = .10*line_count

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
    return testData,validateData,trainData
    

def knn(records, item, feature, k):
    print("item", item)
    distance = []
    for count in range(len(records)):
        value = 0
        '''
        value = abs(records[count][0] - item[0])**2 + abs(records[count][1] - item[1] ) **2+ abs(records[count][2] - item[2] )**2
        + abs(records[count][3] - item[3] ) **2
        + abs(records[count][4] - item[4] ) **2+ abs(records[count][5] - item[5] ) **2+ abs(records[count][6] - item[6] )**2
        + abs(records[count][7] - item[7] )**2
        
        value = abs(records[count][0] - item[0])**2 + abs(records[count][1] - item[1] ) **2+ abs(records[count][2] - item[2] )**2
        + abs(records[count][3] - item[3] ) **2
        + abs(records[count][4] - item[4] ) **2+ abs(records[count][5] - item[5] ) **2+ abs(records[count][6] - item[6] )**2
        + abs(records[count][7] - item[7] )**2
        '''
        for featurelen in (range(len(feature))):
            pos = feature[featurelen]
            distanceMetric = pow(records[count][pos] - item[pos],2)
            value = value + (distanceMetric)
        #value = abs(records[count][1] - item[1] ) **2
            value = math.sqrt(value) #for minkowski 
        distance = distance + [(value, count,   records[count][-1])]
    #printRecords(distance)
    #print("records[1]", records[1])
    distance.sort()


    #printRecords(distance[0:k+1])
    distanceList = distance[0:k]
    neightbours = []
    for count in range(len(distanceList)):
        neightbours += [records[distanceList[count][1]]]
    printRecords(neightbours)
    return neightbours

def voting(listOfNeighbours):
    voteDict = dict()
    for count in range(len(listOfNeighbours)):
        vote = listOfNeighbours[count][-1]
        if(voteDict.has_key(vote)):
            count = voteDict.get(vote)
            voteDict.update( {vote: count+1}  )
        else:
            voteDict.update( {vote: 1}  )
    majority = sorted(voteDict.items(), reverse=True, key = lambda kv:(kv[1], kv[0]))[0][0]
    #print("sorted",sorted(voteDict.items(), key = lambda kv:(kv[1], kv[0])))  
    return majority

def validation(records, outcomes):
    FN = 0
    FP = 0
    TN = 0
    TP = 0
    for count in range(len(records)):
        print("outcomes[count]", outcomes[count])
        if(outcomes[count] == 1 and records[count][-1] == 0):
            FP = FP + 1
        if(outcomes[count] == 0 and records[count][-1] == 1):
            FN = FN + 1
        if(outcomes[count] == 0 and records[count][-1] == 0):
            TN = TN + 1
        if(outcomes[count] == 1 and records[count][-1] == 1):
            TP = TP + 1
    
    
    return ( TP, FP, FN, TN)

def accuracy(records, outcomes):
    value = 0
    for count in range(len(records)):
        if records[count][-1] == outcomes[count]:
            value += 1
        
    
    
    return ((value/float(len(records))) * 100)

if __name__ == '__main__':
    records = getRecords('diabetes.csv')
    
    #printRecords(records)

    sum = getSumCount(records)[0]
    countMat = getSumCount(records)[1]

    #printRecords(sum)
    #printRecords(countMat)

    avg = [0,sum[1]/countMat[1],sum[2]/countMat[2],sum[3]/countMat[3],sum[4]/countMat[4],sum[5]/countMat[5],0,0]

    updateZeroValues(records, avg)

    low = getMinMaxValues(records)[0]
    high = getMinMaxValues(records)[1]

    normalize(records, high,low)

    #23
    random.seed(23)
    random.shuffle(records)

    testData, validateData, trainData = setTrainValidateTestRecords(records)

    #pregn 0 Gluco 1 Bloodp 2 skinth 3 insulin 4 bmi 5 diabetic 6 age 7 
    #features = [1,5,0,6,7]
    features = [1,5]
    #printRecords(trainData)
    knnCount = 9

    learnedOutcomes = []
    learnedOutcomesval = []
    for index in range(0,len(testData)):
        classOfData = voting(knn(trainData, testData[index], features, knnCount))
        #print("testData[1]",testData[1])
        #print("class",classOfData)
        learnedOutcomes += [classOfData]
    for index in range(0,len(validateData)):
        classOfData = voting(knn(trainData, validateData[index], features, knnCount))
        #print("testData[1]",testData[1])
        #print("class",classOfData)
        learnedOutcomesval += [classOfData]

    ACC = accuracy(testData, learnedOutcomes)
    (TP, FP, FN, TN) = validation(validateData, learnedOutcomesval)
    print("accuracy",ACC)
    print("TP",TP)
    print("FP",FP)
    print("FN",FN)
    print("TN",TN)

    

    '''
    print("avg", avg)
    print("countMat", countMat)
    print("sum", sum)
    print("low ", low)
    print("high ", high)
    '''
    
    
        
    