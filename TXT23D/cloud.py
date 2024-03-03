# ==============================
import cloudinary
import cloudinary.uploader
# import cloudinary.api
# Import to format the JSON responses
# ==============================
import json
# Set configuration parameter: return "https" URLs by setting secure=True  
# ==============================
config = cloudinary.config( 
  cloud_name = "dtdh7gkgc", 
  api_key = "614926813383612", 
  api_secret = "DR9yUXTbNXhk2dCt0riJz9jjMWQ",
  secure = True
)
#CLOUDINARY_URL=cloudinary://614926813383612:DR9yUXTbNXhk2dCt0riJz9jjMWQ@dtdh7gkgc
# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

def SaveOnCloudIMG23D(output_path):
 # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  result1 = cloudinary.uploader.upload(output_path, public_id=f"kliky/{output_path.split('/')[-1]}", unique_filename = False, overwrite=True)
  # Build the URL for the image and save it in the variable 'srcURL'
  srcURL1 = cloudinary.CloudinaryImage("kliky").build_url()
  # Log the image URL to the console. 
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****2. Upload an image****\nDelivery URL: ", result1['secure_url'], "\n")
  return result1['secure_url']


def SaveOnCloudTXT23D(output_path, rembg_output_path):
 # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  result1 = cloudinary.uploader.upload(output_path, public_id=f"kliky/{output_path.split('/')[-1]}", unique_filename = False, overwrite=True)
  # Log the image URL to the console. 
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****2. Upload an image****\nDelivery URL: ", result1['secure_url'], "\n")
  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  result2 = cloudinary.uploader.upload(rembg_output_path, public_id=f"kliky/{rembg_output_path.split('/')[-1]}", unique_filename = False, overwrite=True)
  # Log the image URL to the console. 
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****3. Upload an image****\nDelivery URL: ", result2['secure_url'], "\n")
  return result1['secure_url'], result2['secure_url']