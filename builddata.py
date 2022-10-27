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
  filepath_list = ["example/english_example.txt"]
  langs_list=["ENG_EX"]
  vocab = Vocabulary(['[SPACE]'] + LATIN_EXTENDED_ALPHABET)
  utils.make_data_splits(filepath_list, langs_list)

if __name__=="__main__":
  build_and_save_vocab()
  make_test_datasets()
  