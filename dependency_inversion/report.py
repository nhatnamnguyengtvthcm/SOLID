import json
from dicttoxml import dicttoxml
import pandas as pd

def write_report(report):

    # Json format
    report_json = json.dumps(report)
    # xml format
    report_xml = dicttoxml(report)
    
    # write to txt
    with open('report.txt', 'w') as f:
        f.write(report_json)

    # write to xml
    with open('report.xml', 'w') as f:
        f.write(report_xml)
