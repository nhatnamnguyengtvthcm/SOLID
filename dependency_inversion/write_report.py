from writter import ReportWriter, TextFileWriter
from fomatter import JsonFormatter, ReportFormatter, XmlFormatter


def write_report(report, formatter: ReportFormatter, writer: ReportWriter):
    formatted_report = formatter.format(report)
    writer.write(formatted_report)


report = {
    "title": "Monthly Report",
    "data": [1, 2, 3, 4, 5]
}

json_formatter = JsonFormatter()
xml_formatter = XmlFormatter()

txt_writer = TextFileWriter('report.txt')
xml_writer = TextFileWriter('report.xml')

# Ghi báo cáo dưới dạng JSON
write_report(report, json_formatter, txt_writer)

# Ghi báo cáo dưới dạng XML
write_report(report, xml_formatter, xml_writer)