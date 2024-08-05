from patient import *
from treatment import *
import datetime
import sys
import time
import pandas as pd
from tkinter import messagebox
import openpyxl


class PatientManager(object):
    def __init__(self):
        self.patient_list = []   # to store the data of the patient and write it into excel
        self.treatment_list = []  # to store the data of treatment and write it into excel
        self.id_list = []
        self.name = []
        self.gender = []
        self.age = []
        self.address = []
        self.phone = []
        self.emergency = []
        self.emergency_contact = []
        self.allergic = []
        self.history = []
        # we assumed that not every patient will conduct the treatment
        self.date = []
        self.time = []
        self.treat_id = []
        self.treat_name = []
        self.sickness = []
        self.medicine = []
        self.total = []
        self.confirmation = []
        self.appointment = []
        self.remarks = []

    def __del__(self):
        print()

    # as the program entry, start the program and then implement function
    def run(self):
        messagebox.showinfo('Greeting', 'Welcome to use our program !!')
        self.restore_patient()
        self.restore_treatment()
        while True:
            # always call the save function so that every changes is recorded.
            print('*' * 50)
            print('|      Welcome to Zerwan Clinic Online System    |')
            print('*' * 50)
            print()
            print('-' * 50)
            print('Number\t\t\tTransaction Type')
            print('-' * 50)
            self.show_menu()   # call the menu function
            option = input('\nEnter transaction type: ')
            if option == '001':
                self.create_account()
            elif option == '002':
                self.edit_account()
            elif option == '003':
                self.delete_account()
            elif option == '004':
                self.treatment()
            elif option == '005':
                self.report()
            elif option == '006':
                self.edit_appointment_date()
            elif option == '007':
                #self.save_record_patient()
                #self.save_record_treatment()
                self.remove_duplicate()
                print("Thank you for using the Zerwan Clinic's online system. See You!")
                break
            else:
                print('Please enter the appropriate transaction type.\n\n\n')

    # show transaction menu
    @staticmethod
    def show_menu():
        transaction_dict = {
                '001': 'Create a new patient account',
                '002': 'Edit patient account',
                '003': 'Delete patient account',
                '004': 'Add appointment date and treatment detail. List of medicine have been prescribed',
                '005': 'Print Report',
                '006': 'Edit appointment date',
                '007': 'Exit system',
                }
        for key, value in transaction_dict.items():
            print(key, '----->', value)

    @staticmethod
    def progress_bar():   # a progress bar for every create, edit, etc...
        for i in range(1, 101):
            print("\r", end="")
            print("Working Progress: {}%: ".format(i), "▋" * (i // 2), end="")
            sys.stdout.flush()
            time.sleep(0.0005)

    def restore_patient(self):
        # append all the data from the excel in different list
        # after append the list, the data should be store in the patient object (combination of the data)
        # after grouped the data, it should be store in the 'self.patient_list' to make convenience in CRUD on the data.
        df1 = pd.read_excel('Clinic.xlsx', sheet_name='MasterList', header=2)
        self.id_list = df1['Patient ID'].to_list()
        self.name = df1['Patient Name'].to_list()
        self.gender = df1['Gender'].to_list()
        self.age = df1['Age'].to_list()
        self.address = df1['Address, city, state, and ZIP code'].to_list()
        self.phone = df1['Phone number'].to_list()
        self.emergency = df1['Name  of emergency contact'].to_list()
        self.emergency_contact = df1['Phone number of emergency contact'].to_list()
        self.allergic = df1['Allergic on medicine'].to_list()
        self.history = df1['History of sickness'].to_list()
        # return all records into the 'self.patient_list to make convenience to modify the information
        for i in range(len(self.id_list)):
            patient = Patient(self.id_list[i], self.name[i], self.gender[i], self.age[i], self.address[i],
                              self.phone[i], self.emergency[i], self.emergency_contact[i],
                              self.allergic[i], self.history[i])
            self.patient_list.append(patient)

    def restore_treatment(self):
        df = pd.read_excel('Clinic.xlsx', sheet_name='Treatment_Detail', header=2)
        self.date = df['Date'].to_list()
        self.time = df['Time'].to_list()
        self.treat_id = df['Patient ID'].to_list()
        self.treat_name = df['Patient Name'].to_list()
        self.sickness = df['Sickness'].to_list()
        self.medicine = df['Medicine'].to_list()
        self.total = df['Total'].to_list()
        self.confirmation = df['Next Appointment (Yes/No)'].to_list()
        self.appointment = df['Appointment Date'].to_list()
        self.remarks = df['Remarks'].to_list()
        for i in range(len(self.treat_id)):
            treatment_record = Treatment(self.date[i], self.time[i], self.treat_id[i], self.treat_name[i],
                                         self.sickness[i], self.medicine[i], self.total[i], self.confirmation[i],
                                         self.appointment[i], self.remarks[i])
            self.treatment_list.append(treatment_record)

    @staticmethod
    def remove_duplicate():
        data1 = pd.read_excel('Clinic.xlsx', sheet_name='MasterList', header=2)
        data2 = pd.read_excel('Clinic.xlsx', sheet_name='Treatment_Detail', header=2)
        data1.drop_duplicates()
        data2.drop_duplicates()

    def save_record_patient(self):    # write into excel
        wb = openpyxl.load_workbook('Clinic.xlsx')
        ws1 = wb['MasterList']
        new_patient_list = []
        for i in range(len(self.id_list)):
            new_patient_list.append([self.id_list[i], self.name[i], self.gender[i], self.age[i], self.address[i],
                                     self.phone[i], self.emergency[i], self.emergency_contact[i], self.allergic[i],
                                     self.history[i]])
        for i in new_patient_list:
            ws1.append(i)
        wb.save('Clinic.xlsx')

    def save_record_treatment(self):
        wb = openpyxl.load_workbook('Clinic.xlsx')
        ws2 = wb['Treatment_Detail']
        new_treatment_list = []
        for i in range(len(self.treat_id)):
            new_treatment_list.append([self.date[i], self.time[i], self.treat_id[i], self.treat_name[i],
                                       self.sickness[i], self.medicine[i], self.total[i], self.confirmation[i],
                                       self.appointment[i], self.remarks[i]])
        for i in new_treatment_list:
            ws2.append(i)
        wb.save('Clinic.xlsx')

    def create_account(self):   # 001
        try:
            patient_id = int(input('Enter a patient ID to create account: '))
        except Exception as e:
            print(e)
            try:
                patient_id = int(input('Enter a patient ID in NUMBER form only: '))
            except Exception as e:
                print(e)
                patient_id = int(input('Enter a patient ID in NUMBER form only: '))
        while patient_id in self.id_list:
            print('This ID is already occupied by others.Try again...')
            try:
                patient_id = int(input('Enter other patient ID to create account: '))
            except Exception as e:
                print(e)
                patient_id = int(input('Enter a patient ID in NUMBER form only: '))
        self.id_list.append(patient_id)
        name = input('Patient Name: ')
        while True:  # loop until the user key in the correct gender
            gender = input('Gender (M/F): ').upper()
            if gender in ['M', 'F']:
                break
            else:
                print('Please enter the correct gender format\nMale-->M\nFemale-->F')
        if gender == 'M':
            gender = 'Male'
        else:
            gender = 'Female'
        try:  # only give one chance of error for input of age
            age = int(input('Enter age: '))
        except Exception as e:
            print(e)
            print('Please enter proper age format.\n*Note: age should be integer.')
            age = int(input('Enter age: '))
        address = input('Address: ')
        city = input('City: ')
        state = input('State: ')
        zipcode = input('ZipCode: ')
        while len(zipcode) != 5:
            print('Please enter a proper zipcode. For example: 12345.')
            zipcode = input('ZipCode: ')
        full_add = address + ', ' + zipcode + ', ' + city + ', ' + state
        hp = input('Phone Number: ')
        print('*------------------------For Emergency use------------------------*')
        name_emergency = input('Enter emergency contact name>> ')
        hp_emergency = input('Enter emergency contact phone number>> ')
        allergic = input('What is your allergic on medicine: ')
        history = input('Sickness history: ')
        # call object from 'patient.py.'
        patient = Patient(patient_id, name, gender, age, full_add,
                          hp, name_emergency, hp_emergency, allergic, history)
        self.patient_list.append(patient)
        # show the list of information to the user
        print('Here is your account details. Please check it before you exit the system to store it. Thank you!!')
        print('-' * 60)
        print(f"ID: {patient_id}\nName: {name}\nGender: {gender}\nAge: {age}\nAddress: {full_add}\nContact No: {hp} "
              f"\nEmergency Contact Name: {name_emergency}\nEmergency Contact Name: {hp_emergency}"
              f"\nAllergic on medicine: {allergic}\nSickness History: {history}")
        print('-' * 60)
        self.progress_bar()
        print('\nThe account have been created.')
        print('-' * 60)

    def edit_account(self):   # 002
        try:
            edit_id = int(input("Enter Patient ID: "))
        except Exception as e:
            print(e)
            edit_id = int(input('Enter Patient ID in number form only: '))
        for i in self.patient_list:
            if edit_id == i.id:
                i.id = edit_id   # the patient's id could not be change (keep the ori one)
                i.name = input('Enter name: ')
                while True:  # loop until the user key in the correct gender
                    i.gender = input('Gender (M/F): ').upper()
                    if i.gender in ['M', 'F']:
                        break
                if i.gender == 'M':
                    i.gender = 'Male'
                else:
                    i.gender = 'F'
                    i.gender = 'Female'
                try:
                    i.age = int(input('Enter your current age: : '))
                except Exception as e:
                    print(e)
                    i.age = int(input('Enter your current age in NUMBER form only: : '))
                i.address = input('Address: ')
                i.city = input('City: ')
                i.state = input('State: ')
                try:
                    i.zipcode = input('ZipCode: ')
                except Exception as e:
                    print(e)
                # to make sure that the zipcode is in number form and 5 characters.
                i.zipcode = input('ZipCode: ')
                while len(i.zipcode) != 5:
                    print('Please enter a proper zipcode. For example: 12345.')
                    i.zipcode = input('ZipCode: ')
                # convert it into a combination of full address from (street + city + state + zipcode)
                i.full_add = i.address + ', ' + i.zipcode + ', ' + i.city + ', ' + i.state
                i.hp = input('Phone Number: ')
                print('*--------For Emergency use---------*')
                i.name_emergency = input('Enter emergency contact name>> ')
                i.hp_emergency = input('Enter emergency contact phone number>> ')
                i.allergic = input('What is your allergic on medicine: ')
                i.sickness = input('Sickness history: ')
                print('Updating your particular...Please wait for a while')
                self.progress_bar()
                print("Patient's information have been successfully updated.")
                print('Please check whether correct. If not, try to edit one more time.')
                # After successful, the information should be display for checking purpose
                print('#' * 50)
                print(f"ID: {i.id}\nName: {i.name}\nGender:{i.gender}\nAge: {i.age}\nAddress: {i.full_add}"
                      f"\nCity: {i.city}\nState: {i.state}\nZipCode: {i.zipcode}\nHP: {i.hp}")
                print('#' * 50)
                break
        else:
            print('This ID does not exist in our record.Try again...')

    def delete_account(self):    # 003
        ask_list = ['yes', 'no']
        ask = ''
        try:
            del_id = int(input('Enter the Patient ID that you want to delete: '))
        except Exception as e:
            print(e)
            del_id = int(input('ID only in the NUMBER form only>> '))
        for i in self.patient_list:
            if i.id == del_id:
                while ask not in ask_list:
                    ask = input('Do you really want to delete your account?(yes/no): ').lower()
                if ask == 'yes':
                    print('Deleting your account.....')
                    self.progress_bar()
                    print('\nYour account have been deleted successfully')
                    self.id_list.remove(del_id)
                    break
        else:
            print('#' * 70)
            print('We could not found your ID in our record')

    def treatment(self):   # 004
        t_date = datetime.date.today()
        t_time = datetime.datetime.now()
        # "%H:%M:%S"
        try:
            patient = int(input('Enter your ID: '))
        except Exception as e:
            print(e)
            patient = int(input('Enter your ID in a number form: '))
        while patient in self.treat_id:
            print('This ID is already occupied by others. Try another ID...')
            patient = int(input('Enter other ID: '))
        self.treat_id.append(patient)
        name = input('Patient Name: ')
        sick = input('Enter your sickness: ')
        medicine = input('Medicine: ')
        try:
            total = float(input('Total amount: RM'))
        except Exception as e:
            print(e)
            print('The Amount of Total should be in number forms only.')
            total = float(input('Total amount: RM'))
        option = ['yes', 'no']
        next_app = ''
        while next_app not in option:
            next_app = input('Do you want to make next appointment? (yes/no)>> ').lower()
        if next_app == 'yes':
            try:
                appointment_date = input('Enter the appointment date(in <dd/mm/yyyy>format): ')
                datetime.datetime.strptime(appointment_date, "%d/%m/%Y").date()
            except Exception as e:
                print(e)
                appointment_date = input('Enter the appointment date(in <dd/mm/yyyy>format): ')
                datetime.datetime.strptime(appointment_date, "%d/%m/%Y").date()
        else:
            appointment_date = 'None'
        remarks = input('Remarks: ')
        treatment_record = Treatment(t_date, t_time, patient, name, sick, medicine, total, next_app,
                                     appointment_date, remarks)
        self.treatment_list.append(treatment_record)
        print('Saving your treatment detail......Please wait patiently')
        self.progress_bar()
        print('\nYour treatment detail is saved successfully!!!')

    def report(self):  # 005
        df1 = pd.read_excel('Clinic.xlsx', sheet_name='MasterList', header=2)
        df2 = pd.read_excel('Clinic.xlsx', sheet_name='Treatment_Detail', header=2)
        try:
            patient_id = int(input("Enter Patient ID: "))
        except Exception as e:
            print(e)
            patient_id = int(input('Enter Patient ID in number form only: '))
        option_list = [1, 2]
        option = -1
        while option not in option_list:
            print('Which report do you want to print out?\n')
            print('1 --> Patient Particular Detail.')
            print('2 --> Treatment Detail of the patient.\n')
            option = int(input('>>>> '))
        if option == 1:
            if patient_id in self.id_list:
                for i in range(len(self.id_list)):
                    if patient_id == self.id_list[i]:
                        position_of_patient = i
                        print('Getting your information......')
                        self.progress_bar()
                        print('\n')
                        print('#' * 100)
                        print(df1.iloc[position_of_patient])
                        print('#' * 100)
                        print()
                        break
            else:
                print('This Patient is not found in our record.')
        else:
            if patient_id in self.treat_id:
                for i in range(len(self.treat_id)):
                    if patient_id == self.treat_id[i]:
                        position = i
                        print('Getting your information...Please wait patiently...')
                        self.progress_bar()
                        print('\n')
                        print('#' * 100)
                        print(df2.iloc[position])
                        print('#' * 100)
                        print()
            else:
                print('This patient is not found in our record')

    def edit_appointment_date(self):     # 006
        patient = int(input('Enter the patient id you want to add appointment date: '))
        for j in self.treatment_list:
            if j.id == patient:
                j.t_date = datetime.date.today()
                j.t_time = datetime.datetime.now()
                j.id = patient
                j.name = j.name
                j.sick = j.sick
                j.medicine = j.medicine
                j.total = j.total
                option_list = ['yes', 'no']
                option = ''
                while option not in option_list:
                    j.next_app = input('Do you want to add next appointment? (yes/no): ').lower()
                if j.next_app == 'yes':
                    # give 3 chances of key in error for the date
                    try:
                        j.appointment = input('Enter appointment date (in <dd/mm/yyyy>format): ')
                        datetime.datetime.strptime(j.appointment, '%d/%m/%Y').date()
                    except Exception as e:
                        print(e)
                        print('Please enter the proper format of the date')
                        print('eg: 30-Jun-2023 --> 30/06/2023')
                        j.appointment = input('Enter appointment date (in <dd/mm/yyyy>format): ')
                        datetime.datetime.strptime(j.appointment, '%d/%m/%Y').date()
                        try:
                            j.appointment = input('Enter appointment date (in <dd/mm/yyyy>format): ')
                            datetime.datetime.strptime(j.appointment, '%d/%m/%Y').date()
                        except Exception as e:
                            print(e)
                            print('Please enter the proper format of the date')
                            print('eg: 30-Jun-2023 --> 30/06/2023')
                            j.appointment = input('Enter appointment date (in <dd/mm/yyyy>format): ')
                            datetime.datetime.strptime(j.appointment, '%d/%m/%Y').date()
                else:
                    j.next_app = 'no'
                    j.appointment = '-'
                    break
                self.progress_bar()
                print("Patient's information have been successfully updated.")
                print('-' * 60)
                print('Please check whether correct. If not, try to edit one more time.')
                # After successful, the information should be display for checking purpose
                print(f"Latest edited Date: {j.t_date}\nLatest Edited Time: {j.t_time}\nPatient ID:{j.id}"
                      f"\nName: {j.name}\nSickness: {j.sick}\nMedicine Prescribed: {j.medicine}\nTotal: {j.total},"
                      f" \nNext Appointment: {j.next_app}, \nDate of Next Appointment: {j.appointment}")
                break
            else:
                print('Patient is not found in our record...')
