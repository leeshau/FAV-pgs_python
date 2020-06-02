# TheMap -> workplace -> ZS/LS -> subject -> Pr/Cv -> action_id -> student
import sys
import filecheck
import DataCarrier

f = open(sys.argv[2], 'r')
data = DataCarrier.DataCarrier()
if filecheck.check_input() == ".txt":
    import txt_parser
    txt_parser.parse_file(f, data)
    # print(map)
else:
    # TODO dodej xml parser
    pass
f.close()

print("Počet všech předzápisových akcí: " + str(data.all_actions))
print("Počet zrušených akcí (delete): " + str(data.delete))
print("Počet skutečně zapsaných akcí: " + str(data.sign_in))
print("Počet studentů: " + str(data.students))
print("Počet předmětů: " + str(data.subjects))
print("Počet pracovišť: " + str(len(data.ws_list)))
for x in data.ws_list:
    res = 0
    for subject in data.ws_list[x]:
        res += data.ws_list[x][subject]
    # print(str(x) + ": " + str(len(stats.workplace_subject[x])))
    print(str(x) + ": " + str(res))