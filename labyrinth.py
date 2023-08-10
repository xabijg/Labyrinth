def solution(labyrinth):
    n = len(labyrinth)  # Filas
    m = len(labyrinth[0])  # Columnas
    
    def valid(x, y):
        return 0 <= x < n and 0 <= y < m and labyrinth[x][y] != '#'
    
    def rotate(x, y, orientation):
        if orientation == 0:  # Horizontal
            return [(x, y), (x, y + 1), (x, y + 2)]
        else:  # Vertical
            return [(x, y), (x + 1, y), (x + 2, y)]
    
    start = (0, 1, 0)  # (x, y, orientation)
    end = (n - 1, m - 1, 0)
    
    q = [start]
    visited = {(0, 1, 0): (0, None)}  # Inicializamos con el estado inicial y padre
    
    while q:
        x, y, orientation = q.pop(0)
        
        if (x, y, orientation) == end:
            path = []
            while (x, y, orientation) != (0, 1, 0):
                path.append((x, y))
                x, y, orientation = visited[(x, y, orientation)][1]
            path.append((0, 1))
            return list(reversed(path)), len(path) - 2  # Restamos 2 para omitir el primer y último movimiento
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if valid(new_x, new_y) and ((new_x, new_y, orientation) not in visited):
                visited[(new_x, new_y, orientation)] = ((x, y, orientation), (x, y, orientation))
                q.append((new_x, new_y, orientation))
        
        if orientation == 0:  # Horizontal
            rotated = rotate(x, y, 1)  # Rotate to vertical
            if all(valid(rx, ry) for rx, ry in rotated):
                valid_rotation = True
                for rx, ry in rotated:
                    if any(labyrinth[rx + dx][ry + dy] == '#' for dx in range(-1, 2) for dy in range(-1, 2) if valid(rx + dx, ry + dy)):
                        valid_rotation = False
                        break
                if valid_rotation and all(labyrinth[x + dx][y + dy] != '#' for dx in range(2) for dy in range(-1, 2) if valid(x + dx, y + dy)):
                    if (x + 1, y, 1 - orientation) not in visited:
                        visited[(x + 1, y, 1 - orientation)] = ((x, y, orientation), (x, y, orientation))
                        q.append((x + 1, y, 1 - orientation))
        else:  # Vertical
            rotated = rotate(x, y, 0)  # Rotate to horizontal
            if all(valid(rx, ry) for rx, ry in rotated):
                valid_rotation = True
                for rx, ry in rotated:
                    if any(labyrinth[rx + dx][ry + dy] == '#' for dx in range(-1, 2) for dy in range(-1, 2) if valid(rx + dx, ry + dy)):
                        valid_rotation = False
                        break
                if valid_rotation and all(labyrinth[x + dx][y + dy] != '#' for dx in range(-1, 2) for dy in range(2) if valid(x + dx, y + dy)):
                    if (x, y + 1, 1 - orientation) not in visited:
                        visited[(x, y + 1, 1 - orientation)] = ((x, y, orientation), (x, y, orientation))
                        q.append((x, y + 1, 1 - orientation))
    
    return [], -1
