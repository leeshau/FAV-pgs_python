from xml.sax import handler, make_parser
import DataCarrier


class XML_parser(handler.ContentHandler):

    def __init__(self):
        super().__init__()
        self.data = DataCarrier.DataCarrier()
        self.content = ""
        self.student = ""
        self.insert_remove = ""
        self.action_id = ""
        self.workplace = ""
        self.get_subject = False
        self.subject = ""
        self.prcv = ""
        self.zsls = ""

    def parse_file(self, f):
        parser = make_parser()
        parser.setContentHandler(self)
        parser.parse(f)

    def startElement(self, name, attrs):
        if name == "actor":
            self.student = attrs["personalNumber"]
        elif name == "processedData":
            self.insert_remove = attrs["activity"]
        elif name == "timetableAction":
            self.action_id = attrs["tt:id"]
        elif name == "tt:subject":
            self.get_subject = True
            self.prcv = attrs["kind"]
        self.content = ""

    def endElement(self, name):
        if self.get_subject:
            self.subject = self.content
            self.get_subject = False
        elif name == "tt:term":
            self.zsls = self.content
        elif name == "tt:department":
            self.workplace = self.content
        elif name == "event":
            line = [self.student, self.insert_remove, self.action_id, self.workplace, self.subject, self.prcv,
                    self.zsls]
            self.data.all_actions += 1
            if self.insert_remove == "insert":
                self.data.insert_line(line)
                self.data.sign_in += 1
            elif self.insert_remove == "delete":
                self.data.remove_line(line)
                self.data.delete += 1
                self.data.sign_in -= 1
            else:
                print("Chyba I/O. Končím.")
                exit(3)

    def characters(self, content):
        self.content += content
