import csv

def parse_csv(file, select=None, types=None, has_headers=None, delimiter=None, silence_errors=None):
    '''
    Parse a CSV file into a list of records
    '''
    records = []            
    if has_headers:
        rows = csv.reader(file)
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        for i, row in enumerate(rows, start=1):
            try:
                if not row:
                    continue
                if indices:
                    row = [row[index] for index in indices]
                    if types:
                        row = [func(val) for func, val in zip(types, row)]                
                record = dict(zip(headers, row))
                records.append(record)                    
            except ValueError:
                if silence_errors:
                    continue
                else:                        
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: invalid literal for int() with base 10: ''")
                
        
    else:
        rows = csv.reader(file)
        if select:
            raise RuntimeError("select argument requires column headers")                            
        else:                        
            for i, row in enumerate(rows, start=1):
                try:
                    if not row:
                        continue
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                    
                    records.append(row)                        
                except ValueError:
                    if silence_errors:
                        continue
                    else:                            
                        print(f"Row {i}: Couldn't convert {row}")
                        print(f"Row {i}: Reason invalid literal for int() with base 10: ''")
        records = dict(records)
                                    
    return records

