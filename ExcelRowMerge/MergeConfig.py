# Available values for 'WhichValue' properties: ['FirstValue', 'LastValue', 'Biggest', 'Smallest', 'Empty', 'Average']
'''
    Empty, FirstValue, LastValue 通用
    CheckBox:
        Data示例: TRUE, FALSE, 1, 0, YES, NO
        WhichValue 限制: 'Biggest', 'Smallest'
    Date:
        Date示例: 2020-02-02 只接受YYYY-MM-DD格式
        WhichValue 限制: 'Biggest', 'Smallest'
    Number:
        Date示例: 123456
        WhichValue 限制: 'Biggest', 'Smallest', 'Average': todo
    All:
        Value示例: whatever you want
        WhichValue 限制: 'Empty', 'FirstValue', 'LastValue'
    ---------------------------------------------------------------------------------------
    todo:
        Average 这个类型没做. 看心情....
        Empty 感觉没必要...手动打开Excel把整列清空就行...
'''

RowMergeMap = {
    'KeyFields': ['Name'],

    'FieldMap': {
        'Default': {
            'FieldType': 'All',
            'WhichValue': 'FirstValue'
        },
        'Showroom_Visit_Lead__c': {
            'FieldType': 'CheckBox',
            'WhichValue': 'Biggest'
        },
        'Showroom_Visit_Date__c': {
            'FieldType': 'Date',
            'WhichValue': 'Biggest'
        },
        'Total_Order_Taken__c': {
            'FieldType': 'CheckBox',
            'WhichValue': 'Biggest'
        },
        'Order_Date__c': {
            'FieldType': 'Date',
            'WhichValue': 'Biggest'
        },
        'Total_Test_Drives_Taken__c': {
            'FieldType': 'CheckBox',
            'WhichValue': 'Biggest'
        },
        'Last_TD_Date__c': {
            'FieldType': 'Date',
            'WhichValue': 'Biggest'
        },
        'Total_Handover__c': {
            'FieldType': 'CheckBox',
            'WhichValue': 'Biggest'
        },
        'Handover_Date__c': {
            'FieldType': 'Date',
            'WhichValue': 'Biggest'
        }
    },

    'DataPreConvertMap': {
        'TRUE': 1,
        'FALSE': 0,
        '1': 1,
        '0': 0,
        'YES': 1,
        'NO': 0,
        True: 1,
        False: 0
    }
}
