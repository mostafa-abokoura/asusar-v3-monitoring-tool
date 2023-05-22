#include <scheduler.h>


int main(void)
{
    Scheduler_Init();           /* Initialize Scheduler */
    Scheduler_Loop();           /* Start Scheduler */

    for (;;)
    {
        /* NOT REACHABLE */
    }
}
