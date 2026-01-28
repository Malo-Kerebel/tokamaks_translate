pdflatex charge_sheet.tex
cd shielding/ && gfortran potential.f90 && ./a.out && cd ..
pdflatex potential.tex
pdflatex displaced_electrons.tex
pdflatex displaced_electrons_2.tex
pdflatex grad_B.tex
pdflatex ExB.tex
pdflatex drift_grad_B.tex
pdflatex ion_drift.tex
pdflatex polarisation_drift.tex
