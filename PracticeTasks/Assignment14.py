class LogManager:
    def __init__(self, filename):
        self.filename = filename

    def add_log_entry(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

    def display_log_contents(self):
        try:
            with open(self.filename, 'r') as file:
                contents = file.read()
                print("Log Contents:")
                print(contents)
        except FileNotFoundError:
            print("Log file not found.")

# Create an instance of LogManager
log_manager = LogManager('my_log.txt')

# Add log entries
log_manager.add_log_entry("Log entry 1")
log_manager.add_log_entry("Log entry 2")

# Display log contents
log_manager.display_log_contents()
