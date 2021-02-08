from statistics import*
def average(a):
  try:
    if len(a) == 0:
      return ("no inputs")
    x = mean(a)
  except TypeError:
      return TypeError
  return x
