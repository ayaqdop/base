class Field:

    def __init__(self):
        self.field = self.prepare_field()

    def prepare_field(self):
        result = self.field_numbers()
        self.field_letters(result)
        self.field_clean_up(result)
        return result

    def field_clean_up(self, field):
        for i in range (1,17):
            for j in range(1,25):
                field[i][j] = None
        return field

    def field_letters(self, field):
        for i, c in enumerate(" abcdefghijklmnop "):
            field[i][0] = c
            field[i][25] = c
        return field

    def field_numbers(self):
        result = []
        for i in range(18):
            row = []
            for j in range(26):
                row.append(j)
            result.append(row)
        return result

    def print_field(self):
        field_len = []
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        for i in range(16):
            for row in range(24):
                field_len.append(" ")
            self.field.append(field_len)
            field_len = []

        print ('    0','  1','  2','  3','  4','  5','  6','  7','  8','  9','  10',' 11',' 12',' 13',' 14',' 15',' 16',' 17',' 18',' 19',' 20',' 21',' 22',' 23')
        print (' '+'-'*98)
        for a,d in zip(self.field,alp):
            print (d,'|', end = ' ')
            for b in range(24):
                print (a[b], '|', end = ' ')
            print ('\n','-'*98)
