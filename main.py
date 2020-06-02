# TheMap -> workplace -> ZS/LS -> subject -> Pr/Cv -> action_id -> student
import sys
import filework

if filework.check_input() == ".txt":
    import txt_parser
    parser = txt_parser.TXT_parser()
else:
    import xml_parser
    parser = xml_parser.XML_parser()

f = open(sys.argv[2], 'r')
# data = DataCarrier.DataCarrier()
parser.parse_file(f)
f.close()
filework.export_file(parser.data)
