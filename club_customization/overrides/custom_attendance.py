import frappe
import datetime
from erpnext.hr.doctype.attendance.attendance import Attendance

class CustomAttendance(Attendance):

    def before_submit(self):
        if (self.in_time):
            in_time = str(self.in_time).split(' ')
            self.in_time_date = in_time[0]
            self.in_time_time = in_time[1][0:8]
        if (self.out_time):
            out_time = str(self.out_time).split(' ')
            self.out_time_date = out_time[0]
            self.out_time_time = out_time[1][0:8]

        if (self.working_hours):
            hours = int(self.working_hours)
            minutes = round((self.working_hours - hours) * 60)
            self.exact_working_hours = f"{hours}:{minutes}"
