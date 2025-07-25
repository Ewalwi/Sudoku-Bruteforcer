from show import show_board

table = [[0 for _ in range(9)] for _ in range(9)]

def setup(grid):
    show_board(grid)
    
    for line in range(9):
        for col in range(9):
            while True:
                show_board(grid, line, col)
                
                try:
                    print(f"\n📍 Case [{line+1}, {col+1}]")
                    saisie = input("Valeur (1-9 ou 0/Entrée pour vide): ").strip()
                    
                    if saisie == "":
                        valeur = 0
                    else:
                        valeur = int(saisie)
                    
                    if 0 <= valeur <= 9:
                        grid[line][col] = valeur
                        break
                    else:
                        print("❌ Veuillez entrer un nombre entre 0 et 9")
                        input("appuyer sur entrée pour continuer...")
                        
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide")
                    input("Appuyez sur entrée pour continuer...")
    
    show_board(grid)
    
    return grid

def isValid(table, line, num, num_pos):
    for n in table[line]:
        if num == n:
            return False

    for i in range(9):
        if table[i][num_pos] == num:
            return False

    start_line = (line // 3) * 3
    start_col = (num_pos // 3) * 3
    for i in range(start_line, start_line + 3):
        for j in range(start_col, start_col + 3):
            if table[i][j] == num:
                return False
            
    return True

def resolve(table, speed = True):
    for x, line in enumerate(table):
        for y, _ in enumerate(line):
            if table[x][y] == 0:
                for i in range(1, 10):
                    if isValid(table, x, i, y):
                        table[x][y] = i
                        if not speed:
                            show_board(table)
                        if resolve(table):
                            return True
                        table[x][y] = 0
                        if not speed:
                            show_board(table)
                return False
    return True


setup(table)

speed = input("Speed Mode ? [y/n] (default enabled)")

if resolve(table, True if speed == "y" else False):
    show_board(table)
    print("Resolved")
    input("")
else:
    print("Couldn't find solution")
    input("")