from collections import deque

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
    
    start = (0, 0, 0)  # (x, y, orientation)
    end = (n - 1, m - 1, 0)
    
    q = deque([start])
    visited = {(0, 0, 0): 0}  # Inicializamos con el estado inicial
    
    while q:
        x, y, orientation = q.popleft()
        
        if (x, y, orientation) == end:
            return visited[(x, y, orientation)]
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if valid(new_x, new_y) and ((new_x, new_y, orientation) not in visited):
                visited[(new_x, new_y, orientation)] = visited[(x, y, orientation)] + 1
                q.append((new_x, new_y, orientation))
        
        if orientation == 0:  # Horizontal
            rotated = rotate(x, y, 1)
            if all(valid(rx, ry) for rx, ry in rotated) and valid(x + 1, y + 1) and ((x, y, 1 - orientation) not in visited):
                visited[(x, y, 1 - orientation)] = visited[(x, y, orientation)] + 1
                q.append((x, y, 1 - orientation))
        else:  # Vertical
            rotated = rotate(x, y, 0)
            if all(valid(rx, ry) for rx, ry in rotated) and valid(x + 1, y + 1) and ((x, y, 1 - orientation) not in visited):
                visited[(x, y, 1 - orientation)] = visited[(x, y, orientation)] + 1
                q.append((x, y, 1 - orientation))
    
    return -1

# Example labyrinth
labyrinth = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

result = solution(labyrinth)
print(result)  # Output: 2
