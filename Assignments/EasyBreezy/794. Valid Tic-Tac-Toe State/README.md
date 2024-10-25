# 794. Valid Tic-Tac-Toe State

Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.

The first player always places 'X' characters, while the second player always places 'O' characters.

'X' and 'O' characters are always placed into empty squares, never filled ones.

The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.

The game also ends if all squares are non-empty.

No more moves can be played if the game is over.
 

## Example 1:

Input: board = ["O  ","   ","   "]

![image](https://github.com/user-attachments/assets/3ee3827f-1188-46ec-8043-2d16435c0736)

Output: false

Explanation: The first player always plays "X".


## Example 2:


Input: board = ["XOX"," X ","   "]

![image](https://github.com/user-attachments/assets/786f308b-ad83-40b8-8686-318cb1c2eec6)

Output: false

Explanation: Players take turns making moves.

## Example 3:


Input: board = ["XOX","O O","XOX"]

![image](https://github.com/user-attachments/assets/13f40072-f869-481c-8362-563b441ee754)

Output: true
 

## Constraints:

board.length == 3

board[i].length == 3

board[i][j] is either 'X', 'O', or ' '.
