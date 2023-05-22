#ifndef MESSAGE_SERVICES_H_
#define MESSAGE_SERVICES_H_

#include "can.h"
#include "common.h"
#include "uart_stdio.h"
#include "usb_pro.h"

#define MONITOR_CAN0    1
#define MONITOR_CAN1    2

extern void MessageServices_EncodeMessage(uint8_t ch, uint32_t timeStamp);

#endif /* MESSAGE_SERVICES_H_ */
