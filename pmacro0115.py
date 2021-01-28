import subprocess as sp
import asyncio
#commandcharacter
macrofile="/home/Osumi/macropython/"
MASK="MASK"
vA="3D_Py_A.py"
vD="3D_Py_D.py"
x1="BION-A"
x2="BION-D"
cha="change"
imp="improve.py"
impnext="improvenext.py"
arrpy="arrraw.py"
bionpy="bion.py"
datapy="data.py"
arrraw="np_save_first"
save="save"
np="np"
npy=".npy"
result="result"
csv=".csv"
point="point"
seed="seed"
slid="sild"
html=".html"
mplotmtv="mplotmtv"
py=".py"
dq='"'
space=' '
under="_"
sr="/"
pm_go="pm_go.sh"
getpy="get_change.py"
readyimp="ready_imp.py"
improvedirectory="improve"
pm_imp="pm_imp.sh"
bestpy="para_best.py"
best_d_py="best_directory.py"
comparepy="para_compare.py"
f2pyfile="f2py_module.cpython-38-x86_64-linux-gnu.so"
# interpolatepy="interpolate.py"
#dataparamater
defocus_chr = "defocus"
ntfftx_chr = "ntfftx"
ntffty_chr = "ntffty"
bion_focus_chr = "bion_focus"
improveth_plus_chr = "improveth_plus"
improveth_minus_chr = "improveth_minus"
improvefeedback_plus_chr = "improvefeedback_plus"
improvefeedback_minus_chr = "improvefeedback_minus"
spacedensity_chr = "spacedensity"
intparamater_chr = "intparamater"
phasereverseparamater_chr = "phasereverseparamater"
duplicateparamater_chr = "duplicateparamater"
field_chr = "field"
digt_EMT_phase_chr = "digt_EMT_phase"
digt_EMT_intensity_chr = "digt_EMT_intensity"
improveparamater_chr = "improveparamater"
size_chr="size"
interpolatenumber_chr="interpolatenumber"


async def bashwait(num,asylist):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None)
    asylist[num].wait()
def commandwait(asylist):
    loop.run_until_complete(asyncio.gather(*[bashwait(x,asylist[x]) for x in asylist]))






def setdat(a1,a2,a3):
    with open(a1) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        xxx = [line for line in lines_strip if a2 in line]
        yyy = xxx[0].split(' ')
        return yyy[a3]
def setdat_chr(a1,a2):
    with open(a1) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        xxx = [line for line in lines_strip if a2 in line]
        return xxx[0]
def transport(b1,b2,b3):
    cmd = "cp -p {0} {1}".format(b1,b2)
    sp.run(cmd,shell=True,cwd=b3)
    return None
def digt_EMT_function(c1):
    c2="{:.2f}".format(c1-0.1)
    c3="{:.2f}".format(c1+0.1)
    return c2,c3
cmd = "pwd" 
current=sp.check_output(cmd.split()).decode('utf-8')
current=current.replace('\n',"")
print(current)
cmd = "ls" 
w = sp.check_output(cmd.split()).decode('utf-8')
w=w.replace('\n',"")
print(w)
y1 = w.split('.')[0]
print(y1)
yy=y1
minimamlist=[vD,x1,x2,imp,arrpy,bionpy,pm_go,pm_imp,impnext,f2pyfile]
firstlist=[cha,getpy,readyimp,best_d_py,comparepy]
filelist=minimamlist+firstlist
wlist=[w]
cplist = minimamlist+wlist
for i in range(len(filelist)):
    cmd = "cp -p {0}{1} {2}".format(macrofile,filelist[i],current)
    sp.run(cmd,shell=True) 

cmd = "chmod -R 777 {}".format(current)
sp.run(cmd,shell=True)

