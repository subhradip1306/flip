import random as rn

def flip(x):
    if x==1:
        x=0

    elif x==0:
        x=1
    
    return(x)


grid=[0,0,0,0,0,0,0,0,0]

for j in range(9):
    grid[j]=rn.randint(0,1)

grid[rn.randint(0,8)]=0

print('Welcome to FLIP. \nThe grid you are shown below has 9 elements \nYou can choose an element to switch it from a 0 to 1 or from a 1 to 0 \n\nYour goal is to flip all of the elements to 1 \n\nThe catch is that any element you choose will also flip the values of the horizontally and vertically adjacent elements\n\n')
print('\nYou may press a numpad number key and hit enter for the corresponding element to be flipped')


while grid.count(1)<9:
    print('Current grid:\n', grid[6:9], '\n', grid[3:6], '\n', grid[0:3])
    
    
    x=(int(input())-1)
    

    grid[x]=flip(grid[x])
    
    
    
    try:
        if x>=3:
            grid[x-3]=flip(grid[x-3])
            
    except IndexError:
        continue
    
    
    if x%3==0:
        grid[x+1]=flip(grid[x+1])
        

    elif x%3==1:
        grid[x-1]=flip(grid[x-1])
        
        grid[x+1]=flip(grid[x+1])
        

    elif x%3==2:
        grid[x-1]=flip(grid[x-1])
        


    try:
        grid[x+3]=flip(grid[x+3])
        
    except IndexError:
        continue
    
    



print('\nCONGRATULATIONS!!! \nYou have completed the grid! \n', grid[6:9], '\n', grid[3:6], '\n', grid[0:3])

