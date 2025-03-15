def distances(prison):
    res = [ [0 for w in range(len(prison[0]))] for h in range(len(prison)) ]

    for i in range(len(prison)):
        for j in range(len(prison[i])):
            if prison[i][j] == -1 or prison[i][j] == -2:
                res[i][j] = prison[i][j]
                continue
            
            res[i][j] = bfs(prison, i, j)
    return res

def bfs(prison, i, j, cache = None):
    if cache is None:
        cache = set()
    
    # row, colum and depth i,j,d
    queue = [(i, j, 0)]
    while queue:
        i, j, d = queue.pop(0)
        
        # cell already visited?
        if (i, j) in cache:
            continue
        
        # Termination condition, target reached
        if prison[i][j] == -2:
            return d

        cache.add((i,j))
        
        # Check before move right
        if 0 <= i < len(prison) and 0 <= j + 1 < len(prison[i]) and prison[i][j + 1] != -1:
            queue.append((i, j + 1, d + 1))
        
        # Check before move down
        if 0 <= i + 1 < len(prison) and 0 <= j < len(prison[i]) and prison[i + 1][j] != -1:
            queue.append((i + 1, j, d + 1))

        # Check before move left
        if 0 <= i < len(prison) and 0 <= j - 1 < len(prison[i]) and prison[i][j - 1] != -1:
            queue.append((i, j - 1, d + 1))
        
        # Check before move up
        if 0 <= i - 1 < len(prison) and 0 <= j < len(prison[i]) and prison[i - 1][j] != -1:
            queue.append((i - 1, j, d + 1))


def bfs_path(prison, i, j, cache = None):
    if cache is None:
        cache = set()
    
    queue = [(i, j, 0)]
    path = [[]]
    while queue:
        i, j, d = queue.pop(0)
        
        if (i, j) in cache:
            continue

        path = list(map(lambda x: [*x, (i ,j, d)], path))
        
        if prison[i][j] == -2:
            break

        cache.add((i,j))
        
        if 0 <= i < len(prison) and 0 <= j + 1 < len(prison[i]) and prison[i][j + 1] != -1:
            queue.append((i, j + 1, d + 1))
        
        if 0 <= i + 1 < len(prison) and 0 <= j < len(prison[i]) and prison[i + 1][j] != -1:
            queue.append((i + 1, j, d + 1))

        if 0 <= i < len(prison) and 0 <= j - 1 < len(prison[i]) and prison[i][j - 1] != -1:
            queue.append((i, j - 1, d + 1))
        
        if 0 <= i - 1 < len(prison) and 0 <= j < len(prison[i]) and prison[i - 1][j] != -1:
            queue.append((i - 1, j, d + 1))

    return path

if __name__ == "__main__":
    prison1 = [
        [0, -1, -2],
        [0, 0, 0],
    ]

    prison2 = [
        [0, 0, 0, -1, -2],
        [0, 0, 0,  0,  0],
        [-2, 0, 0,  0,  0],
    ]

    print(distances(prison1))
    print(distances(prison2))