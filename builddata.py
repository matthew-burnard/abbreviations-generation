from joeynmt.vocabulary import Vocabulary
from pathlib import Path
from alphabets import LATIN_EXTENDED_ALPHABET
import utils
from tokenizer import Tokenizer


#Make vocabulary
def build_and_save_vocab():
  vocab = Vocabulary(['[SPACE]'] + LATIN_EXTENDED_ALPHABET)
  vocab.to_file(Path("example/vocab.txt"))

#Make dataset files
def make_test_datasets():
  filepath_list = ["langs/english_numpy.txt"]
  langs_list=["ENG"] #Add the language tag to the front
  vocab = Vocabulary(['[SPACE]'] + LATIN_EXTENDED_ALPHABET)
  utils.make_data_splits(filepath_list, langs_list, verbose=True)

if __name__=="__main__":
  build_and_save_vocab()
  make_test_datasets()
  