class Field(object):

    def __init__(self):
        self.field = []

    def print_field(self):
        self.field = []
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
Field().print_field()            