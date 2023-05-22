#include "message_services.h"

static const uint8_t preamble[] = {0xAA, 0xAA, 0xAA, 0xAB};
static const uint8_t preamble_length = sizeof(preamble) / sizeof(uint8_t);
static uint8_t g_pui8Can0Message[17];


void MessageServices_SendPreamble() {
    USBBufferWrite((tUSBBuffer *)&g_sTxBuffer,
                   (uint8_t *)&preamble, preamble_length);
}

void MessageServices_SendCANMessage(uint8_t channel, uint32_t timeStamp)
{
    uint8_t i, msg_length = g_rxCANMessage.ui32MsgLen;
    uint8_t total_length = 9 + msg_length;

    g_pui8Can0Message[0] = 0;
    g_pui8Can0Message[1] = total_length;

    g_pui8Can0Message[2] = timeStamp >> 24;
    g_pui8Can0Message[3] = timeStamp >> 16;
    g_pui8Can0Message[4] = timeStamp >>  8;
    g_pui8Can0Message[5] = timeStamp >>  0;

    g_pui8Can0Message[6] = channel;
    g_pui8Can0Message[7] = g_rxCANMessage.ui32MsgID >> 8;
    g_pui8Can0Message[8] = g_rxCANMessage.ui32MsgID;
    for (i=0; i<msg_length; ++i) {
        g_pui8Can0Message[9+i] = g_rxCANMessage.pui8MsgData[i];
    }

    MessageServices_SendPreamble();
    USBBufferWrite((tUSBBuffer *)&g_sTxBuffer,
                   (uint8_t *)&g_pui8Can0Message, total_length);
}

void MessageServices_EncodeMessage(uint8_t ch, uint32_t timeStamp)
{
    switch (ch)
    {
    case MONITOR_CAN0:
        MessageServices_SendCANMessage(ch, timeStamp);
        break;
    case MONITOR_CAN1:
        return;
    default:
        return;
    }
}
