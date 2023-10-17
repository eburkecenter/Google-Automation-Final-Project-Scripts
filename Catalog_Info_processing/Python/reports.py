#!/usr/bin/env python3

import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(filename, title, summary):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_name = Paragraph(title, styles["BodyText"])
    report_weight = Paragraph(summary, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([report_name, empty_line, report_weight])
    print(report)
