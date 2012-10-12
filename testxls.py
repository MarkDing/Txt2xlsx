#!python
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter

from openpyxl.cell import get_column_letter
from openpyxl import style
from openpyxl.style import Color, Fill

row1_data = [
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

reg_data = []

tmp = ['SPI','','','','','','','','','','',
       'Enhanced Serial Peripheral Interface',
       2]
reg_data.append(tmp)
tmp = ['','SPI0CFG','0x00','','','','','','','','SPI0 Configuration',
       '',
       3]
reg_data.append(tmp)

tmp = ['','','','0','RXBMT','R','1','','','','Receive Buffer Empty (valid in slave mode only)',
       'This bit will be set to logic 1 when the receive buffer has been read and contains no new information. If there is new information available in the receive buffer that has not been read, this bit will return to logic 0. RXBMT = 1 when in Master Mode.',
       4]
reg_data.append(tmp)
tmp = ['','','','1','SRMT','R','1','','','','Shift Register Empty (valid in slave mode only)',
       'This bit will be set to logic 1 when all data has been transferred in/out of the shift register, and there is no new information available to read from the transmit buffer or write to the receive buffer. It returns to logic 0 when a data byte is transferred to the shift register from the transmit buffer or by a transition on SCK. SRMT = 1 when in Master Mode',
       5]
reg_data.append(tmp)
tmp = ['','SPI0CN','0x01','','','','','','','','SPI0 Control',
       '',
       6]
reg_data.append(tmp)

tmp = ['','','','0','RXBMT','R','1','','','','Receive Buffer Empty (valid in slave mode only)',
       'This bit will be set to logic 1 when the receive buffer has been read and contains no new information. If there is new information available in the receive buffer that has not been read, this bit will return to logic 0. RXBMT = 1 when in Master Mode.',
       7]
reg_data.append(tmp)
tmp = ['','','','1','SRMT','R','1','','','','Shift Register Empty (valid in slave mode only)',
       'This bit will be set to logic 1 when all data has been transferred in/out of the shift register, and there is no new information available to read from the transmit buffer or write to the receive buffer. It returns to logic 0 when a data byte is transferred to the shift register from the transmit buffer or by a transition on SCK. SRMT = 1 when in Master Mode',
       8]
reg_data.append(tmp)
tmp = ['','','','','','','','FIRST_EDGE','0','','',
       'Data centered on first edge of SCK period',
       9]
reg_data.append(tmp)

def write_row(row_data):
    row = row_data[-1]
    high_light = 0
    if row_data[1] != '':  # register name field
        high_light = 1
    for i in range(0,len(row_data)-1):
        col = get_column_letter(i+1)
        if high_light == 1:
            ws.cell('%s%s'%(col, row)).style.fill.fill_type = Fill.FILL_SOLID
            ws.cell('%s%s'%(col, row)).style.fill.start_color.index = Color.YELLOW
        ws.cell('%s%s'%(col, row)).value = row_data[i]
            
    
def write_regs(reg):
    # write first line
    for col_idx in range(0, len(row1_data)):
        col = get_column_letter(col_idx+1)
        ws.cell('%s%s'%(col, 1)).value = row1_data[col_idx]
        ws.cell('%s%s'%(col, 1)).style.font.bold = True
    for i in range(0,len(reg)):
        write_row(reg[i])

    

wb = Workbook()

dest_filename = r'empty_book.xlsx'

ws = wb.worksheets[0]

ws.title = "Base_alias"
ws._freeze_panes = 'A2'


write_regs(reg_data)

ws = wb.create_sheet()
ws.title = 'version'
ws.cell('F5').value = 3.14

wb.save(filename = dest_filename)


# Row 1
#for col_idx in range(1, 13):
#    col = get_column_letter(col_idx)
#    ws.cell('%s%s'%(col, 1)).value = row1_data[col_idx - 1]
#    ws.cell('%s%s'%(col, 1)).style.font.bold = True

# Register name row
#for col_idx in range(1, 13):
#    col = get_column_letter(col_idx)
#    ws.cell('%s%s'%(col, 2)).value = '%s%s' % (col, 2)
#    ws.cell('%s%s'%(col, 2)).style.fill.fill_type = Fill.FILL_SOLID
#    ws.cell('%s%s'%(col, 2)).style.fill.start_color.index = Color.YELLOW
    
# common row
#for col_idx in range(1, 13):
#    col = get_column_letter(col_idx)
#    print('col=%s'%col)
#    for row in range(3, 60):
#        ws.cell('%s%s'%(col, row)).value = '%s%s' % (col, row)
