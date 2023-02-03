A regular expression, commonly called a **regexp**, is a sequence of characters that define a search pattern.
It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a **find and replace** command).
While it is a very powerful tool, it is also very dangerous because of its complexity.

### Regex Quick Reference
```
[abc]	      A single character of: a, b, or c
[^abc]	    Any single character except: a, b, or c
[a-z]	      Any single character in the range a-z
[a-zA-Z]	  Any single character in the range a-z or A-Z
^	          Start of line
$	          End of line
\A	        Start of string
\z	        End of string
.	          Any single character
\s	        Any whitespace character
\S	        Any non-whitespace character
\d	        Any digit
\D	        Any non-digit
\w	        Any word character (letter, number, underscore)
\W	        Any non-word character
\b	        Any word boundary
(...)	      Capture everything enclosed
(a|b)	      a or b
a?	        Zero or one of a
a*	        Zero or more of a
a+	        One or more of a
a{3}	      Exactly 3 of a
a{3,}	      3 or more of a
a{3,6}	    Between 3 and 6 of a
```

This README describes what each script/program is doing:

The file `0-simply_match_school.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method.

The file `1-repetition_token_0.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method.

The file `2-repetition_token_1.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method.

The file `3-repetition_token_2.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method.

The file `4-repetition_token_3.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method.

The file `5-beginning_and_end.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method that matches a string that starts with `h` ends with `n` and can have any single character in between.

The file `6-phone_number.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method that matches a 10 digit phone number.

The file `7-OMG_WHY_ARE_YOU_SHOUTING.rb` is a ruby script that accepts one argument and pass it to a regular expression matching method that matches only capital letters.
