import zmq
import json

def JSONDump(data):
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

def init_server():
    #initilises the socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5554")
    return socket

def JSONLoad():
    #read JSON Database's data
    with open('data.json', 'r') as file:
            return json.load(file)


def main():
    socket = init_server()
    data = JSONLoad()
    while True:
        #  Wait for next request from client
        message = socket.recv()

        #changes the recieved JSON to normal data
        message = json.loads(message)
        print(message)

        if message[0] == 1:
            # Get User Points
            print("Get User Points")
            retMessage = Create_TTS.create()
            socket.send_string(str(retMessage))
            JSONDump(data)
        elif message[0] == 2:
            #Add Points
            print("Add Points")
            retMessage = Delete_TTS.delete()
            socket.send_string(str(retMessage))
            JSONDump(data)

if __name__ == "__main__":
    main()
