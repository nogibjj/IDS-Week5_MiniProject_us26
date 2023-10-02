## SQLite Lab

[![SQL CI/CD](https://github.com/nogibjj/IDS-Week5_MiniProject_us26/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS-Week5_MiniProject_us26/actions/workflows/cicd.yml)

![4 17-etl-sqlite-RAW](https://github.com/nogibjj/sqlite-lab/assets/58792/b39b21b4-ccb4-4cc4-b262-7db34492c16d)


		
4.Makefile with the following:

      - install: using requirements.txt file to install required packages

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/install.png" alt="install">
</p>

      - test:


python -m pytest -vv --cov=main *.py
<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/test.png" alt="install">
</p>



      - format: using black formatter

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/format.png" alt="format">
</p>

      
      - lint: using ruff and nbqa plugin for .ipynb files

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/lint.png" alt="lint">
</p>	
