@echo off
git clone https://github.com/datasets/covid-19
set path=%cd%
cd ITSC-3155-Group

rmdir Datasets /s /q

md Datasets

cd ../covid-19

copy "data" "%path%/ITSC-3155-Group/Datasets"

cd %path%
rmdir covid-19 /s /q

