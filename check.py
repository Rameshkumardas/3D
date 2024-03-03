# from alive_progress import alive_bar
# from tqdm import tqdm
# import time

# with alive_bar(1000) as bar:
#     for i in range(1):
#         time.sleep(5)
#         bar()

import torch
from diffusers import EulerDiscreteScheduler, StableDiffusionPipeline

seed = 33

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", requires_safety_checker=False
)
pipe = pipe.to("mps")
pipe.scheduler = EulerDiscreteScheduler.from_config(
    pipe.scheduler.config, use_karras_sigmas=True
)

prompt = "an astronaut riding a horse on mars"


def progress(step, timestep, latents):
    print(step, timestep, latents[0][0][0][0])


generator = torch.Generator(device="mps").manual_seed(seed)
image = pipe(
    prompt,
    generator=generator,
    num_inference_steps=20,
    callback=progress,
    callback_steps=1,
).images[0]

