The `for` loop is the first of the three shell looping constructs.
This loop allows for specification of a list of values. A list of commands is executed for each value in the list.

The syntax for this loop is:
```bash
for NAME in LIST; do
  COMMANDS
done
```

This README describes what each script/program is doing:

The file `0-RSA_public_key.pub` is a RSA public key.

The file `1-for_best_school` is a bash script that displays `Best School` 10 times using the `for` loop.

The file `2-while_best_school` is a bash script that displays `Best School` 10 times using the `while` loop.

The file `3-until_best_school` is a bash script that displays `Best School` 10 times using the `until` loop.

The file `4-if_9_say_hi` is a bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.

The file `5-4_bad_luck_8_is_your_chance` is a bash script that loops from 1 to 10 and:
  - displays `bad luck` for the 4th loop iteration
  - displays `good luck` for the 8th loop iteration
  - displays `Best School` for the other iterations
  
The file `6-superstitious_numbers` is a bash script that displays numbers from 1 to 20 and:
  - displays `4` and then `bad luck from China` for the 4th loop iteration
  - displays `9` and then `bad luck from Japan` for the 9th loop iteration
  - displays `17` and then `bad luck from Italy` for the 17th loop iteration

The file `7-clock` is a bash script that displays the time for 12 hours and 59 minutes.

The file `8-for_ls` is a bash script that displays:
  - The content of the current directory
  - In a list format
  - Where only the part of the name after the first dash is displayed

The file `9-to_file_or_not_to_file` is a bash script that gives you information about the `school` file.

The file `10-fizzbuzz` is a bash script that displays numbers from 1 to 100:
  - Displays `FizzBuzz` when the number is a multiple of 3 and 5
  - Displays `Fizz` when the number is multiple of 3
  - Displays `Buzz` when the number is a multiple of 5
  - Otherwise, displays the number
  - In a list format
