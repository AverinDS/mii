import pandas


def load_from_csv(variant):
    path_to_csv = 'C:\Users\DELL\YandexDisk\ulstu\CourceWorkMII\Chicago_Crimes_2001_to_2004.csv'
    # path_to_csv = 'C:\Users\DELL\YandexDisk\ulstu\CourceWorkMII\Chicago_Crimes_2005_to_2007.csv'
    # path_to_csv = 'C:\Users\DELL\YandexDisk\ulstu\CourceWorkMII\Chicago_Crimes_2008_to_2011.csv'
    # path_to_csv = 'C:\Users\DELL\YandexDisk\ulstu\CourceWorkMII\Chicago_Crimes_2012_to_2017.csv'

    data = pandas.read_csv(path_to_csv, index_col='ID', sep=',', error_bad_lines=False, nrows=150)
    if variant == True:
        return data[['Community Area', 'Primary Type']].as_matrix()
    elif variant == False:
        return data[['Community Area', 'FBI Code']].as_matrix()