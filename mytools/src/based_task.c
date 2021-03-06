/* based_task.c -- A basic real-time task skeleton. 
 *
 * This (by itself useless) task demos how to setup a 
 * single-threaded LITMUS^RT real-time task.
 */

/* First, we include standard headers.
 * Generally speaking, a LITMUS^RT real-time task can perform any
 * system call, etc., but no real-time guarantees can be made if a
 * system call blocks. To be on the safe side, only use I/O for debugging
 * purposes and from non-real-time sections.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

/* Second, we include the LITMUS^RT user space library header.
 * This header, part of liblitmus, provides the user space API of
 * LITMUS^RT.
 */
#include <litmus.h>

/* Next, we define period and execution cost to be constant. 
 * These are only constants for convenience in this example, they can be
 * determined at run time, e.g., from command line parameters.
 *
 * These are in milliseconds.
 */
#define PERIOD            4000
#define RELATIVE_DEADLINE 4000
#define EXEC_COST         3000

char FOLDER_PATH[5][47] = {"python3.9 src/main.py --input_folder ./imgs0/", 
							"python3.9 src/main.py --input_folder ./imgs1/", 
							"python3.9 src/main.py --input_folder ./imgs2/", 
							"python3.9 src/main.py --input_folder ./imgs3/", 
							"python3.9 src/main.py --input_folder ./imgs4/"};

/* Catch errors.
 */
#define CALL( exp ) do { \
		int ret; \
		ret = exp; \
		if (ret != 0) \
			fprintf(stderr, "%s failed: %m\n", #exp);\
		else \
			fprintf(stderr, "%s ok.\n", #exp); \
	} while (0)


/* Declare the periodically invoked job. 
 * Returns 1 -> task should exit.
 *         0 -> task should continue.
 */
int job(char *iPath);

void *feathertrace(void *args);
void *rt_task(void *args);

/* typically, main() does a couple of things: 
 * 	1) parse command line parameters, etc.
 *	2) Setup work environment.
 *	3) Setup real-time parameters.
 *	4) Transition to real-time mode.
 *	5) Invoke periodic or sporadic jobs.
 *	6) Transition to background mode.
 *	7) Clean up and exit.
 *
 * The following main() function provides the basic skeleton of a single-threaded
 * LITMUS^RT real-time task. In a real program, all the return values should be 
 * checked for errors.
 */
int main(int argc, char** argv)
{
	int do_exit = 0;
	struct rt_task param;
	pthread_t tid1, tid2;

	/* Setup task parameters */
	init_rt_task_param(&param);
	param.exec_cost = ms2ns(EXEC_COST);
	param.period = ms2ns(PERIOD);
	param.relative_deadline = ms2ns(RELATIVE_DEADLINE);

	/* What to do in the case of budget overruns? */
	param.budget_policy = NO_ENFORCEMENT;

	/* The task class parameter is ignored by most plugins. */
	param.cls = RT_CLASS_SOFT;

	/* The priority parameter is only used by fixed-priority plugins. */
	param.priority = LITMUS_LOWEST_PRIORITY;

	/* The task is in background mode upon startup. */


	/*****
	 * 1) Command line paramter parsing would be done here.
	 */

	// --------------------------------------------------
	// read the folder path containing all images.
	// do some processing to generate the filepath of all the images
	// --------------------------------------------------
	
	printf("\nParsed  command line inputs");

	/*****
	 * 2) Work environment (e.g., global data structures, file data, etc.) would
	 *    be setup here.
	 */
	printf("\nSetup work environment done");


	/*****
	 * 3) Setup real-time parameters. 
	 *    In this example, we create a sporadic task that does not specify a 
	 *    target partition (and thus is intended to run under global scheduling). 
	 *    If this were to execute under a partitioned scheduler, it would be assigned
	 *    to the first partition (since partitioning is performed offline).
	 */
	CALL( init_litmus() );

	/* To specify a partition, do
	 *
	 * param.cpu = CPU;
	 * be_migrate_to(CPU);
	 *
	 * where CPU ranges from 0 to "Number of CPUs" - 1 before calling
	 * set_rt_task_param().
	 */
	CALL( set_rt_task_param(gettid(), &param) );
	printf("\nSetup real-time parameters done");

	/*****
	 * 4) Transition to real-time mode.
	 */
	CALL( task_mode(LITMUS_RT_TASK) );

	/* The task is now executing as a real-time task if the call didn't fail. 
	 */
	printf("\nWorking as a real-time task");


	/*****
	 * 5) Invoke real-time jobs.
	 */

		// create a thread t1 and call the feather trace api below
		// pthread_create(&tid1, NULL, feathertrace,  NULL);
		

	// printf("\n called pthread for tid1");

		// in another thread t2, call this real-time task. once the thread completes, press enterto stop tracing
		// pthread_create(&tid2, NULL, rt_task, NULL);
		
		// pthread_join(tid2, NULL);
		// pthread_join(tid1, NULL);

	do {
		int count = 0;
		for(count = 0; count < 5; count++)
		{
			/* Wait until the next job is released. */
			sleep_next_period();
			/* Invoke job. */
			printf("\nFolder Path - %s\n", FOLDER_PATH[count]);
			job(FOLDER_PATH[count]);	
		}

		if(5 == count)
		{
			do_exit = 1;
		}			
	} while (!do_exit);

	printf("\ninvoked real-time jobs");
	
	/*****
	 * 6) Transition to background mode.
	 */
	CALL( task_mode(BACKGROUND_TASK) );
	printf("\ntransitioned to background mode");


	/***** 
	 * 7) Clean up, maybe print results and stats, and exit.
	 */
	return 0;
}


int job(char iPath[47]) 
{
	/* Do real-time calculation. */
    int      i = 0;
    for (i = 0 ; i < 10; i ++)   {
        printf("%d\t",i);
    }
	int status;


	// status = system(iPath);

	/* Don't exit. */
	// return 0;
	return 0;
}

void *feathertrace(void *arg)
{
	printf("\nin feather thread");
	system("./../feather-trace-tools/st-trace-schedule rt-trace");
	printf("\nafter feather");
	return NULL;
}

void *rt_task(void *arg)
{
	printf("\nin rt-thread");
	int count ;
	for(count = 0; count < 5; count++)
		{
			/* Wait until the next job is released. */
			sleep_next_period();
			/* Invoke job. */
			printf("\nFolder Path - %s\n", FOLDER_PATH[count]);
			job(FOLDER_PATH[count]);	
		}
	// return (void *) 42;
	return NULL;
}