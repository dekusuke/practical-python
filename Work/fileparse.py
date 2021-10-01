import csv

def parse_csv(filename, select=None, types=None, has_headers=None, delimiter=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:                        
        rows = csv.reader(f)
        records = []            
        if has_headers:
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
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: invalid literal for int() with base 10: ''")
                    
            
        else:
            headers = next(rows)
            if select:
                raise RuntimeError("select argument requires column headers")                            
            else:                        
                for i, row in enumerate(rows, start=1):
                    try:
                        if not row:
                            continue
                        if types:
                            row = [func(val) for func, val in zip(types, row)]
                        record = tuple(row)
                        records.append(record)
                    except ValueError:
                        print(f"Row {i}: Couldn't convert {row}")
                        print(f"Row {i}: Reason invalid literal for int() with base 10: ''")
                        
        return records
