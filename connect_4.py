def connect_4(a_game):
    #horizontal
    for i in range(5):
      #  print(i)
        count = 1
        for j in range(6):
         #   print(j)
            var = a_game[i][j]
         #   print(var)
            if j < 5 and a_game[i][j]==a_game[i][j+1] and not a_game[i][j] is None:
                count += 1
                if count >= 4:
                    return var
            else:
                count = 1

    #vertical
    for i in range(6):
        count = 1
        for j in range(5):
            var = a_game[j][i]
            if j < 4 and a_game[j][i]==a_game[j+1][i] and not a_game[j][i] is None:
                count += 1
                if count >= 4:
                    return var
            else:
                count = 1

    #diagonal left to right

    for x in range(4):
        i = 0
        j = x
        count = 1
        while i<=4 and j<=5:
            if i+1 <=5 and j <= 6 and j+1<=6:
                var = a_game[i][j]
                if var == a_game[i+1][j+1] and var is not None:
                    count += 1
                    if count >= 4:
                        return var
                else:
                    count = 1
            i += 1
            j += 1

    for x in range(1,3):
        i = x
        j = 0
        count = 1
        while i<=4 and j<=5:
            if i+1 <=5 and j <= 6 and j+1<=6:
                var = a_game[i][j]
                if var == a_game[i+1][j+1] and var is not None:
                    count += 1
                    if count >= 4:
                        return var
                else:
                    count = 1
            i += 1
            j += 1

    #diagonal right to left
    for x in range(4):
        i = 0
        j = 6-x
        count = 1
        while i<=4 and j>=0:
            if i+1 <=5 and j >=0 and j-1>=0:
                var = a_game[i][j]
                if var == a_game[i+1][j-1] and var is not None:
                    count += 1
                    if count >= 4:
                        return var
                else:
                    count = 1
            i += 1
            j -= 1

    for x in range(1,3):
        i = x
        j = 6
        count = 1
        while i<=4 and j>=0:
            if i+1 <=5 and j >=0 and j-1>=0:
                var = a_game[i][j]
                if var == a_game[i+1][j-1] and var is not None:
                    count += 1
                    if count >= 4:
                        return var
                else:
                    count = 1
            i += 1
            j -= 1
