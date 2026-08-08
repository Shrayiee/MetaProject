from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse

from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
asit_router4 = APIRouter()
from .dictionary import Dictionary_1

@asit_router4.post("/flow-test")
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
                "status":"active"
            }
        }
    
    elif "title_of_image" in decrypted_data["data"]:
        obj=Dictionary_1()
        ans=obj.return_dict()
        # print(ans[decrypted_data["data"]["title_of_image"]])
        response={
            "screen":"final_page",
            "data":{
                "title_of_image":ans[decrypted_data["data"]["title_of_image"]]["title_of_image"],
                "image_of_link":ans[decrypted_data["data"]["title_of_image"]]["image_of_link"]
            }
        }
    

    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')