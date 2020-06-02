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

ws_final = {}
final_subjects = 0
for workplace in data.ws_list:
    res = 0
    for subject in data.ws_list[workplace]:
        res += data.ws_list[workplace][subject]
    ws_final[str(workplace)] = int(res)
    final_subjects += res

print("Počet všech předzápisových akcí: " + str(data.all_actions))
print("Počet zrušených akcí (delete): " + str(data.delete))
print("Počet skutečně zapsaných akcí: " + str(data.sign_in))
print("Počet studentů: " + str(data.students))
print("Počet předmětů: " + str(final_subjects))
print("Počet pracovišť: " + str(len(data.ws_list)))
i = 1
for workplace, ws_count in sorted(ws_final.items(), key=lambda x: (x[1], x[0])):
    print(str(i) + ". " + str(workplace) + ": " + str(ws_count))
    i += 1