## Code Challenge 02 - Word Values Part II - a simple game

Instructions [here](http://pybit.es/codechallenge02.html).

Previous challenges and About [here](http://pybit.es/pages/challenges.html).

Last time we provided unittests and a guiding template. We received feedback that this was a bit too stringent. Therefore we provide two templates this time: game-help.py and game-nohelp.py
 * We load in the necessary data structures to focus on the game:
 		# Note that DICTIONARY is a set for O(1) lookups
		from data import DICTIONARY, LETTER_VALUES, POUCH
 * Draw 7 random letters from POUCH.
 	As said POUCH is given and contains a distribution of Scrabble letters so that the player gets enough vowels (equally drawing A-Z makes it extremely hard because you need more vowels to make words):
 		['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C',
		'D', 'D', 'D', 'D', ...]
 * Ask the player to form a word with one or more of the 7 letters of the draw. Validate input for:
 		1) all letters of word are in draw;
		2) word is in DICTIONARY.
 * Calculate the word value and show it to the player.
 	To focus on this challenge we re-use two methods from the previous challenge for this: calc_word_value and max_word_value.
 * Calculate the optimal word (= max word value) checking all permutations of the 7 letters of the draw, cross-checking the DICTIONARY set for valid ones. This is a bit more advanced, but allows you to score the player (next).
 * Show the player what the optimal word and its value is.
 * Give the player a score based on the previous steps, basically: player_score / optimal_score.
