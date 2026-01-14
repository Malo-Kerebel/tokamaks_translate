pdflatex charge_sheet.tex
cd shielding/ && gfortran potential.f90 && ./a.out && cd ..
pdflatex potential.tex
