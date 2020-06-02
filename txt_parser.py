import DataCarrier


# TheMap -> workplace -> ZS/LS -> subject -> Pr/Cv -> action_id -> student
def parse_file(f, data):
    for i in f:
        line = i.split(";")
        if line[0] == "###\n":
            break
        if len(line) < 2:
            continue
        data.all_actions += 1
        if line[1] == "insert":
            data.insert_line(line)
            data.sign_in += 1
        elif line[1] == "delete":
            data.remove_line(line)
            data.delete += 1
            data.sign_in -= 1
        else:
            print("Wrong file structure at line " + i)
            exit(3)
    data.students = len(data.student_list)
