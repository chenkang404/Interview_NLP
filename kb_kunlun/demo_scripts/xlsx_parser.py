from typing_extensions import Literal
import xlrd





# 定义一个函数来获取单元格的值，如果是合并单元格，则返回合并单元格的起始单元格的值
def get_cell_value(sheet, row_index, col_index):
    merged_cells = sheet.merged_cells
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged_cells:
        if row_index >= rlow and row_index < rhigh and col_index >= clow and col_index < chigh:
            cell_value = sheet.cell_value(rlow, clow)
            break
    if cell_value is None:
        cell_value = sheet.cell_value(row_index, col_index)
    return cell_value



def read_xlsx(abs_path):
    print("处理xls文件名称：{}".format(abs_path))
    workbook = xlrd.open_workbook(filename=abs_path)
    names = workbook.sheet_names()
    # xls 最多解析3页

    
    for sheet_index, name in enumerate(names):
        table_row_list = []
        if name == "sheet1":
            continue
        print("解析处理页数：第{}页".format(sheet_index))
        table = workbook.sheet_by_name(sheet_name=name)
        # 获取行数
        rows = table.nrows
        # 获取列数
        cols = table.ncols
        
        # 获取合并单元格的信息

        # 循环获取每行的数据
        
        
        for row_index in range(rows):
            # table_row = {'疾病分类':'', '诊断疾病':'', '具体诊断或症状':'', '病情现状':'', '体检项目':'', 
                        # '项目结果':'', '重疾险':'', '防癌':'', '护理':'', '医疗险':'', '意外险':'', '备注':''}
            table_row = {}
            for col_index in range(cols):
                cell_value = get_cell_value(table, row_index, col_index)
                table_row[table.cell_value(0, col_index)] = cell_value.replace("\n","")
            table_row_list.append(table_row)
        with open(f'save_data/{name}.txt', 'w', encoding='utf-8') as file:
            # 遍历列表中的每个元素
            for item in table_row_list[1:]:
                # 将每个元素写入文件，并在每个元素后添加换行符
                file.write(str(item) + '\n\n')
    
    # return table_row_list
            # find_table_row = []
            # table_row_str = []
            # for cell_index, row_value in enumerate(table_row):
            #     data_type = row_types[cell_index]

if __name__ == '__main__':
    print("开始解析xlsx文件")
    # abs_path = '泌尿系统.xlsx'
    # abs_path = '测试用例糖尿病.xlsx'
    abs_path = './昆仑健康_核保指引_20230522.xlsx'

    table_row_list = read_xlsx(abs_path)

    # 打开一个文件用于写入，如果文件不存在则创建
    # with open('昆仑健康_核保指引.txt', 'w', encoding='utf-8') as file:
    #     # 遍历列表中的每个元素
    #     for item in table_row_list[1:]:
    #         # 将每个元素写入文件，并在每个元素后添加换行符
    #         file.write(str(item) + '\n\n')
    
    # print(table_row_list)