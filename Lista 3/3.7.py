def torreDeHanoi(n, origem, destino, torre_aux1,torre_aux2):

    if (n == 0):
        return
    if (n == 1):
        print("Mover disco", n, "da torre", origem, "até a torre", destino)
        return

    torreDeHanoi(n-2, origem, torre_aux1,torre_aux2, destino)
    print("Mover disco", n-1, "da torre", origem,"até a torre", torre_aux2)

    print("Mover disco", n, "da torre", origem,"até a torre", destino)

    print("Mover disco", n-1, "da torre", torre_aux2,"até a torre", destino)
    torreDeHanoi(n-2, torre_aux1, destino,origem, torre_aux2)


n = 5
torreDeHanoi(n, 'A', 'D', 'B', 'C')