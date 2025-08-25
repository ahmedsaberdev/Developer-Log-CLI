import argparse
from pathlib import Path
from datetime import date, datetime

parser = argparse.ArgumentParser()
parser.add_argument('entry', type=str, help='add entry to devlog file')
args = parser.parse_args()

def add_entry(file: str, entry: str):
  today_date = date.today().strftime('%d-%m-%Y')
  file_path = Path(file)

  if not file_path.exists():
    with file_path.open('w') as f:
      f.write(f'{today_date}\n - {entry}')
    return

  with file_path.open('r') as f:
    lines = f.readlines()

  if any(line.strip() == today_date for line in lines):
    with file_path.open('a') as f:
      f.write(f' - {entry}')
  else:
    with file_path.open('a') as f:
      f.write(f'{today_date}\n - {entry}')


if __name__ == "__main__":
  add_entry('devlog.txt', args.entry)