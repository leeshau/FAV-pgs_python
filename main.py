# TheMap -> workplace -> ZS/LS -> subject -> Pr/Cv -> action_id -> student
import sys
import filecheck
import stats

format = filecheck.check_input()
f = open(sys.argv[2], 'r')
if(format == ".txt"):
    import txt_parser
    map = txt_parser.create_map(f)
    # print(map)
else:
    # TODO dodej xml parser
    a = 5
f.close()

print("Počet všech předzápisových akcí: " + str(stats.all_actions))
print("Počet zrušených akcí (delete): " + str(stats.delete))
print("Počet skutečně zapsaných akcí: " + str(stats.sign_in))
print("Počet studentů: " + str(stats.students))
print("Počet předmětů: " + str(stats.subjects))
print("Počet pracovišť: " + str(stats.workplaces))