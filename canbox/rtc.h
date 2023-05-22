#ifndef RTC_H_
#define RTC_H_


#include "types.h"
#include "common.h"
#include <time.h>
#include "inc/hw_hibernate.h"
#include "inc/hw_memmap.h"
#include "inc/hw_ssi.h"
#include "inc/hw_types.h"
#include "driverlib/gpio.h"
#include "driverlib/hibernate.h"
#include "driverlib/pin_map.h"
#include "driverlib/ssi.h"
#include "driverlib/sysctl.h"

extern void RTC_Init(void);
extern void RTC_Reset(void);
extern uint32_t RTC_GetTimeStamp(void);


#endif /* RTC_H_ */
