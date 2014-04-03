.. SUMOn documentation master file, created by
   sphinx-quickstart on Wed Mar 26 01:17:54 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SUMOn's documentation!
=================================

Contents:

.. toctree::
   :maxdepth: 2

General Syntax
=================================

[function] [card] [location]

Sample code:
---------------------------------

special hex 5 5
summon jonokuchi 3
move 2 3 3

- First command will apply the hex card ability on the wrestler in the the (5,5) tile.
- Second command summons a jonokuchi at the (0,3) or (7,3) tile. Row depends on which player programmed the code.
- Third command moves the wrestler in the (3,3) tile forward by two.

Functions:
---------------------------------

There are only three functions: summon, move, special. We can think of [card] and [location] as the parameters of these functions. Note that [location] may require more than one integer input from the user. This will be further discussed in the next two sections.

Location
---------------------------------

For location, a player may input [row] [col] for special and move functions; and only [col] for the summon function, since the row is fixed when summoning. The game will check which row to place the wrestler based on who programmed the code. Player 1 summons in row 7 while player 2 summons in row 0. For reference, the top-left tile has the position (7,0) while the bottom-right tile has the position (0,7). Index starts at 0.

Special note on move function: the location indicates the position of the wrestler you want to move *during the turn the card is used*. If you use two move cards consecutively, the row and column will be different. For example: if the original position is (7,0) and you place a Move 2 card and a Move 1 card, then the syntax would be "move 2 7 0" and "move 1 7 0" respectively.

Cards
---------------------------------

For the summon function, the player can only use the following wrestler_type cards: jonokuchi, komusubi, sekiwake, ozeki, yokuzana. Each wrester_type has a corresponding mana cost that will be deducted from the player.

For the move function, the player may input any number between 1 and 5, inclusive. This number also corresponds to the mana cost of the card.

For the special function, the player can only use the following special_type cards: jump, fatup, takedown, reverse, kamikaze, avatar, swap, hex. Most cards will only require one set of [row] [col] for location. Swap will require two. (e.g. "special swap 5 5 0 7")

Other Notes
---------------------------------

We use whitespace and newline as delimiters. Space separates the terms; newline separates commands. Each card has a corresponding command, and one command is executed per concurrent turn.

Non-numerical input should be in lowercase. Remove space for those with more than one word. (e.g. "takedown" instead of "take down").

Players may only code the cards given to them. Mana cost will be computed first before the player may end his turn in programming. That is, the total mana cost of the player's code should be less than or equal to the mana he or she has; otherwise the game will not let the player end his programming turn.

Contributors
.................................
Andres, Mireya Gen P.
Calabroso, Neil Francis M.
Esguerra, Tricia Mae R.
Mendoza, Kristoffer Marion L.
Shen, Mara O.




