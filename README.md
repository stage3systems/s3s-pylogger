```markdown
# s3s-pylogger

A lightweight, emoji-enhanced, color-coded logger for Python services.

## 📦 Installation

Add this to your `requirements.txt`:

```

git+ssh://git\@github.com/stage3systems/s3s-pylogger.git\@main#egg=s3s-pylogger

````

Or install directly:

```bash
pip install 'git+ssh://git@github.com/stage3systems/s3s-pylogger.git@main#egg=s3s-pylogger'
````

---

## 🚀 Usage

```python
from pylogger import CLogger

logger = CLogger(
  app_name="MyApp"
  display_color=True
  display_prefix=False
)

logger.set_level("debug")  # Optional: set log level

logger.info("Starting service")
logger.debug("Connecting to %s on port %d", "localhost", 8080)
logger.warning("Using fallback configuration")
logger.error("Failed to load module: %s", "auth")
logger.critical("Shutting down due to fatal error")
```

### Output Example

```
2025-06-12 13:00:00,001 - INFO - ℹ️  MyApp: Starting service
2025-06-12 13:00:00,002 - DEBUG - 🐞  MyApp: Connecting to localhost on port 8080
2025-06-12 13:00:00,003 - WARNING - ⚠️  MyApp: Using fallback configuration
2025-06-12 13:00:00,004 - ERROR - ❌  MyApp: Failed to load module: auth
2025-06-12 13:00:00,005 - CRITICAL - 🔥  MyApp: Shutting down due to fatal error
```

> 💡 Emoji and colors can be turned off via `display_prefix=False` and `display_color=False`.

---

## 🛠 Features

* ✅ Color-coded logs (optional)
* ✅ Emoji-prefixed messages (optional)
* ✅ Works with standard Python `logging`
* ✅ Can log with formatting args
* ✅ Service/app name tagging

