from pathlib import Path

def read_lines(current__file__, test=False):
    file_name = "test.txt" if test else "data.txt"
    day_folder = Path(current__file__).stem.split("_")[0]
    path = Path("data") / day_folder / file_name
    return path.read_text().split("\n")
