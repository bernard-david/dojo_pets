from ninja import Ninja
from pets import Pets

bessie = Pets("Bessie", "cow", "Flying over the moon")
ninja1 = Ninja("david", "bernard", "grass", "grass from whole foods", bessie)

ninja1.walk().feed().bathe()