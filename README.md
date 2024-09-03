# JSON generator for configuration of the plc's dbs.

Install dependency:
```
pip install fpdf2
```

This program generate a JSON file which contain the distribution of the dbs of a plc.
The input of the program are csv files that containt the name, type and offset of the differents values of the db.
The name of the csv file must be the name of the db and the number of the db. Such as that: "NameOfDB[DB3]"

## Example of input file:
```csv
,Value1,Bool,0.0
,Value2,Bool,0.1
,Value3,Real,2.0
,Value4,Bool,4.0

```

The output file has the following structure:
``` python
    {
    "DB3":[
        {
            "Name": "Name",
            "DataType": "Type" ,
            "Offset": 0.0
        },
        {
            "Name": "Name",
            "DataType": "Type" ,
            "Offset": 0.0
        }
        .
        .
        .
        ],
    "DB4":[
        {
            "Name": "Name",
            "DataType": "Type" ,
            "Offset": 0.0
        },
        {
            "Name": "Name",
            "DataType": "Type" ,
            "Offset": 0.0
        }
        .
        .
        .
        .
        ]
        .
        .
        . 
    }
```