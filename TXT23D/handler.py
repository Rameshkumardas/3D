from client import request_for_txt23d
import asyncio
import runpod
# =============================================
def handler(job):
    text = job['inputs']['text']  
    context = asyncio.run(request_for_txt23d(text))    
    return context
 
runpod.serverless.start({"handler": handler})
