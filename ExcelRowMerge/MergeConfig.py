# Available values for 'WhichValue' properties: ['FirstValue', 'LastValue', 'Biggest', 'Smallest', 'Average']
'''
    FirstValue, LastValue 通用
    CheckBox:
        Data示例: TRUE, FALSE, 1, 0, YES, NO
        WhichValue Limit: 'Biggest', 'Smallest'
    Date:
        Date示例: 2020-02-02 只接受YYYY-MM-DD格式
        WhichValue Limit: 'Biggest', 'Smallest'
    Number:
        Number示例: 123456
        WhichValue Limit: 'Biggest', 'Smallest', 'Average': todo
    Text:
        Text示例: 'fsfsdf', '发生的发生', '23433434343'
        WhichValue Limit: 'OrderedList'
        OrderedList: ['2', '3', '4']   // Required for 'OrderedList' type only, omit this field if type is others.
        FieldName: columnName   // Required for 'OrderedList' type only, omit this field if type is others.
    All:
        Value示例: whatever you want
        WhichValue Limit: 'FirstValue', 'LastValue'
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
        },
        'StageName': {
            'FieldType': 'Text',
            'WhichValue': 'OrderedList',
            'OrderedList': ['Handover', 'Order Taken', 'Offer/Quotation'],
            'FieldName': 'StageName'
        },
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
