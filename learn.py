def solve_psne(p1_matrix, p2_matrix):

    best_row = [0] * 2
    best_col = [0] * 2

    for j in range(2):

        if p1_matrix[0][j] >= p1_matrix[1][j]:
            best_row[j] = 0
        else:
            best_row[j] = 1

    
    for i in range(2):

        if p2_matrix[i][0] >= p2_matrix[i][1]:
            best_col[i] = 0
        else:
            best_col[i] = 1

    found = False

  
    for i in range(2):
        for j in range(2):

            if best_row[j] == i and best_col[i] == j:

                print(f"PSNE at: ({i},{j})")
                found = True

    if not found:
        print("No PSNE found.")


p1_matrix = []
p2_matrix = []

for _ in range(2):
    p1_matrix.append(list(map(int, input().split())))

for _ in range(2):
    p2_matrix.append(list(map(int, input().split())))

solve_psne(p1_matrix, p2_matrix)