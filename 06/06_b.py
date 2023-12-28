time = 46807866
record_distance = 214117714021024

ways = 0

for i in range(1, time):
    print(i, i / time)
    speed = i
    time_remaining = time - i
    distance = time_remaining * speed
    if distance > record_distance:
        ways += 1

print(ways)