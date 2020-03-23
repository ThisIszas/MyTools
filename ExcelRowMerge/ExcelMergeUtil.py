from ExcelRowMerge.MergeConfig import RowMergeMap
# import MergeConfig
from datetime import datetime

class ExcelMerge:
    def __init__(self, DataList: []):
        self.returnMap = {}
        self.DataList: [] = DataList
        self.configMap: {} = RowMergeMap

    def MergeDatas(self):
        for eachRow in self.DataList:
            currentRowKey = ''
            for eachKey in self.configMap.get('KeyFields'):
                currentRowKey += eachRow.get(eachKey)
            if not self.returnMap.__contains__(currentRowKey):  # If this key isn't in the return map, initiate it
                self.returnMap[currentRowKey] = {}              # with blank obj

            for fieldName in eachRow.keys():
                fieldConfig = {}
                if self.configMap.get('FieldMap').__contains__(fieldName):
                    # print(fieldName)
                    fieldConfig = self.configMap.get('FieldMap').get(fieldName)

                else:
                    # print('null defined', fieldName)
                    fieldConfig = self.configMap.get('FieldMap').get('Default')

                self.singleFieldMerge(fieldConfig, currentRowKey, eachRow.get(fieldName), fieldName)
        # print('35:',self.returnMap)
        return self.returnMap

    def singleFieldMerge(self, fieldCfg: {}, rowKey, value, fieldName):
        currentRow = self.returnMap.get(rowKey)
        fieldType = fieldCfg.get('FieldType')
        try:
            upperValue = value.upper()
        except Exception:
            # print(value)
            upperValue = value

        preParsedValue = value if not self.configMap.get('DataPreConvertMap').__contains__(upperValue) \
            else self.configMap.get('DataPreConvertMap').get(upperValue)
        # print(preParsedValue)

        if not currentRow.__contains__(fieldName):
            if fieldCfg.get('FieldType') == 'Date' and preParsedValue:
                try:
                    preParsedValue = self.parseDate(preParsedValue)
                except Exception:
                    print(fieldName, ', ', preParsedValue, ', ',value, 'rowKey')
                    quit()
            currentRow[fieldName] = preParsedValue

        if fieldCfg.get('WhichValue') == 'FirstValue' and preParsedValue:
            if not currentRow.get(fieldName):  # 存在已添加field, 但是value为none的情况
                currentRow[fieldName] = preParsedValue
            self.returnMap[rowKey] = currentRow
            return
        elif fieldCfg.get('WhichValue') == 'LastValue' and preParsedValue:
            currentRow[fieldName] = preParsedValue  # 只要value不为none直接覆盖
            self.returnMap[rowKey] = currentRow
            return

        if fieldType in ['CheckBox', 'Number']:
            isBigger = True if currentRow.get(fieldName) < preParsedValue else False
            if fieldCfg.get('WhichValue') == 'Biggest' and isBigger:
                currentRow[fieldName] = preParsedValue
            elif fieldCfg.get('WhichValue') == 'Smallest' and not isBigger:
                currentRow[fieldName] = preParsedValue

        elif fieldType == 'Date':
            # try:
            dateValue = preParsedValue if not isinstance(preParsedValue, str) else self.parseDate(preParsedValue)
            isBigger = False
            if dateValue:
                if not currentRow.get(fieldName):
                    isBigger = True
                else:
                    isBigger = True if currentRow.get(fieldName) < dateValue else False

            if fieldCfg.get('WhichValue') == 'Biggest' and isBigger:
                currentRow[fieldName] = dateValue
            elif fieldCfg.get('WhichValue') == 'Smallest' and not isBigger:
                currentRow[fieldName] = dateValue

        self.returnMap[rowKey] = currentRow

    @staticmethod
    def parseDate(value):
        dateValue = None
        if len(value) <= 10 and value:
            dateValue = datetime.strptime(value, '%Y-%m-%d')
        elif value:
            dateValue = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return dateValue
#
# DataList = [
#     {'Mobile': '123', 'Show Room Traffic': 'true', 'Show Room Date': '2020-03-01', 'Other': 'other1'},
#     {'Mobile': '123', 'Show Room Traffic': 'true', 'Show Room Date': '2020-03-02', 'Other': 'other2'},
#     {'Mobile': '123', 'Show Room Traffic': 'false', 'Show Room Date': ''},
#     {'Mobile': '1234', 'Show Room Traffic': 'true', 'Show Room Date': '2020-04-05'},
#     {'Mobile': '1234', 'Show Room Traffic': 'true', 'Show Room Date': '2020-03-01'},
#     {'Mobile': '123', 'Show Room Traffic': 'false', 'Show Room Date': ''},
#     {'Mobile': '12345', 'Show Room Traffic': 'fasle', 'Show Room Date': ''},
#     {'Mobile': '12345', 'Show Room Traffic': 'true', 'Show Room Date': '2020-03-05'},
#     {'Mobile': '123456', 'Show Room Traffic': 'true', 'Show Room Date': '2020-06-08'},
#     {'Mobile': '1234567', 'Show Room Traffic': 'false', 'Show Room Date': ''},
#     {'Mobile': '1235555', 'Show Room Traffic': 'TRUE', 'Show Room Date': '2020-04-07'},
#     {'Mobile': '1235555', 'Show Room Traffic': 'TRUE', 'Show Room Date': '2020-04-08'},
#     {'Mobile': '1235555', 'Show Room Traffic': 'FALSE', 'Show Room Date': ''},
#     {'Mobile': '12355558', 'Show Room Traffic': 'FALSE', 'Show Room Date': ''},
# ]
#
# # MergeDataObj = {
# #     'DataList': DataList
# # }
# # # print(MergeDataObj)
# ExcelMerge(DataList)
