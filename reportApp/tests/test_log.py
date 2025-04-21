import pytest

from contextlib import nullcontext

from logs import OpenLog, HandlerReportReader
from settings import pattern
from testlog_answers import handler_logs_answer


@pytest.mark.parametrize(
        'filepath, context',
        [
            ('tests/testfiles/test1.log', nullcontext()),
            ('tests/testfiles/test404.log', pytest.raises(FileNotFoundError))
        ]
)
def test_openlog_file_not_found(filepath, context):
    with context:
        with OpenLog(filepath) as file:
            pass


@pytest.mark.parametrize(
        'filepath, pattern, openlog',
        [

            ('tests/testfiles/test1.log', pattern, OpenLog),
            ('tests/testfiles/test2.log', pattern, OpenLog)
        ]
)
def test_handler_reader(filepath, pattern, openlog):

    parsed_logs = HandlerReportReader(pattern=pattern,
                                      file_path=filepath,
                                      openlog=openlog)

    res = parsed_logs.parselogs()
    assert res == handler_logs_answer[filepath]
