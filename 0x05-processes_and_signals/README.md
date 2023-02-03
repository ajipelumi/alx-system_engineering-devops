A **process** can be thought of as an instance of a program in execution.
We called this an **instance of a program**, because if the same program is run lets say 10 times then there will be 10 corresponding processes.

Each process has its own unique process ID through which it is identified in the system.
Besides it own ID, a parent’s process ID is also associated with a process.
The default maximum value of PIDs is *32,767*.
This maximum is important because it is essentially the maximum number of processes that can exist simultaneously on a system.

In Linux, processes can be of *two* types:

**Foreground Processes**
- depend on the user for input
- also referred to as interactive processes

**Background Processes**
- run independently of the user
- referred to as non-interactive or automatic processes

This README describes what each script/program is doing:

The file `0-what-is-my-pid` is a bash script that displays its own PID.

The file `1-list_your_processes` is a bash script that displays a list of currently running processes.

The file `2-show_your_bash_pid` is a bash script that displays lines containing the `bash` word, thus allowing us to easily get the PID of your Bash process.

The file `3-show_your_bash_pid_made_easy` is a bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

The file `4-to_infinity_and_beyond` is a bash script that displays `To infinity and beyond` indefinitely.

The file `5-dont_stop_me_now` is a bash script that stops 4-to_infinity_and_beyond process using `kill` command.

The file `6-stop_me_if_you_can` is a bash script that stops 4-to_infinity_and_beyond process using `pkill` command.

The file `7-highlander` is a bash script that displays:
- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a `SIGTERM` signal

The file `8-beheaded_process` is a bash script that kills the process 7-highlander.

The file `100-process_and_pid_file` is a bash script that:
- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a SIGTERM signal
- Displays `Y U no love me?!` when receiving a SIGINT signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

The file `manage_my_process` is a bash script that:
- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for 2 seconds

The file `101-manage_my_process` is a bash script that manages `manage_my_process`.

The file `102-zombie.c` is a C program that creates 5 zombie processes.
