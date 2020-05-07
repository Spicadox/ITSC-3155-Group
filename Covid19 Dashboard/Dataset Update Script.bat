@echo off
git clone https://github.com/datasets/covid-19
set path=%cd%

cd ../../ITSC-3155-Group
set path2=%cd%
rmdir Datasets /s /q

md Datasets

cd %path%/covid-19

copy "data" "%path2%/Datasets"

cd %path%
rmdir covid-19 /s /q

