for n in range(1,100):
    s = str(n)
    c = s.count('3') + s.count('6') + s.count('9')
    if c < 1:
        continue

    print('{0} {1}'.format(s, '짝' * c))