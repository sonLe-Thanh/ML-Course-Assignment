## NER Tagger

This NER Tagger was originally from https://github.com/glample/tagger. Small adjustments have been made to work with Python 3.


## Tag sentences

There are 2 pretrained models. They can be called using

```
python tagger.py --model <model path> --input <input file> --output <output file>
```

The input file should contain one sentence by line, and they have to be tokenized. Otherwise, the tagger will perform poorly.


## Train a model

To train a model, you need to use the train.py script:

```
python train.py --train <train file> --dev <dev file> --test <test file>
```

The training script will automatically give a name to the model and store it in ./models/
There are many parameters you can tune (CRF, dropout rate, embedding dimension, LSTM hidden layer size, etc). To see all parameters, run

```
python train.py --help
```

Input files for the training script have to follow the same format as the CoNLL2003 sharing task: each word has to be on a separate line, and there must be an empty line after each sentence. A line must contain at least 2 columns, the first one being the word itself, the last one being the named entity. It does not matter if there are extra columns that contain tags or chunks in between. Tags have to be given in the IOB format (it can be IOB1 or IOB2).

## 