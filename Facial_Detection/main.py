from deepface import DeepFace
from IPython.display import Image 

path = "/Users/ayanalikhan/Desktop/CS/Development/Projects/Facial_Detection/Lionel_Messi_20180626.jpg"
Image(filename=path)

obj = DeepFace.analyze(
    img_path=path,
    actions=["age","gender","emotion","race"],
    prog_bar=False,
)
print(obj["age"])
emotions = obj["emotion"]
print(max(emotions,key = emotions.get))
print(obj['gender'])
