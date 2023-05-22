/****************************************************************************** 
 * Module      : CAN Bus                                                      * 
 * File Name   : can.h                                                        * 
 * Description : Header file for can module                                   * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef CAN_H_
#define CAN_H_

/* TIVAWARE */
#include <stdbool.h>
#include <stdint.h>
#include "inc/hw_can.h"
#include "inc/hw_ints.h"
#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "driverlib/can.h"
#include "driverlib/gpio.h"
#include "driverlib/interrupt.h"
#include "driverlib/pin_map.h"
#include "driverlib/sysctl.h"
#include "driverlib/uart.h"

/****************************************************************************** 
 *                                                                            * 
 *                              Shared Variables                              *
 *                                                                            * 
 ******************************************************************************/

/* CAN RX & TX messages. */
extern uint8_t g_rxCAN[8];
extern uint8_t g_txCAN[8];
tCANMsgObject g_rxCANMessage;

/* Interrupt handler flag to indicate that a message was received. */
extern volatile bool g_CANRXFlag;

/* Interrupt handler flag to indicate that a message was transmitted. */
extern volatile bool g_CANTXFlag;

/* A flag to indicate that some reception error occurred. */
extern volatile bool g_CANErrFlag;

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

extern void CAN_Init(void);

extern void CAN_ReceiveConfig(void);
extern void CAN_TransmitConfig(void);

extern void CAN_Transmit(void);
extern void CAN_Receive(void);

extern void CAN_SetTXMessageLength(uint8_t);
extern uint32_t CAN_GetRXMessageLength();

#endif /* CAN_H_ */
