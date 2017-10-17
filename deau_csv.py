import codecs
import csv

def test():
    csv_file =codecs.open (u'/Users/lipeng/Desktop/replace_data.csv', 'r',encoding=u"utf-8")
    reader = csv.reader(csv_file)
    for lin in reader:
        print(str(lin))


test()