points = [(192,105), (17,56), (200,119), (1, 193), (42,99)]

prime = 223


for point in points :
    left_hand_side = ((point[1])**2)%prime 
    right_hand_side = ((point[0]**3)+7)%prime
    if left_hand_side == right_hand_side and left_hand_side >= 0 and left_hand_side <= prime-1 and right_hand_side >= 0 and right_hand_side <= prime-1:

        print("YES")
    else:
        print("NO")


