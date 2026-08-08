from fastapi import APIRouter, Body,Depends
from fastapi.responses import PlainTextResponse
from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
from .orm_file import database_connection
from .orm_file import models
from .orm_file import differen_operation
from sqlalchemy.orm import Session
import random
import string

models.Base.metadata.create_all(bind=database_connection.engine)

shray_db_dynamic_router = APIRouter()

@shray_db_dynamic_router.post("/test-flow")
async def flow1(body: dict = Body(),db:Session=Depends(database_connection.get_db)):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    
    print(decrypted_data)
    list_of_user=[{"id":"1","title":"Applicant"},{"id":"2","title":"Authorized User"}]

    if decrypted_data["action"]=="ping":
        response={
            "data":{
                "status":"active",
            }
        }
    
    elif decrypted_data["data"]=={}:
        response={
            "screen":"sumangal_first_page",
            "data":{
                "footer_enabled":False,
                "types_of_login":list_of_user
            }
        }

    elif decrypted_data["data"]["trigger"]=="user_type":
        if decrypted_data["data"]["value"]=="1":
            value="".join(random.choices(string.ascii_letters+string.digits,k=5))
            with open("captcha.txt","w") as file:
                file.write(f"captcha:{value}")
            response={
                "screen":"applicant_page",
                "data":{
                    "captcha":value
                }
            }  
    
    elif decrypted_data["data"]["trigger"]=="enter_otp":
        if not ("phone_number" in decrypted_data["data"] and "password" in decrypted_data["data"]):
            response ={
                "screen":"applicant_page",
                "data":{
                    "error_message":"Required fields are missing!."
                }
            }
        else:
            if not differen_operation.validate_user(decrypted_data["data"].get("phone_number"),decrypted_data["data"].get("password"),db):
                response={
                    "screen":"applicant_page",
                    "data":{
                        "error_message":"User credential is wrong"
                    }
                }
            

            else:
                
                response={
                    "screen":"applicant_page",
                    "data":{
                        "message":"active"
                    }
                }    

    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')
