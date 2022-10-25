from random import shuffle

def make_data_splits(filepath, ratio=0.8):
  with open(filepath, 'r') as file:
    lines = file.readlines()
  train_size=ratio
  train_idx_end=len(lines)*train_size
  dev_size=(1-ratio)/2
  dev_idx_end=train_idx_end+len(lines)*dev_size
  test_size=(1-ratio)/2
  
  shuffle(lines)
  
  train_lines = lines[:train_idx_end]
  dev_lines=lines[train_idx_end:dev_idx_end]
  test_lines=lines[dev_idx_end:]
  
  train_file=open("data.train", 'w')
  for line in trainlines:
    train_file.write(line)
  train_file.close()
  
  dev_file=open("data.dev", 'w')
  for line in devlines:
    dev_file.write(line)
  dev_file.close()
  
  test_file=open("data.test", 'w')
  for line in testlines:
    test_file.write(line)
  test_file.close()