n = int(input())

if n:
    temperatures = sorted([int(temp) for temp in input().split()], key=lambda x: abs(x))
    try:
        if temperatures[0] < 0 and temperatures.index(abs(temperatures[0])):
            temperatures[0] = abs(temperatures[0])
    except ValueError:
        pass
    print(temperatures[0])
else:
    print(0)