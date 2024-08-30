from abc import ABC, abstractmethod

# Define an abstract base class for all notification channels
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete implementations for each notification channel
class EmailNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending push notification: {message}")

# Notification class uses the NotificationChannel interface
class Notification:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def send(self, message):
        self.channel.send(message)

# Usage
email_notifier = Notification(EmailNotification())
email_notifier.send("Hello via Email!")

sms_notifier = Notification(SMSNotification())
sms_notifier.send("Hello via SMS!")

push_notifier = Notification(PushNotification())
push_notifier.send("Hello via Push Notification!")
