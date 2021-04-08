#!flask/bin/python

from locLib import *
from locFunction import *

app = Flask(__name__)

@app.route('/')
def welcome():
   return "Добро пожаловать в наш сервис"

@app.route('/requestApi', methods=['POST'])
def requestApi():

    symptoms_list = request.json['symptom']
    print(symptoms_list)

    url = 'https://cs.socmedica.com/api/pars/ParsingConcept'

    param = {'key': '9244f7d34ca284b1',
             'lib': [25],
             'text': symptoms_list
             }

    response = requests.post(url, param)
    outs = response.json()
    print(outs)

    conceptName = []
    conceptId = []
    conceptCh = []

    for out in outs['Result']:
        print(out['nameConcept'])
        print(out['idConcept'])
        # print(out['id'])
        print(out['chance'])
        conceptName.append(out['nameConcept'])
        conceptId.append(out['idConcept'])
        conceptCh.append(out['chance'])

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

    out = model.predict(testConceptIndexes01)
    print(out)
    print(np.argmax(out))
    print(classes[np.argmax(out)])

    model = load_model('/content/drive/My Drive/Neuro/NLP/models/model_best290321.hdf5')

    probability = (max(out[0]) * 100)
    diagnosis = classes[np.argmax(out)]



    result = {'Вероятность совпадения': Chance, 'Диагноз ': diagnosis }
    return result



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8088)