import os

path = "experiment/CaseStudies/"
input_path = path + "input/"
output_path = path + "output_CoNLL++/"

threshold = 6638

for i in range(threshold):
    command = "python tagger.py --model models/CoNLL++/ " \
              "--input experiment/CaseStudies/input/" + str(i) + ".txt " \
                                                                 "--output_CoNLL++ experiment/CaseStudies/output_CoNLL++/"+ str(i) + ".txt"
    os.system(command)