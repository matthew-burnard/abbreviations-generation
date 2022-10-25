from random import shuffle

def make_data_splits(filepath_list, lang_list, ratio=0.8, space_tok='[SPACE]'):
  train_src_file=open("data/train.src", 'w')
  train_tgt_file=open("data/train.tgt", 'w')
  dev_src_file=open("data/dev.src", 'w')
  dev_tgt_file=open("data/dev.tgt", 'w')
  test_src_file=open("data/test.src", 'w')
  test_tgt_file=open("data/test.tgt", 'w')
  for filepath,lang in zip(filepath_list,lang_list):
    with open(filepath, 'r') as file:
      lines = file.readlines()
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
    
    def _write_toks(lines, src_file, tgt_file):
      for line in lines:
        tgt,src=line.lower().split(',')
        toks=[]
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
      src_file.flush()
      tgt_file.flush()
    
    _write_toks(train_lines, train_src_file, train_tgt_file)
    _write_toks(dev_lines, dev_src_file, dev_tgt_file)
    _write_toks(test_lines, test_src_file, test_tgt_file)
  
  train_src_file.close()
  train_tgt_file.close()
  dev_src_file.close()
  dev_tgt_file.close()
  test_src_file.close()
  test_tgt_file.close()