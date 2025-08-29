import sys
from collections import defaultdict
sys.stdin = open('NFAinput.txt', 'r')


# Current state(x)
# Transition_fn(T)
# Final_states(f)
# input_word(word)
# Index_of_current_character(i)
def fn ( x , T , f , word, i): 
  if i>=len(word):
    if x in f :
      return 1
    else:
      return 0
  if len(T[str(x)+str(word[i])])==0:
    return 0
  flag=0
  for j in range(len(T[str(x)+str(word[i])])):
    a = fn ( T[str(x)+str(word[i])][j], T, f, word, i+1 )
    if a==1:
      flag=1
      break
  if flag==1:
    return 1
  else:
    return 0

# Input
n,t = map(int, input().split()) # No. of states(n) and No. of transitions(p)

s = int(input()) # The start state

f = list(map(int, input().split())) # The final states

T = defaultdict(list) # The set containing the transitions
for i in range(t):
  x,y,c = input().split() # Transition from state x to state y with character c
  T[x+c].append(int(y))
# print(T)

w = input() # The input word

if w=='-': # The empty word
  if s in f :
    print("Accepted")
  else:
    print("Not Accepted")
else:
  if fn( s, T, f, w, 0) :
    print("Accepted")
  else:
    print("Not Accepted")