def fullname(a,b):
  try:

    a = a + " " + b
  except TypeError:
    return ("bad input")
  return a
