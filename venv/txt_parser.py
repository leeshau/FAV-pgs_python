from collections import defaultdict
import stats
# TheMap -> workplace -> ZS/LS -> subject -> Pr/Cv -> action_id -> student
map = {}
student_list = {}

# basically works like put method in java HashMap
# def set_key(dictionary, key, value):
#     if key not in dictionary:
#         dictionary[key] = value
#     elif type(dictionary[key]) == list and value not in dictionary[key]:
#         dictionary[key].append(value)
#     elif value not in dictionary[key]:
#         dictionary[key] = [dictionary[key], value]

def insert_line(line):
    workplace = line[3]
    zsls = line[6]
    subject = line[4]
    prcv = line[5]
    action_id = line[2]
    student = line[0]

    skip = False
    if not map.__contains__(workplace):
        map[workplace] = {}
        stats.workplaces += 1
        skip = True #if map doesn't contain this workplace it won't contain the zsls, subject and so on, so we don't need to check that

    if skip == True or (not map[workplace].__contains__(zsls)):
        map[workplace][zsls] = {}
        skip = True

    if skip == True or (not map[workplace][zsls].__contains__(subject)):
        map[workplace][zsls][subject] = {}
        stats.subjects += 1
        skip = True

    if skip == True or (not map[workplace][zsls][subject].__contains__(prcv)):
        map[workplace][zsls][subject][prcv] = {}
        skip = True

    if skip == True or (not map[workplace][zsls][subject][prcv].__contains__(action_id)):
        map[workplace][zsls][subject][prcv][action_id] = {}

    # if not map[workplace][zsls][subject][prcv][action_id].__contains__(student):
    map[workplace][zsls][subject][prcv][action_id][student] = {}
    if student_list.__contains__(student):
        student_list[student] += 1
    else:
        student_list[student] = 1


def remove_line(line):
    workplace = line[3]
    zsls = line[6]
    subject = line[4]
    prcv = line[5]
    action_id = line[2]
    student = line[0]
    if map[workplace][zsls][subject][prcv][action_id].__contains__(student):
        del map[workplace][zsls][subject][prcv][action_id][student]
    if student_list.__contains__(student):
        student_list[student] -= 1
        if student_list[student] == 0:
            del student_list[student]
    else:
        print("Student " + student + " jde do minusu v delete.")

def create_map(f):
    for i in f:
        stats.all_actions += 1
        line = i.split(";")
        if(line[1] == "insert"):
            insert_line(line)
            stats.sign_in += 1
        elif(line[1] == "delete"):
            remove_line(line)
            stats.delete += 1
            stats.sign_in -= 1
        else:
            print("Wrong file structure at line " + i)
            exit(3)
    stats.students = len(student_list)
    return map