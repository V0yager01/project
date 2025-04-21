import sys
from multiprocessing import Pool
from typing import Dict, Type, List

from console_parser import get_args
from logs import HandlerReportReader, OpenLog, ReportReaderABC
from printer import Printer
from utils import bind_dict_get_and_parse_logs, merge_log_reports


ReportReaderMap: Dict[str, Type[ReportReaderABC]] = {
    'handlers': HandlerReportReader
}


def get_and_create_tasks() -> List[Dict[str, object]]:
    args = get_args()
    path = args.log_files
    report = args.report

    tasks = [
        {'path': file,
         'reader': ReportReaderMap[report],
         'openlog': OpenLog} for file in path
    ]
    return tasks


if __name__ == "__main__":
    tasks = get_and_create_tasks()
    try:
        with Pool() as p:
            res = p.map(bind_dict_get_and_parse_logs, tasks)
        report = merge_log_reports(res)
    except Exception as e:
        print(f'{e}')
        sys.exit(1)
    Printer(report).consolerender()
