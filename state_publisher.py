import tkinter as tk
import paho.mqtt.client as mqtt
from state_holder import store_states
root = tk.Tk()
states = store_states()

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def on_button_click():
    print("updating state")
    states.update_state()
    client.publish("test/state", states.state.name)


button = tk.Button(root, text="Next State", command=on_button_click)

button.pack()

root.mainloop()