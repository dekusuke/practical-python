class TextTableFormatter:
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

        




    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()



class CSVTableFormatter:

    def headings(self, headers):
        print(','.join(headers))


    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter:

    def headings(self, headers):
        print('<tr><th>', end='')
        print('</th><th>'.join(headers), end='')
        print('</th></tr>')



    def row(self, rowdata):
        print('<td><td>', end='')
        print('</td><td>'.join(rowdata), end='')
        print('</td></td>')

class FormatError(Exception):
    pass

def create_formatter(name):

    
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(objects, columns, formatter):

        formatter.headings(columns)
        for data in objects:
            formatter.row(str(getattr(data, what)) for what in columns)
