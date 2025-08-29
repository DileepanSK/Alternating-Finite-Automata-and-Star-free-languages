import sys
from collections import defaultdict
sys.stdin = open('AFAinput.txt', 'r')


def rewrite(exp, i):
  explist = []
  j = 0
  while j < len(exp):
      if exp[j].isdigit():
          # for multi-digit number
          k = j
          while k < len(exp) and exp[k].isdigit():
              k += 1
          q = int(exp[j:k])
          explist.append(f"fn({q}, g, f, word, {i+1})")
          j = k
      else:
          explist.append(exp[j])
          j += 1
  exp2 = "".join(explist)
  # print(exp)
  # replace ops
  exp2 = exp2.replace("&"," and ")
  exp2 = exp2.replace("|"," or ")
  exp2 = exp2.replace("~"," not ")
  exp2 = exp2.replace("F"," False ")
  exp2 = exp2.replace("T"," True ")
  return exp2


# Current state(x)
# Transition_fn(T)
# Final_states(f)
# input_word(word)
# Index_of_current_character(i)
def fn ( x , g , f , word, i): 
  if i>=len(word):
    if x in f :
      return 1
    else:
       return 0
  exp = rewrite(g[str(x)+word[i]] , i)
  # print("EVAL:", str(exp))
  return eval(str(exp))

# Input
n,t = map(int, input().split()) # No. of states(n) and No. of transitions(p)

s = int(input()) # The start state

f = list(map(int, input().split())) # The final states

g = defaultdict(list) # The set containing the transitions
for i in range(t):
  x,y,c = input().split() # Transition from state x to state y with character c
  g[x+c] = y
# print(g)

w = input() # The input word

if fn( s, g, f, w, 0) :
  print("Accepted")
else:
  print("Not Accepted")