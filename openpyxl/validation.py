#!/usr/bin/env python3

# conda install openpyxl==3.1.2
from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.cell_range import CellRange
import openpyxl

if __name__ == '__main__':
    filename = "example.xlsx"
    workbook = openpyxl.Workbook(filename)
    # # 创建sheet1
    sheet = workbook.create_sheet('sheet1')
    workbook.save(filename)

    workbook = openpyxl.load_workbook(filename)
    ws = workbook.active
    ws.cell(row=1, column=1).value = "高"
    # 创建数据验证对象
    dv = DataValidation(
        type="list",
        formula1='"高,中,低"',  # 这里是你要提供的选项，用逗号分隔
        showDropDown=True,
        allow_blank=True,
    )

    # https://openpyxl.readthedocs.io/en/3.1.2/validation.html

    ws.add_data_validation(dv)
    dv.add(ws["A1"])
    workbook.save("example.xlsx")
