import json
import argparse
from pathlib import Path
from datetime import date, datetime

parser = argparse.ArgumentParser()
parser.add_argument('entry', type=str, help='add entry to devlog file')
args = parser.parse_args()

with open('config.json', 'r') as f:
  config = json.load(f)

DATE_FORMAT = config['date-format']
TIME_FORMAT = config['time-format']

def add_entry(file: str, entry: str):
  today_date = date.today().strftime(DATE_FORMAT)
  now_time = datetime.now().strftime(TIME_FORMAT)
  file_path = Path(file)

  if not file_path.exists():
    with file_path.open('w') as f:
      f.write(f'{today_date}\n - ({now_time})\n    {entry}\n')
    return

  with file_path.open('r') as f:
    lines = f.readlines()

  if any(line.strip() == today_date for line in lines):
    with file_path.open('a') as f:
      f.write(f'- ({now_time})\n    {entry}\n')
  else:
    with file_path.open('a') as f:
      f.write(f'{today_date}\n - ({now_time})\n    {entry}\n')


if __name__ == "__main__":
  add_entry('devlog.txt', args.entry)