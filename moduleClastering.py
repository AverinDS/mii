import Clusterisation, LoadData, MakePlot, PDF_maker, PrepareData, DataFromClusters

n_clusters = 10 #or -1 for clasters == crimeies not more 156
primaryType = False # == !FBI code

X, y, data, dictionary_crimes = PrepareData.prepareData(LoadData.load_from_csv(primaryType), primaryType)  # dictionary is exist onprimaryType == True

k_means, n_clusters = Clusterisation.make_k_means(n_clusters, data)

MakePlot.make_plot(k_means, X, y, n_clusters)

data_clusters = DataFromClusters.get_data_clusters(k_means, X, y)

if primaryType:
    n = 1
    for i in data_clusters:
        PDF_maker.make_pdf_clusters(i,dictionary_crimes, n)
        n += 1
else:
    n = 1
    for i in data_clusters:
        PDF_maker.make_pdf_clusters_without_descr(i, n)
        n += 1

PDF_maker.makeCounter(data, dictionary_crimes, primaryType)

