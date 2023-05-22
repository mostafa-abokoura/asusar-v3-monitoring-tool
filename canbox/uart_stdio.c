#include "uart_stdio.h"

bool g_UART0_available = false;

void UART0_Init(void)
{
    /* Set MCU clock. */
    SysCtlClockSet(SYSCTL_SYSDIV_5|
                   SYSCTL_USE_PLL|
                   SYSCTL_XTAL_16MHZ|
                   SYSCTL_OSC_MAIN);

    /* Enable UART0 module & its port. */
    SysCtlPeripheralEnable(SYSCTL_PERIPH_UART0);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);

    /* Configure UART0 pins. */
    GPIOPinConfigure(GPIO_PA0_U0RX);
    GPIOPinConfigure(GPIO_PA1_U0TX);
    GPIOPinTypeUART(GPIO_PORTA_BASE,
                    GPIO_PIN_0|GPIO_PIN_1);
    
    /* Enable UART0 interrupt if needed. */
    UARTIntEnable(UART0_BASE, UART_INT_RX | UART_INT_RT);
    
    /* Configure UART0. */
    UARTConfigSetExpClk(UART0_BASE, 
                        SysCtlClockGet(),
                        UART0_BAUDRATE,
                        (UART_CONFIG_WLEN_8|
                         UART_CONFIG_PAR_NONE|
                         UART_CONFIG_STOP_ONE));
}

void UART0_SendByte(char byte)
{
    /* Send a byte. */
    UARTCharPut(UART0_BASE, byte);
}

void UART0_Send(char *arr, int size)
{
uint32_t index;                 /* string index */

    /* Loop over until a 'null character'. */
    for(index=0; index<size; ++index)
    {
        /* Send a byte. */
        UARTCharPut(UART0_BASE, arr[index]);
    }
}

char UART0_ReceiveByte(void)
{
    /* Check UART buffer */
    if (UARTCharsAvail(UART0_BASE))
    {
        /* Set availability flag. */
        g_UART0_available = true;
        
        /* Return received byte. */
        return UARTCharGet(UART0_BASE);
    }
    else /* NO DATA RECEIVED */
    {
        /* Clear availability flag. */
        g_UART0_available = false;
        
        /* Return empty. */
        return UART0_EMPTY_BYTE;
    }
}
