import logging

# Configure logging
logging.basicConfig(
    filename="reports/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation Started")

logging.info("Downloading Stock Data")

logging.info("Analyzing Stock Data")

logging.info("Training Machine Learning Model")

logging.info("Predicting Stock Price")

logging.info("Generating AI Insights")

logging.info("Automation Completed")

print("✅ Log file created successfully!")