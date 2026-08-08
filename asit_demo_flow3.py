from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse

from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
import json
l1=[]
asit_router3 = APIRouter()
@asit_router3.post("/flow-test")
async def flow1(body: dict = Body()):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    
    response = {"message": "Flow1"}
    print("decrypted data:- ",decrypted_data)

    gender_list=[{"id":"1","title":"Male"}, {"id":"2","title":"Female"}]

    if decrypted_data["action"]=="ping":
        print("test")
        response={
            "screen":"first_screen",
            "data":{
                "status":"active"
            }
        }
    elif decrypted_data["data"]=={}:
        response={
            "screen":"first_screen",
            "data":{
                "message":"Alright guys.",
                "gender":gender_list
            }
        }

    elif "gender" in decrypted_data["data"] and  decrypted_data["data"]["gender"]=="1":
        # print("male is selected!.")
        response={
            "screen":"female_screen",
            "data":{
                    "is_heading":True,
                    "wife_name":True,
                    "wife_age":True,
                    "message":"success"
            }
        }
    
    elif "gender" in decrypted_data["data"] and decrypted_data["data"]["gender"]=="2":
        response={
            "screen":"male_screen",
            "data":{
                    "is_heading":True,
                    "wife_name":True,
                    "wife_age":False,
                    "wife_final_page":False,
                    "message":"success"
            }
        }

    elif "name_validator" in decrypted_data["data"]:
        if not (decrypted_data["data"]["name_validator"].isalpha() and len(decrypted_data["data"]["name_validator"])>5 and decrypted_data["data"]["name_validator"].capitalize()==decrypted_data["data"]["name_validator"]):
            response={
                "screen":"male_screen",
                "data":{
                    "error_message":"Name must be greater than 5 and it must have capitalize and it must be numeric as well, please met all the condition and try again."
                }
            }
        else:
            with open("name.json","w") as file:
                json.dump(decrypted_data["data"],file,indent=4)

            # file read.
            # with open("name.json","r") as file:
            #     content=json.load(file)

            #     print("content:- ",content["name_validator"])
            
            response={
                "screen":"male_screen",
                "data":{
                    "message":"success!.",
                    "wife_age":True

                }
            }
    elif "age_of_user" in decrypted_data["data"]:
        age=decrypted_data["data"]["age_of_user"]
        if not (age.isnumeric() and int(age)>=18):
            response={
                "screen":"male_screen",
                "data":{
                    "error_message":"age must be numeric and it must be greater than 18."
                }
            }

        else:
            with open("name.json","r") as file:
                content=json.load(file)
            response={
                "screen":"main_screen",
                "data":{
                    "message":"active",
                    "name":content["name_validator"],
                    "age":decrypted_data["data"]["age_of_user"]
                }
            }


    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')