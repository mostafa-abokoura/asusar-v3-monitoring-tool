import cantools
db = cantools.db.load_file('dbc.dbc')
for i in range(len(db.messages)):
    msg = db.messages[i]
    print(hex(msg.frame_id))
    print(msg.name)
    print(msg._cycle_time)
    

##mas=db.get_message_by_frame_id(17)
##print(mas)
##mas=db.get_message_by_frame_id()
##print(mas)
##print(mas.name)
##print(hex(mas.frame_id))
##print(mas.is_extended_frame)
##print(mas.length)
##message = db.get_message_by_name('Engine_Msg')
##print("Input cycle time: ", message.dbc.attributes['GenMsgCycleTime'].value)
