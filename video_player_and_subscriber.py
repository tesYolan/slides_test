import cv2
import paho.mqtt.client as mqtt
from state_holder import state

state = "LOADING"
def on_message(client, userdata, message):
    print("here is here")
    global state

    state = f"{message.payload.decode()}"
    print(f"received message: {message.payload.decode()} on topic {message.topic}")
def state_machines():
    all_video_player_loading()
    all_video_player_melting()
    all_video_player_blender()



def all_video_player_loading():
    cap = cv2.VideoCapture("vids/loading.mp4")
    while(state == "LOADING"):
        # Capture frame-by-frame
        print(state)
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            cap = cv2.VideoCapture("vids/loading.mp4")
def all_video_player_melting():
    cap = cv2.VideoCapture("vids/melting.mp4")
    while(state == "MELTING"):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print(state)
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            cap = cv2.VideoCapture("vids/melting.mp4")
def all_video_player_blender():
    cap = cv2.VideoCapture("vids/blender.mp4")
    while(state == "BLENDER"):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print(state)
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            cap = cv2.VideoCapture("vids/blender.mp4")
def all_video_player_please_upload_again():
    cap = cv2.VideoCapture("vids/please_upload.mp4")
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print(state)
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            cap = cv2.VideoCapture("vids/please_upload.mp4")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_message = on_message

    client.connect("localhost", 1883, 60)
    client.subscribe("test/state")
    client.loop_start()

    while True:
        state_machines()