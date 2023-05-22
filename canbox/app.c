#include "app.h"
#include "button.h"
#include "indicator_led.h"
#include "uart_stdio.h"
#include "can.h"
#include "can1.h"
#include "message_services.h"
#include "usb_pro.h"
#include "rtc.h"

void receive() {
    if (g_CANRXFlag) {
        uint32_t ts = RTC_GetTimeStamp();
        CAN_Receive();
        MessageServices_EncodeMessage(MONITOR_CAN0, ts);
    }
}

/****************************************************************************** 
 *                                                                            * 
 *                              Tasks Container                               * 
 *                                                                            * 
 ******************************************************************************/
Task_t Task[] =
{
    {
        .is_enabled = true,
        .code = receive,
        .period = 1
    }
};

/****************************************************************************** 
 *                                                                            * 
 *                              Global Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* Number of Tasks for scheduler */
const uint8_t Num_Of_Tasks = (sizeof(Task) / sizeof(Task_t));

/******************************************************************************
 * Name         : Task_Init                                                   *
 * Inputs       : None                                                        *
 * Outputs      : None                                                        *
 * Return Value : None                                                        *
 * Description  : Initializes tasks used in application.                      *
 ******************************************************************************/
void Task_Init(void)
{
    /* Initializes indicator LED. */
    IndicatorLED_Init();
    
    /* Initializes switch 1. */
    Button_Init(SW1_CH);

    /* Initializes switch 2. */
    Button_Init(SW2_CH);

    USB0_Init();

    CAN_Init();
    CAN_TransmitConfig();
    CAN_ReceiveConfig();

    CAN1_Init();
    CAN1_TransmitConfig();
    CAN1_ReceiveConfig();

    UART0_Init();

    /* Initialize RTC */
    RTC_Init();
    RTC_Reset();



}
