#!flask/bin/python

from locLib import *
from locFunction import *



allLoadData = []  # ......... указатель на функцию загрузки дата сэта -  в процессе создания
loaded_test = []  # ......... указатель на функцию загрузки тестового дата сэта -  в процессе создания
classes = []  # ......... указатель на функцию создания классов -  в процессе создания
nClasses = len(classes)


allIdInClass = []
allIdForVoc = []
allSum = 0


for i in range(len(allLoadData)):
    allNum = []
    for num in allLoadData[i]:
        for sym in num:
            allNum.append(sym)
            allIdForVoc.append(sym)

    allIdInClass.append(allNum)

# print(newAllLoadData[i])
print('Общее количество симптомов в классе ', classes[i], ' - ', len(allIdInClass[i]))
allSum += len(allIdInClass[i])
print('Общее количество симптомов по всем классам -', allSum)

vocabulary = createVocabulary(allIdForVoc)
maxConceptsCount = len(allIdForVoc)

conceptIndexes = []
for i in range(len(allIdInClass)):
    conceptIndexes.append(concept2Indexes(allIdInClass[i], vocabulary, maxConceptsCount))

nval = 100
trainConcepts = []
valConcepts = []

for i in range(len(conceptIndexes)):
    trainConcepts.append(conceptIndexes[i][:-nval])
    valConcepts.append(conceptIndexes[i][-nval:])
    print(i, classes[i], len(trainConcepts[i]), len(valConcepts[i]))

allIdcount = maxConceptsCount
xLen = 50
step = 1
(xTrain, yTrain) = createSetsMultiClasses(trainConcepts, xLen, step)
xTrain01 = changeSetTo01(xTrain, allIdcount)

(xVal, yVal) = createSetsMultiClasses(valConcepts, xLen, step)
xVal01 = changeSetTo01(xVal, allIdcount)



xTrainIndex = []
xValIndex = []
for i in range(len(conceptIndexes)):
    (xTrain, yTrain, xVal, yVal) = createTestsClasses(conceptIndexes[i], 0.8)
    xTrainIndex.append(xTrain)
    xValIndex.append(xVal)


(xTest, yTest) = createSetsMultiClasses(xTestIndex, xLen, step)
xTest01 = changeSetTo01(xTest, allIdcount)

for i in range(len(xTestIndex)):
    testConceptIndexes = np.array(xTestIndex[i]).reshape(1, len(xTestIndex[i]))
    testConceptIndexes = pad_sequences(testConceptIndexes, xLen)
    testConceptIndexes01 = changeSetTo01(testConceptIndexes, allIdcount)
    out = model_BOW.predict(testConceptIndexes01)
    # print(out)
    # print(np.argmax(out))

    print('Распознала сеть - ', classes[np.argmax(out)], ' | ', 'Фактический симптом - ', classes[i])


testConceptIndexes = np.array(loaded_test).reshape(1,len(loaded_test))
testConceptIndexes = pad_sequences(testConceptIndexes, xLen)
testConceptIndexes01 = changeSetTo01(testConceptIndexes, allIdcount)
