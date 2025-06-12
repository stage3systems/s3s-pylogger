import logging
import sys

class CLogger:
    """
    Custom logger with color-coded, emoji-prefixed messages.
    """

    LOG_COLORS = {
        'info': "\033[38;5;108m",      # Soft green
        'debug': "\033[38;5;67m",      # Subtle blue
        'warning': "\033[38;5;179m",   # Amber/goldenrod
        'error': "\033[38;5;203m",     # Light red
        'critical': "\033[38;5;199m",  # Violet-pink
    }

    LOG_PREFIXES = {
        'info': "ℹ️",
        'debug': "🐞",
        'warning': "⚠️",
        'error': "❌",
        'critical': "🔥",
    }

    RESET_COLOR = "\033[0m"

    def __init__(self, app_name: str = None, display_color: bool = True, display_prefix: bool = True):
        self.app_name = app_name or ""
        self.display_color = display_color
        self.display_prefix = display_prefix  # Default to True for prefix display
        self.logger = logging.getLogger(self.app_name)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _get_log_message(self, log_type: str, message: str) -> str:
        if self.app_name:
            message = f"{self.app_name}: {message}"

        prefix = self.LOG_PREFIXES.get(log_type, "") + "  " if self.display_prefix else ""
        if self.display_color and log_type in self.LOG_COLORS:
            color = self.LOG_COLORS[log_type]
            message = f"{color}{prefix}{message}{self.RESET_COLOR}"
        else:
            message = f"{prefix}{message}"
        return message

    def set_level(self, level: str):
        levels = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        if level not in levels:
            raise ValueError(f"Invalid logging level: {level}")
        self.logger.setLevel(levels[level])

    def info(self, message: str, *args, **kwargs):
        if args:
            message = message % args
        self.logger.info(self._get_log_message('info', message), **kwargs)

    def debug(self, message: str, *args, **kwargs):
        if args:
            message = message % args
        self.logger.debug(self._get_log_message('debug', message), **kwargs)

    def warning(self, message: str, *args, **kwargs):
        if args:
            message = message % args
        self.logger.warning(self._get_log_message('warning', message), **kwargs)

    def error(self, message: str, *args, **kwargs):
        if args:
            message = message % args
        self.logger.error(self._get_log_message('error', message), **kwargs)

    def critical(self, message: str, *args, **kwargs):
        if args:
            message = message % args
        self.logger.critical(self._get_log_message('critical', message), **kwargs)
