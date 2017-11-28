import numpy as np

def sort_col(i):
    return i[0]

def filterNan(lingvistic_second_col, prep):
    if lingvistic_second_col:
        data_for_classification = [i for i in prep if not (np.isnan(i[0]))]
        data_for_classification.sort(key=sort_col)
        return data_for_classification
    else:
        data_for_classification = [i for i in prep if not (np.isnan(i[0]) or np.isnan(i[1]))]
        data_for_classification.sort(key=sort_col)
        return data_for_classification


def prepareData(data, lingvistic_second_col):
    prep = []
    dictionary = dict()
    max_value = 0  # max value in Dictionary
    for i in data:
        try:
            l = []
            l.append(float(str(i[0]).strip()))
            item = str(i[1]).strip()

            if lingvistic_second_col:  # it 'if' contains two cases: for FBI code as second col or
                #  PrimaryDescription (linguist's mark)
                if item in dictionary:  # if dic contains key item
                    l.append(int(dictionary[item]))
                else:
                    dictionary[item] = max_value
                    max_value += 1
                    l.append(int(dictionary[item]))
            else:
                item = item.replace('A', '')
                item = item.replace('B', '')
                l.append(int(item))

            prep.append(l)
        except:
            print "Ignore: ", i
            continue
    filter_data = filterNan(lingvistic_second_col, prep)
    X = []
    y = []
    for i in filter_data:
        X.append(i[0])
        y.append(i[1])

    X = np.matrix(X).reshape(-1, 1)
    y = np.matrix(y).reshape(-1, 1)
    return X, y, filter_data, dictionary

