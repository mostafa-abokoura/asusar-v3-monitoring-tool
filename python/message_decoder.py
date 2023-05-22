# message_decoder

# Channel types
UART = [0x10, 0x11]
SPI = [0x20]
I2C = [0x30]
CAN = [0x01, 0x02]
ETH = [0x40]

# Communication types tuple
COMM = {'UART': UART,
        'SPI': SPI,
        'I2C': I2C,
        'CAN': CAN,
        'ETH': ETH}


def identify_channel(channel):
    can_dir = 'TX' if channel & 0x80 else 'RX'
    channel = channel & 0x7F
    for name, comm in COMM.items():
        for ch in range(len(comm)):
            if channel == comm[ch]:
                return name, ch, can_dir
    return 'NONE', -1, 'NONE'

def decode_can_message(msg):
    can_id = ('%02x %02x' % (msg[0], msg[1])).upper()
    can_data = ''
    for i in range(2, len(msg)):
        can_data = ('%02x ' % msg[i]).upper() + can_data
    return can_id, can_data


def decode(msg):
    ts = int.from_bytes(msg[:4], byteorder='big', signed=False) / 32768
    msg = list(msg[4:])
    comm, ch, can_dir = identify_channel(msg[0])
    if ch != -1:
        if comm == 'CAN':
            can_id, can_data = decode_can_message(msg[1:])
            can_ch = 'CAN%d' % ch
            return (ts, can_dir, can_ch, can_id, can_data)
        else:
            return (ts, 'NONE', 'NONE', '0x----', '-- (not coded yet) --')
    else:
        return (ts, 'NONE', 'NONE', '0x----', '-- -- -- --')
