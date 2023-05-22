#include "rtc.h"

void RTC_Init(void)
{
    SysCtlPeripheralEnable(SYSCTL_PERIPH_HIBERNATE);
    HibernateClockConfig(HIBERNATE_OSC_LFIOSC);
    HibernateRTCEnable();
}


void RTC_Reset(void)
{
    HibernateRTCSet(0);
}


uint32_t RTC_GetTimeStamp(void)
{
    return HibernateRTCSSGet() + HibernateRTCGet()*32768;
}
