import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

lines = loadStrings("highscore.txt")
highscore = int(lines[0])
score = 0

def log2(x):
    return (log(x)/log(2))

def drawGrid(grid):
    background(255)
    global score
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score += grid[i][j]
            if grid[j][i] == 0:
                fill(255)
                rect(i*150, j*150, 150, 150, 7)
            else:
                yellow = 255 - map(log2(grid[j][i]),0,15,0,255)
                fill(255,yellow,0)
                rect(i*150, j*150, 150, 150, 7)
                textSize(32)
                textAlign(CENTER)
                fill(0)
                text("%s"%grid[j][i], 75 + i*150, 90 + j*150)
    textSize(20)
    textAlign(CENTER)
    fill(200,0,0)
    text("Score => %d,  High Score => %s"%(score, highscore), 300,640)

def setup():
    size(600,650)
    background(255)
    strokeWeight(3)
    drawGrid(grid)
    noLoop()
    
def moveAllUp(grid):
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            shiftcount = 0
            for shift in range(1,i+1):
                if grid[i-shift][j] == 0:
                    shiftcount += 1
                else:
                    if grid[i-shift][j] == grid[i][j]:
                        shiftcount += 1
                        break
                    else:
                        break
            if shiftcount > 0:
                grid[i-shiftcount][j] += grid[i][j]
                grid[i][j] = 0

def moveAllRight(grid):
    for i in range(len(grid)):
        for j in range(2,-1,-1):
            shiftcount = 0
            for shift in range(j+1,4):
                if grid[i][shift] == 0:
                    shiftcount += 1
                else:
                    if grid[i][shift] == grid[i][j]:
                        shiftcount += 1
                        break
                    else:
                        break
            if shiftcount > 0:
                grid[i][j + shiftcount] += grid[i][j]
                grid[i][j] = 0

def moveAllLeft(grid):
    for i in range(len(grid)):
        for j in range(1,4):
            shiftcount = 0
            for shift in range(1,j+1):
                if grid[i][j-shift] == 0:
                    shiftcount += 1
                else:
                    if grid[i][j-shift] == grid[i][j]:
                        shiftcount += 1
                        break
                    else:
                        break
            if shiftcount > 0:
                grid[i][j-shiftcount] += grid[i][j]
                grid[i][j] = 0

def moveAllDown(grid):
    for i in range(2,-1,-1):
        for j in range(4):
            shiftcount = 0
            for shift in range(i+1,4):
                if grid[shift][j] == 0:
                    shiftcount += 1
                else:
                    if grid[shift][j] == grid[i][j]:
                        shiftcount += 1
                        break
                    else:
                        break
            if shiftcount > 0:
                grid[i+shiftcount][j] += grid[i][j]
                grid[i][j] = 0
    

def generate_new(grid):
    global score, highscore
    empties = []
    win = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                empties.append([i,j])
            if grid[i][j] == 2048:
                win = True
    if len(empties) == 0:
        textSize(40)
        textAlign(CENTER)
        if highscore < score:
            fill(0,255,0)
            text("HIGH SCORE!!\nR to restart", 300,300)
            scoretoSave = [str(score)]
            saveStrings("highscore.txt", scoretoSave)
            highscore = score
            score = 0
        else:
            fill(255,0,0)
            text("GAME OVER\nR to restart", 300,300)
            score = 0
        
        return -1
    if win:
        drawGrid(grid)
        textSize(40)
        textAlign(CENTER)
        fill(0,255,0)
        text("SUCCESS", 300,300)
        return -1
    pos = int(random(len(empties)))
    nums = [2,4]
    choice = nums[int(random(2))]
    grid[empties[pos][0]][empties[pos][1]] = choice
    return grid

def draw():
    global grid
    if grid == -1:
        pass
    else:
        grid = generate_new(grid)
        if grid == -1:
            pass
        else:
            drawGrid(grid)

def keyPressed():
    global grid
    if grid != -1:
        if keyCode == UP:
            moveAllUp(grid)
            redraw()
        if keyCode == RIGHT:
            moveAllRight(grid)
            redraw()
        if keyCode == LEFT:
            moveAllLeft(grid)
            redraw()
        if keyCode == DOWN:
            moveAllDown(grid)
            redraw()
    else:
        if keyCode==82:
            grid = [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
            redraw()