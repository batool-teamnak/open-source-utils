# Open Source Utils

A collection of open-source Python utilities and helper scripts for common development tasks — file handling, API wrappers, text processing, and automation helpers.

## Utilities

| Script | Description |
|--------|-------------|
| `file_utils.py` | File search, copy, move, and cleanup helpers |
| `api_wrapper.py` | Generic REST API wrapper with retry logic |
| `text_utils.py` | String cleaning, formatting, and parsing helpers |
| `date_utils.py` | Date range generation, formatting, timezone conversion |
| `json_utils.py` | Deep merge, flatten, filter JSON structures |
| `log_utils.py` | Colored console logger with file rotation |

## Installation

```bash
git clone https://github.com/batool-teamnak/open-source-utils
cd open-source-utils
pip install -r requirements.txt
```

## Usage

```python
from file_utils import find_files, cleanup_empty_dirs
from text_utils import slugify, truncate
from date_utils import date_range

for date in date_range("2024-01-01", "2024-01-31"):
    print(date)
```

## Contributing

PRs welcome. Keep utilities focused, well-named, and dependency-free where possible.

## License

MIT

<!-- Updated -->
