def volume(a,b,c):
  try:
    vol = int(a)*int(b)*int(c)
    if vol <= 0:
      return("bad inputs result was negative")
  except ValueError:
    return TypeError

  return vol