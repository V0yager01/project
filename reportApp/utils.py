from collections import defaultdict
from typing import Dict, List

from logs import OpenLogABC, ReportReaderABC
from settings import pattern


def get_and_parse_logs(path: str,
                       reader: ReportReaderABC,
                       openlog: OpenLogABC) -> Dict[str, Dict[str, int]]:
    log = reader(pattern, path, openlog)
    return dict(log.parselogs())


def bind_dict_get_and_parse_logs(kwargs):
    return get_and_parse_logs(**kwargs)


def merge_log_reports(reports: List[Dict[str, Dict[str, int]]]) -> Dict[str, Dict[str, int]]:
    merged = defaultdict(lambda: {"CRITICAL": 0,
                                  "DEBUG": 0,
                                  "INFO": 0,
                                  "WARNING": 0,
                                  "ERROR": 0})
    for report in reports:
        for path, levels in report.items():
            for level, count in levels.items():
                merged[path][level] += count

    return dict(merged)
