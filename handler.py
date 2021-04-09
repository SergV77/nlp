#!flask/bin/python

from locLib import *
from locFunction import *



def handlerConcept(conceptId):

    #загружаем словарь параметров для обработки данных
    with open('models/model_best090421.pickle', 'rb') as infile:
        libs = pickle.load(infile)

    # загружаем обученную модель нейросети
    model = load_model('models/model_best090421.hdf5')


    loaded_test = conceptId  # загружаем полученные концепты
    # определяем параметры для обработки концептов

    vocabulary = libs['vocabulary']
    classes = libs['classes']
    nClasses = len(classes)
    xLen = libs['xLen']
    maxConceptsCount = len(vocabulary)

    # преобразуем полученный массив концептов в массив индексов согласно словаря
    conceptIndexes = []

    conceptIndexes.append(concept2Indexes(loaded_test, vocabulary, maxConceptsCount))

    xTest = changeSetTo01(conceptIndexes, maxConceptsCount)

    out = model.predict(xTest)
    print(out)
    print(np.argmax(out))

    print('Распознала сеть - ', classes[np.argmax(out)])

    diagnosis1 = classes[np.argmax(out)]


    return diagnosis1 #diagnosis2
