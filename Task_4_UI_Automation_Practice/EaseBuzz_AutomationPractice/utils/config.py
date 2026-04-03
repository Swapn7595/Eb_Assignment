# config.py

import logging
import os

# Configure logging
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'test_execution.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('PracticePageTestLogger')

# Added a utility to dynamically log test steps
class TestStepLogger:
    def __init__(self):
        self.steps = []

    def log_step(self, step_description):
        self.steps.append(step_description)
        logger.info(f"Test Step: {step_description}")

    def get_steps(self):
        return "\n".join(self.steps)

# Create a global instance of TestStepLogger
test_step_logger = TestStepLogger()

environments = {
    'qa': {
        'base_url': 'https://rahulshettyacademy.com/AutomationPractice/',
        # Add other environment-specific settings here
    },
    'dev': {
        'base_url': 'https://rahulshettyacademy.com/AutomationPractice/',
        # Add other environment-specific settings here
    },
    'prod': {
        'base_url': 'https://rahulshettyacademy.com/AutomationPractice/',
        # Add other environment-specific settings here
    }
}
