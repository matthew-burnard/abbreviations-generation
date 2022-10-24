import numpy as np

class LanguageNotImplementedException(Exception):
  pass
class CharNotInAlphabetException(Exception):
  pass
class InputMismatchException(Exception):
  pass


class Tokenizer:
  def __init__(self, lang='en',
      pad_idx=0, pad_tok='[PAD]', start_idx=1, start_tok='[START]', end_idx=2, end_tok='[END]', space_idx=3, space_tok='[SPACE]'):
    #set alphabet used by language
    if lang=='en':
      alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    else:
      raise LanguageNotImplementedException(f"Language not implemented: {lang}")
    #Set our special tokens
    self.pad_idx=pad_idx
    self.pad_tok=pad_tok
    self.start_idx=start_idx
    self.start_tok=start_tok
    self.end_idx=end_idx
    self.end_tok=end_tok
    self.space_idx=space_idx
    self.space_tok=space_tok
    #Add tokens to the alphabet
    alphabet.insert(pad_idx, self.pad_tok)
    alphabet.insert(start_idx, self.start_tok)
    alphabet.insert(end_idx, self.end_tok)
    alphabet.insert(space_idx, self.space_tok)
    self.alphabet=alphabet
    self.alphabet_size=len(self.alphabet)
    
    print(f"Alphabet: {self.alphabet}")
    print(f"Alphabet size: {self.alphabet_size}")
  
  ## Returns a list of token indexes for each character in the input string, padded to max_len
  def tokenize(self, string_in, max_len=-1, pad=True):
    list_out=[]
    list_out.append(self.start_idx)
    for char in string_in:
      char_idx=None
      if char==' ':
        char_idx=self.space_idx
      else:
        try:
          char_idx=self.alphabet.index(char)
        except:
          raise CharNotInAlphabetException(f"Character {char} is not in the alphabet")
      list_out.append(char_idx)
    list_out.append(self.end_idx)
    if pad==True:
      if max_len==-1:
        raise InputMismatchException("Must specify max length to pad")
      for i in range(len(list_out), max_len):
        list_out.append(self.pad_idx)
    return np.array(list_out)
  
  ## Returns a list of the tokens from a token list
  def print_tok_list(self, list_in):
    list_out = []
    for tok in list_in:
      list_out.append(self.alphabet[tok])
    return list_out
  
  ## Returns the string representation of a token list
  def detokenize(self, list_in):
    string_out = []
    for tok in list_in[1:-1]:
      if tok==self.space_idx:
        string_out.append(' ')
      elif tok==self.end_idx:
        break
      else:
        string_out.append(self.alphabet[tok])
    return "".join(string_out)

