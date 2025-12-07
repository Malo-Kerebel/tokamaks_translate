pdflatex triple_product.tex
pdflatex potential_energy.tex
pdflatex cross_section.tex

cd integrand/ && python reaction_rate.py --no-show && cd ..
pdflatex sigma_v.tex

cd integrand/ && python eps_exp.py --no-show && cd ..
pdflatex integrand.tex
pdflatex sigma_v_3_rections.tex

cd ignition/ && python n_tau_E.py --no-show && cd ..
pdflatex n_tau_E_ignition.tex

cd power_plots/ && python power_comp.py --no-show && cd ..
pdflatex power_comp.tex

cd power_plots/ && python wireframe.py --no-show && cd ..
yes "" | lualatex --shell-escape Contour.tex
yes "" | lualatex wireframe.tex

cd power_plots/ && python stability_condition.py --no-show && cd ..
yes "" | lualatex stability_condition.tex

cd power_plots/ && python power_comp_tau_E.py --no-show && cd ..
pdflatex power_comp_tau_E.tex

pdflatex schematic_tokamak_1.tex
pdflatex schematic_tokamak_2.tex
pdflatex schematic_tokamak_3.tex
pdflatex schematic_tokamak_4.tex
pdflatex schematic_tokamak_5.tex
pdflatex schematic_tokamak_6.tex
pdflatex schematic_tokamak_7.tex
pdflatex schematic_tokamak_8.tex
pdflatex schematic_tokamak_9.tex
pdflatex schematic_tokamak_10.tex
pdflatex power_density.tex

rm *.aux
rm *.log
rm *.script
rm *.dat
rm *.table
