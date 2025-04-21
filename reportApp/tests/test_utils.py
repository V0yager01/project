import pytest

from logs import OpenLog, HandlerReportReader
from utils import get_and_parse_logs, merge_log_reports
from testlog_answers import handler_merged_answer


@pytest.fixture
def create_list_for_merge():
    report1 = get_and_parse_logs('tests/testfiles/test1.log',
                                 HandlerReportReader,
                                 OpenLog)
    report2 = get_and_parse_logs('tests/testfiles/test2.log',
                                 HandlerReportReader,
                                 OpenLog)
    return [report1, report2]


def test_merge(create_list_for_merge):
    merged = merge_log_reports(create_list_for_merge)
    assert merged == handler_merged_answer
