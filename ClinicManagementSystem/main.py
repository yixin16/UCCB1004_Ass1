from managerSystem import *
# when 'main.py' is running, call the 'run' function --->run function consists all the CRUD function
# start the patient management system
if __name__ == '__main__':
    patient_manager = PatientManager()
    patient_manager.run()