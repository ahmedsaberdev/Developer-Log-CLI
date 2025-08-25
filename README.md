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
  "date-format": "%Y-%m-%d",
  "time-format": "%H:%M",
  "default-log-file": "devlog.txt"
}
```
