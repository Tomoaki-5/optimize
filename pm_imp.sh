#!/usr/bin/bash
number=improveparamater
supnum=1
impnum=0
#commandcharacter
MASK="MASK"
vA="3D_Py_A.py"
vD="3D_Py_D.py"
x1="BION-A"
x2="BION-D"
cha="change"
imp="improvenext.py"
arrpy="arrraw.py"
bionpy="bion.py"
datapy="data.py"
f2pyfile="f2py_module.cpython-38-x86_64-linux-gnu.so"
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
str00="00"
str0="0"
under="_"
before="before"
after="after"



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
command cp -p SEED $yy
#division number +3,+4
m3=$(echo `expr $m + 3`)
m4=$(echo `expr $m + 4`)

firstseed="Sfirst"

for ((s=0; s < $number; s++));do

    if [ $supnum = 1 ] ; then
        command mkdir $current/$supnum
        y1=$(echo "$yy$under$supnum")
        command mv -f $yy $y1
        command cp -p $y1 $current/$supnum
        # command cp -p $beforenumpy $current/$supnum
        echo $supnum
    fi
    if [ $supnum -gt 1 ] ; then
        y1=$(echo "$yy$under$supnum")
        echo $supnum
    fi



    command cd $current
    #command cp -p $vA $current/$supnum
    # command cp -p $vD $current/$supnum
    command cp -p $x1 $current/$supnum
    command cp -p $x2 $current/$supnum
    command cp -p $imp $current/$supnum
    command cp -p $datapy $current/$supnum
    command cp -p $bionpy $current/$supnum
    command cp -p $firstseed $current/$supnum
    command cp -p $f2pyfile $current/$supnum

    command cd $current/$supnum
    echo $supnum




    #graph snum change
    #command sed -i -e "s/snum/$supnum/g" $vA


    #character connect

    #y2=$(echo "$y1$str001")
    #y3=$(echo "$y1$str00")
    #main program

    #command mv -f $y1 $y2
    echo $x1
    echo $y1
    echo $pwd
    command BION_ARIES $x1 $y1
    wait
    command mtv_split $x1'_'$y1'_mplotmtv'

    if [ $m3 -gt 9 ] ; then
        command bion_digt_EMT -i "$digt_num" $x1'_'$y1'_mplotmtv'_0$m3 $x1'_'$y1'_mplotmtv'_0$m4 > MASK_plotmtv
    fi
    if [ $m3 = 9 ] ; then
        command bion_digt_EMT -i "$digt_num" $x1'_'$y1'_mplotmtv'_00$m3 $x1'_'$y1'_mplotmtv'_0$m4 > MASK_plotmtv
    fi
    if [ $m4 -lt 9 ] ; then
        command bion_digt_EMT -i "$digt_num" $x1'_'$y1'_mplotmtv'_00$m3 $x1'_'$y1'_mplotmtv'_00$m4 > MASK_plotmtv
    fi


    command bion_to_rect MASK_plotmtv > $MASK

    command garies $x2 $MASK
    maskcha=$(echo "$x2$under$MASK$under$mplotmtv")
    command mtv_split $maskcha 



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

    maskdata=$(echo $MASK$under$y1)
    command mv -f $MASK $maskdata

    impnum=$(echo `expr $impnum + 1`)
    command cp -p $y1 Sbefore
    command sed -i -e "1 s/1/$impnum/g" $imp
    command python $imp
    wait
    y2=$y1
    supnum=$(echo `expr $supnum + 1`)
    y1=$(echo "$yy$under$supnum")
    command cp -p Simprove $y1
    #echo $supnum



    command mkdir $current/$supnum
    command cp -p $y1 $current/$supnum
    # command cp -p $afternumpy $current/$supnum
    # command mv -f $current/$supnum/$afternumpy $current/$supnum/$beforenumpy
    
    savenum=$(echo `expr $supnum - 1`)

    newfile=$(echo "$save$savenum")
    Digitalnpy="np_saveD_before.npy"
    numpyname=$(echo "$y2$npy")
    command cp -p $Digitalnpy $numpyname
    command mkdir $current/$newfile
    resultnew="result.csv"
    # nextseedgraphic=$(echo "$seed$y1$under$supnum$html")
    # pointgraphic=$(echo "$point$yy$under$D$under$savenum$html")
    # Npointgraphic=$(echo "$N$under$point$yy$under$D$under$savenum$html")
    # slidgraphic=$(echo "$slid$yy$under$D$under$savenum$html")
    command cp -p *.html $current/$newfile/
    command cp -p $numpyname $current/$newfile/
    command cp -p $resultnew $current/$newfile/
    wait
    command cp -p $y1 $current/$newfile/
    command cp -p $imp $current/$newfile/
    command cp -p $maskdata $current/$newfile/ 
    command cp -p $datapy $current/$newfile/
    command cp -p $bionpy $current/$newfile/
    # command cp -p $arrfirst $current/$newfile/
    # command cp -p $y2 $current/$newfile/
    command cd $current
    
    
    command rm -rf $savenum
    
    
    # if [ $supnum = $number ] ; then
    # break
    # fi


done
