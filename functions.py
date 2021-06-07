
def PrintArray(list):
    for i in range(len(list)):
        print(f'\n{i + 1}° ', end='')
        for j in range(len(list[i])):
            if j == 0:
                print(list[i][j], end='')
            elif j == 1:
                print(' Album:',list[i][j], end='')
            else:
                print(' Ano:',list[i][j], end='')

