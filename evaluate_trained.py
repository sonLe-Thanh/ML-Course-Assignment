import optparse
import loader
from model import Model
from utils import evaluate
from loader import word_mapping, char_mapping, tag_mapping
from loader import update_tag_scheme, prepare_dataset

optparser = optparse.OptionParser()
optparser.add_option(
    "-m", "--model", default="",
    help="Model location"
)

optparser.add_option(
    "-T", "--train", default="",
    help="Train set location"
)
optparser.add_option(
    "-d", "--dev", default="",
    help="Dev set location"
)
optparser.add_option(
    "-t", "--test", default="",
    help="Test set location"
)

opts = optparser.parse_args()[0]

# Load existing model
print("Loading model...")
model = Model(model_path=opts.model)
parameters = model.parameters

# Load the model
f_train, f_eval = model.build(training=False, **parameters)
model.reload()

# Data parameters
lower = parameters['lower']
zeros = parameters['zeros']
tag_scheme = parameters['tag_scheme']

# Load sentences
train_sentences = loader.load_sentences(opts.train, lower, zeros)
dev_sentences = loader.load_sentences(opts.dev, lower, zeros)
test_sentences = loader.load_sentences(opts.test, lower, zeros)

# Use selected tagging scheme (IOB / IOBES)
update_tag_scheme(train_sentences, tag_scheme)
update_tag_scheme(dev_sentences, tag_scheme)
update_tag_scheme(test_sentences, tag_scheme)

# Load reverse mappings
word_to_id, char_to_id, tag_to_id = [
    {v: k for k, v in x.items()}
    for x in [model.id_to_word, model.id_to_char, model.id_to_tag]
]

# Index data
train_data = prepare_dataset(
    train_sentences, word_to_id, char_to_id, tag_to_id, lower
)
dev_data = prepare_dataset(
    dev_sentences, word_to_id, char_to_id, tag_to_id, lower
)
test_data = prepare_dataset(
    test_sentences, word_to_id, char_to_id, tag_to_id, lower
)

dico_words, word_to_id, id_to_word = word_mapping(train_sentences, lower)
dico_words_train = dico_words

dico_chars, char_to_id, id_to_char = char_mapping(train_sentences)
dico_tags, tag_to_id, id_to_tag = tag_mapping(train_sentences)

print("Dev result")
dev_score = evaluate(parameters, f_eval, dev_sentences, dev_data, id_to_tag, dico_tags)
print("Test result")
test_score = evaluate(parameters, f_eval, test_sentences, test_data, id_to_tag, dico_tags)
print("Score on dev: %.5f" % dev_score)
print("Score on test: %.5f" % test_score)
