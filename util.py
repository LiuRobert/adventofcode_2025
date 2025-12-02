from pathlib import Path
import inspect

def read_lines(test=False):
    file_name = "test.txt" if test else "data.txt"
    # Hack för att hitta rätt folder, funkar bara om anropande filen anropar det här direkt
    current_frame = inspect.currentframe()
    calling_frame = inspect.getouterframes(current_frame)[1]
    day_folder = Path(calling_frame.filename).stem.split("_")[0]
    path = Path("data") / day_folder / file_name
    return path.read_text().split("\n")
