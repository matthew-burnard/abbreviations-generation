from random import shuffle
from joeynmt.vocabulary import Vocabulary
from tqdm import tqdm
import re

def make_data_splits(filepath_list, lang_list, ratio=0.8, space_tok='[SPACE]', include_lang_tok=True, verbose=False):
  if verbose:
    print("Making data splits")
  train_src_file=open("data/train.src", 'w')
  train_tgt_file=open("data/train.tgt", 'w')
  dev_src_file=open("data/dev.src", 'w')
  dev_tgt_file=open("data/dev.tgt", 'w')
  test_src_file=open("data/test.src", 'w')
  test_tgt_file=open("data/test.tgt", 'w')
  lang_line_list=[]
  total=0
  for filepath,lang in zip(filepath_list,lang_list):
    with open(filepath, 'r') as file:
      lines = file.readlines()
    lang_line_list.append((lang,lines))
    total+=len(lines)
  
  pbar = tqdm(total=total) if verbose else None
  for lang,lines in lang_line_list:
    lang_tok = '[' + lang + ']'
    train_size=ratio
    train_idx_end=int(len(lines)*train_size)
    dev_size=(1-ratio)/2
    dev_idx_end=int(train_idx_end+len(lines)*dev_size)
    test_size=(1-ratio)/2
    
    shuffle(lines)
    
    train_lines = lines[:train_idx_end]
    dev_lines = lines[train_idx_end:dev_idx_end]
    test_lines = lines[dev_idx_end:]
    
    def _write_toks(lines, src_file, tgt_file, pbar=None):
      for line in lines:
        tgt,src=line.lower().split(',')
        toks=[]
        if include_lang_tok:
          toks.append(lang_tok)
        for char in src[:-1]:
          if char==' ':
            toks.append(space_tok)
          else:
            toks.append(char)
        src_file.write(" ".join(toks) + '\n')
        toks=[]
        for char in tgt:
          if char==' ':
            toks.append(space_tok)
          else:
            toks.append(char)
        tgt_file.write(" ".join(toks) + '\n')
        if type(pbar)!=type(None):
          pbar.update()
      src_file.flush()
      tgt_file.flush()
    
    _write_toks(train_lines, train_src_file, train_tgt_file, pbar=pbar)
    _write_toks(dev_lines, dev_src_file, dev_tgt_file, pbar=pbar)
    _write_toks(test_lines, test_src_file, test_tgt_file, pbar=pbar)
  
  train_src_file.close()
  train_tgt_file.close()
  dev_src_file.close()
  dev_tgt_file.close()
  test_src_file.close()
  test_tgt_file.close()

def make_outputs(out_filepath="./outputs.txt"):
  preds_dev="./preds.dev"
  src_dev="./data/dev.src"
  tgt_dev="./data/dev.tgt"
  
  out=[["source","target","pred"]]
  # Get dev data and preds
  src_file,tgt_file,pred_file=open(src_dev),open(tgt_dev),open(preds_dev)
  src_lines,tgt_lines,pred_lines=src_file.readlines(),tgt_file.readlines(),pred_file.readlines()
  src_file.close(),tgt_file.close(),pred_file.close()
  for src,tgt,pred in zip(src_lines,tgt_lines,pred_lines):
    src=re.sub('[ \n]+','', src)
    src=src.replace("[SPACE]",' ')
    tgt=re.sub('[ \n]+','', tgt)
    pred=re.sub('[ \n]+','', pred)
    out.append([src,tgt,pred])
  
  #Get test data and preds
  preds_test="./preds.test"
  src_test="./data/test.src"
  tgt_test="./data/test.tgt"
  src_file,tgt_file,pred_file=open(src_test),open(tgt_test),open(preds_test)
  src_lines,tgt_lines,pred_lines=src_file.readlines(),tgt_file.readlines(),pred_file.readlines()
  src_file.close(),tgt_file.close(),pred_file.close()
  for src,tgt,pred in zip(src_lines,tgt_lines,pred_lines):
    src=re.sub('[ \n]+','', src)
    src=src.replace("[SPACE]",' ')
    tgt=re.sub('[ \n]+','', tgt)
    pred=re.sub('[ \n]+','', pred)
    out.append([src,tgt,pred])
  
  outfile=open(out_filepath, 'w')
  for src,tgt,pred in out:
    outfile.write(f"{src}, {tgt}, {pred}\n")
  outfile.close()
  