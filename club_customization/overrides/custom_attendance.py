import frappe
from erpnext.hr.doctype.attendance.attendance import Attendance

class CustomAttendance(Attendance):
    def before_submit(self):
        if(self.in_time):
            self.in_time_date, self.in_time_time  = self.in_time.split(' ')
        if(self.out_time):
            self.out_time_date, self.out_time_time = self.out_time.split(' ')

        if(self.working_hours):
            hours = int(self.working_hours)
            minutes = round((self.working_hours - hours) * 60)
            self.exact_working_hours= f"{hours}:{minutes}"