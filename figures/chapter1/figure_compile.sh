pdflatex triple_product.tex
python cross_section_data/plot.py
pdflatex potential_energy.tex
pdflatex cross_section.tex
pdflatex sigma_v.tex
pdflatex integrand.tex
pdflatex sigma_v_3_rections.tex
pdflatex n_tau_E_ignition.tex
pdflatex power_comp.tex
yes "" | lualatex --shell-escape Contour.tex
yes "" | lualatex wireframe.tex
yes "" | lualatex stability_condition.tex
pdflatex schematic_tokamak_1.tex
pdflatex schematic_tokamak_2.tex
pdflatex schematic_tokamak_3.tex
pdflatex schematic_tokamak_4.tex
pdflatex schematic_tokamak_5.tex
pdflatex schematic_tokamak_6.tex
pdflatex schematic_tokamak_7.tex
pdflatex schematic_tokamak_8.tex
pdflatex schematic_tokamak_9.tex

rm *.aux
rm *.log
rm *.script
rm *.dat
