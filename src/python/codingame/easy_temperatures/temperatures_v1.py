n = int(input())
# n = 5

if n > 0:
    # int_temperatures = [int(temp) for temp in input().split()] # can be replaced with input().split(), and convert the string values to int in the main loop in one pass
    temperatures = input().split()
    # temperatures = ['1', '-2', '-8', '4', '5']
    min_temperature = int(temperatures[0])

    for i in range(len(temperatures)):
        if i > 0:
            temperature = int(temperatures[i])
            if abs(temperature) <= abs(min_temperature):
                previous_min_temp = min_temperature
                if temperature < 0 and abs(min_temperature) == previous_min_temp:
                    min_temperature = previous_min_temp
                else:
                    min_temperature = temperature

    print(min_temperature)
else:
    print(0)

