import random 
import time

matriz = [[0 for x in range(10)] for y in range(10)]

person_pos = [4, 4]

matriz[person_pos[0]][person_pos[1]] = 1

while True:
    for item in matriz: print(item, flush=True)

    flag = random.random()
    matriz[person_pos[0]][person_pos[1]] = 0
    
    if flag <= 0.25:
        if not person_pos[0] == 9:
            person_pos[0] += 1

    if 0.25 < flag <= 0.5:
        if not person_pos[1] == 9:
            person_pos[1] += 1

    if 0.5 < flag <= 0.75:
        if not person_pos[0] == 0:
            person_pos[0] -= 1
    
    if flag > 0.75:
        if not person_pos[1] == 0:
            person_pos[1] -= 1

    matriz[person_pos[0]][person_pos[1]] = 1

    time.sleep(0.5)
    
