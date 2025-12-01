import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5554")



# -- TEST 1 --

#request with serilization
print("make")
siReq = [1, "Hello World!"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()


#------
#play
print("play")
siReq = [2]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()


#-----

#delete
print("delete")
siReq = [3]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)

#receive responce
message = socket.recv()

# -- END TEST 1 -- 

