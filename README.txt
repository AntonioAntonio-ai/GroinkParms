This program is safe with negative parameter numbers. It will ignore them because I don't believe that there is a single significant negative parameter number out there.
This program is safe with very big and small parameter numbers, which python really wants to display in scientific formula and mess up the delicate process.

CREATE BACKUPS (of the data folder) PLEEEEASE

Oh, and also any modified Pikmin 2 ISOs could be impossible to 100%, any%, play past a certain point, or play at all if this program sinks its teeth into its parameter files

==Author==
Mousejuggler (Mr. 2 Bon Kurei Comma#9007)

==Helpful Links==
https://pikmintkb.com/wiki/Pikmin_2_identifiers

==Setup==
Step 1. Extract the "enemyParms.szs" file from the "enemy" folder of a "root" folder extracted from a legally acquired .iso file of Pikmin 2. This should give you a folder named "data".

Step 2. Place that folder into the same folder as this program. The folder must be named "data" and should have all of the parameter txt files of every enemy in the game.

Step 3. Run the program. Follow the steps.

==Technical Information==
The algorithm for randomizing a parameter is something similar to...

parameter = randint(1*randomness,mod*randomness) / randomness
if randint(0,1) == 1:
	parameter = 1 / parameter
parameter = parameter / [THE ACTUAL PARAMETER NUMBER TAKEN FROM THE FILE]
parameter = parameter * lean
Then shave off a bunch of digits and do a little rounding and a little adding zeroes to match format.
And reinsert it into the parameter file by replacing text.

==Variables==
mod = Maximum random multiplier (You really oughtn't make this less than 1 and ought to make this an integer)
randomness = Randomness multiplication modifier (You really oughtn't make this less than 1 and ought to make this an integer)
lean = End product multiplier (lean) (no negative numbers)(Also don't make this zero)

So, if mod = 2, randomness = 2, and lean = 1.5, the parameter can be multiplied by 0.75, 1, 1.5, 2.25, or 3

==Fringe Cases==
If, for example, mod = 1, randomness = 1, and lean = 1.5, every parameter will be multiplied by 1.5

If, for example, mod = 1.5 and randomness = 1, the program gives an error and doesn't change that enemy's file. (That randint I don't want to replace, you see)

If, for example, mod = 1.5 and randomness = 4, the parameter can be multiplied or divided by 1, 1.25, or 1.5

If, for example, mod = 2 and randomness = -2, the program gives an error and doesn't change that enemy's file. (Randint again)

If, for example, mod = 4 and randomness = 0.5, the program gives an error and doesn't change that enemy's file. (Randint, yet again)

If, for example, mod = 0.5 and randomness = -8, the parameter can be multiplied or divided by 1, 8/7, 4/3, 8/5, or 2

If, for example, mod = -0.5 and randomness = -8, the parameter can be multiplied or divided by 1, 8/7, 4/3, 8/5, 2, 8/3, 4, 8, 0, -8, -4, -8/3, and -2, which causes a lot of problems. For one thing, I don't even want to consider what negative numbers can do when they've been unleashed into this program or a parameter file. For another thing, whether the number has (simplification) decided to be multiplied or divided by the zero, it will not change that enemy's file. Basically, there is a 1/13 chance in this case for the parameter file to not be changed at all per parameter randomized. This gives less than (much, much less in some cases.) a (12/13)^30 (9%) chance for the parameter file to be changed. If randomness was -4, 

So, trying for precision with this program is a lost cause. Good luck ;)

==What to do if you get softlocked==
Allow a randomized game to have the same save file as an unrandomized game. If you get stuck, switch to the unrandomized game and play until the next save point. Then, switch to the softlocked randomized game and hope for the best. Better still, have multiple randomized games that you switch between when you are locked from doing something.

==Coming Soon???==
I'll probably update this program and work out some kinks in like a week or 2 years.

==Copyright==
I don't care about this, just don't claim that you made this program.

==Specil Thanks==
WeirdBoo