m = setdat(x1,defocus_chr,3)
#digital
mdigital = setdat(x2,defocus_chr,3)
zstart = setdat(x2,defocus_chr,1)
zend = setdat(x2,defocus_chr,2)
ntfftx = setdat(x2,ntfftx_chr,1)
ntffty = setdat(x2,ntffty_chr,1)
bion_focus = setdat(x1,bion_focus_chr,1)
#gapz = -1*gapnum

fieldx = setdat(x1,field_chr,3)
fieldy = setdat(x1,field_chr,4)
xstart = setdat(x1,field_chr,1)
ystart = setdat(x1,field_chr,2)
#impnum = setdat(imp,improve_chr,2)
improveth_plus = setdat(cha,improveth_plus_chr,1)
improveth_minus = setdat(cha,improveth_minus_chr,1)
improveparamater = setdat(cha,improveparamater_chr,1)
size = setdat(cha,size_chr,1)
interpolatenumber = setdat(cha,interpolatenumber_chr,1)
# improveth_plus = setdat_chr(cha,improveth_plus_chr).split()
improvefeedback_plus= setdat_chr(cha,improvefeedback_plus_chr).split()
# improveth_minus = setdat_chr(cha,improveth_minus_chr).split()
improvefeedback_minus= setdat_chr(cha,improvefeedback_minus_chr).split()
spacedensity = setdat_chr(cha,spacedensity_chr).split()
intparamater= setdat_chr(cha,intparamater_chr).split()
phasereverseparamater = setdat_chr(cha,phasereverseparamater_chr).split()
duplicateparamater= setdat_chr(cha,duplicateparamater_chr).split()
digt_EMT_phase = setdat_chr(cha,digt_EMT_phase_chr).split()
digt_EMT_intensity= setdat_chr(cha,digt_EMT_intensity_chr).split()
# improveparamater= setdat_chr(cha,improveparamater_chr).split()


#digt_num=dq+digt_num+dq

#only analog
Azstart = setdat(x1,defocus_chr,1)
Azend = setdat(x1,defocus_chr,2)
Antfftx = setdat(x1,ntfftx_chr,1)
Antffty = setdat(x1,ntffty_chr,1)


fixnamelist=["m","mdigital","zstart","zend","ntfftx","ntffty","bion_focus","fieldx",\
        "fieldy","xstart","ystart","Azstart","Azend","Antfftx","Antffty","field",\
        "improveth_plus","improveth_minus","improveparamater","size","interpolatenumber"]
changenamelist=["improvefeedback_plus","improvefeedback_minus",\
            "spacedensity","intparamater","phasereverseparamater","duplicateparamater",\
             "digt_EMT_phase","digt_EMT_intensity"]
fixdatalist=[m,mdigital,zstart,zend,ntfftx,ntffty,bion_focus,\
            fieldx,fieldy,xstart,ystart,Azstart,Azend,Antfftx,Antffty,fieldx,\
            improveth_plus,improveth_minus,\
            improveparamater,size,interpolatenumber]
changedatalist=[improvefeedback_plus,improvefeedback_minus,spacedensity,\
    intparamater,phasereverseparamater,duplicateparamater,digt_EMT_phase,digt_EMT_intensity]




