from fastapi import APIRouter, Body, Query
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List,Dict
import json
from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY

asit_router = APIRouter()


department_location={
    "shopping":[
        {"id":"1","title":"Reliance"},
        {"id":"2","title":"panda"},
        {"id":"3","title":"big bazaar"},
        {"id":"4","title":"esplanade"}
    ], 
    "clothing":[
        {"id":"1","title":"C1"},
        {"id":"2","title":"C2"},
        {"id":"3","title":"C3"},
        {"id":"4","title":"C4"}
    ],
    "home":[
         {"id":"1","title":"H1"},
        {"id":"2","title":"H2"},
        {"id":"3","title":"H3"},
        {"id":"4","title":"H4"}
    ],
    "electronics":[
         {"id":"1","title":"E1"},
        {"id":"2","title":"E2"},
        {"id":"3","title":"E3"},
        {"id":"4","title":"E4"}
    ],
    "beauty":[
        {"id":"1","title":"B1"},
        {"id":"2","title":"B2"},
        {"id":"3","title":"B3"},
        {"id":"4","title":"B4"}
    ]
}
 

@asit_router.post("/test-flow")
async def flow1(body: dict = Body()):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    print("decrypted_data:- ",decrypted_data)
    print("aes_key:- ",aes_key)
    # print("location enabled or not:- ",decrypted_data.get("is_location_enabled",False))
    if decrypted_data['action'] == 'ping':
        response = {
            "data": {
                "status": "active"
            }
        }
    elif decrypted_data["data"]["trigger"]=="department_selected":
        print("decrypted data:- ",decrypted_data)
        response={
                "screen":"APPOINTMENT",
                "data":{
                    "is_location_enabled":True,
                    "location":department_location[decrypted_data["data"]["department"]]
                }
            }
    elif decrypted_data["data"]["trigger"]=="location_selected":
        response={
            "screen":"APPOINTMENT",
            "data":{
                "message":f"User You have selected {decrypted_data["data"]["location"]}"
            }
        }

    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')