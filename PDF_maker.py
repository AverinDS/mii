# In PDF
from collections import Counter

from pypdflite import PDFLite


def make_pdf_clusters(data, dictionary, number):
    writer = PDFLite("reports/Cluster#"+str(number)+".pdf")
    writer.set_information(title="Statistic")
    document = writer.get_document()
    n_cluster = 1
    index_list = 0
    for i in data:
        if index_list == 0 or index_list == 1:
            index_list+=1
            continue
        index_list += 1
        line = "Area#" + str(i[0]) + " Description: " + str({key for key, value in dictionary.iteritems() if value == i[1]})\
            .replace('set([','').replace('])','') + "\n"
        document.add_text("Cluster #" + str(n_cluster) + ":" + line)
    writer.close()

def make_pdf_clusters_without_descr(data, number):
    writer = PDFLite("reports/Cluster#" + str(number) + ".pdf")
    writer.set_information(title="Statistic")
    document = writer.get_document()
    n_cluster = 1
    index_list = 0
    for i in data:
        if index_list == 0 or index_list == 1:
            index_list += 1
            continue
        index_list += 1
        line = "Area#" + str(i[0]) + " FBI CODE: " + str(i[1]) + "\n"
        document.add_text("Cluster #" + str(n_cluster) + ":" + line)
    writer.close()

def makeCounter(data, dictionary, isLingvistic):

    data_counter = []
    for i in data:
        if isLingvistic:
            data_counter.append("In area #" + str(i[0]) + " crimea " + str({key for key, value in dictionary.iteritems() if value == i[1]})\
            .replace('set([','').replace('])','') + " contains ones ")
        else:
            data_counter.append("In area #" + str(i[0]) + " crimea " + str(i[1]) + " contains ones ")

    writer = PDFLite("reports/Counter.pdf")
    writer.set_information(title="Statistic")
    document = writer.get_document()
    counter = Counter(data_counter)
    for i in counter.most_common(len(counter)):
        document.add_text(str(i[0]) + " " + str(i[1]) + "\n")
    writer.close()
