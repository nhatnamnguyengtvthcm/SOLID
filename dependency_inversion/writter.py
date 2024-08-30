from abc import ABC, abstractmethod


class ReportWriter(ABC):
    @abstractmethod
    def write(self, content):
        pass

class TextFileWriter(ReportWriter):
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)

            