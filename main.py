###################################################################
import random
import emoji
###################################################################

## Me hubiese gustado utilizar la libreria emoji, pero muchos de ellos salen feos con iconos extra, asi que he seleccionado algunos emojis mas sencillos

emojis = [
    
    "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😎", "😍",
    "😘", "😗", "😙", "😚", "🤗", "🤔", "😐", "😑", "😶", "😏", "🙄", "😮", "😯",
    "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤧", "🥳", "🤠", "🥸", "😇",
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁", "🐮", "🐷",
    "🐸", "🐵", "🙈", "🙉", "🙊", "🐒", "🐧", "🐦", "🐤", "🐥", "🐺", "🐗", "🐴",
    "🦄", "🐝", "🐞", "🦋", "🐌", "🐛", "🐜", "🦟", "🦆", "🐢", "🐍", "🦖", "🦕",
    "🍎", "🍊", "🍌", "🍉", "🍇", "🍓", "🍒", "🍍", "🥥", "🥝", "🍅", "🥑",
    "🍞", "🥖", "🧀", "🍖", "🍗", "🍔", "🍟", "🍕", "🌭", "🥪", "🌮", "🌯",
    "🍿", "🥤", "🍩", "🍪", "🍰", "🎂", "🧁", "🍫", "🍬", "🍭", "☕", "🍵",
    "🎒", "🧸", "🎈", "🎉", "🎊", "🎁", "🏆", "📱", "💻", "📷", "🎥", "🎮",
    "🎸", "🎻", "🥁", "🎺", "🎷", "📚", "📒", "🖋", "🖊", "✂️", "🖍", "🖌",
    "💡", "🔦", "🕯", "📡", "💵", "💴", "💶", "💷", "💰", "💳", "💎", "🔔",
    "🚗", "🚕", "🚙", "🚌", "🚎", "🏎", "🚓", "🚑", "🚒", "🚐", "🚚", "🚜",
    "🚲", "🛴", "🛵", "🏍", "🚤", "🛥", "🛳", "✈️", "🚁", "🛸", "🚀", "🛶",
    "❤️", "💛", "💚", "💙", "💜", "🖤", "💔", "💖", "💗", "💘", "✨", "💫",
    "⭐", "🌟", "🌈", "🔥", "💥", "☃️", "🌌", "🌠", "💤", "💢", "💬", "🗯"
]

print("¡Bienvenido al juego Memory!")

# ETAPA 1: CREACION DEL TABLERO

## Dimensiones del tablero y control de errores
while True:
    try:
        print("Primero debes indicar el tamaño del tablero. Mínimo: 2x2. Máximo: 6x5 (también válido 5x6).")
        filas = int(input("Dime el número de filas: "))
        columnas = int(input("Dime el número de columnas: "))

        if not ((2 <= filas <= 6 and 2 <= columnas <= 5) or (2 <= filas <= 5 and 2 <= columnas <= 6)):
            print("Error: Las dimensiones deben estar entre 2x2 y 6x5 (también válido 5x6). Por favor, vuelve a intentarlo.")
            continue

        if (filas * columnas) % 2 != 0:
            print("Error: El número total de posiciones debe ser par. Por favor, vuelve a intentarlo.")
            continue

        break
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

## Creacion de las parejas aleatorias
parejas = (random.sample(emojis, ((filas * columnas) // 2))) * 2
random.shuffle(parejas)

## Creacion de un tablero oculto
tablero_oculto = []
for i in range(filas):
    fila = []
    for i in range(columnas):
        fila.append("_")
    tablero_oculto.append(fila)

print("¡Listo! Aquí está el tablero inicial:")
for i in range(filas):
    for j in range(columnas):
        print(tablero_oculto[i][j], end=" ")	
    print()

## Creacion del tablero de juego con las parejas
tablero = []
pos = 0
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(parejas[pos])
        pos += 1
    tablero.append(fila)

# print("Tablero con parejas de emojis:")
# for i in range(filas):
#     for j in range(columnas):
#         print(tablero[i][j], end=" ")	
#     print()