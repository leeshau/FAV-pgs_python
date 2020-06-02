import DataCarrier


class TXT_parser:
    def __init__(self):
        self.data = DataCarrier.DataCarrier()

    def parse_file(self, f):
        for i in f:
            line = i.split(";")
            if len(line) < 2:
                continue
            self.data.all_actions += 1
            if line[1] == "insert":
                self.data.insert_line(line)
                self.data.sign_in += 1
            elif line[1] == "delete":
                self.data.remove_line(line)
                self.data.delete += 1
                self.data.sign_in -= 1
            else:
                print("Wrong file structure at line " + i)
                exit(3)
