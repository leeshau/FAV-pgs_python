def contains_student(subject_shortcut, student):
    """Checks if the current subject has the student in parameter signed in."""
    if subject_shortcut.__contains__('Cv'):
        for action_id_shortcut in subject_shortcut['Cv']:
            if action_id_shortcut.__contains__(student):
                return True
    if subject_shortcut.__contains__('Př'):
        for action_id_shortcut in subject_shortcut['Př']:
            if action_id_shortcut.__contains__(student):
                return True
    return False


class DataCarrier:
    def __init__(self):
        self.the_map = {}
        self.all_actions = 0
        self.delete = 0
        self.sign_in = 0
        self.students = 0
        self.subjects = 0
        self.workplaces = 0
        self.ws_list = {}
        self.student_list = {}

    def insert_line(self, line):
        """Inserts new data from line to the_map."""
        workplace = line[3]
        zsls = line[6]
        subject = line[4]
        prcv = line[5]
        action_id = line[2]
        student = line[0]

        skip = False
        if not self.the_map.__contains__(workplace):
            self.the_map[workplace] = {}
            self.workplaces += 1
            skip = True  # if map doesn't contain this workplace it won't contain the zsls, subject and so on, so we don't need to check that

        if skip or not self.the_map[workplace].__contains__(zsls):
            self.the_map[workplace][zsls] = {}
            skip = True

        if skip or not self.the_map[workplace][zsls].__contains__(subject):
            self.the_map[workplace][zsls][subject] = {}
            self.subjects += 1
            skip = True

        if skip or not self.the_map[workplace][zsls][subject].__contains__(prcv):
            self.the_map[workplace][zsls][subject][prcv] = {}
            skip = True

        if skip or not self.the_map[workplace][zsls][subject][prcv].__contains__(action_id):
            self.the_map[workplace][zsls][subject][prcv][action_id] = {}

        if skip or not self.the_map[workplace][zsls][subject][prcv][action_id].__contains__(student):
            """Here the student is signed in."""
            self.the_map[workplace][zsls][subject][prcv][action_id][student] = ""

            if not self.ws_list.__contains__(workplace):
                self.ws_list[workplace] = {}
            if not self.ws_list[workplace].__contains__(subject):
                self.ws_list[workplace][subject] = 1
            elif not contains_student(self.the_map[workplace][zsls][subject], student):
                self.ws_list[workplace][subject] += 1
            """Increasing student's subject count by one."""
            if self.student_list.__contains__(student):
                self.student_list[student] += 1
            else:
                self.student_list[student] = 1
        else:
            print("The student " + str(student) + " is trying to sing in twice to the action : " + str(action_id) + " .")

    def remove_line(self, line):
        """Removes data from the_map due to the remove line in the parameters."""
        workplace = line[3]
        zsls = line[6]
        subject = line[4]
        prcv = line[5]
        action_id = line[2]
        student = line[0]
        if self.the_map[workplace][zsls][subject][prcv][action_id].__contains__(student):
            del self.the_map[workplace][zsls][subject][prcv][action_id][student]
            if not contains_student(self.the_map[workplace][zsls][subject], student) and self.ws_list.__contains__(
                    workplace) and self.ws_list[workplace].__contains__(subject):
                self.ws_list[workplace][subject] -= 1
                if self.ws_list[workplace][subject] == 0:
                    del self.ws_list[workplace][subject]
            if self.student_list.__contains__(student):
                self.student_list[student] -= 1
                if self.student_list[student] == 0:
                    del self.student_list[student]
        else:
            print("Student " + student + " jde do minusu v delete.")
            exit(3)

        if self.ws_list.__contains__(workplace):
            if self.ws_list[workplace].__contains__(subject):
                self.ws_list[workplace][subject] -= 1
                if self.ws_list[workplace][subject] == 0:
                    del self.ws_list[workplace][subject]
            if len(self.ws_list[workplace]) == 0:
                del self.ws_list[workplace]