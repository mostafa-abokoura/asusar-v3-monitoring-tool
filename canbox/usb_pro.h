#include <stdbool.h>
#include <stdint.h>
#include "inc/hw_ints.h"
#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "inc/hw_gpio.h"
#include "inc/hw_uart.h"
#include "inc/hw_sysctl.h"
#include "driverlib/debug.h"
#include "driverlib/fpu.h"
#include "driverlib/gpio.h"
#include "driverlib/interrupt.h"
#include "driverlib/pin_map.h"
#include "driverlib/sysctl.h"
#include "driverlib/timer.h"
#include "driverlib/uart.h"
#include "driverlib/usb.h"
#include "usblib/usblib.h"
#include "usblib/usbcdc.h"
#include "usblib/usb-ids.h"
#include "usblib/device/usbdevice.h"
#include "usblib/device/usbdcdc.h"
#include "utils/ustdlib.h"
#include "usb_serial_structs.h"
#include "utils/uartstdio.h"

//*****************************************************************************
//
// Defines required to redirect UART0 via USB.
//
//*****************************************************************************
#define USB_UART_BASE           UART0_BASE
#define USB_UART_PERIPH         SYSCTL_PERIPH_UART0
#define USB_UART_INT            INT_UART0

//*****************************************************************************
//
// Default line coding settings for the redirected UART.
//
//*****************************************************************************
#define DEFAULT_BIT_RATE        115200
#define DEFAULT_UART_CONFIG     (UART_CONFIG_WLEN_8 | UART_CONFIG_PAR_NONE | \
                                 UART_CONFIG_STOP_ONE)

//*****************************************************************************
//
// Defines required to redirect UART0 via USB.
//
//*****************************************************************************
#define TX_GPIO_BASE            GPIO_PORTA_BASE
#define TX_GPIO_PERIPH          SYSCTL_PERIPH_GPIOA
#define TX_GPIO_PIN             GPIO_PIN_1

#define RX_GPIO_BASE            GPIO_PORTA_BASE
#define RX_GPIO_PERIPH          SYSCTL_PERIPH_GPIOA
#define RX_GPIO_PIN             GPIO_PIN_0


//*****************************************************************************
//
// Flags used to pass commands from interrupt context to the main loop.
//
//*****************************************************************************
#define COMMAND_PACKET_RECEIVED 0x00000001
#define COMMAND_STATUS_UPDATE   0x00000002


extern void USB0_Init(void);
