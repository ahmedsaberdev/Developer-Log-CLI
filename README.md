# Developer log CLI

A simple command-line tool to maintain a daily developer log.  
Automatically groups entries under today's date, timestamps each entry, and allows you to view your full log history.

---

## Features

- **Automatic Date & Time**: Adds today's date and current time automatically.
- **Grouped Entries**: Multiple entries per day are grouped under a single date header.
- **Customizable Formats**: Date/time format and log file location are read from a `config.json`.
- **View Past Logs**: Quickly display all previous entries with the `--view` flag.

---

## Installation

1. Make sure you have **Python 3.8+** installed.
2. Clone this repository or copy the files into your project folder.
3. Install any required dependencies (none beyond the Python standard library).

---

## Configuration

Create a `config.json` file in the project root with the following structure:

```json
{
  "default-log-file": "devlog.txt",
  "date-format": "%Y-%m-%d",
  "time-format": "%H:%M"
}
```

---

## Usage

1. Add a New Entry

```bash
python devlog.py "Fixed a bug in the authentication module"

```

Automatically adds under today's date in your log file.

2. View All Logs

```bash
python devlog.py --view
```

Prints the entire devlog.txt content to the terminal.

---

## Example Log Output

```markdown
2025-08-25

- (14:30)
  Fixed a bug in authentication module

- (16:45)
  Improved logging system
```

---

## Future Ideas (Optional)

- Write logs to Markdown format for better formatting.
- Auto-push logs to GitHub for backup.
- Support editing/deleting specific entries.

---

## License

This project is open-source. Use it and modify it freely.
