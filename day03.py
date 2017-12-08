inp = 325489
current_x = 0
current_y = 0
grid_x_lower = 0
grid_x_higher = 0
grid_y_lower = 0
grid_y_higher = 0
direction = 0 # 0 - left, 1 - up, 2 - right, 3 - down
for i in range(2, inp + 1):
    direction_mod = direction % 4
    if direction_mod == 0:
        current_x += 1
        if current_x > grid_x_higher:
            grid_x_higher = current_x
            direction += 1
    elif direction_mod == 1:
        current_y += 1
        if current_y > grid_y_higher:
            grid_y_higher = current_y
            direction += 1
    elif direction_mod == 2:
        current_x += -1
        if current_x < grid_x_lower:
            grid_x_lower = current_x
            direction += 1
    elif direction_mod == 3:
        current_y += -1
        if current_y < grid_y_lower:
            grid_y_lower = current_y
            direction += 1
print(abs(current_x) + abs(current_y))
