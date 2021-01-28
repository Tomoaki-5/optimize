import bion

csvname="seedcheck.csv"       
txtname="SEED"
basetxt="Sfirst"
plot_csvname="plot_seed.csv"
bion.seedcsv_to_plotcsv(csvname,txtname,basetxt,plot_csvname)

plot_html="Plot_RAW.html"
plot=bion.Change(plot_html,plot_csvname)
plot.plot_txt()

