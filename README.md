
# crisu_Memory
Welcome to the Memory Game! Also known as Pairs Search Game.

- Coded with Python 3.12.6
- Playable in terminal (GUI soon)
- Made by myself [@crisuroll](https://www.github.com/crisuroll)

## What is the Memory game?
The memory game, also known as the pair search game, is a classic card-based matching game that exercises memory and concentration. In this game, a set of cards (usually placed face down) contains pairs of images, symbols, numbers, or other graphics. The objective is to find and match all pairs by remembering the location of each card after it's been revealed.

Players take turns flipping over two cards at a time to see if they match.
- If they do, the player keeps the pair and gets another turn. 
- If not, the cards are flipped back over, and the next player takes a turn. 
![Memory game example](https://img.freepik.com/free-vector/hand-drawn-memory-game-card_23-2150138543.jpg?t=st=1730911742~exp=1730915342~hmac=1eb24fffbb7c52eb918dbe30530f3a5ad34fbf6afe9f29fb9c707ae3a79e72c0&w=996)
The game continues until all pairs have been found. The player with the most pairs at the end wins.

## Game modes and difficulty levels

This is a local game. You can do:
- Player 1 vs Player 2
- Player vs CPU
- CPU 1 vs CPU 2

The CPU has a memory to help it remember all cards and try to make pairs strategically. The memory is available in four levels of difficulty:
- Easy: The memory is always empty and the CPU chooses random cards.
- Medium: The memory only stores the last two cards seen.
- Hard: The memory remembers all cards seen and tries to make pairs.
- Expert: The memory contains all pairs since the game starts.

The difficulty levels are available on Player vs CPU and CPU 1 vs CPU 2 modes.

## Future versions
I plan to make a GUI in a future. For now, the game is playable on a command terminal and uses emojis to portray the cards. Unflipped cards are shown as underscores (_).

I also plan to improve the CPU memory, since sometimes it gets bugged and doesn't make pairs properly even knowing the position of two cards with the same icon.