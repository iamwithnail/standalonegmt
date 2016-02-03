__author__ = 'chris'

import xlrd
import simplejson as json


def import_workbook(filename='static/GT180116.xlsx'):
    try:
        wb = xlrd.open_workbook(filename)
    except(IOError):
        raise
    return wb

def import_sheet(workbook, sheetname='UK GRANTS'):
    sheet = workbook.sheet_by_index(2)
    return sheet

def transform_date_from_row(row_value):
    from datetime import date
    initial = xlrd.xldate_as_tuple(row_value,0)
    output_date = date(initial[0], initial[1], initial[2])
    return output_date

def read_sheet(sheet, open=False):
    grants_list = []
    from datetime import datetime

    #Get the values for the column names, and append to list so grants_list[0] is header in template.
    header_values = sheet.row_values(0)
    grants_list.append(header_values)
    print header_values
    #work through sheet, then create a dictionary for each grant, appending it to the final list as appropriate
    for rownum in range(1, sheet.nrows):
        grant = {}
        row_values = sheet.row_values(rownum)
        #cycle through the headernames to create the subdictionary
        for i, header in enumerate(header_values):
            grant[header] = row_values[i]

        print grant
        if not open:
            grants_list.append(grant)
        else:
            try:
                if not isinstance(grant["Date Closes"], str):
                    if grant["Closes"] > datetime.now().date():
                        grants_list.append(grant)
                    else:
                        #we don't need to include this in open grants
                        pass
                else:
                    pass
            except ValueError, KeyError:
                #silently skip that error if date is invalid or not provided
                pass
    return grants_list


def jsonify(list):
    return json.dumps(list)

def build_json(open=False):
    workbook = import_workbook()
    sheet = import_sheet(workbook)
    bare_grants_list = read_sheet(sheet, open)
    #grant_detail = jsonify(bare_grants_list)
    return bare_grants_list
