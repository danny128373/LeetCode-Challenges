def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    starting = []
    ending = []
    for i in paths:
        for j, city in enumerate(i):
            if j == 0:
                starting.append(city)
            elif j == 1:
                ending.append(city)
    for k in ending:
        if k in starting:
            continue
        else:
            return k


print(destCity([["London", "New York"], [
      "New York", "Lima"], ["Lima", "Sao Paulo"]]))
