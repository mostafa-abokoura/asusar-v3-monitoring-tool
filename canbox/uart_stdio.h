#ifndef UART0_STDIO_H_
#define UART0_STDIO_H_

#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_memmap.h"
#include "driverlib/sysctl.h"
#include "driverlib/uart.h"
#include "driverlib/pin_map.h"
#include "driverlib/gpio.h"

/****************************************************************************** 
 *                                                                            * 
 *                               Configuration                                * 
 *                                                                            * 
 ******************************************************************************/

/* Baud Rate */
#define UART0_BAUDRATE   (115200)

/* Empty byte */
#define UART0_EMPTY_BYTE (0)

/****************************************************************************** 
 *                                                                            * 
 *                              Shared Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* UART available flag */
extern bool g_UART0_available;

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Initializes UART */
extern void UART0_Init(void);

extern void UART0_SendByte(char byte);
extern void UART0_Send(char*, int);
extern char UART0_ReceiveByte(void);


#endif /* UART0_STDIO_H_ */
