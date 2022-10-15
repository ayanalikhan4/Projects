from deepface import DeepFace
from IPython.display import Image 

path = "Mark-Zuckerberg-012.jpg"
Image(filename=path)

obj = DeepFace.analyze(
    img_path=path,
    actions=["age","gender","emotion","race"],
    prog_bar=False,
)