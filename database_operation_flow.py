from fastapi import APIRouter, Body,Depends
from fastapi.responses import PlainTextResponse

from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
from .image_tob64 import media_to_bytes
from sqlalchemy.orm import Session
from .orm_file import models,differen_operation,database_connection
import json

crud_with_db = APIRouter()

@crud_with_db.post("/test-flow")
async def flow1(body: dict = Body(),db:Session=Depends(database_connection.get_db)):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    
    various_operation=[{"id":"1","title":"Create","description":"You can create user by clicking this option."},{"id":"2",
"title":"Read","description":"you can read a user detail by clicking this option."},{"id":"3","title":"Update","description":"You can update the detail of the user by clicking this option"},{"id":"4","title":"Delete","description":"You can delete the detail of the user by clicking this link"}]
    
    print(decrypted_data)
    
    if "action" in decrypted_data and decrypted_data["action"]=="ping":
        response={
            "screen":"operation_page",
            "data":{
                "status":"active"
            }
        }
    elif decrypted_data["action"] == "BACK":
        response={
            "screen":"operation_page",
            "data":{
                "various_operation":various_operation,
                 "init_operation":""
            }
        }

    elif decrypted_data["data"]=={}:
        response={
            "screen":"operation_page",
            "data":{
                "various_operation":various_operation,
                 "init_operation":""
            }
        }

    elif decrypted_data["action"]=="data_exchange" and decrypted_data["data"]["trigger"]=="various_operation" and decrypted_data["data"]["option_clicked"]=='':
        response={
            "screen":"operation_page",
            "data":{
                "message":"success",
                "various_operation":various_operation
            }
        }
    elif decrypted_data["data"]["trigger"]=="various_operation":

        if decrypted_data["data"]["option_clicked"]=="1":
            response={
                "screen":"create_page",
                "data":{
                    "message":"success",
                   
                }
            }
        
        elif decrypted_data["data"]["option_clicked"]=="2":
            response={
                "screen":"read_page",
                "data":{
                    "message":"success",
                    "all_fields":False,
                    "init_operation":""
                }
            }


        elif decrypted_data["data"]["option_clicked"]=="3":
            response={
                "screen":"user_validation_page",
                "data":{
                    "message":"success",
                    "image_watch":False,
                    "init_operation":""
                }
            }
        
        elif decrypted_data["data"]["option_clicked"]=="4":
            response={
                "screen":"delete_page",
                "data":{
                    "init_operation":"",
                    "message":"success",
                    "init_operation":""
                }
            }
    
        
    elif decrypted_data["data"]["trigger"]=="read_data_from_db":
        ans=differen_operation.data_from_email(decrypted_data["data"]["email"],db)
        print("Anwerrrrrr:- ",ans)
        if ans!=None:
            response={
                "screen":"read_page",
                "data":{
                    "all_fields":True,
                    "email":ans[0],
                    "password":ans[1],
                    "dob":ans[2],
                    "hobby":ans[3],
                    "gender":ans[4],
                    "photo":ans[5]
                }
            }
        else:
            response={
                "screen":"read_page",
                "data":{
                    "error_message":"There is no mail found in the database"
                }
            }

    elif decrypted_data["data"]["trigger"]=="retreive_photo":
        ans=differen_operation.validate_user(decrypted_data["data"]["email"],decrypted_data["data"]["password"],db)
        if ans[0]:
            response={
                "screen":"user_validation_page",
                "data":{
                    "image_watch":True,
                    "image_src":ans[1]
                }
            }

        else:
            response={
                "screen":"user_validation_page",
                "data":{
                    "error_message":"User credential is wrong"
                }
            }
    
    elif decrypted_data["data"]["trigger"]=="user_validate_e_p":
        ans=differen_operation.validate_user(decrypted_data["data"]["email"],decrypted_data["data"]["password"],db)
        if ans[0]:
            all_values=differen_operation.fetch_detail(decrypted_data["data"]["email"],db)
            with open("email_address.txt","w") as file:
                file.write(all_values[0])
            response={
                "screen":"Update_page",
                "data":{
                    "email":all_values[0],
                    "password":all_values[1],
                    "dob":all_values[2],
                    "hobby":all_values[3],
                    "gender":all_values[4],
                    "photo":all_values[5]
                }
            }
        else:
            response={
                "screen":"user_validation_page",
                "data":{
                    "error_message":"user credential is wrong"
                }
            }
    elif decrypted_data["data"]["trigger"]=="user_update_detail":
        get_email=""
        with open("email_address.txt","r") as file:
            get_email=file.read()
            print("get email:- ",get_email)
            if decrypted_data["data"]["photo"]!=[]:
                base_64_link=media_to_bytes(decrypted_data["data"]["photo"])
                differen_operation.update_detail_db(get_email,db,decrypted_data["data"]["password"],decrypted_data["data"]["dob"],decrypted_data["data"]["hobby"],decrypted_data["data"]["gender"],base_64_link)
            else:
                differen_operation.update_detail_db(get_email,db,decrypted_data["data"]["password"],decrypted_data["data"]["dob"],decrypted_data["data"]["hobby"],decrypted_data["data"]["gender"])
        response={
            "screen":"final_page",
            "data":{
                "message":"success"
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="delete_data_from_db":
        ans=differen_operation.validate_user(decrypted_data["data"]["email"],decrypted_data["data"]["password"],db)
        if ans[0]:
            differen_operation.delete_from_db(decrypted_data["data"]["email"],db)
            response={
                "screen":"delete_feedback",
                "data":{
                    "message":"success"
                }
            }
        else:
            response={
                "screen":"delete_page",
                "data":{
                    "error_message":"User not found in the database"
                }
            }



    elif decrypted_data["data"]["trigger"]=="user_details":
        base_64_image=media_to_bytes(decrypted_data["data"]["photo"])
        decrypted_data["data"]["photo"]=base_64_image
        decrypted_data["data"].pop("trigger")
        print("modified_decrypted_data")
        new_record=models.user_operation(**decrypted_data["data"])
        db.add(new_record)
        db.commit()
        response={
            "screen":"final_page",
            "data":{
                "message":"success"
            }
        }
    

                    

    

    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')