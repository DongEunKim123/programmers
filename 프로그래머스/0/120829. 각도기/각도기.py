def solution(angle):
    if 90>angle and angle>0:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 180 > angle > 90:
        answer = 3
    else:
        answer = 4
    return answer