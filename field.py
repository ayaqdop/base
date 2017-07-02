import console

class Field:

    def __init__(self):
        self.field = self.prepare_field()
        self.console = console.Console()

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
        result = ""
        for row in self.field:
            for item in row:
                result += "|"
                if item is None:
                    result += "  "
                else:
                    result += self.console.color(str(item).ljust(2), console.CYAN)
            result += "|\n" + (len(row) * 3 * "-")  + "-\n"
        print(result)
