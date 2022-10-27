from joeynmt.vocabulary import Vocabulary
from pathlib import Path
from alphabets import LATIN_EXTENDED_ALPHABET
import utils
from tokenizer import Tokenizer


def raw_to_src():
  with open("langs/english_example.txt", 'r') as file:
    en_lines = file.readlines()

  batch_size=5

  targets,inputs=[],[]
  for line in en_lines[:batch_size]:
    target,input = line.lower().strip().split(',')
    inputs.append(input)
    targets.append(target)

  max_len=max([len(str) for str in inputs])+2

  tokenizer = Tokenizer(lang='en')

  target_toks,input_toks = [],[]
  for target_str,input_str in zip(targets,inputs):
    target_tok =tokenizer.tokenize(target_str, max_len)
    target_toks.append(target_tok)


#Make vocabulary
def build_and_save_vocab():
  vocab = Vocabulary(['[SPACE]'] + LATIN_EXTENDED_ALPHABET)
  vocab.to_file(Path("example/vocab.txt"))

#Make dataset files
def make_test_datasets():
  filepath_list = ["example/english_example.txt"]
  langs_list=["ENG_EX"]
  vocab = Vocabulary([' '] + LATIN_EXTENDED_ALPHABET)
  utils.make_data_splits(filepath_list, langs_list)

if __name__=="__main__":
  raw_to_src()
  make_test_datasets()