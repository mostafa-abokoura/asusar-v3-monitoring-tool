/****************************************************************************** 
 * Module      : CAN Bus                                                      * 
 * File Name   : can.c                                                        * 
 * Description : Source file for can module                                   * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#include "can.h"

uint8_t g_rxCAN1[8];
uint8_t g_txCAN1[8];

tCANMsgObject g_rxCAN1Message, g_txCAN1Message;

volatile bool g_CAN1RXFlag = false;
volatile bool g_CAN1TXFlag = true;
volatile bool g_CAN1ErrFlag = false;


void CAN1IntHandler(void)
{
uint32_t ui32Status;

    /* Get CAN interrupt status. */
    ui32Status = CANIntStatus(CAN1_BASE, CAN_INT_STS_CAUSE);

    /* Check if Error */
    if(ui32Status == CAN_INT_INTID_STATUS)
    {
        /* Get CAN status. */
        ui32Status = CANStatusGet(CAN1_BASE, CAN_STS_CONTROL);

        /* Set CAN Error Flag. */
        g_CAN1ErrFlag = true;
    }
    else if (ui32Status == 1)
    {
        /* Clear interrupt for object #1. */
        CANIntClear(CAN1_BASE, 1);

        /* Set CAN receive flag. */
        g_CAN1RXFlag = true;

        /* Clear CAN Error Flag. */
        g_CAN1ErrFlag = false;
    }
    else if (ui32Status == 2)
    {
        /* Clear interrupt for object #2. */
        CANIntClear(CAN1_BASE, 2);

        /* Set CAN transmission flag. */
        g_CAN1TXFlag = true;

        /* Clear CAN Error Flag. */
        g_CAN1ErrFlag = false;
    }
    else
    {
        /* MISRA */
    }
}

void CAN1_Init(void)
{
    /* Enable PORTB clock. */
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);

    /* Configure CAN pins. */
    GPIOPinConfigure(GPIO_PA0_CAN1RX);
    GPIOPinConfigure(GPIO_PA1_CAN1TX);

    /* Select CAN mode for its pins. */
    GPIOPinTypeCAN(GPIO_PORTA_BASE, GPIO_PIN_0 | GPIO_PIN_1);

    /* Enable CAN0 peripheral. */
    SysCtlPeripheralEnable(SYSCTL_PERIPH_CAN1);

    /* Initialize CAN0 to known state. */
    CANInit(CAN1_BASE);

    /* Select CAN bit-rate. */
    CANBitRateSet(CAN1_BASE, SysCtlClockGet(), 500000);

    /* Enable CAN interrupt. */
    CANIntEnable(CAN1_BASE, CAN_INT_MASTER | CAN_INT_ERROR | CAN_INT_STATUS);
    IntEnable(INT_CAN1);

    /* Enable CAN0. */
    CANEnable(CAN1_BASE);
}

void CAN1_ReceiveConfig(void)
{
    /* Select CAN Message ID. */
    g_rxCAN1Message.ui32MsgID = 0;

    /* Select CAN Message Mask. */
    g_rxCAN1Message.ui32MsgIDMask = 0;

    /* Set CAN Message flags. */
    g_rxCAN1Message.ui32Flags = MSG_OBJ_RX_INT_ENABLE | MSG_OBJ_USE_ID_FILTER;

    /* Select CAN Message length. */
    g_rxCAN1Message.ui32MsgLen = 8;

    /* Select CAN Message data receiving container size. */
    g_rxCAN1Message.pui8MsgData = g_rxCAN1;

    /* Set as receiving container. */
    CANMessageSet(CAN1_BASE, 1, &g_rxCAN1Message, MSG_OBJ_TYPE_RX);
}

void CAN1_TransmitConfig(void)
{
    /* Select CAN Message ID. */
    g_txCAN1Message.ui32MsgID = 1;

    /* Select CAN Message Mask. */
    g_txCAN1Message.ui32MsgIDMask = 0;

    /* Set CAN Message flags. */
    g_txCAN1Message.ui32Flags = MSG_OBJ_TX_INT_ENABLE;

    /* Select CAN Message length. */
    g_txCAN1Message.ui32MsgLen = 8;

    /* Select CAN Message transmission data container. */
    g_txCAN1Message.pui8MsgData = g_txCAN1;
}

uint32_t CAN1_GetRXMessageLength()
{
    return g_rxCAN1Message.ui32MsgLen;
}

void CAN1_SetTXMessageLength(uint8_t message_length)
{
    /* Select CAN Message length. */
    g_txCAN1Message.ui32MsgLen = message_length;
}

void CAN1_Transmit(void)
{
    /* Check if transmission is allowed. */
    if ((true == g_CAN1TXFlag) && (false == g_CAN1ErrFlag))
    {
        /* Clear Flag. */
        g_CAN1TXFlag = false;

        /* Send over CAN. */
        CANMessageSet(CAN1_BASE, 2, &g_txCAN1Message, MSG_OBJ_TYPE_TX);
    }
}

void CAN1_Receive(void)
{
    /* Clear Flag. */
    g_CAN1RXFlag = false;

    /* Update Message. */
    CANMessageGet(CAN1_BASE, 1, &g_rxCAN1Message, 0);
}
