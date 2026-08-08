from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse

from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
asit_router6 = APIRouter()

@asit_router6.post("/flow-test")
async def flow1(body: dict = Body()):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    
    if decrypted_data["action"]=="ping":
        response={
            "data":{
                "status":"active"
            }
        }
    # if "trigger" in decrypted_data["data"] and decrypted_data["trigger"]=="e_link":
    #     pri

    print(decrypted_data)


    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')
