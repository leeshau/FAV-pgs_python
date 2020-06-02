import sys
import filework

print("Zdravím. Program spuštěn.")
if filework.check_input() == ".txt":
    import txt_parser
    parser = txt_parser.TXT_parser()
else:
    import xml_parser
    parser = xml_parser.XML_parser()

f = open(sys.argv[2], 'r')
parser.parse_file(f)
f.close()
filework.export_file(parser.data, sys.argv[4])
print("\nVše proběhlo v pořádku. Export hotový. \n\nMějte se.")