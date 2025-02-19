import math
from os import system
## recieve world coordinates
def motors(Px,Py):
    global current_angles
## calculate angle for each motor
    L2 = 120
    L3 = 100
    h1 = 120 # height up to link2 rotation
    h2 = 100 # from link5 rotation to gripper tip
    Ph = math.sqrt(Px**2+Py**2)
    
    dif = math.sqrt(L2**2-(h2+L3-h1)**2)

    if h1 == h2:
        te = 0
    else:
        te = math.atan(Ph/(h1-h2))
    Pr = math.sqrt((h1-h2)**2+Ph**2)

    if Px > 0 and Py > 0:   #quadrant 1
        t1 = math.atan(Py/Px)
    elif Px < 0 and Py > 0:   #quadrant 2
        t1 = math.pi+math.atan(Py/Px)
    elif Px > 0 and Py < 0:   #quadrant 4
        t1 = math.atan(Py/Px)
    elif Px < 0 and Py < 0:   #quadrant 3
        t1 = math.pi+math.atan(Py/Px)
    else:
        if Px == 0:
            if Py > 0:
                t1 = math.pi/2
            elif Py < 0:
                t1 = 3*math.pi/2
            else:
                return('invalid')
        elif Py == 0:
            if Px > 0:
                t1 = 0
            elif Px < 0:
                t1 = math.pi
            else:
                return('invalid')
        else:
            return('invalid')

    if math.sqrt(Px**2+Py**2) <= dif:
        return('invalid')
    else:
        None

    t2 = math.pi-math.acos((L2**2+Pr**2-L3**2)/(2*L2*Pr))-te

    t3 = math.pi-math.acos((L2**2-Pr**2+L3**2)/(2*L2*L3))

    t4 = math.pi-(t2+t3)

    angles = [t1, t2, t3, t4]

    angles_degrees = []

    for i in range(len(angles)):
        angles_degrees.append(math.degrees(angles[i]))

## determine angle change for each motor
    angles_change = list()
    for item1, item2 in zip(angles_degrees, current_angles):
        item = item1 - item2
        angles_change.append(item)
    angles_change_rd = [float(round(b/1.8)*1.8) for b in angles_change]
## calculate step size for each angle
    step_size = [int(x/1.8) for x in angles_change_rd]
    print(step_size)
## redefine variables
    for item1, item2, i in zip(current_angles, angles_change_rd, [0, 1, 2, 3]):
        item = item1 + item2
        current_angles[i]=item

## send step size to motors, return current angles
    for i in step_size:
        text = (f'mosquitto_pub -d -t {mcu_sub[i]} -m "{step_size[i]}"')
        system(text)

    return current_angles
