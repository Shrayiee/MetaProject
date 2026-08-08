from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse
from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
from .image_tob64 import media_to_bytes

shray_router5 = APIRouter()

@shray_router5.post("/test-flow")
async def flow1(body: dict = Body()):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    
    print(decrypted_data)
    if decrypted_data["action"]=="ping":
        response={
            "data":{
                "status":"active",
            }
        
        }
    elif decrypted_data["data"]=={}:
        response={
            "screen":"document_page",
            "data":{
                "message":"active",
                "image2_visible":False,
                "image3_visible":False
            }
        }
    

    elif "trigger" in decrypted_data["data"] and decrypted_data["data"]["trigger"]=="clicked":
        print(decrypted_data)
        # print("image object:- ",decrypted_data["data"]["image"])
        # print("Total number of images:- ",len(decrypted_data["data"]["image"]))
        list_of_images=[]
        for i in decrypted_data["data"]["image"]:
            list_of_images.append(media_to_bytes(i))
        
        if len(list_of_images)==1:
            response={
                "screen":"final_page",
                "data":{
                    "message":"success",
                    "name":decrypted_data["data"]["name"],
                    "image1":list_of_images[0],
                    "image2_visible":False,
                    "image3_visible":False
                }
            }
        elif len(list_of_images)==2:
            response={
                "screen":"final_page",
                "data":{
                    "message":"success",
                    "name":decrypted_data["data"]["name"],
                    "image1":list_of_images[0],
                    "image2_visible":True,
                    "image2":list_of_images[1],
                    "image3_visible":False
                }
            } 

        elif len(list_of_images)==3:
            response={
                "screen":"final_page",
                "data":{
                    "message":"success",
                    "name":decrypted_data["data"]["name"],
                    "image1":list_of_images[0],
                    "image2_visible":True,
                    "image2":list_of_images[1],
                    "image3_visible":True,
                    "image3":list_of_images[2]
                }
            }

    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')
