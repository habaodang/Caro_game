def input_size_table():
    while(1):
        try:
            size_t=int(input('Enter size table( size > 4): '))
            if size_t>= 5:
                break
        except:
            print('Error data type !!!')
    return size_t

def set_table(size_t):
    table = [[-1]*size_t]*size_t
    return table
def show_table(table):
    for i in range(0,len(table)):
        for j in range (0,len(table[0])):
            if table[i][j]==-1:
                print ('*',end='')
            elif table[i][j]==0:
                print ('O',end='')
            else:
                print ('X',end='')
        print()

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
        break_f=input('thoat')
        if (break_f=='0'):
            break
    show_table(table)

table=set_table(9)
input_user(table)