class Para:
    def __init__(self,data_set_list,data_set_name_list,namechangelist,datachangelist):
        self.data_set_list=data_set_list
        self.data_set_name_list=data_set_name_list
        self.namechangelist=namechangelist
        self.datachangelist=datachangelist
    def bash_pmgo(self):
        for cm in range(2,len(self.namechangelist)):
            folder=r"{0}".format(current)
            tempfile=current+sr+self.namechangelist[cm]
            cmd = f"mkdir {tempfile}"
            sp.run(cmd,shell=True,cwd=folder)
            for cm1 in range(1,len(self.datachangelist[cm])):
                folder=r"{0}".format(current)
                tempfile=current+sr+self.namechangelist[cm]+sr+str(cm1)
                cmd = f"mkdir {tempfile}"
                sp.run(cmd,shell=True,cwd=folder)
                folder=r"{0}/{1}".format(current,self.namechangelist[cm])

                dataset_changelist=[self.datachangelist[i][cm1] if i == cm else self.datachangelist[i][1]  for i in range(len(self.datachangelist))] 
                print(dataset_changelist)
                f = open(datapy,'w')
                for i in range(0,len(self.data_set_list)):
                    f.write(f"{self.data_set_name_list[i]} = {self.data_set_list[i]}\n")
                for i in range(len(self.namechangelist)):
                    f.write(f"{self.namechangelist[i]} = {dataset_changelist[i]}\n")
                if self.namechangelist[cm]=="digt_EMT_intensity":
                    f.write("digtalnumber='{0} {1} 1 180 {2} 3'\n"\
                        .format(digt_EMT_function(float(self.datachangelist[7][cm1]))[0],\
                        digt_EMT_function(float(self.datachangelist[7][cm1]))[1],\
                        self.datachangelist[6][1]))
                if self.namechangelist[cm]=="digt_EMT_phase":
                    f.write("digtalnumber='{0} {1} 1 180 {2} 3'\n"\
                        .format(digt_EMT_function(float(self.datachangelist[7][1]))[0],\
                        digt_EMT_function(float(self.datachangelist[7][1]))[1],\
                        self.datachangelist[6][cm1]))
                if self.namechangelist[cm]!="digt_EMT_phase" and self.namechangelist[cm]!="digt_EMT_intensity":
                    f.write("digtalnumber='{0} {1} 1 180 {2} 3'\n"\
                        .format(digt_EMT_function(float(self.datachangelist[7][1]))[0],\
                        digt_EMT_function(float(self.datachangelist[7][1]))[1],\
                        self.datachangelist[6][1]))


                f.write("yy = '{0}'\n".format(yy))
                foldername=current+sr+self.namechangelist[cm]+sr+str(cm1)
                f.write("foldername = '{0}'\n".format(foldername))
                operation=current+sr+self.namechangelist[cm]
                f.write("operation = '{0}'\n".format(operation))
                f.write("current = '{0}'\n".format(current))
                f.write("paramatername = '{0}'\n".format(self.namechangelist[cm]))
                f.write("paramaternumber = '{0}'\n".format(str(cm1)))
                f.write("paramaterchange = '{0}'\n".format(self.datachangelist[cm][cm1]))
                
                f.close()
                folder=r"{0}".format(current)
                if cm1 == 1:
                    cmd = "cp -p {0} {1}".format(datapy,operation)
                    sp.run(cmd,shell=True,cwd=folder)
                    cmd = "cp -p {0} {1}".format(cha,operation)
                    sp.run(cmd,shell=True,cwd=folder)
                    cmd = "cp -p {0} {1}".format(getpy,operation)
                    sp.run(cmd,shell=True,cwd=folder)
                filec=current+sr+self.namechangelist[cm]+sr+str(cm1)
                cmd = "mv -f {0} {1}".format(datapy,filec)
                sp.run(cmd,shell=True,cwd=folder)

                for i in range(len(cplist)):
                    cmd = "cp -p {0} {1}".format(cplist[i],filec)
                    sp.run(cmd,shell=True,cwd=folder)

                folder=r"{0}".format(foldername)
                cmd = 'sed -i -e "s*foldername*{0}*g" {1}'.format(foldername,pm_go)
                sp.run(cmd,shell=True,cwd=folder)

    def bash_pmdone(self):
        for i in range(2,len(self.namechangelist)):
            for j in range(1,len(self.datachangelist[i])):
                pmcont=[]
                cmd = "bash {}".format(pm_go)
                folder=r"{0}/{1}/{2}".format(current,self.namechangelist[i],str(j))
                pm = sp.Popen(cmd,shell=True,cwd=folder)
                pmcont.append(pm)
        return pmlist
        for i in range(len(pmcont)):
            pmcont[i].wait()

    def bestget(self):
        for i in range(2,len(self.namechangelist)):
            folder=r"{0}/{1}".format(current,self.namechangelist[i])
            cmd = "python {0}".format(getpy)
            sp.run(cmd,shell=True,cwd=folder)
        f = open("{0}".format(bestpy),'a')

        for i in range(0,len(self.data_set_name_list)):
            f.write("{0} = {1}\n".format(self.data_set_name_list[i],self.data_set_list[i]))
        f.write("w = '{0}'\n".format(w))
        f.write("yy = '{0}'\n".format(yy))
        f.write("current = '{0}'\n".format(current))
        f.close()

        folder=r"{0}".format(current)
        cmd = "python {0}".format(readyimp)
        sp.run(cmd,shell=True,cwd=folder) 
    def bash_pmimp(self):
        folder=r"{0}".format(current)
        cmd = "mkdir {0}".format(improvedirectory)
        sp.run(cmd,shell=True,cwd=folder)

        for i in range(1,len(self.datachangelist[0])):
            folder_i=current+sr+improvedirectory
            folder=r"{0}".format(current)
            cmd = "mkdir {0}/{1}".format(folder_i,str(i))
            sp.run(cmd,shell=True,cwd=folder)
            for j in range(1,len(self.datachangelist[0])):
                cmd = "mkdir {0}/{1}/{2}".format(folder_i,str(i),str(j))
                sp.run(cmd,shell=True,cwd=folder)
                
                filec=folder_i+sr+str(i)+sr+str(j)
                cmd = "cp -p {0} {1}".format(bestpy,filec)
                sp.run(cmd,shell=True,cwd=folder)

                tmpfolder = r"{0}".format(filec)
                cmd = "cp -p {0} {1}".format(bestpy,datapy)
                sp.run(cmd,shell=True,cwd=tmpfolder)

                f = open("{0}/{1}".format(filec,datapy),'a')
                f.write("{0} = {1}\n".format(self.namechangelist[0],self.datachangelist[0][i]))
                f.write("{0} = {1}\n".format(self.namechangelist[1],self.datachangelist[1][j]))
                f.write("plus_number = {0}\n".format(str(i)))
                f.write("minus_number = {0}\n".format(str(j)))
                f.close()

                for k in range(len(cplist)):
                    cmd = "cp -p {0} {1}".format(cplist[k],filec)
                    sp.run(cmd,shell=True,cwd=folder)

                cmd = 'sed -i -e "s*foldername*{0}*g" {1}'.format(filec,pm_imp)
                sp.run(cmd,shell=True,cwd=tmpfolder)
                cmd = 'sed -i -e "s*improveparamater*{0}*g" {1}'.format(improveparamater,pm_imp)
                sp.run(cmd,shell=True,cwd=tmpfolder)
     
        pm_cont=[]
        for i in range(1,len(self.datachangelist[0])):
            for j in range(1,len(self.datachangelist[1])):
                folder=r"{0}/{1}/{2}/{3}".format(current,improvedirectory,str(i),str(j))
                cmd = "bash {}".format(pm_imp)
                pm = sp.Popen(cmd,shell=True,cwd=folder)
                pm_cont.append(pm)
        for i in range(0,((len(self.datachangelist[0])-1)*(len(self.datachangelist[1])-1)-1)):
            pm_cont[i].wait()
    def compare(self):
        folder=r"{0}".format(current)
        cmd = "python {0}".format(best_d_py)
        sp.run(cmd,shell=True,cwd=folder)

        cmd = "python {0}".format(comparepy)
        sp.run(cmd,shell=True,cwd=folder)

XX=Para(fixdatalist,fixnamelist,changenamelist,changedatalist)
XX.bash_pmgo()
paralist=XX.bash_pmdone()
XX.bestget()
XX.bash_pmimp()
XX.compare()

