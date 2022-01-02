from nltk.tokenize import sent_tokenize
import pandas as pd

path = "experiment/CaseStudies/"
input_path = path + "input/"
output_path = path + "output_CoNLL++/"

df = pd.read_excel(path + 'CaseStudies.xlsx')
contents = df['Details of the impact'].str.replace('\n', " ")

threshold = 6638
for index, row in contents.iteritems():
    if index < threshold:
        list_sentences = sent_tokenize(str(row))
        file_input = input_path + str(index) + ".txt"
        textfile = open(file_input, "a")
        for ele in list_sentences:
            textfile.write(ele + "\n")
        textfile.close()
