import schedule
import time
import os
import subprocess
from datetime import datetime

LOG_FILE = 'C:/Users/ELITE/Documents/AGROALERT/scheduler_log.txt'

def log(msg):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')

def run_notebook(notebook_path):
    log(f"Running: {notebook_path}")
    result = subprocess.run([
        'python', '-m', 'jupyter', 'nbconvert',
        '--to', 'notebook',
        '--execute', '--inplace',
        '--ExecutePreprocessor.timeout=600',
        notebook_path
    ], capture_output=True, text=True)
    if result.returncode == 0:
        log(f"✓ Success: {notebook_path}")
    else:
        log(f"✗ Error: {result.stderr[:300]}")

BASE = 'C:/Users/ELITE/Documents/AGROALERT/notebooks/'

def weekly_pipeline():
    log("=" * 50)
    log("AGROALERT WEEKLY PIPELINE STARTED")
    log("=" * 50)
    run_notebook(BASE + '02_ndvi_data.ipynb')
    run_notebook(BASE + '03_weather_data.ipynb')
    run_notebook(BASE + '04_soil_moisture.ipynb')
    run_notebook(BASE + '05_data_processing.ipynb')
    run_notebook(BASE + '06_random_forest.ipynb')
    run_notebook(BASE + '07_ensemble.ipynb')
    run_notebook(BASE + '08_alerts.ipynb')
    log("AGROALERT WEEKLY PIPELINE COMPLETE")
    log("=" * 50)

schedule.every().monday.at("08:00").do(weekly_pipeline)
log("AgroAlert scheduler started — running every Monday at 08:00 AM")

# Test run
log("Running initial test...")
weekly_pipeline()

while True:
    schedule.run_pending()
    time.sleep(60)