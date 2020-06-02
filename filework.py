import sys


def check_input():
    """Checks if the arguments are right."""
    result = ""
    if sys.argv[1] != "-i" or sys.argv[3] != "-o":
        print("Špatný input, končím.")
        exit(1)
    for i in range(2, 5, 2):
        length = len(sys.argv[i])
        end = sys.argv[i][length - 4: length]
        if i == 2:
            result = end
        if end != ".txt" and end != ".xml":
            if i == 2:
                print("Špatné koncovky input souboru, musí být buď '.txt' nebo '.xml'. Končím.")
            else:
                print("Špatné koncovky output souboru, musí být '.txt'. Končím.")
            exit(2)
    return result


def export_file(data, filename):
    """
    Creates ws_final (workplace => number_of_studentsubjects) from ws_list.
    Then it exports the results to a file.
    """
    ws_final = {}
    final_subjects = 0
    for workplace in data.ws_list:
        res = 0
        for subject in data.ws_list[workplace]:
            res += data.ws_list[workplace][subject]
        ws_final[str(workplace)] = int(res)
        final_subjects += res

    try:
        out = open(filename, "w+")
        out.write("Počet všech předzápisových akcí: " + str(data.all_actions) + "\n")
        out.write("Počet zrušených akcí (delete): " + str(data.delete) + "\n")
        out.write("Počet skutečně zapsaných akcí: " + str(data.sign_in) + "\n")
        out.write("Počet studentů: " + str(len(data.student_list)) + "\n")
        out.write("Počet předmětů: " + str(final_subjects) + "\n")
        out.write("Počet pracovišť: " + str(len(data.ws_list)) + "\n")
        i = 1
        for workplace, ws_count in sorted(ws_final.items(), key=lambda x: (x[1], x[0])):
            out.write(str(i) + ". " + str(workplace) + ": " + str(ws_count) + "\n")
            i += 1
    except Exception:
        print("Chyba při zapisování do souboru. Končím.")
        sys.exit(4)
