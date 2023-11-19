# TeamPeppe
# Create una cartella con il vostro nome e ci mettete dentro i vostri esercizi
Laboratory on Sets and Dictionaries
1. Write a function that given a string S and and integer k>0 generates a set M whose elements are 
all the substrings of length k of S.
Example: S=”mamma mia”, k=2 → {“ma”,”am”,”mm”,”a “,” m”,”mi”,”ia”}
2. Write a function that given two strings S1 and S2 return the list, sorted in alphabetical order, of 
all the characters that appear in both strings.
Example: S1=”peace”, S2=”patience” → [“a”,”c”,“e”,”p”]
Hint: from the strings obtain two sets of characters and then compute the intersection.
3. Write a function that given a string S creates a dictionary whose keys are the characters from the 
string and the values the number of their occurrences.
Example: S=”peace and love”→ {“p”:1, ”e”:3, ”a”:2, ”c”:1, ”n”:1, ”d”:1, ”l”:1, ”o”:1, ”v”:1}
4a. Write a function that given an integer N returns the list of all of its proper divisors
Example: 18 → [1,2,3,6,9]
(hint: k is a proper divisor of N if N%k==0, you may use brute force to find all of them and try to 
divide N by k=1,up to k=N/2 and checking the remainder)
4b. Write a function that given a list of integers L returns a dictionary whose keys are the integers in
L and whose values are the lists of their proper divisors.
Example: [5,18,42]→ {5:[1,5], 18:[1,2,3,6,9],42:[1,2,3,6,7,14,21]}
5. The following is a table of the RGB component of some digital colors
Color name R G B
Cyan 0 255 255
Pink 255 0 255
Yellow 255 255 0
Silver 128 128 128
Ivory 225 204 79
Pearl 234 230 202
Cobalt 30 32 61
Chartreuse 127 255 0
Chestnut 221 173 175
Mauve 131 51 102
a. create a dictionary C whose keys are the color names and the values the triples of their RGB 
values.
b. write a function that given C and a letter “R”,”G”,”B”, returns the name of the color with the 
highest value of R, G and B respectively.
c. write a function that given C returns the mean value of R,G,B over all the row of the table.
d. write a function that given C, a letter “R”,”G”,”B” and an integer k, returns a new dictionary with
only the colors such that R,G, B respectively have value greater than k.
e. write a function that given C returns a triple (r,g,b) such that 
- r is the number of colors where the R value is greater of both G and B
- g is the number of colors where the G value is greater of both R and B
- b is the number of colors where the B value is greater of both R and G
f. creates a dictionary T whose keys are the strings “Color”,”R”,”G”,”B”, and whose values are the 
list containing the respective columns of the table above

Laboratory on Strings and List in Python
1. Write a function that counts the NOT vowels in a string;
2. Write a function that given a long string (a text) counts the words in it;
3. Write a function that given a long string (a text) computes the frequencies of the vowels in it;
4. Write a function that given a list returns a string representation of it;
5. Write a function that given a list of numbers gives back the product of all its elements;
6. Write a function that given two lists checks if they have common elements;
7. Write a function that capitalizes all (and only) the vowels in a string;
8. Write a function that given a list returns a list with three lists as elements: one for the numbers, 
one for the strings and one for the boolean;
9. Write a function that given a list computes the arithmetic mean of the numbers in it;
10. Write a function that given a list of strings returns the mean length of the strings in it;
11. Write a function that given a list of numbers returns the maximum;
12. Write a function that given a list of numbers returns the minimum;
13. Write a function that given a list of numbers returns the median;
14. Write a function that given a list of numbers returns the quartiles;
15. Write a function that given a integer in decimal returns a list of characters with the single digits 
as elements.
16. Write a function that given a string in roman literals returns the decimal value (use only 
“additive roman numerals”.
17. Write a function that given two days of a non-leap year counts how many days are in between.
18. Write a function that given two hours of a day in the format of strings like “06.34:15” computes 
how many seconds are included in between.
19. Write a function that given a number of seconds returnr the value in days, hours, minutes and 
seconds.
20. Write a function that given an integer n and k generates the list of the k-th power of the first n 
integers