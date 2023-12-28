races = [(46, 214),(80, 1177), (78, 1402),(66, 1024)]

result = 1
for time, record_distance in races:
    ways = 0
    for i in range(1, time):
        speed = i
        time_remaining = time - i
        distance = time_remaining * speed
        if distance > record_distance:
            ways += 1

    result *= ways
print(result)




