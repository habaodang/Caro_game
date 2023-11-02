#input size table user
def input_size_table():
    while(1):
        try:
            size_t=int(input('Enter size table( size > 4): '))
            if size_t>= 5:
                break
        except:
            print('Error data type !!!')
    return size_t

#initi list 2D with value = -1
def set_table(size_t):
    table = [[-1] * size_t for _ in range(size_t)]
    return table

#
def show_table(table):
    print('\t',end='')
    for i in range (0,len(table[0])):
        print (i,end =' ')
    print()
    idx_col=0
    for row in table:
        print (idx_col,end='\t')
        for value in row:
            if value==-1:
                print ('*',end=' ')
            elif value==0:
                print ('O',end=' ')
            else:
                print ('X',end=' ')
        idx_col+=1
        print()

#check point win
def pointWin(count, point_win):
    if count==point_win:
        return True
    else:
        return False
    
def left_right(table, x, y):
    count=0
    for i in range(0,4):
        if y+i+1<len(table[x]):
            if table[x][y]==table[x][i+y+1]:
                count+=1
            else: 
                break
            if pointWin(count,4):
                return True
        else:
            break
    for i in range(0,4):
        if y-i-1>0:
            if table[x][y]==table[x][y-i-1]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break
    return pointWin(count,4)
       
        
def top_bottom(table, x, y):
    count=0
    for i in range(0,4):
        if x+i+1<len(table[x]):
            if table[x][y]==table[x+i+1][y]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break
    for i in range(0,4):
        if x-i-1>0:
            if table[x][y]==table[x-i-1][y]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break

    return pointWin(count,4)   
    
def topLeft_bottomRight(table,x,y):
    count=0
    for i in range(0,4):
        if x+i+1<len(table[x]) and y+i+1<len(table[x]):
            if table[x][y]==table[x+i+1][y+i+1]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break
    for i in range(0,4):
        if x-i-1>0 and y-i-1>0:
            if table[x][y]==table[x-i-1][y-i-1]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break

    return pointWin(count,4)   
    
def bottomLeft_topRight(table,x,y):
    count=0
    for i in range(0,4):
        if x-i-1<len(table[x]) and y+i+1<len(table[x]):
            if table[x][y]==table[x-i-1][y+i+1]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break
    for i in range(0,4):
        if x+i+1<len(table[x]) and y-i-1>0:
            if table[x][y]==table[x+i+1][y-i-1]:
                count+=1
            else:
                break
            if pointWin(count,4):
                return True
        else:
            break

    return pointWin(count,4)   


def check_win(table, x, y):
    if(left_right(table, x, y) or top_bottom(table,x,y) or topLeft_bottomRight(table,x,y) or bottomLeft_topRight(table,x,y)):
        print("You are win!")
        return True
    else:
        return False

def input_user(table):
    x_o=0
    while(1):
        pos_x=int(input('Enter position x: '))
        pos_y=int(input('Enter position y: '))
        table[pos_x][pos_y]=x_o
        if (x_o==0): 
            x_o=1
        else:
            x_o=0
        show_table(table)
        if(check_win(table,pos_x,pos_y)):
            break
          

table=set_table(10)
input_user(table)

