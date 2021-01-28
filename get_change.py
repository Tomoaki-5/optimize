import subprocess as sp
import csv
import data
filename="result.csv"
bestfile="para_best.py"
save="save"
sr="/"
under="_"
cha="change"
evalue = 0
enumber = 0
#dataparamater
spacedensity_chr = "spacedensity"
intparamater_chr = "intparamater"
phasereverseparamater_chr = "phasereverseparamater"
duplicateparamater_chr = "duplicateparamater"
field_chr = "field"
digt_EMT_phase_chr = "digt_EMT_phase"
digt_EMT_intensity_chr = "digt_EMT_intensity"
improveparamater_chr = "improveparamater"


def setdat_chr(a1,a2):
    with open(a1) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        xxx = [line for line in lines_strip if a2 in line]
        return xxx[0]

filelist = setdat_chr(cha,data.paramatername).split()

implist=[]
impnumber_list=[]
for i in range(1,len(filelist)):
# paradata = pd.read_csv(filename)
# print(paradata)
    operationfile = data.operation+sr+save+under+str(i)+sr+filename
    #operationfile = filename
    # import numpy as np
    try: 
        cont=[]
        with open(operationfile)as f:
            for row in csv.reader(f):
                arr=row
                cont.append(arr)
    except FileNotFoundError :
        continue
    if data.paramatername == spacedensity_chr:
        impsingle=float(cont[5][1])
        implist.append(impsingle)
        impnumber_single=cont[9][2]
        impnumber_list.append(impnumber_single)
    if data.paramatername == intparamater_chr:
        impsingle=float(cont[5][1])
        implist.append(impsingle)
        impnumber_single=cont[9][2]
        impnumber_list.append(impnumber_single)
    if data.paramatername == phasereverseparamater_chr:
        impsingle=float(cont[5][1])
        implist.append(impsingle)
        impnumber_single=cont[9][2]
        impnumber_list.append(impnumber_single)
    if data.paramatername == duplicateparamater_chr:
        impsingle=float(cont[5][1])   
        implist.append(impsingle)
        impnumber_single=cont[9][2]
        impnumber_list.append(impnumber_single)
    if data.paramatername == digt_EMT_phase_chr:
        impsingle=float(cont[5][1])
        implist.append(impsingle) 
        impnumber_single=cont[9][2]
        impnumber_list.append(impnumber_single)
    if data.paramatername == digt_EMT_intensity_chr:
        impsingle=float(cont[5][1])
        implist.append(impsingle)
        impnumber_single=cont[9][2]
        impnumber_list.append(impnumber_single)

if data.paramatername == spacedensity_chr:
    evalue = max(implist)
    enumber = implist.index(max(implist))
if data.paramatername == intparamater_chr:
    evalue = max(implist)
    enumber = implist.index(max(implist))
if data.paramatername == phasereverseparamater_chr:
    evalue = max(implist)
    enumber = implist.index(max(implist))
if data.paramatername == duplicateparamater_chr:
    evalue = max(implist)
    enumber = implist.index(max(implist))
if data.paramatername == digt_EMT_phase_chr:
    evalue = max(implist)
    enumber = implist.index(max(implist))
if data.paramatername == digt_EMT_intensity_chr:
    evalue = max(implist)
    enumber = implist.index(max(implist))

parabestplace=data.current+sr+bestfile
f = open(parabestplace,'a')

f.write("{0} = {1}\n".format(data.paramatername,impnumber_list[enumber]))

f.close()
