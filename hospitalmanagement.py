from tkinter import*
from tkinter import ttk
 import random
 import time
 import datetime
 from tkinter import messagebox
 import mysql. connector


class Hospital:
     def _init_(self, root):
         self.root=root
         self.root. title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

self.Nameoftablets=StringVar()
self.ref=StringVar()
self.Dose=StringVar()
self.Numberoftablets=StringVar()
self.Lot=StringVar()
self.Issuesdate=StringVar()
self.ExpDate=StringVar()
self.DailyDose=StringVar()
self.SideEfect=StringVar()
self.FurtherInformation=StringVar()
self.storageAdvice=StringVar()
self.DrivingUsingMachine=StringVar()
self.HowToUseMedication=StringVar()
self.PatientId=StringVar()
self.DateOfBirth=StringVar()
self.PatientAddress=StringVar()

lbltitle=Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", ,fg="red", ,bg="white", ,font=("time new roman",50,"bold"))
lbltitle.pack(side=TOP,fill=x)

#=============================Dataframe=============================
Dataframe=Frame(self.root,bd=20,relief=RIDGE)
Dataframe.place(x=0,y=130,width=1530,height=400)


Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                  font=("times new roman",12,"bold"),text="patient Information")
Dataframe.place(x=0,y=5,width=980,height=350)

Dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                    font=("times new roman",12,"bold"),text="Prescription")
DataframeRight.place(x=990,y=5,width=460,height=350) 

#===================== buttons frame================================


Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
Buttonframe.place(x=0,y=530,width=1530,height=70)


#===================== Details frame================================


Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
Detailsframe.place(x=0,y=600,width=1530,height=190)

#=========================Dataframeleft==================================

lblNameTablet=Label(DataframeLeft,font=("arial",12,"bold"),text="Name of Tablet",padx=2,pady=6)
lblNameTablet.grid(row=0,column=0,sticky=w)

comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),
                                                                        width=33)
comNametablet["values"]=("Nice","Corona Vacacine”, “Acetaminophen”, "Adderall", “Amlodipine”,"Ativan")
comNameTablet.current(0)
comNameTablet.grid(row=0,column=1)

lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
lblref.grid(row=1,column=0,sticky=w)
txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
txtref.grid(row=1,column=1)

lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose",padx=2,pady=4)
lblDose.grid(row=2,column=0,sticky=w)
txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
txtDose.grid(row=2,column=1)

lblNooftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets",padx=2,pady=6)
lblNooftablets.grid(row=3,column=0,sticky=w)
txtNooftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NoOfTablets,width=35)
txtNooftablets.grid(row=3,column=1)

lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
lblLot.grid(row=4,column=0,sticky=w)
txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
txtLot.grid(row=4,column=1)

lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="issueDate",padx=2,pady=6)
lblissueDate.grid(row=5,column=0,sticky=w)
txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.IssueDate,width=35)
txtissueDate.grid(row=5,column=1)

lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="ExpDate:",padx=2,pady=6)
lblExpDate.grid(row=6,column=0,sticky=w)
txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
txtExpDate.grid(row=6,column=1)

lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="DailyDose:",padx=2,pady=4)
lblDailyDose.grid(row=7,column=0,sticky=w)
txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
txtDailyDose.grid(row=7,column=1)

lblSideEffect =Label(DataframeLeft,font=("arial",12,"bold"),text="SideEffect:",padx=2,pady=6)
lblSideEffect.grid(row=8,column=0,sticky=w)
txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.SideEffect,width=35)
txtSideEffect.grid(row=8,column=1)

lblFurtherinfo =Label(DataframeLeft,font=("arial",12,"bold"),text="Furtherinfo:",padx=2)
lblFurtherinfo.grid(row=0,column=2,sticky=w)
txtFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Furtherinfo,width=35)
txtFurtherinfo.grid(row=0,column=3)

