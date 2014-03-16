set terminal jpeg
#Zadanie 1
set output 'Z01a.jpg'
plot 'File1.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z01b.jpg'
plot 'File2.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z01c.jpg'
plot 'File3.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z01d.jpg'
plot 'File1.txt' u 1:4 w p title 'jawnie','File2.txt' u 1:4 w p title 'niejawnie','File3.txt' u 1:4 w p title 'trapezów'

#Zadanie 2

set output 'Z02a.jpg'
plot 'File4.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z02b.jpg'
plot 'File5.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z02c.jpg'
plot 'File6.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z02d.jpg'
plot 'File7.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set yrange [-4:4]
set output 'Z02e.jpg'
plot 'File4.txt' u 1:4 w l title '0.01','File5.txt' u 1:4 w l title '0.1','File6.txt' u 1:4 w l title '0.25','File7.txt' u 1:4 w l title '0.27'

set autoscale y
set output 'Z03a.jpg'
plot 'File8.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

#Zadanie 3
set output 'Z03b.jpg'
plot 'File9.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03c.jpg'
plot 'File10.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03d.jpg'
plot 'File11.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03e.jpg'
plot 'File12.txt' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set yrange [-4:4]
set output 'Z03f.jpg'
plot 'File8.txt' u 1:4 w l title '0.01','File9.txt' u 1:4 w l title '0.1','File10.txt' u 1:4 w l title '0.25','File11.txt' u 1:4 w l title '0.27','File12.txt' u 1:4 w l title '0.27'

#Zadanie 4

set autoscale y
set output 'Z04a.jpg'
plot 'File13.txt' u 1:2 w lp title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z04b.jpg'
plot 'File14.txt' u 1:2 w lp title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z04c.jpg'
plot 'File15.txt' u 1:2 w lp title 'numerycznie','' u 1:3 w l title 'analitycznie'

#Zadanie 5

set output 'Z05a.jpg'
plot 'File16.txt' u 1:2 w lp title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z06a.jpg'
plot 'File17.txt' u 1:2 w lp title 'numerycznie'

set output 'Z07a.jpg'
plot 'File18.txt' u 1:2 w lp title 'numerycznie'

set output 'Z08a.jpg'
plot 'File19.txt' u 1:2 w lp title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z08b.jpg'
plot 'File19.txt' u 1:4 w lp title 'błąd'