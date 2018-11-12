from pathlib import Path

data_folder = Path("5CE30E51C640_Logs_11-09-18-08-40AM/nvram2/logs/")
file_to_open = data_folder / "ArmConsolelog.txt.0"
f = open(file_to_open, "r", encoding='UTF8')
print(f.read())