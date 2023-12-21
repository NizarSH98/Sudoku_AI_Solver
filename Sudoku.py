import random
# import pygame library
import pygame

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((500, 500))

# Title and Icon 
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('C:\\Users\\1\\Downloads\\sudoku-game-python\\SUDOKU GAME\\icon.png')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.


def is_valid(board, row, col, num):
    # Check if 'num' is not present in the current row, column, and the 3x3 grid
    return all(num != board[row][i] for i in range(9)) and \
           all(num != board[i][col] for i in range(9)) and \
           all(num != board[row // 3 * 3 + i][col // 3 * 3 + j] for i in range(3) for j in range(3))

def fill_board(board):
    # Iterate through each cell in the board and fill in a valid number
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):  # Recursively fill the next cell
                            return True
                        board[row][col] = 0  # Backtrack if the current configuration is invalid
                return False  # No valid number found for the current cell
    return True  # The entire board has been filled

def generate_sudoku():
    # Initialize an empty 9x9 grid
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill in the initial values to generate a valid Sudoku grid
    fill_board(board)

    # Remove some numbers to create the puzzle
    for _ in range(40):
        i, j = random.randint(0, 8), random.randint(0, 8)
        while board[i][j] == 0:
            i, j = random.randint(0, 8), random.randint(0, 8)
        board[i][j] = 0

    return board
	
grid = generate_sudoku()

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

# Highlight the cell selected
def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
		pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 


# Function to draw required lines for making Sudoku grid		 
def draw():
	# Draw the lines
		
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:

				# Fill blue color in already numbered grid
				pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

				# Fill grid with default numbers specified
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 15, j * dif + 15))
	# Draw lines horizontally and verticallyto form grid		 
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	 

# Fill value entered in cell	 
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    # Calculate the center of the cell
    cell_center_x = x * dif + dif // 2
    cell_center_y = y * dif + dif // 2
    # Calculate the position to center the text in the cell
    text_x = cell_center_x - text1.get_width() // 2
    text_y = cell_center_y - text1.get_height() // 2
    screen.blit(text1, (text_x, text_y )) 

# Raise error when wrong value entered
def raise_error1():
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 

# Check if the value entered in board is valid
def valid(m, i, j, val):
	for it in range(9):
		if m[i][it]== val:
			return False
		if m[it][j]== val:
			return False
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3):
		for j in range (jt * 3, jt * 3 + 3):
			if m[i][j]== val:
				return False
	return True

# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump() 
	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			# white color background\
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background\
			screen.fill((255, 255, 255))
		
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(50) 
	return False

# Display instruction for the game
def instruction():
	text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
	text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
	screen.blit(text1, (20, 520))	 
	screen.blit(text2, (20, 540))

# Display options when solved
def result():
	text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

def handle_key_event(event):
    global val, flag2, rs, error

    if event.key == pygame.K_LEFT:
        x -= 1
        flag1 = 1
    elif event.key == pygame.K_RIGHT:
        x += 1
        flag1 = 1
    elif event.key == pygame.K_UP:
        y -= 1
        flag1 = 1
    elif event.key == pygame.K_DOWN:
        y += 1
        flag1 = 1
    elif pygame.K_1 <= event.key <= pygame.K_9:
        val = event.key - pygame.K_0  # Convert key to integer value
    elif event.key == pygame.K_RETURN:
        flag2 = 1
    elif event.key == pygame.K_r:
        rs = 0
        error = 0
        flag2 = 0
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0]
			]
        
    elif event.key == pygame.K_d:
        rs = 0
        error = 0
        flag2 = 0
        grid = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
			[6, 0, 0, 0, 7, 5, 0, 0, 9],
			[0, 0, 0, 6, 0, 1, 0, 7, 8],
			[0, 0, 7, 0, 4, 0, 2, 6, 0],
			[0, 0, 1, 0, 5, 0, 9, 3, 0],
			[9, 0, 4, 0, 6, 0, 0, 0, 5],
			[0, 7, 0, 3, 0, 0, 0, 1, 2],
			[1, 2, 0, 0, 0, 7, 4, 0, 0],
			[0, 4, 9, 2, 0, 6, 0, 0, 7]
        	]
# The loop thats keep the window running
while run:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        elif event.type == pygame.KEYDOWN:
            handle_key_event(event)
            
    if flag2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:         
        draw_val(val)
        # print(x)
        # print(y)
        if valid(grid, int(x), int(y), val) == True:
            grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error2() 
        val = 0
    
    if error == 1:
        raise_error1() 
    if rs == 1:
        result()     
    draw() 
    if flag1 == 1:
        draw_box()   
    instruction() 

    # Update window
    pygame.display.update()

# Quit pygame window 
pygame.quit()	 
	
