from cloud import SaveOnCloudTXT23D, SaveOnCloudIMG23D
import runpod
from diffusers import DiffusionPipeline, EulerAncestralDiscreteScheduler
import urllib.request
#Text2Image
from diffusers import StableDiffusionXLPipeline
import rembg
# =============================================
import torch
import requests
from PIL import Image
import time

import asyncio
import websockets




_GPU_ID = 0
device = "cuda" if torch.cuda.is_available() else "cpu"
temp_img_name = int(time.time()+300)


async def start_model(websocket):
    text = await websocket.recv()
    # ==============================
    print(f'Server Received: {text}')

    # text-to-image with SDXL for text-to-image-to-3d
    pipeline = StableDiffusionXLPipeline.from_single_file(
        "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True
    ).to(device)
    pipeline.enable_model_cpu_offload()

    num_images_per_prompt = 1
    res = 1024
    bkgd_color = "white"
    prompt = f"a ((full-body:2)) shot of a ((single:2)) {text}, isolated on {bkgd_color} background, 4k, highly detailed"
    images = pipeline(prompt=prompt, num_images_per_prompt=num_images_per_prompt, height=res, width=res).images
    image = images[0]
    image.show()
    output_path = str(temp_img_name)+"kliky-output.png"
    image.save(output_path)
    image = rembg.remove(image)
    rembg_output_path = str(temp_img_name)+"kliky-output-rembg.png"
    image.save(rembg_output_path)

    output_path_url, rembg_output_path_url = await SaveOnCloudTXT23D(output_path, rembg_output_path)
    context = {
        "output_path_url":output_path_url,
        "rembg_output_path_url":rembg_output_path_url,
    }
        
    # ==============================
    await websocket.send(context)
    print(f'Server Sent: {context}')



async def main():
    async with websockets.serve(start_model, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())