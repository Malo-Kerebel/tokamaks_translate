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
pdflatex orthogonal_velocity.tex
pdflatex collision.tex
cd FP_coeff/ && gfortran FP_coeff.f90 && ./a.out && cd ..
pdflatex FP_coeff.tex
pdflatex field_electrons_test_ions.tex
pdflatex field_test_equal_mass.tex
pdflatex field_ions_test_electrons.tex
