def wave(people):
    wave = []
    for i in range(len(people)):
        people[i] != ' ' and wave.append(
            people[:i] + people[i].upper() + people[i+1:])
    return wave


print(wave('codewars'))
print(wave(' gap '))
