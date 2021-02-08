cc = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,
      "blue":6,"violet":7,"grey":8,"white":9}

def value(colors):
    v = ""
    for c in colors[0:2]:
        v += str(cc[c])
    return int(v)
