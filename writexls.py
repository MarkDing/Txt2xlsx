from xlwt import Workbook, easyxf
from xlwt.Utils import rowcol_to_cell

row0_style = easyxf(
    'font: name Calibri, bold True, height 220;'
    )
reg_row_style = easyxf(
    'pattern: pattern solid, fore_colour yellow;'
    'font: name Calibri, height 220;'
    )
common_style = easyxf(
    'font: name Calibri, height 220;'
    )

row0_data = [
    'Module',
    'Register',
    'Offset',
    'Bit Num',
    'Bit',
    'Bit Access',
    'Bit Field Reset',
    'Enum Name',
    'Enum Value',
    'Special',
    'Short Name',
    'Description',
    ]

w = Workbook()
#sheet1 = w.add_sheet('version')

sheet2= w.add_sheet('Base_alias')
sheet2.panes_frozen = True
sheet2.remove_splits = True
sheet2.horz_split_pos = 1
for col in range(12):
    sheet2.write(0,col,row0_data[col],row0_style)
for col in range(12):
    sheet2.write(1,col,rowcol_to_cell(1,col),reg_row_style)
for col in range(12):
    for row in range(2,80):
        sheet2.write(row,col,rowcol_to_cell(row,col),common_style)
w.save('panes.xls')
