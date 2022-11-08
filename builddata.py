from joeynmt.vocabulary import Vocabulary
from pathlib import Path
from alphabets import LATIN_EXTENDED_ALPHABET,TASK_TOKS,LANG_TOKS
import utils
from tokenizer import Tokenizer
import os
import argparse
  

#Make dataset files
def make_test_datasets(filepath_list, langs_list):
  vocab = Vocabulary(['[SPACE]'] + LANG_TOKS + LATIN_EXTENDED_ALPHABET)
  vocab.to_file(Path("data/vocab.txt"))
  utils.make_data_splits(filepath_list, langs_list, verbose=True)

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--datapath', type=str)
  args = parser.parse_args()
  return args

if __name__=="__main__":
  args=get_args()
  datapath=args.datapath
  filepath_list = []
  langs_list=[]
  if datapath==None:
    filepath_list.append("langs/english_numpy.EN") #default to english abbreviations
    langs_list=["EN"]
  elif os.path.isfile(datapath):
    filepath_list.append(datapath)
    lang=datapath.rsplit('.', 1)[1]
    langs_list.append(lang)
  elif os.path.isdir(datapath):
    #Need to walk the file and produce a list of languages and a list of 
    raise NotImplementedError("Getting multiple languages from one filepath not yet implemented.")
  else:
    raise FileNotFoundError(f"\"{datapath}\" is not a file or directory")
  make_test_datasets(filepath_list, langs_list)
  