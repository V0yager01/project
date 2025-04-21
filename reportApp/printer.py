class Printer():
    def __init__(self, logs):
        self.headers = ['HANDLERS',
                        'DEBUG',
                        'INFO',
                        'WARNING',
                        'ERROR',
                        'CRITICAL']
        self.level_counter = {"DEBUG": 0,
                              "INFO": 0,
                              "WARNING": 0,
                              "ERROR": 0,
                              "CRITICAL": 0}
        self.total = 0
        self.serialized = []
        self.logs = logs

    def consolerender(self) -> None:
        for head in self.headers:
            print(head, end=' '*(22-len(head)))
        print()
        for url, level_dict in sorted(self.logs.items()):
            print(url, end=' '*(22-len(url)))
            for level in self.headers[1::]:
                print(level_dict[level], end=' '*(22-len(str(level_dict[level]))))
                self.level_counter[level] += level_dict[level]
            print()
        print(end=" "*22)
        for value in self.level_counter.values():
            self.total += value
            print(value, end=" "*(22-len(str(value))))
        print()
        print(f"Total requests: {self.total}")
