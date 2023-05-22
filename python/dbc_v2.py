import cantools
db = cantools.db.load_file('dbc.dbc')
print (db)
mas=db.get_message_by_frame_id(17)
sigs=mas.signals
print(mas.signals)
for i in mas.signals:
    print(i.name)
    print(i.start)
    print(i.length)
    print(i.byte_order)
    print(i.is_signed)
    print(i.offset)
    print(i.minimum)
    print(i.maximum)
print(hex(mas.frame_id))
print(mas.is_extended_frame)
print(mas.length)
message = db.get_message_by_name('Engine')
#print("Input cycle time: ", message.dbc.attributes['GenMsgCycleTime'].value)

'''
q = 14//4
w = 14%4
e = ['0', '1', '3', '7']
r += q*'F'
t = int(e[w]+r, 16)
start = 2
b = (int(a, 16) >> start) & t
'''
