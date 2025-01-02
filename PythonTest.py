dashboard_left = bool(int(input("Dashboard_Left Enter 1 for Open and 0 for Closed: ")))
dashboard_right = bool(int(input("Dashboard_Right Enter 1 for Open and 0 for Closed: ")))
child_lock = bool(int(input("Child_Lock Enter 1 for Open and 0 for Closed: ")))
master_lock = bool(int(input("Master_Lock Enter 1 for Open and 0 for Closed: ")))
inside_left = bool(int(input("Inside_Left Enter 1 for Open and 0 for Closed: ")))
inside_right = bool(int(input("Inside_Right Enter 1 for Open and 0 for Closed: ")))
outside_left = bool(int(input("Outside_Left Enter 1 for Open and 0 for Closed: ")))
outside_right = bool(int(input("Outside_Right Enter 1 for Open and 0 for Closed: ")))
gear_shift = input("Set one gear (P, N ,D ,1 ,2 ,3, R): ")

left_door_opens= False
right_door_opens = False

if gear_shift == "P" and master_lock :
    if dashboard_left or not child_lock and inside_left  or outside_left :
        left_door_opens = True
    elif dashboard_right  or not child_lock and inside_right  or outside_right :
        right_door_opens = True

if left_door_opens and right_door_opens:
    print("Both Doors Open")
elif left_door_opens:
    print("Left Door Opens")
elif right_door_opens:
    print("Right Door Opens")
else:
    print("Both Doors Stay Closed")
