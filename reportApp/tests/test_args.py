import sys

from console_parser import get_args


def test_arg_parser(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['main.py',
                                      'file1.log',
                                      'file2.log',
                                      '--report',
                                      'handlers'])
    args = get_args()
    path = args.log_files
    report = args.report
    assert report == 'handlers'
    assert path == ['file1.log', 'file2.log']