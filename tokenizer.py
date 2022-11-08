import alphabets

class Tokenizer:
  def __init__(self, alphabet='latin',
      pad_idx=0, pad_tok='[PAD]', start_idx=1, start_tok='[SOS]', end_idx=2, end_tok='[EOS]', space_idx=3, space_tok='[SPACE]', lang_idx=4):
    #set alphabet used by language
    if alphabet=='latin':
      self.alphabet = alphabets.LATIN_EXTENDED_ALPHABET
      lang_tok='[ENG]'
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
    self.lang_idx=lang_idx
    self.lang_tok=lang_tok
    #Add tokens to the alphabet
    self.alphabet.insert(self.pad_idx, self.pad_tok)
    self.alphabet.insert(self.start_idx, self.start_tok)
    self.alphabet.insert(self.end_idx, self.end_tok)
    self.alphabet.insert(self.space_idx, self.space_tok)
    self.alphabet.insert(self.lang_idx, self.lang_tok)
    self.alphabet_size=len(self.alphabet)
    
    print(f"Alphabet: {self.alphabet}")
    print(f"Alphabet size: {self.alphabet_size}")
  
  ## Returns a list of token indexes for each character in the input string, padded to max_len
  def tokenize(self, string_in, max_len, pad=True):
    list_out=[]
    list_out.append(self.lang_idx)
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
      for i in range(len(list_out), max_len):
        list_out.append(self.pad_idx)
    return list_out
  
  ## Returns a list of the tokens from a token list
  def str_of_tok_list(self, list_in, ignore_pad=False):
    list_out = []
    for tok in list_in:
      if ignore_pad and tok==self.pad_idx:
        break
      list_out.append(self.alphabet[tok])
    return " ".join(list_out)
  
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

