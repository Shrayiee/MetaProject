from fastapi import APIRouter, Body,HTTPException
from fastapi.responses import PlainTextResponse

from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY

shray_router2 = APIRouter()

age=False
number=False


@shray_router2.post("/test-flow")
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
    if decrypted_data['data']=={}:
         response={
            "screen":"First_Page",
            "data":{
                "is_phone_number_required":False,
                "is_phone_number_visible":False,
                "is_final_submit_enabled":False
            }
        }

    elif "age_of_user" in decrypted_data["data"] and not decrypted_data["data"]["age_of_user"].isnumeric():
        raise HTTPException(status_code=400,detail=f"Age can only be integer")

    elif "age_of_user" in decrypted_data["data"] and int(decrypted_data["data"]["age_of_user"])<18:
        response={
            "screen":"First_Page",
            "data":{
                "error_message":"Age must be greater than 18"
            }
        }

    elif "age_of_user" in decrypted_data["data"] and int(decrypted_data["data"]["age_of_user"])>=18:
        response={
            "screen":"First_Page",
            "data":{
                "message":"Everything is allright!.",
                "is_phone_number_required":True,
                "is_phone_number_visible":True,
            },

        }

    elif decrypted_data["data"]["trigger"]=="validate_number":
        if not (decrypted_data["data"]["contact_number"].isnumeric() and len(decrypted_data["data"]["contact_number"])==10):
            response={
                "screen":"First_Page",
                "data":{
                    "error_message":"Number must be numeric and it must be of length 10"
                }
            }
        else:
            response={
                "screen":"First_Page",
                "data":{
                    "message":"success",
                    "is_final_submit_enabled":True
                }
            }


    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')
