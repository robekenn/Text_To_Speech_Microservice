import zmq
import json
import Create_TTS
import Play_TTS
import Delete_TTS
import time

def init_server():
    #initilises the socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5554")
    return socket

def main():
    socket = init_server()
    while True:
        #  Wait for next request from client
        message = socket.recv()

        #changes the recieved JSON to normal data
        message = json.loads(message)
        print(message)

        if message[0] == 1:
            # Create audio
            print("Create Audio")
            retMessage = Create_TTS.create(message[1])
            socket.send_string(str(retMessage))
            time.sleep(.5)
        elif message[0] == 2:
            #Play Sound
            print("Play Sound")
            retMessage = Play_TTS.play_wav()
            socket.send_string(str(retMessage))
            time.sleep(.5)
        elif message[0] == 3:
            #Delete Sound
            print("Delete Sound")
            retMessage = Delete_TTS.delete()
            socket.send_string(str(retMessage))
            time.sleep(.5)

if __name__ == "__main__":
    main()
