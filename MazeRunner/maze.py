size=raw_input("Enter maze size like 6x6,3x3: ")
grid=[]
size=int(size[0])

finishSign=0

def make_grid(size):
	global grid
	for i in range(size):
		grid.append([])
		for j in range(size):
			grid[i].append(" ")


make_grid(size)

points=raw_input("Enter a beginning point and an ending point respectively in range of 1 to "+str(size*size)+": ")
points=points.split(" ")
beg=int(points[0])
fin=int(points[1])

if beg%size==0:
	beg_line=beg/size-1
	beg_row=beg%size-1
elif beg%size!=0:
	beg_line=beg/size
	beg_row=beg%size-1
grid[beg_line][beg_row]="B"
if fin%size==0:
	end_line=fin/size-1
	end_row=fin%size-1
elif fin%size!=0:
	end_line=fin/size
	end_row=fin%size-1
grid[end_line][end_row]="F"

obstacles=raw_input("Enter where will be "+str(size)+" obstacles(Give index number for every obstacle): ")
obstacles=obstacles.split(" ")

for i in range(size):
	if int(obstacles[i])%size==0:
		obstacle_line=int(obstacles[i])/size-1
		obstacle_row=int(obstacles[i])%size-1
	else:
		obstacle_line=int(obstacles[i])/size
		obstacle_row=int(obstacles[i])%size-1
	grid[obstacle_line][obstacle_row]="O"


def maze_runner(line,row):
	global grid
	if grid[line][row]=="F":
		finishSign=1
		print "Maze solved"
		grid[beg_line][beg_row]="B"
		for line in grid:
			print line
		return True
	elif grid[line][row]=="O":
		return False
	elif grid[line][row]=="X":
		return False
	grid[line][row]="X"
	if (-1<line<size-1 and -1<row<size and maze_runner(line+1,row)) or (-1<line<size and -1<row<size-1 and maze_runner(line,row+1)) or (0<line<size and -1<row<size and maze_runner(line-1,row)) or (-1<line<size and 0<row<size and maze_runner(line,row-1)):
		return True
	elif not (-1<line<size-1 and -1<row<size and maze_runner(line+1,row)) or (-1<line<size and -1<row<size-1 and maze_runner(line,row+1)) or (0<line<size and -1<row<size and maze_runner(line-1,row)) or (-1<line<size and 0<row<size and maze_runner(line,row-1)):
		grid[line][row]=" "
		return False
maze_runner(beg_line,beg_row)

if finishSign!=1:
	print "Maze cannot be solved"
	exit()

executed={}
counter2=1
for line in grid:
	for row in line:
		executed.setdefault(counter2,grid[grid.index(line)][line.index(row)])
		counter2+=1

beginning=beg_line*size+beg_row+1
path=[beginning]

while True:
	if beginning+1 in executed.keys():
		if (beginning+1)%size==1 or beginning+1 in path:
			pass
		elif executed[beginning+1]=="X":
			path.append(beginning+1)
			beginning+=1
			continue
		elif executed[beginning+1]=="F":
			path.append(beginning+1)
			break
		pass
	if beginning-1 in executed.keys():
		if (beginning-1)%size==0 or beginning-1 in path:
			pass
		elif executed[beginning-1]=="X":
			path.append(beginning-1)
			beginning-=1
			continue
		elif executed[beginning-1]=="F":
			path.append(beginning-1)
			break
		pass
	if beginning+size in executed.keys():
		if beginning+size in path:
			pass
		elif executed[beginning+size]=="X":
			path.append(beginning+size)
			beginning+=size
			continue
		elif executed[beginning+size]=="F":
			path.append(beginning+size)
			break
		pass
	if beginning-size in executed.keys():
		if beginning-size in path:
			pass
		elif executed[beginning-size]=="X":
			path.append(beginning-size)
			beginning-=size
			continue
		elif executed[beginning-size]=="F":
			path.append(beginning-size)
			break
		pass

for item in range(len(path)):
	path[item]=str(path[item])
	
print "Path from the beginning to finish is goes from theese cells: " + " ".join(path)
