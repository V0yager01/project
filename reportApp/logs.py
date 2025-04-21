import re

from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, TextIO


class OpenLogABC(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass


class OpenLog(OpenLogABC):
    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.file_path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.file_path} does not exist.')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


class ReportReaderABC(ABC):
    def __init__(self,
                 pattern: str,
                 file_path: str,
                 openlog: type[OpenLogABC]):
        self.pattern = pattern
        self.openlog = openlog(file_path)

    @abstractmethod
    def parselogs(self) -> Dict[str, Dict[str, int]]:
        pass


class HandlerReportReader(ReportReaderABC):
    def parselogs(self) -> Dict[str, Dict[str, int]]:
        logs = defaultdict(lambda: {"CRITICAL": 0,
                                    "DEBUG": 0,
                                    "INFO": 0,
                                    "WARNING": 0,
                                    "ERROR": 0})
        with self.openlog as log:
            for line in log:
                match = re.search(self.pattern, line)
                if match:
                    url = match.group('HANDLER')
                    level = match.group('level')
                    logs[url][level] += 1
        return dict(logs)
