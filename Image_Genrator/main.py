import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype = torch.float32,
    use_auth_token = True
)

prompt = ("An imaginary animal whith wings"
        "full HD 4K resolution"
)
image = pipe(prompt,guidance_scale = 7.5)["sample"][0]

image.save("An imaginary animal whith wings.jpg")

#plt.axis = ("off")
#plt.imshow(image);