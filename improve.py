impnum = 1

import bion

bion.csv_to_np()
arrdata=bion.load_np()
#arrnor=bion.np_normalization(arrdata)


seedfirstname="Sfirst"
seedbeforename="Sbefore"
seedaftername="Simprove"
plot_csvname="Simprove.csv"
seedimprove_htmlname="Simprove.html"
eva_csv="Evaluation.csv"
arr_csv = "Graphic_inter.csv"
arr_html = "Graphic_inter.html"
improveC=bion.Improve(seedfirstname,seedbeforename,seedaftername,arrdata,impnum,eva_csv,arr_csv)
improveC.evaluation()
improveC.single()
bion.seedtxt_to_plotcsv(seedaftername,plot_csvname)

plot=bion.Change(seedimprove_htmlname,plot_csvname)
plot.plot_txt()


#sild_Graphic

# slid_html_name="Graphic_slid.html"
# slidcut=100
# bion.plot_slid(arrnor,slid_html_name,slidcut)


eva_plus_html = "eva_plus.html"
eva_minus_html = "eva_minus.html"
eva_html = "eva.html" 
plot_evaluation_plus=bion.Change(eva_plus_html,eva_csv)
plot_evaluation_plus.plot_csv_plus()
plot_evaluation_minus=bion.Change(eva_minus_html,eva_csv)
plot_evaluation_minus.plot_csv_minus()

plot=bion.Change(eva_html,eva_csv)
plot.plot_csv()

plot=bion.Change(arr_html,arr_csv)
plot.plot_csv()

# plot_csvname="Simprove.csv"
# bion.seedtxt_to_plotcsv(seedaftername,plot_csvname)

# plot=bion.Change(seedimprove_htmlname,plot_csvname)
# plot.plot_txt()

# no_inter_graphic_csv="Graphic.csv"
# graphic_htmlname="Graphic.tml"
# csv_change=bion.Change(no_inter_graphic_csv,arrnor)
# pointcut=3
# csv_change.arr_to_csv(pointcut)
# plot=bion.Change(graphic_htmlname,no_inter_graphic_csv)
# plot.plot_csv()

# slid_html_name="Graphic_slid.html"
# slidcut=100
# bion.plot_slid(arrnor,slid_html_name,slidcut)



# arr_inter=bion.interpolatefunction(arrdata)
# arr_inter_nor = bion.np_normalization(arr_inter)

# inter_graphic_csv="Graphic_inter.csv"
# inter_graphic_htmlname="Graphic_inter.tml"
# csv_change_inter=bion.Change(inter_graphic_csv,arr_inter_nor)
# csv_change_inter.arr_to_csv(pointcut)
# plot=bion.Change(inter_graphic_htmlname,inter_graphic_csv)
# plot.plot_csv()



# seedfirstname="SEED"
# seedbeforename="Sbefore"
# seedaftername="Simprove"
# improveC=bion.Improve(seedfirstname,seedbeforename,seedaftername,arr_inter_nor,impnum)
# improveC.evaluation()
# improveC.single()

# # txtname="Simprove"
# plot_csvname="Simprove.csv"
# bion.seedtxt_to_plotcsv(seedaftername,plot_csvname)
# seedimprove_htmlname="Simprove.html"
# plot=bion.Change(seedimprove_htmlname,plot_csvname)
# plot.plot_txt()


# # plot_before=bion.Change("before","Simprove")
# # plot_before.plot_txt_pointcut()
# eva_csvname="Evaluation.csv"
# eva_plus_html = "eva_plus.html"
# eva_minus_html = "eva_minus.html"
# eva_html = "eva.html" 
# plot_evaluation_plus=bion.Change(eva_plus_html,eva_csvname)
# plot_evaluation_plus.plot_csv_plus()
# plot_evaluation_minus=bion.Change(eva_minus_html,eva_csvname)
# plot_evaluation_minus.plot_csv_minus()

# plot=bion.Change(eva_html,eva_csvname)
# plot.plot_csv()