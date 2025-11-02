# keylogger009
A keylogger tool that captures the keys when pressed 

# Python Educational Keylogger

This project is a simple keylogger built in Python. It is intended **strictly for educational purposes** to demonstrate how system-level hooks and event listeners work.

The script captures keystrokes and saves them to a local file named `key_log.txt`. It does **not** send any data over the network.

## Ethical Warning
"Do not use this tool on any computer you do not own or have explicit permission to monitor."

Capturing keystrokes without consent is a violation of privacy and is illegal in most places. This project is for learning about cybersecurity and programming, not for spying.

## How to Run

1.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv my_venv
    source my_venv/bin/activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install pynput
    ```

3.  **Run the Script:**
    ```bash
    python helloworldl.py
    ```

4.  The logger will start. Press the **`Esc`** key to stop it.
5.  The output will be saved in `key_log.txt`.
