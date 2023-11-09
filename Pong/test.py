import sys

def solution(S):
  sys.stderr.write(
      'Tip: Use sys.stderr.write() to write debug messages on the output tab.\n'
  )
  hash_map = {}
  max_value = 9
  for letter in S:
    if letter not in hash_map:
      hash_map[letter]=max_value
      max_value -=1
      print(hash_map)
  """number = 0
  for letter in S:
    number = number * 10 + hashmap[letter]
  return number"""

  solution("BABBC")