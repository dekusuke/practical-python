import csv

def parse_csv(filename, select=None, types=None, has_headers=None, delimiter=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        if delimiter:            
            rows = csv.reader(f, delimiter=' ')
            records = []
            if has_headers:
                headers = next(rows)
                if select:
                    indices = [headers.index(colname) for colname in select]
                    headers = select
                else:
                    indices = []
                for row in rows:
                    if not row:
                        continue
                    if indices:
                        row = [row[index] for index in indices]
                        if types:
                            row = [func(val) for func, val in zip(types, row)]
                    record = dict(zip(headers, row))
                    records.append(record)
                
            else:
                for row in rows:
                    if not row:
                        continue
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                    record = tuple(row)
                    records.append(record)


    return records

        
