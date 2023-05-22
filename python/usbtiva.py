# usbtiva

import datetime
import threading
import serial.tools.list_ports


# Parameters
DEVICE_SERIAL = 'MONITOR7'  # Serial stored in monitoring tool
BAUD_RATE = 115200          # in Hz
MSG_LENGTH = 2              # in bytes
PREAMBLE = [0xAA, 0xAA, 0xAA, 0xAB]
                            # Start of Frame to sync

# Threading timers
TIMER0_TIME = 0.1
TIMER1_TIME = 0.001


def sync(ser):
    # Byte received and index
    byte, idx = 0, 0
    # Make sure to receive all preamble consecutive bytes
    while idx != len(PREAMBLE):
        # Receive byte
        byte = list(ser.read())[0]
        # update index
        idx = idx+1 if byte == PREAMBLE[idx] else 0

    

def decode(msg):
    lst, msg = list(msg), ''
    for i in lst:
        msg += ('%02x' % i).upper() + ' '
    return msg


class communication:
    def __init__(self):
        self.serEstablished, self.isConnected, self.com = False, False, None
        self.verbose, self.msgs, self.ser, self.store = True, [], None, True

        self.InitTimers()

    def t0_KeepAlive(self):
        self.KeepAlive()

        if self.isConnected and not self.serEstablished:
            try:
                self.ser = serial.Serial(self.com, BAUD_RATE, timeout=1)
                self.serEstablished = True
                threading.Timer(TIMER1_TIME, self.t1_StoreData).start()
                print("COM Status: Connected")
            except:
                print("COM Status: Serial Error (device not responding)")
        elif not self.isConnected and self.serEstablished:
            self.serEstablished = False
            self.ser.close()
            print("COM Status: Disconnected")

        threading.Timer(TIMER0_TIME, self.t0_KeepAlive).start()

    def t1_StoreData(self):
        while self.isConnected:            
            try:
                sync(self.ser)
                length = int.from_bytes(self.ser.read(MSG_LENGTH),
                                        byteorder='big') - MSG_LENGTH
            except:
                length = 0
                self.isConnected = False

            if length:
                time = datetime.datetime.now()
                msg = self.ser.read(length)

                # print if verbose is allowed
                if self.verbose:
                    time_str = time.strftime("%H:%M:%S.%f")[:-2]
                    print('Received at %s:' % time_str, decode(msg))
                # store if storage is allowed
                if self.store:
                    self.msgs.append((time, msg))

            # threading.Timer(TIMER1_TIME, self.t1_StoreData).start()
        else:
            pass

    def Dequeue(self):
        if len(self.msgs):
            return self.msgs.pop(0)
        else:
            return None

    def Transmit(self, msg):
        if self.isConnected:
            try:
                self.ser.write(bytes(msg))
            except:
                pass

    def InitTimers(self):
        threading.Timer(TIMER0_TIME, self.t0_KeepAlive).start()

    def KeepAlive(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.serial_number == DEVICE_SERIAL:
                self.isConnected, self.com = True, port.device
                return
        self.isConnected, self.com = False, None


if __name__ == "__main__":
    com = communication()
    #com.setStore(True)
    
