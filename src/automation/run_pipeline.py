import subprocess
import sys

print("=" * 40)
print(" Financial AI Platform Automation ")
print("=" * 40)

python = sys.executable

steps = [
    ("Downloading Stock Data", "src/data/download_data.py"),
    ("Analyzing Stock Data", "src/data/analyze_data.py"),
    ("Training Machine Learning Model", "src/ml/train_model.py"),
    ("Predicting Next Stock Price", "src/ml/predict.py"),
    ("Generating AI Insights", "src/ai/insights.py"),
]

for title, script in steps:
    print(f"\nStep : {title}")

    result = subprocess.run([python, script])

    if result.returncode == 0:
        print("✅ Success")
    else:
        print("❌ Failed")
        break

print("\nAutomation Finished")