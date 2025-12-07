# tokamaks_translate
Une traduction non officielle' du livre "tokamaks" de John Wesson

## Compilation

Les figures des différents chapitres se trouve dans les sous dossier figures/chapterN/ avec N le numéro du chapitre, pour compiler les figures un fichier figure_compile.sh est fourni, il suffit d'utiliser "./figure_compile.sh".
Des bibliothèques python standarts sont nécessaires, numpy et sys, et lualatex est nécessaire pour certaines figures.
Vous pouvez aussi executer manuellement les codes python dans ce cas la bibliothèque matplotlib sera nécessaire, ou bien vous pouvez executer avec l'option --no-show.

Une fois les figures compilées, chaque chapitre peut-être compilé individuellement avec "pdflatex chapitreN.tex" (où N edt le numéro du chapitre) ou alors le livre entier peut-être compilé avec "pdflatex main.tex"