lblBloodPressure =Label(DataframeLeft,font=("arial",12,"bold"),text="BloodPressure:",padx=2,pady=6)
lblBloodPressure.grid(row=1,column=2,sticky=w)
txtBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.BloodPressure,width=35)
txtBloodPressure.grid(row=1,column=3)

lblStorage =Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
lblStorage.grid(row=2,column=2,sticky=w)
txtStorage=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
txtStorage.grid(row=2,column=3)

lblMedicine =Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
lblMedicine.grid(row=3,column=2,sticky=w)
txtMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Medication,width=35)
txtMedicine.grid(row=3,column=3,sticky=w)

lblPatientId =Label(DataframeLeft,font=("arial",12,"bold"),text="PatientId:",padx=2,pady=6)
lblPatientId.grid(row=4,column=2,sticky=w)
txtPatientId=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
txtPatientId.grid(row=4,column=3)

lblNhsNumber =Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
lblNhsNumber.grid(row=5,column=2,sticky=w)
txtNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.NHSNumber,width=35)
txtNhsNumber.grid(row=5,column=3)

lblPatientname =Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6)
lblPatientname.grid(row=6,column=2,sticky=w)
txtPatientname=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
txtPatientname.grid(row=6,column=3)

lblDateofBirth =Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth",padx=2,pady=6)
lblDateofBirth.grid(row=7,column=2,sticky=w)
txtDateofBirth=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
txtDateofBirth.grid(row=7,column=3)

lblPatientAddress =Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
lblPatientAddress.grid(row=8,column=2,sticky=w)
txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
txtPatientAddress.grid(row=8,column=3)


#====================== DataFrameRight======================================
self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
self.txtPrescription.grid(row=0,column=0)

#======================Buttons=================================================

btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnPrescription.grid(row=0,column=0)

btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnPrescriptionData.grid(row=0,column=1)

btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnUpdate.grid(row=0,column=2)

btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnDelete.grid(row=0,column=3)

btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnClear.grid(row=0,column=4)

btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnExit.grid(row=0,column=5)

#====================================Table======================================
#=======================================Scrollbar=======================
scroll_x=ttk.Scrollbar(Detailsframe,orient= HORIZONTAL)
scroll_y=ttk.Scrollbar(Detailsframe,orient= VERTICAL)
self.hospital_table=ttk.Treeview(FrameDetails,coiumn=("nameoftable","ref","dose","nooftablets","lot","issuedate,","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack=(side=BOTTOM,fill=X)
scroll_y.pack=(side=BOTTOM,fill=Y)

scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

self.hospital_table.heading("nameoftable",text="Nameof Table")
self.hospital_table.heading("ref",text="Reference No")
self.hospital_table.heading("dose",text="Dose")
self.hospital_table.heading("nameoftablets",text="Nameof Tablets")
self.hospital_table.heading("lot",text="Lot")
self.hospital_table.heading("issuedate",text="Issue Date")
self.hospital_table.heading("expdate",text="Exp Date")
self.hospital_table.heading("dailydose",text="Daily Date")
self.hospital_table.heading("storage",text="Storage")
self.hospital_table.heading("nhsnumber",text="NHS Number")
self.hospital_table.heading("pname",text="Patient Name")
self.hospital_table.heading("dob",text="DOB")
self.hospital_table.heading("address",text="Address")

self.hospital_table["show"]="headings"

self.hospital_table.column("nameoftable",width=100)
self.hospital_table.column("ref",width=100)
self.hospital_table.column("dose",width=100)
self.hospital_table.column("nameoftablets",width=100)
self.hospital_table.column("lot",width=100)
self.hospital_table.column("issuedate",width=100)
self.hospital_table.column("expdate",width=100)
self.hospital_table.column("dailydose",width=100)
self.hospital_table.column("storage",width=100)
self.hospital_table.column("nhsnumber",width=100)
self.hospital_table.column("pname",width=100)
self.hospital_table.column("dob",width=100)
self.hospital_table.column("address",width=100)

self.hospital_table.pack(fill=BOTH,expand=1)












root=Tk()
ob= Hospital(root)
root.mainloop()
