BWT

This is a repository for code I'm writing to perform the Burrows-Wheeler Transform, its inverse, and any related work on handling/searching through transformed texts.

suffixArray.py is dependant upon readText.py in order to acquire its input, this will change in a future update to make the input an argument, as it should be.

transform.py performs the Burrows-Wheeler transform, using output from suffixArray.py - the suffixArray and the BWT are closely related.

recover.py uses the suffix array in order to quickly recover the transformed text, again using output from suffixArray. It is a simple inverse of the code in transform.py

===
