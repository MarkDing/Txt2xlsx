#!python
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter

from openpyxl.cell import get_column_letter
from openpyxl import style
from openpyxl.style import Color, Fill

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


wb = Workbook()

dest_filename = r'empty_book.xlsx'

ws = wb.worksheets[0]

ws.title = "Base_alias"
ws._freeze_panes = 'A2'

# Row 0
for col_idx in range(1, 13):
    col = get_column_letter(col_idx)
    ws.cell('%s%s'%(col, 1)).value = row0_data[col_idx - 1]
    ws.cell('%s%s'%(col, 1)).style.font.bold = True
    
# Register name row
for col_idx in range(1, 13):
    col = get_column_letter(col_idx)
    ws.cell('%s%s'%(col, 2)).value = '%s%s' % (col, 2)
    ws.cell('%s%s'%(col, 2)).style.fill.fill_type = Fill.FILL_SOLID
    ws.cell('%s%s'%(col, 2)).style.fill.start_color.index = Color.YELLOW
    
# common row
for col_idx in range(1, 13):
    col = get_column_letter(col_idx)
    print('col=%s'%col)
    for row in range(3, 60):
        ws.cell('%s%s'%(col, row)).value = '%s%s' % (col, row)



ws = wb.create_sheet()
ws.title = 'version'
ws.cell('F5').value = 3.14

wb.save(filename = dest_filename)
