import alphabets
from tqdm import tqdm
import random

def gen_random_copy_pair(alphabet, min_len=1, max_len=10):
  length = random.randrange(min_len,max_len)
  string = "".join(random.choice(alphabet) for _ in range(length))
  return f"{string},{string}"

def build_copy_data(alphabet, num_lines=10000, out_path="./copy-data/data.COPY", verbose=False):
  if verbose:
    print("Building copy data")
  lines = []
  pbar = tqdm(total=num_lines) if verbose else None
  for _ in range(num_lines):
    lines.append(gen_random_copy_pair(alphabet))
    if verbose:
      pbar.update()
  pbar.close()
  if verbose:
    print(f"Saving to {out_path}")
  with open(out_path, 'w') as outfile:
    for line in lines:
      outfile.write(f"{line}\n")

if __name__=="__main__":
  alphabet = alphabets.LATIN_SIMPLE_ALPHABET
  build_copy_data(alphabet, num_lines=1000, verbose=True)