__author__ = 'brammoha'
import random

#credit: Ned Batchelder
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w > r:
         return c
      upto += w
   assert False, "Shouldn't get here"


def getseq(length, choices):
    outstring = ""
    for i in range(length):
        outstring += weighted_choice(choices)
    return outstring

sample_size = 1000
prob_dict = {}
prob_dict['total'] = 0
choice_map = [('a', 0.1), ('b', 0.5), ('c', 0.15), ('d', 0.25)]
for sample in range(sample_size):
    str = getseq(5, choice_map)
    print(str)
    for char in str:
        try:
            prob_dict[char] += 1
        except KeyError:
            prob_dict[char] = 0
        prob_dict['total']+=1

print("\nSample Probabilities")
for key in prob_dict:
    print("Char : %s , Prob: %f" % (key, prob_dict[key]/prob_dict['total']) )

