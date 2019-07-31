# STV

Contains my work on how to count single transferable votes using Python. 

Random selection is my code for counting STV using the random selection method for transferring surplus. I am planning to add the variant of using fractional transfer method soon.

The random selection method I employ is that a random ballot with a valid next preference from the winner with the highest vote total is selected one at a time, until his vote total reaches the quota or the second highest's count, whichever comes first. Whenever there is such a tie, a random ballot is selected from each winner and the preference is distributed simultaneously. 

An important feature of this counting method is that preference to candidate already elected is distributed exactly like to those not yet elected, eliminating the bias that occurs in the usual method. I do believe my method, the randomness notwithstanding and ignoring the practicalities, is logically and mathematically the fairest implementation, and free of arbitrariness as in Warren or Meek methods.
