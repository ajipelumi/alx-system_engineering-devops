#include <stdio.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - creates 5 zombie processes
 *
 * Return: SUCCESS
 */

int main(void)
{
	int i, process, pid;

	for (i = 0; i < 5; i++)
	{
		process = fork();
		if (process == -1)
		{
			return (1);
		}
		if (process == 0) /* child process */
		{
			pid = getpid();
			printf("Zombie process created, PID: %d\n", pid);
		}
		else /* parent process */
		{
			infinite_while();
		}
	}
	return (0);
}

/**
 * infinite_while - calls main to sleep
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
