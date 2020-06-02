def contains_student(subject_shortcut, student):
    """Checks if the student is signed in the current subject. Reading from the_map."""
    if subject_shortcut.__contains__('Cv'):
        for action_id in subject_shortcut['Cv']:
            if student in subject_shortcut['Cv'][action_id]:
                return True
    if subject_shortcut.__contains__('Př'):
        for action_id in subject_shortcut['Př']:
            if student in subject_shortcut['Př'][action_id]:
                return True
    return False


class DataCarrier:
    def __init__(self):
        self.the_map = {}
        self.all_actions = 0
        self.delete = 0
        self.sign_in = 0
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
        subject_ws_list = str(subject) + " " + str(zsls)
        skip = False
        if not self.the_map.__contains__(workplace):
            self.the_map[workplace] = {}
            skip = True  # if map doesn't contain this workplace it won't contain the zsls, subject and so on, so we don't need to check that

        if skip or not self.the_map[workplace].__contains__(zsls):
            self.the_map[workplace][zsls] = {}
            skip = True

        if skip or not self.the_map[workplace][zsls].__contains__(subject):
            self.the_map[workplace][zsls][subject] = {}
            skip = True

        if skip or not self.the_map[workplace][zsls][subject].__contains__(prcv):
            self.the_map[workplace][zsls][subject][prcv] = {}
            skip = True

        if skip or not self.the_map[workplace][zsls][subject][prcv].__contains__(action_id):
            self.the_map[workplace][zsls][subject][prcv][action_id] = {}

        if skip or not self.the_map[workplace][zsls][subject][prcv][action_id].__contains__(student):
            """Here the student is signed in."""
            contained_student_before_adding = contains_student(self.the_map[workplace][zsls][subject], student)
            self.the_map[workplace][zsls][subject][prcv][action_id][student] = ""

            if not self.ws_list.__contains__(workplace):
                self.ws_list[workplace] = {}
            if not self.ws_list[workplace].__contains__(subject_ws_list):
                self.ws_list[workplace][subject_ws_list] = 1
            elif not contained_student_before_adding:
                self.ws_list[workplace][subject_ws_list] += 1
            """Increasing student's subject count by one."""
            if self.student_list.__contains__(student):
                self.student_list[student] += 1
            else:
                self.student_list[student] = 1
        else:
            print("Student " + str(student) + " se pokouší dostat na akci " + str(action_id) + " podruhé. Zamítnuto.")

    def remove_line(self, line):
        """Removes data from the_map due to the remove line passed in the parameter."""
        workplace = line[3]
        zsls = line[6]
        subject = line[4]
        prcv = line[5]
        action_id = line[2]
        student = line[0]
        subject_ws_list = str(subject) + " " + str(zsls)
        if self.the_map[workplace][zsls][subject][prcv][action_id].__contains__(student):
            del self.the_map[workplace][zsls][subject][prcv][action_id][student]
            """Updating ws_list"""
            if not contains_student(self.the_map[workplace][zsls][subject], student) \
                    and self.ws_list.__contains__(workplace) \
                    and self.ws_list[workplace].__contains__(subject_ws_list):
                self.ws_list[workplace][subject_ws_list] -= 1
                if self.ws_list[workplace][subject_ws_list] == 0:
                    del self.ws_list[workplace][subject_ws_list]
            """Updating student_list"""
            if self.student_list.__contains__(student):
                self.student_list[student] -= 1
                if self.student_list[student] == 0:
                    del self.student_list[student]
        else:
            print("Student " + student + " jde do mínusu v delete. \nChyba I/O. Končím.")
            exit(3)

        if self.ws_list.__contains__(workplace):
            if self.ws_list[workplace].__contains__(subject):
                self.ws_list[workplace][subject] -= 1
                if self.ws_list[workplace][subject] == 0:
                    del self.ws_list[workplace][subject]
            if len(self.ws_list[workplace]) == 0:
                del self.ws_list[workplace]
