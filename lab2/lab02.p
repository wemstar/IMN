set terminal jpeg

set output 'Z01a.jpg'
plot 'File1' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z01b.jpg'
plot 'File2' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z01c.jpg'
plot 'File3' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z01d.jpg'
plot 'File3' u 1:4 w p title 'jawnie','File2' u 1:4 w p title 'niejawnie','File3' u 1:4 w p title 'trapezów',

set output 'Z02a.jpg'
plot 'File4' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z02b.jpg'
plot 'File5' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z02c.jpg'
plot 'File6' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z02d.jpg'
plot 'File7' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set yrange [-4:4]
set output 'Z02e.jpg'
plot 'File4' u 1:4 w l title '0.01','File5' u 1:4 w l title '0.1','File6' u 1:4 w l title '0.25','File7' u 1:4 w l title '0.27'

set autoscale y
set output 'Z03a.jpg'
plot 'File8' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03b.jpg'
plot 'File9' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03c.jpg'
plot 'File10' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03d.jpg'
plot 'File11' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set output 'Z03e.jpg'
plot 'File12' u 1:2 w p title 'numerycznie','' u 1:3 w l title 'analitycznie'

set yrange [-4:4]
set output 'Z03f.jpg'
plot 'File8' u 1:4 w l title '0.01','File9' u 1:4 w l title '0.1','File10' u 1:4 w l title '0.25','File11' u 1:4 w l title '0.27','File12' u 1:4 w l title '0.27'

set autoscale y
set output 'Z04a.jpg'
plot 'File13' u 1:2 w lp title 'numerycznie'