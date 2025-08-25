import json
import argparse
from pathlib import Path
from datetime import date, datetime

parser = argparse.ArgumentParser()
parser.add_argument('entry', nargs='?', type=str, help='Add entry to devlog file')
parser.add_argument('-v', '--view', action='store_true', help='View all past logs')
args = parser.parse_args()

with open('config.json', 'r') as f:
  config = json.load(f)

DATE_FORMAT = config['date-format']
TIME_FORMAT = config['time-format']
LOG_FILE = config['default-log-file']

def add_entry(file: str, entry: str):
  today_date = date.today().strftime(DATE_FORMAT)
  now_time = datetime.now().strftime(TIME_FORMAT)
  file_path = Path(file)

  if not file_path.exists():
    with file_path.open('w') as f:
      f.write(f'{today_date}\n - ({now_time})\n      {entry}\n\n')
    return

  with file_path.open('r') as f:
    lines = f.readlines()

  if any(line.strip() == today_date for line in lines):
    with file_path.open('a') as f:
      f.write(f' - ({now_time})\n      {entry}\n\n')
  else:
    with file_path.open('a') as f:
      f.write(f'{today_date}\n - ({now_time})\n      {entry}\n\n')


if __name__ == "__main__":
  if args.entry:
    add_entry(LOG_FILE, args.entry)

  if args.view:
    with open(LOG_FILE, 'r') as f:
      print(f.read())