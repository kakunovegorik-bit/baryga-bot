import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='admin_activity.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class AdminBot:
    def __init__(self, admin_user='@dddltasa'):
        self.admin_user = admin_user

    def log_message(self, message):
        logging.info(f'Message from user: {message}')

    def log_photo(self, photo_url):
        logging.info(f'Photo sent: {photo_url}')

    def log_activity(self, activity):
        logging.info(f'User activity: {activity}')

    # Other bot methods go here

# Example usage
admin_bot = AdminBot()
admin_bot.log_message('User message goes here')  # Example of logging a user message
