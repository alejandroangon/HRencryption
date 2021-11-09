# HRencryption
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:
[√L] <= row <= column <= [√L] where [x] is floor function and [x] is ceil function 
Example
s = if man was meant to stay on the ground god would have given us roots
After removing spaces, the string is 54 characters long.  is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.
ifmanwas
meanttos
tayonthe
dwouldha
vegivenu
sroots
The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

Create a function to encode a message.

Function Description

Complete the encryption function in the editor below.

encryption has the following parameter(s):

string s: a string to encrypt
Returns

string: the encrypted string
Input Format

One line of text, the string S

Constraints
1 <= length of s <= 81

s contains characters in the range ascii[a-z] and space, ascii(32).

sample input
haveaniceday

sample output
hae and via ecy

explanation
L=12 | \/12 is between 3 and 4.
Rewritten with 3 rows and 4 columns:
have
anic
eday
