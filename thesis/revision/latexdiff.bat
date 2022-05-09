@echo off
setlocal

set "old_path=C:\Users\User\Uni\masterarbeit_first_draft\masterthesis\thesis\"
set "new_path=C:\Users\User\Uni\Masterarbeit\thesis\"
set "doc_name_filename=thesis"

echo Generate %doc_name_filename%_flat.tex for %new_path%
cd %new_path%
latexpand %doc_name_filename%.tex > %doc_name_filename%_flat.tex

echo Generate %doc_name_filename%_flat.tex for %old_path%
cd %old_path%
latexpand %doc_name_filename%.tex > %doc_name_filename%_flat.tex

echo Generate diff
cd %new_path%
latexdiff %old_path%thesis_flat.tex %doc_name_filename%_flat.tex > diff.tex
pdflatex  --max-print-line=10000 -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -recorder  diff.tex 2>&1 > NUL
echo PDF generated in case of problems see diff.log

echo Cleaning up
del %doc_name_filename%_flat.tex
del %old_path%%doc_name_filename%_flat.tex

pause