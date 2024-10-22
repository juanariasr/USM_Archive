def ciudades(norte, sur, tam):
    dp = [[[]]*(tam+1) for _ in range(tam+1)]
    for i in range(tam+1):
        for j in range(tam+1):
            if i == 0 or j == 0:
                dp[i][j] = []
            elif norte[i-1] == sur[j-1]:
                dp[i][j] = dp[i-1][j-1] + [norte[i-1]]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    
    print(len(dp[tam][tam]))
    for i in dp[tam][tam]:
        print(i)
    return


norte = []
sur = []
f = open("input4.txt",'r') #poner el nombre del .txt que tiene los datos para el problema
cities = f.readlines()
tam = int(cities[0].strip())
for i in cities[1:tam+1]:
    norte.append(i.strip())

for i in cities[tam+1:]:
    sur.append(i.strip())

ciudades(norte,sur,tam)
f.close()