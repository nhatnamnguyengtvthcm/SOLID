class Notification:
    def send(self, message, channel):
        if channel == 'email':
            self.send_email(message)
        elif channel == 'sms':
            self.send_sms(message)
        elif channel == 'push':
            self.send_push_notification(message)
        else:
            raise ValueError("Unknown channel")

    def send_email(self, message):
        print(f"Sending email: {message}")

    def send_sms(self, message):
        print(f"Sending SMS: {message}")

    def send_push_notification(self, message):
        print(f"Sending push notification: {message}")

# Usage
notifier = Notification()
notifier.send("Hello World!", 'email')
notifier.send("Hello World!", 'sms')
notifier.send("Hello World!", 'push')
