#!/usr/bin/bash

#commandcharacter
MASK="MASK"
# vA="3D_Py_A.py"
# vD="3D_Py_D.py"
x1="BION-A"
x2="BION-D"
cha="change"
imp="improve.py"
arrpy="arrraw.py"
bionpy="bion.py"
datapy="data.py"
arrraw="np_save_first"
result="result.csv"
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
str00="00"
str0="0"
under="_"


command cd foldername
current=$(pwd)
#setdat
command grep defocus $x1>de.txt
m=$(cut -f 4 --delim=" " de.txt)
command grep defocus $x2>de2.txt
mdigital=$(cut -f 4 --delim=" " de2.txt)
start=$(cut -f 2 --delim=" " de2.txt)
end=$(cut -f 3 --delim=" " de2.txt)

command grep ntfftx $x2>ntfftx.txt
ntfftx=$(cut -f 2 --delim=" " ntfftx.txt)
command grep ntffty $x2>ntffty.txt
ntffty=$(cut -f 2 --delim=" " ntffty.txt)

command grep bion_focus $x1>bion_focus.txt
bionfocus=$(cut -f 2 --delim=" " bion_focus.txt)

focusplus=$(echo `expr \-1 \* $bionfocus`)

# command grep thresh $cha>thresh.txt
# thresh=$(cut -f 2 --delim=" " thresh.txt)

# command grep nresi $cha>nresi.txt
# nresi=$(cut -f 2 --delim=" " nresi.txt)

command grep field $x1>field.txt
field=$(cut -f 4 --delim=" " field.txt)
x0=$(cut -f 2 --delim=" " field.txt)
y0=$(cut -f 3 --delim=" " field.txt)
command grep digtalnumber $datapy>digt.txt
digt_num=$(cut -f 2 --delim="'" digt.txt)
command grep paramaternumber $datapy>digt.txt
paramaternumber=$(cut -f 2 --delim="'" digt.txt)
command grep yy $datapy>yy.txt
yy=$(cut -f 2 --delim="'" yy.txt)
y1=$yy
# only Analog

Astart=$(cut -f 2 --delim=" " de.txt)
Aend=$(cut -f 3 --delim=" " de.txt)
w=$(echo "$yy$py")

wait
command python $w
wait
command python $arrpy
wait
command cp -p SEED $y1
#division number +3,+4
m3=$(echo `expr $m + 3`)
m4=$(echo `expr $m + 4`)

command BION_ARIES $x1 $y1
wait
command mtv_split $x1'_'$y1'_mplotmtv'
wait
if [ $m3 -gt 9 ] ; then
    command bion_digt_EMT -i "$digt_num" $x1'_'$y1'_mplotmtv'_0$m3 $x1'_'$y1'_mplotmtv'_0$m4 > MASK_plotmtv
fi
if [ $m3 = 9 ] ; then
    command bion_digt_EMT -i "$digt_num" $x1'_'$y1'_mplotmtv'_00$m3 $x1'_'$y1'_mplotmtv'_0$m4 > MASK_plotmtv
fi
if [ $m4 -lt 9 ] ; then
    command bion_digt_EMT -i "$digt_num" $x1'_'$y1'_mplotmtv'_00$m3 $x1'_'$y1'_mplotmtv'_00$m4 > MASK_plotmtv
fi

wait
command bion_to_rect MASK_plotmtv > $MASK
wait
command garies $x2 $MASK
maskcha=$(echo "$x2$under$MASK$under$mplotmtv")
wait
command mtv_split $maskcha 
wait


p=$(echo `expr $mdigital`)
if [ $p -gt 9 ] ; then 
    p1=10
else
    p1=$(echo `expr $p + 1`)
fi
for ((k=1; k < $p1; k++)); do

    mtv=$(echo "$maskcha$under$str00$k")
    command mtv_to_csv.pl "$mtv" > 3D-test_GD00$k.csv
done

if [ $p -gt 9 ] ; then 
    p2=$(echo `expr $p + 1`)
for ((k=10; k < $p2; k++)); do
    mtv=$(echo "$maskcha$under$str0$k")
    command mtv_to_csv.pl "$mtv" > 3D-test_GD0$k.csv
done
fi

wait

maskdata=$(echo $MASK$under$yy)
command mv -f $MASK $maskdata
wait
command cp -p SEED Sbefore
wait
command python $imp
wait


command cd ..
tempd=$(pwd)
saved=$(echo $tempd$sr$save$under$paramaternumber)
command mkdir $saved
command cd foldername
resultcsv="result.csv"
first="SEED"
Digitalnpy="np_saveD_before.npy"
data_max_min="max_min.csv"
command cp -p $resultcsv $saved
wait
command cp -p $datapy $saved
command cp -p *.html $saved
command cp -p $bionpy $saved
command cp -p $imp $saved
# command cp -p $arrfirst $saved
command cp -p $yy $saved
# command cp -p $w $saved
command cp -p $Digitalnpy $saved
command cp -p $data_max_min $saved
wait
# command cp -p Sim
command cd ..
command rm -rf $current