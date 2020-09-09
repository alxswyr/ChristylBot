class job:

    def __init__(self, teacher_name, teacher_title, report_to, start_date,
                 end_date, start_time, end_time, duration_name, location):
        self.teacher_name = teacher_name
        self.teacher_title = teacher_title
        self.report_to = report_to
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.duration_name = duration_name
        self.location = location

    def get_string_rep_of_job(self):
        return " | ".join([self.teacher_name, self.teacher_title, self.report_to, self.start_date + " - " + self.end_date,
                         self.start_time + " - " + self.end_time, self.duration_name, self.location])

