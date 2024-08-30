from abc import ABC, abstractmethod
import json
from dicttoxml import dicttoxml


class ReportFormatter(ABC):
    @abstractmethod
    def format(self, report):
        pass


class JsonFormatter(ReportFormatter):
    def format(self, report):
        return json.dumps(report)


class XmlFormatter(ReportFormatter):
    def format(self, report):
        return dicttoxml(report).decode('utf-8')