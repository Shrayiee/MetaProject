from fastapi import APIRouter, Body,Depends
from fastapi.responses import PlainTextResponse
from datetime import datetime
from utils.fb_utils import decrypt_request, encrypt_response
from core.keys import PHONE_NUMBER_PRIVATE_KEY
import json
from .sumangal_files import database_connection,different_operation,models
from sqlalchemy.orm import Session

demo_router = APIRouter()
models.Base.metadata.create_all(bind=database_connection.engine)

@demo_router.post("/flow-router")
async def flow1(body: dict = Body(),db:Session=Depends(database_connection.get_db)):
    encrypted_flow_data_b64 = body['encrypted_flow_data']
    encrypted_aes_key_b64 = body['encrypted_aes_key']
    initial_vector_b64 = body['initial_vector']

    decrypted_data, aes_key, iv = decrypt_request(
        encrypted_flow_data_b64, encrypted_aes_key_b64, initial_vector_b64, PHONE_NUMBER_PRIVATE_KEY)
    
    print(decrypted_data)
    
    districts=[
                    {"id": "Angul", "title": "Angul"},
                    {"id": "Balangir", "title": "Balangir"},
                    {"id": "Balasore", "title": "Balasore"},
                    {"id": "Bargarh", "title": "Bargarh"},
                    {"id": "Bhadrak", "title": "Bhadrak"},
                    {"id": "Boudh", "title": "Boudh"},
                    {"id": "Cuttack", "title": "Cuttack"},
                    {"id": "Deogarh", "title": "Deogarh"},
                    {"id": "Dhenkanal", "title": "Dhenkanal"},
                    {"id": "Gajapati", "title": "Gajapati"},
                    {"id": "Ganjam", "title": "Ganjam"},
                    {"id": "Jagatsinghpur", "title": "Jagatsinghpur"},
                    {"id": "Jajpur", "title": "Jajpur"},
                    {"id": "Jharsuguda", "title": "Jharsuguda"},
                    {"id": "Kalahandi", "title": "Kalahandi"},
                    {"id": "Kandhamal", "title": "Kandhamal"},
                    {"id": "Kendrapara", "title": "Kendrapara"},
                    {"id": "Kendujhar", "title": "Kendujhar"},
                    {"id": "Khordha", "title": "Khordha"},
                    {"id": "Koraput", "title": "Koraput"},
                    {"id": "Malkangiri", "title": "Malkangiri"},
                    {"id": "Mayurbhanj", "title": "Mayurbhanj"},
                    {"id": "Nabarangpur", "title": "Nabarangpur"},
                    {"id": "Nayagarh", "title": "Nayagarh"},
                    {"id": "Nuapada", "title": "Nuapada"},
                    {"id": "Puri", "title": "Puri"},
                    {"id": "Rayagada", "title": "Rayagada"},
                    {"id": "Sambalpur", "title": "Sambalpur"},
                    {"id": "Subarnapur", "title": "Subarnapur"},
                    {"id": "Sundargarh", "title": "Sundargarh"}
                ]
    
    blocks={
        "Angul":[
            {"id":"Angul","title":"Angul"},
            {"id":"Banarpal","title":"Banarpal"},
            {"id":"Chhendipada","title":"Chhendipada"},
            {"id":"Athmallik","title":"Athmallik"},
            {"id":"Kishorenagar","title":"Kishorenagar"},
            {"id":"Pallahara","title":"Pallahara"},
            {"id":"Talcher","title":"Talcher"},
            {"id":"Kaniha","title":"Kaniha"}
        ],
        "Balangir":[
           {"id":"Agalpur","title":"Agalpur"},
            {"id":"Balangir","title":"Balangir"},
            {"id":"Bangomunda","title":"Bangomunda"},
            {"id":"Belpara","title":"Belpara"},
            {"id":"Deogaon","title":"Deogaon"},
            {"id":"Gudvella","title":"Gudvella"},
            {"id":"Khaprakhol","title":"Khaprakhol"},
            {"id":"Loisinga","title":"Loisinga"},
            {"id":"Muribahal","title":"Muribahal"},
            {"id":"Patnagarh","title":"Patnagarh"},
            {"id":"Puintala","title":"Puintala"},
            {"id":"Saintala","title":"Saintala"},
            {"id":"Titlagarh","title":"Titlagarh"},
            {"id":"Turekela","title":"Turekela"}
        ],
        "Balasore":[
           {"id":"Bahanaga","title":"Bahanaga"},
            {"id":"Balasore","title":"Balasore"},
            {"id":"Baliapal","title":"Baliapal"},
            {"id":"Basta","title":"Basta"},
            {"id":"Bhograi","title":"Bhograi"},
            {"id":"Jaleswar","title":"Jaleswar"},
            {"id":"Khaira","title":"Khaira"},
            {"id":"Nilgiri","title":"Nilgiri"},
            {"id":"Oupada","title":"Oupada"},
            {"id":"Remuna","title":"Remuna"},
            {"id":"Simulia","title":"Simulia"},
            {"id":"Soro","title":"Soro"}
        ],
        "Bargarh":[
            {"id":"Ambabhona","title":"Ambabhona"},
            {"id":"Attabira","title":"Attabira"},
            {"id":"Bargarh","title":"Bargarh"},
            {"id":"Barpali","title":"Barpali"},
            {"id":"Bhatli","title":"Bhatli"},
            {"id":"Bheden","title":"Bheden"},
            {"id":"Bijepur","title":"Bijepur"},
            {"id":"Gaisilet","title":"Gaisilet"},
            {"id":"Jharbandh","title":"Jharbandh"},
            {"id":"Padampur","title":"Padampur"},
            {"id":"Paikmal","title":"Paikmal"},
            {"id":"Sohella","title":"Sohella"}
        ],
        "Bhadrak":[
             {"id":"Basudevpur","title":"Basudevpur"},
            {"id":"Bhadrak","title":"Bhadrak"},
            {"id":"Bhandaripokhari","title":"Bhandaripokhari"},
            {"id":"Bonth","title":"Bonth"},
            {"id":"Chandabali","title":"Chandabali"},
            {"id":"Dhamnagar","title":"Dhamnagar"},
            {"id":"Tihidi","title":"Tihidi"}
        ],
        "Boudh":[
            {"id":"Boudh","title":"Boudh"},
            {"id":"Harabhanga","title":"Harabhanga"},
            {"id":"Kantamal","title":"Kantamal"}

        ],
        "Cuttack":[
            {"id":"Athagad","title":"Athagad"},
            {"id":"Badamba","title":"Badamba"},
            {"id":"Banki","title":"Banki"},
            {"id":"Baranga","title":"Baranga"},
            {"id":"Cuttack Sadar","title":"Cuttack Sadar"},
            {"id":"Damapada","title":"Damapada"},
            {"id":"Kantapada","title":"Kantapada"},
            {"id":"Mahanga","title":"Mahanga"},
            {"id":"Niali","title":"Niali"},
            {"id":"Nischintakoili","title":"Nischintakoili"},
            {"id":"Salepur","title":"Salepur"},
            {"id":"Tangi-Choudwar","title":"Tangi-Choudwar"}
        ],
        "Deogarh":[
             {"id":"Barkote","title":"Barkote"},
            {"id":"Deogarh","title":"Deogarh"},
            {"id":"Reamal","title":"Reamal"}
        ],
        "Dhenkanal":[
           {"id":"Bhuban","title":"Bhuban"},
            {"id":"Dhenkanal Sadar","title":"Dhenkanal Sadar"},
            {"id":"Gondia","title":"Gondia"},
            {"id":"Hindol","title":"Hindol"},
            {"id":"Kamakshyanagar","title":"Kamakshyanagar"},
            {"id":"Kankadahad","title":"Kankadahad"},
            {"id":"Odapada","title":"Odapada"},
            {"id":"Parjang","title":"Parjang"}
        ],
        "Gajapati":[
           {"id":"Gumma","title":"Gumma"},
            {"id":"Kasinagar","title":"Kasinagar"},
            {"id":"Mohana","title":"Mohana"},
            {"id":"Nuagada","title":"Nuagada"},
            {"id":"Rayagada","title":"Rayagada"},
            {"id":"R.Udayagiri","title":"R.Udayagiri"}
        ],
        "Ganjam":[
            {"id":"Aska","title":"Aska"},
            {"id":"Beguniapada","title":"Beguniapada"},
            {"id":"Bellaguntha","title":"Bellaguntha"},
            {"id":"Bhanjanagar","title":"Bhanjanagar"},
            {"id":"Buguda","title":"Buguda"},
            {"id":"Chhatrapur","title":"Chhatrapur"},
            {"id":"Chikiti","title":"Chikiti"},
            {"id":"Dharakote","title":"Dharakote"},
            {"id":"Dighapahandi","title":"Dighapahandi"},
            {"id":"Ganjam","title":"Ganjam"},
            {"id":"Gopalpur","title":"Gopalpur"},
            {"id":"Hinjilicut","title":"Hinjilicut"},
            {"id":"Jagannathprasad","title":"Jagannathprasad"},
            {"id":"Kabisuryanagar","title":"Kabisuryanagar"},
            {"id":"Khalikote","title":"Khalikote"},
            {"id":"Kodala","title":"Kodala"},
            {"id":"Kukudakhandi","title":"Kukudakhandi"},
            {"id":"Mohana","title":"Mohana"},
            {"id":"Patrapur","title":"Patrapur"},
            {"id":"Polasara","title":"Polasara"},
            {"id":"Purusottampur","title":"Purusottampur"},
            {"id":"Rangeilunda","title":"Rangeilunda"},
            {"id":"Sanakhemundi","title":"Sanakhemundi"},
            {"id":"Sorada","title":"Sorada"},
            {"id":"Surada","title":"Surada"}
        ],
        "Jagatsinghpur":[
            {"id":"Balikuda","title":"Balikuda"},
            {"id":"Biridi","title":"Biridi"},
            {"id":"Erasama","title":"Erasama"},
            {"id":"Jagatsinghpur","title":"Jagatsinghpur"},
            {"id":"Kujang","title":"Kujang"},
            {"id":"Naugaon","title":"Naugaon"},
            {"id":"Raghunathpur","title":"Raghunathpur"},
            {"id":"Tirtol","title":"Tirtol"}
        ],
        "Jajpur":[
            {"id":"Bari","title":"Bari"},
            {"id":"Binjharpur","title":"Binjharpur"},
            {"id":"Dasarathpur","title":"Dasarathpur"},
            {"id":"Dharmasala","title":"Dharmasala"},
            {"id":"Jajpur","title":"Jajpur"},
            {"id":"Rasulpur","title":"Rasulpur"},
            {"id":"Sukinda","title":"Sukinda"}
        ],
        "Jharsuguda":[
            {"id":"Jharsuguda","title":"Jharsuguda"},
            {"id":"Kirmira","title":"Kirmira"},
            {"id":"Laikera","title":"Laikera"},
            {"id":"Lakhanpur","title":"Lakhanpur"},
            {"id":"Kolabira","title":"Kolabira"}
        ],
        "Kalahandi":[
            {"id":"Bhawanipatna","title":"Bhawanipatna"},
            {"id":"Golamunda","title":"Golamunda"},
            {"id":"Jaipatna","title":"Jaipatna"},
            {"id":"Junagarh","title":"Junagarh"},
            {"id":"Kalahandi","title":"Kalahandi"},
            {"id":"Kalampur","title":"Kalampur"},
            {"id":"Karlamunda","title":"Karlamunda"},
            {"id":"Kesinga","title":"Kesinga"},
            {"id":"Lanjigarh","title":"Lanjigarh"},
            {"id":"Madanpur Rampur","title":"Madanpur Rampur"},
            {"id":"M. Rampur","title":"M. Rampur"},
            {"id":"Narala","title":"Narala"},
            {"id":"Narla","title":"Narla"},
            {"id":"Th. Rampur","title":"Th. Rampur"}
        ],
        "Kandhamal":[
            {"id":"Balliguda","title":"Balliguda"},
            {"id":"Chakapada","title":"Chakapada"},
            {"id":"Daringbadi","title":"Daringbadi"},
            {"id":"G. Udayagiri","title":"G. Udayagiri"},
            {"id":"K. Nuagaon","title":"K. Nuagaon"},
            {"id":"Kotagarh","title":"Kotagarh"},
            {"id":"Phiringia","title":"Phiringia"},
            {"id":"Phulbani","title":"Phulbani"},
            {"id":"Raikia","title":"Raikia"},
            {"id":"Tikabali","title":"Tikabali"}
        ],
        "Kendrapara":[
            {"id":"Aul","title":"Aul"},
            {"id":"Derabish","title":"Derabish"},
            {"id":"Garadpur","title":"Garadpur"},
            {"id":"Kendrapara","title":"Kendrapara"},
            {"id":"Mahakalapada","title":"Mahakalapada"},
            {"id":"Marsaghai","title":"Marsaghai"},
            {"id":"Pattamundai","title":"Pattamundai"},
            {"id":"Rajkanika","title":"Rajkanika"},
            {"id":"Rajnagar","title":"Rajnagar"}
        ],
        "Kendhujhar":[
            {"id":"Anandapur","title":"Anandapur"},
            {"id":"Banspal","title":"Banspal"},
            {"id":"Champua","title":"Champua"},
            {"id":"Ghasipura","title":"Ghasipura"},
            {"id":"Ghatgaon","title":"Ghatgaon"},
            {"id":"Harichandanpur","title":"Harichandanpur"},
            {"id":"Hatadihi","title":"Hatadihi"},
            {"id":"Jhumpura","title":"Jhumpura"},
            {"id":"Joda","title":"Joda"},
            {"id":"Keonjhar","title":"Keonjhar"},
            {"id":"Patana","title":"Patana"},
            {"id":"Saharpada","title":"Saharpada"},
            {"id":"Telkoi","title":"Telkoi"}
        ],
        "Khordha":[
            {"id":"Balianta","title":"Balianta"},
            {"id":"Balipatna","title":"Balipatna"},
            {"id":"Banapur","title":"Banapur"},
            {"id":"Begunia","title":"Begunia"},
            {"id":"Bhubaneswar","title":"Bhubaneswar"},
            {"id":"Bolagarh","title":"Bolagarh"},
            {"id":"Chilika","title":"Chilika"},
            {"id":"Jatni","title":"Jatni"},
            {"id":"Kantabada","title":"Kantabada"},
            {"id":"Khordha","title":"Khordha"},
            {"id":"Tangi","title":"Tangi"}
        ],
        "Koraput":[
            {"id":"Baipariguda","title":"Baipariguda"},
            {"id":"Bandhugaon","title":"Bandhugaon"},
            {"id":"Borigumma","title":"Borigumma"},
            {"id":"Damanjodi","title":"Damanjodi"},
            {"id":"Dasamantapur","title":"Dasamantapur"},
            {"id":"Jeypore","title":"Jeypore"},
            {"id":"Kundura","title":"Kundura"},
            {"id":"Koraput","title":"Koraput"},
            {"id":"Kotpad","title":"Kotpad"},
            {"id":"Lamtaput","title":"Lamtaput"},
            {"id":"Laxmipur","title":"Laxmipur"},
            {"id":"Machhkund","title":"Machhkund"},
            {"id":"Nandapur","title":"Nandapur"},
            {"id":"Narayanpatana","title":"Narayanpatana"},
            {"id":"Pottangi","title":"Pottangi"},
            {"id":"Semiliguda","title":"Semiliguda"}
        ],
        "Malkangiri":[
            {"id":"Balimela","title":"Balimela"},
            {"id":"Chitrakonda","title":"Chitrakonda"},
            {"id":"Kalimela","title":"Kalimela"},
            {"id":"Khairaput","title":"Khairaput"},
            {"id":"Korukonda","title":"Korukonda"},
            {"id":"Malkangiri","title":"Malkangiri"},
            {"id":"Mathili","title":"Mathili"},
            {"id":"Motu","title":"Motu"},
            {"id":"Podia","title":"Podia"}
        ],
        'Mayurbhanj':[
            {"id":"Bahalda","title":"Bahalda"},
            {"id":"Bangiriposi","title":"Bangiriposi"},
            {"id":"Baripada","title":"Baripada"},
            {"id":"Betnoti","title":"Betnoti"},
            {"id":"Bijatala","title":"Bijatala"},
            {"id":"Bisoi","title":"Bisoi"},
            {"id":"Gopabandhunagar","title":"Gopabandhunagar"},
            {"id":"Jashipur","title":"Jashipur"},
            {"id":"Jamda","title":"Jamda"},
            {"id":"Karanjia","title":"Karanjia"},
            {"id":"Kaptipada","title":"Kaptipada"},
            {"id":"Khunta","title":"Khunta"},
            {"id":"Kusumi","title":"Kusumi"},
            {"id":"Kuliana","title":"Kuliana"},
            {"id":"Morada","title":"Morada"},
            {"id":"Rairangpur","title":"Rairangpur"},
            {"id":"Raruan","title":"Raruan"},
            {"id":"Rasgovindpur","title":"Rasgovindpur"},
            {"id":"Sarasakana","title":"Sarasakana"},
            {"id":"Samakhunta","title":"Samakhunta"},
            {"id":"Suliapada","title":"Suliapada"},
            {"id":"Thakurmunda","title":"Thakurmunda"},
            {"id":"Tiring","title":"Tiring"}
        ],
        "Nabarangpur":[
            {"id":"Chandahandi","title":"Chandahandi"},
            {"id":"Dabugam","title":"Dabugam"},
            {"id":"Jharigam","title":"Jharigam"},
            {"id":"Kosagumuda","title":"Kosagumuda"},
            {"id":"Nabarangpur","title":"Nabarangpur"},
            {"id":"Nandahandi","title":"Nandahandi"},
            {"id":"Papadahandi","title":"Papadahandi"},
            {"id":"Raighar","title":"Raighar"},
            {"id":"Tentulikhunti","title":"Tentulikhunti"},
            {"id":"Umerkote","title":"Umerkote"}
        ],
        "Nayagarh":[
            {"id":"Bhapur","title":"Bhapur"},
            {"id":"Daspalla","title":"Daspalla"},
            {"id":"Gania","title":"Gania"},
            {"id":"Khandapada","title":"Khandapada"},
            {"id":"Nayagarh","title":"Nayagarh"},
            {"id":"Nuagaon","title":"Nuagaon"},
            {"id":"Odagaon","title":"Odagaon"},
            {"id":"Ranpur","title":"Ranpur"}
        ],
        "Nuapada":[
            {"id":"Boden","title":"Boden"}, {"id":"Khariar","title":"Khariar"}, {"id":"Komna","title":"Komna"}, {"id":"Nuapada","title":"Nuapada"}, {"id":"Sinapali","title":"Sinapali"}

        ],
        "Puri":[
           {"id":"Astaranga","title":"Astaranga"}, {"id":"Brahmagiri","title":"Brahmagiri"}, {"id":"Delanga","title":"Delanga"}, {"id":"Gop","title":"Gop"}, {"id":"Kakatpur","title":"Kakatpur"}, {"id":"Kanas","title":"Kanas"}, {"id":"Krushnaprasad","title":"Krushnaprasad"}, {"id":"Nimapara","title":"Nimapara"}, {"id":"Pipili","title":"Pipili"}, {"id":"Puri Sadar","title":"Puri Sadar"}, {"id":"Satyabadi","title":"Satyabadi"}

        ],
        "Rayagada":[
           {"id":"Bissam Cuttack","title":"Bissam Cuttack"}, {"id":"Chandrapur","title":"Chandrapur"}, {"id":"Gunupur","title":"Gunupur"}, {"id":"Gudari","title":"Gudari"}, {"id":"Kashipur","title":"Kashipur"}, {"id":"Kolnara","title":"Kolnara"}, {"id":"Muniguda","title":"Muniguda"}, {"id":"Padmapur","title":"Padmapur"}, {"id":"Ramanaguda","title":"Ramanaguda"}, {"id":"Rayagada","title":"Rayagada"}

        ],
        "Sambalpur":[
            {"id":"Bamra","title":"Bamra"}, {"id":"Dhankauda","title":"Dhankauda"}, {"id":"Jamankira","title":"Jamankira"}, {"id":"Jujomura","title":"Jujomura"}, {"id":"Kuchinda","title":"Kuchinda"}, {"id":"Kundheigola","title":"Kundheigola"}, {"id":"Maneswar","title":"Maneswar"}, {"id":"Naktideul","title":"Naktideul"}, {"id":"Rairakhol","title":"Rairakhol"}, {"id":"Rengali","title":"Rengali"}

        ],
        "Subarnapur":[
            {"id":"Biramaharajpur","title":"Biramaharajpur"}, {"id":"Binika","title":"Binika"}, {"id":"Dunguripali","title":"Dunguripali"}, {"id":"Sonepur","title":"Sonepur"}, {"id":"Tarabha","title":"Tarabha"}, {"id":"Ulunda","title":"Ulunda"}

        ],
        "Sundargarh":[
            {"id":"Balisankara","title":"Balisankara"}, {"id":"Bargaon","title":"Bargaon"}, {"id":"Bisra","title":"Bisra"}, {"id":"Bonaigarh","title":"Bonaigarh"}, {"id":"Gurundia","title":"Gurundia"}, {"id":"Hemgir","title":"Hemgir"}, {"id":"Kuanrmunda","title":"Kuanrmunda"}, {"id":"Kutra","title":"Kutra"}, {"id":"Lahunipara","title":"Lahunipara"}, {"id":"Lathikata","title":"Lathikata"}, {"id":"Lephripara","title":"Lephripara"}, {"id":"Nuagaon","title":"Nuagaon"}, {"id":"Rajgangpur","title":"Rajgangpur"}, {"id":"Raruan","title":"Raruan"}, {"id":"Sundargarh","title":"Sundargarh"}, {"id":"Subdega","title":"Subdega"}, {"id":"Tangarpali","title":"Tangarpali"}

        ]
    }

    state=[
        {"id":"odisha","title":"odisha"}
    ]

    def time_Calculator(start_date,end_date):
        start_date=datetime.strptime(start_date,"%Y-%m-%d")
        year=end_date.year-start_date.year
        month=end_date.month-start_date.month
        day=end_date.day-start_date.day

        if month<0:
            year-=1
            month+=12
        
        if day<0:
            month-=1
            previous_month= end_date.month-1 if end_date.month>1 else 12
            previous_year=end_date.year if end_date.year>1 else end_date.year-1
            print(previous_month)
            day+=(datetime(previous_year,previous_month+1,1) - datetime(previous_year,previous_month,1)).days
        
        return f"{year},{month},{day}"

    subcaste=[
        {"id": "Adi-Andhra", "title": "Adi-Andhra"},
        {"id": "Amant", "title": "Amant"},
        {"id": "Amat", "title": "Amat"},
        {"id": "Dandachhatra Majhi", "title": "Dandachhatra Majhi"},
        {"id": "Amata", "title": "Amata"},
        {"id": "Amath", "title": "Amath"},
        {"id": "Audhelia", "title": "Audhelia"},
        {"id": "Badaik", "title": "Badaik"},
        {"id": "Bagheti", "title": "Bagheti"},
        {"id": "Baghuti", "title": "Baghuti"},
        {"id": "Bajikar", "title": "Bajikar"},
        {"id": "Bari", "title": "Bari"},
        {"id": "Basor", "title": "Basor"},
        {"id": "Burud", "title": "Burud"},
        {"id": "Bauri", "title": "Bauri"},
        {"id": "Buna Bauri", "title": "Buna Bauri"},
        {"id": "Dasia Bauri", "title": "Dasia Bauri"},
        {"id": "Bauti", "title": "Bauti"},
        {"id": "Bavuri", "title": "Bavuri"},
        {"id": "Bedia", "title": "Bedia"},
        {"id": "Bejia", "title": "Bejia"},
        {"id": "Bajia", "title": "Bajia"},
        {"id": "Beldar", "title": "Beldar"},
        {"id": "Bhata", "title": "Bhata"},
        {"id": "Bhoi", "title": "Bhoi"},
        {"id": "Chachati", "title": "Chachati"},
        {"id": "Chakali", "title": "Chakali"},
        {"id": "Chamar", "title": "Chamar"},
        {"id": "Mochi", "title": "Mochi"},
        {"id": "Muchi", "title": "Muchi"},
        {"id": "Satnami", "title": "Satnami"},
        {"id": "Chamara", "title": "Chamara"},
        {"id": "Chamar-Ravidas", "title": "Chamar-Ravidas"},
        {"id": "Chamar-Rohidas", "title": "Chamar-Rohidas"},
        {"id": "Chandala", "title": "Chandala"},
        {"id": "Chandhai Maru", "title": "Chandhai Maru"},
        {"id": "Dandasi", "title": "Dandasi"},
        {"id": "Dewar", "title": "Dewar"},
        {"id": "Dhibara", "title": "Dhibara"},
        {"id": "Keuta", "title": "Keuta"},
        {"id": "Kaibarta", "title": "Kaibarta"},
        {"id": "Dhanwar", "title": "Dhanwar"},
        {"id": "Dhoba", "title": "Dhoba"},
        {"id": "Dhobi", "title": "Dhobi"},
        {"id": "Rajak", "title": "Rajak"},
        {"id": "Rajaka", "title": "Rajaka"},
        {"id": "Dom", "title": "Dom"},
        {"id": "Dombo", "title": "Dombo"},
        {"id": "Duria Dom", "title": "Duria Dom"},
        {"id": "Adhuria Dom", "title": "Adhuria Dom"},
        {"id": "Adhuria Domb", "title": "Adhuria Domb"},
        {"id": "Dosadha", "title": "Dosadha"},
        {"id": "Ganda", "title": "Ganda"},
        {"id": "Ghantaraghada", "title": "Ghantaraghada"},
        {"id": "Ghantra", "title": "Ghantra"},
        {"id": "Ghasi", "title": "Ghasi"},
        {"id": "Ghasia", "title": "Ghasia"},
        {"id": "Ghogia", "title": "Ghogia"},
        {"id": "Ghusuria", "title": "Ghusuria"},
        {"id": "Godagali", "title": "Godagali"},
        {"id": "Godari", "title": "Godari"},
        {"id": "Godra", "title": "Godra"},
        {"id": "Gokha", "title": "Gokha"},
        {"id": "Gorait", "title": "Gorait"},
        {"id": "Korait", "title": "Korait"},
        {"id": "Haddi", "title": "Haddi"},
        {"id": "Hadi", "title": "Hadi"},
        {"id": "Hari", "title": "Hari"},
        {"id": "Irika", "title": "Irika"},
        {"id": "Jaggali", "title": "Jaggali"},
        {"id": "Jaggili", "title": "Jaggili"},
        {"id": "Jagli", "title": "Jagli"},
        {"id": "Kandra", "title": "Kandra"},
        {"id": "Kandara", "title": "Kandara"},
        {"id": "Kadama", "title": "Kadama"},
        {"id": "Kuduma", "title": "Kuduma"},
        {"id": "Kodma", "title": "Kodma"},
        {"id": "Kodama", "title": "Kodama"},
        {"id": "Karua", "title": "Karua"},
        {"id": "Katia", "title": "Katia"},
        {"id": "Khatia", "title": "Khatia"},
        {"id": "Kela", "title": "Kela"},
        {"id": "Sapua Kela", "title": "Sapua Kela"},
        {"id": "Nalua Kela", "title": "Nalua Kela"},
        {"id": "Sabakhia Kela", "title": "Sabakhia Kela"},
        {"id": "Matia Kela", "title": "Matia Kela"},
        {"id": "Gaudia Kela", "title": "Gaudia Kela"},
        {"id": "Khadala", "title": "Khadala"},
        {"id": "Khadal", "title": "Khadal"},
        {"id": "Khodal", "title": "Khodal"},
        {"id": "Kodalo", "title": "Kodalo"},
        {"id": "Khodalo", "title": "Khodalo"},
        {"id": "Kori", "title": "Kori"},
        {"id": "Kurunga", "title": "Kurunga"},
        {"id": "Laban", "title": "Laban"},
        {"id": "Laheri", "title": "Laheri"},
        {"id": "Madari", "title": "Madari"},
        {"id": "Madiga", "title": "Madiga"},
        {"id": "Mahuria", "title": "Mahuria"},
        {"id": "Mala", "title": "Mala"},
        {"id": "Jhala", "title": "Jhala"},
        {"id": "Malo", "title": "Malo"},
        {"id": "Zala", "title": "Zala"},
        {"id": "Malha", "title": "Malha"},
        {"id": "Jhola", "title": "Jhola"},
        {"id": "Mang", "title": "Mang"},
        {"id": "Mangan", "title": "Mangan"},
        {"id": "Mehra", "title": "Mehra"},
        {"id": "Mahar", "title": "Mahar"},
        {"id": "Mehtar", "title": "Mehtar"},
        {"id": "Bhangi", "title": "Bhangi"},
        {"id": "Mewar", "title": "Mewar"},
        {"id": "Mundapotta", "title": "Mundapotta"},
        {"id": "Musahar", "title": "Musahar"},
        {"id": "Nagarchi", "title": "Nagarchi"},
        {"id": "Namasudra", "title": "Namasudra"},
        {"id": "Paidi", "title": "Paidi"},
        {"id": "Painda", "title": "Painda"},
        {"id": "Pamidi", "title": "Pamidi"},
        {"id": "Pan", "title": "Pan"},
        {"id": "Pano", "title": "Pano"},
        {"id": "Buna Pana", "title": "Buna Pana"},
        {"id": "Desua Pana", "title": "Desua Pana"},
        {"id": "Buna Pano", "title": "Buna Pano"},
        {"id": "Panchama", "title": "Panchama"},
        {"id": "Panika", "title": "Panika"},
        {"id": "Panka", "title": "Panka"},
        {"id": "Pantanti", "title": "Pantanti"},
        {"id": "Pap", "title": "Pap"},
        {"id": "Pasi", "title": "Pasi"},
        {"id": "Patial", "title": "Patial"},
        {"id": "Patikar", "title": "Patikar"},
        {"id": "Patratanti", "title": "Patratanti"},
        {"id": "Patua", "title": "Patua"},
        {"id": "Rajna", "title": "Rajna"},
        {"id": "Relli", "title": "Relli"},
        {"id": "Sabakhia", "title": "Sabakhia"},
        {"id": "Sualgiri", "title": "Sualgiri"},
        {"id": "Swalgiri", "title": "Swalgiri"},
        {"id": "Samasi", "title": "Samasi"},
        {"id": "Sanei", "title": "Sanei"},
        {"id": "Sapari", "title": "Sapari"},
        {"id": "Sauntia", "title": "Sauntia"},
        {"id": "Santia", "title": "Santia"},
        {"id": "Sidhria", "title": "Sidhria"},
        {"id": "Sinduria", "title": "Sinduria"},
        {"id": "Siyal", "title": "Siyal"},
        {"id": "Khajuria", "title": "Khajuria"},
        {"id": "Tanla", "title": "Tanla"},
        {"id": "Turi", "title": "Turi"},
        {"id": "Betra", "title": "Betra"},
        {"id": "Ujia", "title": "Ujia"},
        {"id": "Valamiki", "title": "Valamiki"},
        {"id": "Valmiki", "title": "Valmiki"},
        {"id": "Mangali", "title": "Mangali"},
        {"id": "Mirgan", "title": "Mirgan"}
    ]
    
    all_banks=[
         {"id": "Bank of Baroda", "title": "Bank of Baroda"},
        {"id": "Bank of India", "title": "Bank of India"},
        {"id": "Bank of Maharashtra", "title": "Bank of Maharashtra"},
        {"id": "Canara Bank", "title": "Canara Bank"},
        {"id": "Central Bank of India", "title": "Central Bank of India"},
        {"id": "Indian Bank", "title": "Indian Bank"},
        {"id": "Indian Overseas Bank", "title": "Indian Overseas Bank"},
        {"id": "Punjab and Sind Bank", "title": "Punjab and Sind Bank"},
        {"id": "Punjab National Bank", "title": "Punjab National Bank"},
        {"id": "State Bank of India", "title": "State Bank of India"},
        {"id": "UCO Bank", "title": "UCO Bank"},
        {"id": "Union Bank of India", "title": "Union Bank of India"}
    ]
    

    branch_bank_ifsc_code={
        "Bank of Baroda":{
            "ABADAN":"BARB0ABADAN",
            "ABRAMA":"BARB0ABRSUR"
        },
        "Bank of India":{
            "AIMS BHUBANESWAR":"BKID0005578",
            "ALATI":"BKID0005422"
        },
        "Bank of Maharashtra":{
            "ANJUL":"MAHB0001993",
            "BALANGIR":"MAHB0002140"
        },
        "Canara Bank":{
            "ADAKATA":"CNRB0006778",
            "ADASPUR":"CNRB0000283"
        },
        "Central Bank of India":{
            "ALGUM":"CBIN0282824",
            "ANUGUL":"CBIN0283308"
        },
        "Indian Bank":{
            "AGARPADA":"IDIB000A517",
            "ALARA":"IDIB000A560"
        },
        "Indian Overseas Bank":{
            "ANUGUL":"IOBA0000966",
            "ASIKA":"IOBA0002218"
        },
        "Punjab and Sind Bank":{
            "BALASORE":"PSIB0020943",
            "BANKATI":"PSIB0021610"
        },
        "Punjab National Bank":{
            "AGALPUR":"PUNB0736800",
            "ALIGONDA":"PUNB0134520"
        },
        "State Bank of India":{
            "ADASPUR":"SBIN0013576",
            "ALGINIA":"SBIN0005077"
        },
        "UCO Bank":{
            "ABDALPUR":"UCBA0001571",
            "ADA":"UCBA0001248"
        },
        "Union Bank of India":{
            "ACHARYA VIHAR":"UBIN0814938",
            "ADAPADA":"UBIN0806625"
        }
    }

    all_banks_branch={
        "Bank of Baroda":[
            {"id":"ABADAN","title":"ABADAN"},
            {"id":"ABRAMA","title":"ABRAMA"}
        ],
        "Bank of India":[
            {"id":"AIMS BHUBANESWAR","title":"AIMS BHUBANESWAR"},
            {"id":"ALATI","title":"ALATI"}
        ],
        "Bank of Maharashtra":[
            {"id":"ANJUL","title":"ANJUL"},
            {"id":"BALANGIR","title":"BALANGIR"}
        ],
        "Canara Bank":[
            {"id":"ADAKATA","title":"ADAKATA"},
            {"id":"ADASPUR","title":"ADASPUR"}
        ],
        "Central Bank of India":[
            {"id":"ALGUM","title":"ALGUM"},
            {"id":"ANUGUL","title":"ANUGUL"}
        ],
        "Indian Bank":[
            {"id":"AGARPADA","title":"AGARPADA"},
            {"id":"ALARA","title":"ALARA"}
        ],
        "Indian Overseas Bank":[
            {"id":"ANUGUL","title":"ANUGUL"},
            {"id":"ASIKA","title":"ASIKA"}
        ],
        "Punjab and Sind Bank":[
            {"id":"BALASORE","title":"BALASORE"},
            {"id":"BANKATI","title":"BANKATI"}
        ],
        "Punjab National Bank":[
            {"id":"AGALPUR","title":"AGALPUR"},
            {"id":"ALIGONDA","title":"ALIGONDA"}
        ],
        "State Bank of India":[
            {"id":"ADASPUR","title":"ADASPUR"},
            {"id":"ALGINIA","title":"ALGINIA"}
        ],
        "UCO Bank":[
            {"id":"ABDALPUR","title":"ABDALPUR"},
            {"id":"ADA","title":"ADA"}
        ],
        "Union Bank of India":[
            {"id":"ACHARYA VIHAR","title":"ACHARYA VIHAR"},
            {"id":"ADAPADA","title":"ADAPADA"}
        ]
    }

    if decrypted_data["action"]=="ping":
        response={
            "screen":"husband_page",
            "data":{
                "status":"active",
            }
        }
    elif decrypted_data["data"]=={}:
        response={
            "screen":"husband_page",
            "data":{
                "message":"success",
                "address_before_marriage":"",
                "city_before_marriage":"",
                "district_before_marriage":"",
                "block_before_marriage":"",
                "pin_code_before_marriage":"",
                "state_before_marriage":"",
                "districts":districts,
                "state":state
            }
        }

    elif decrypted_data["data"]["trigger"]=="same_address_before_marriage":
        print("i am executed!.")
        response={
            "screen":"husband_page",
            "data":{
                "address_before_marriage":decrypted_data["data"]["husband_address"],
                "city_before_marriage":decrypted_data["data"]["city_of_husband"],
                "district_before_marriage":decrypted_data["data"]["district_selected_by_husband"],
                "block_before_marriage":decrypted_data["data"]["block_selected_by_husband"],
                "pin_code_before_marriage":decrypted_data["data"]["pin_of_husband"],
                "state_before_marriage":decrypted_data["data"]["state_of_husband"]
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="district_of_husband":
        response={
            "screen":"husband_page",
            "data":{
                "blocks":blocks[decrypted_data["data"]["actual_district"]]
            }
        }
        
    elif decrypted_data["data"]["trigger"]=="district_of_husband_before_marriage" and decrypted_data["data"]["actual_district"]=="":
        response={
            "screen":"husband_page",
            "data":{
                "message":"success"
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="district_of_wife_before_marriage" and decrypted_data["data"]["actual_district"]=="":
        response={
            "screen":"wife_page",
            "data":{
                "message":"success"
                }
            }

    elif decrypted_data["data"]["trigger"]=="husband_all_info_page":
        print("all data of husband:- ",decrypted_data)
        decrypted_data["data"].pop("trigger")
        response={
            "screen":"wife_page",
            "data":{
                "districts":districts,
                "state":state,
                "wife_address":"",
                "wife_city":"",
                "wife_district":"",
                "wife_block":"",
                "wife_passcode":"",
                "wife_state":"",
                "all_data":decrypted_data["data"],
            }
        }
    elif decrypted_data["data"]["trigger"]=="wife_address_same_as_before":
        response={
            "screen":"wife_page",
            "data":{
                "wife_address":decrypted_data["data"]["wife_address"],
                "wife_city":decrypted_data["data"]["city_of_wife"],
                "wife_district":decrypted_data["data"]["district_of_wife"],
                "wife_block":decrypted_data["data"]["block_selected_by_wife"],
                "wife_passcode":decrypted_data["data"]["pin_of_wife"],
                "wife_state":decrypted_data["data"]["state_of_wife"]
            }
        }

    elif decrypted_data["data"]["trigger"]=="district_of_wife":
        response={
            "screen":"wife_page",
            "data":{
                "blocks":blocks[decrypted_data["data"]["actual_district"]]
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="wife_all_info_page":
        # print(decrypted_data["data"])
        final_dict=decrypted_data["data"]["all_data"]
        print("final_dict:- ",final_dict)
        del decrypted_data["data"]["all_data"]
        print(decrypted_data["data"])
        decrypted_data["data"].pop("trigger")
        final_dict.update(decrypted_data["data"])
        response={
            "screen":"other_info_detail",
            "data":{
                "all_data":final_dict,
                "subcaste":subcaste,
                "received_grant_earlier":False,
                "marriage_register_yes_common":False,
                "marriage_date_now_show":False,
                "marriage_date_till_now":False,
                "wife_age_show":False,
                "husband_age_show":False,
                "wife_husband_first_marriage_or_not":False,
                "husband_age_right_now":"",
                "actual_calculated_husband_age":"",
                "wife_age_right_now":"",
                "actual_calculated_wife_age":"",
                "max_date_of_marriage":f"{datetime.now().year}/{datetime.now().month}/1",
                "marriage_date_now":"",
                "marriage_date_till_now":"",
                "marriage_registration_date_current":"",
                "date_grant_earlier":""
            }
        }

    elif decrypted_data["data"]["trigger"]=="dob_of_husband":
        print(decrypted_data["data"])
        year,month,day=str(time_Calculator(decrypted_data["data"]["husband_age"],datetime.now())).split(",")
        print("year:- ",year)
        print("Month:- ",month)
        print("day:- ",day)
        decorated_str=f"{year} years {month} months {day} days" 
        response={
            "screen":"other_info_detail",
            "data":{
                "husband_age_show":True,
                "husband_age_right_now":f"Husband Age on ({year}/{month}/{day})",
                "actual_calculated_husband_age":decorated_str
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="dob_of_wife":
        wife_age=decrypted_data["data"]["wife_age"]
        year,month,day=str(time_Calculator(decrypted_data["data"]["wife_age"],datetime.now())).split(",")
        decorated_str=f"{year} years {month} months {day} days" 
        response={
            "screen":"other_info_detail",
            "data":{
                "wife_age_show":True,
                "wife_age_right_now":f"Wife Age on ({year}/{month}/{day})",
                "actual_calculated_wife_age":decorated_str
            }
        }
    elif decrypted_data["data"]["trigger"]=="date_of_marriage_happened":
        year,month,day=str(time_Calculator(decrypted_data["data"]["date_of_marriage"],datetime.now())).split(",")
        decorated_str=f"{year} years {month} months {day} days" 
        response={
            "screen":"other_info_detail",
            "data":{
                "marriage_date_now_show":True,
                "marriage_date_now":f"marriage date on {year}/{month}/{day}",
                "marriage_date_till_now":decorated_str
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="marriage_registered_or_not":
        yes_or=decrypted_data["data"]["marriage_registered_status"]
        if yes_or=="Yes":
            response={
                "screen":"other_info_detail",
                    "data":{
                        "marriage_register_yes_common":True,
                        "marriage_registration_date_current":f"{datetime.now().year}/{datetime.now().month}/1"
                    }
                }
        else:
            response={
                "screen":"other_info_detail",
                "data":{
                    "marriage_register_yes_common":False
                }
            }
    
    elif decrypted_data["data"]["trigger"]=="first_marriage_of_both_or_not":
        if decrypted_data["data"]["husband_first_marriage"]=="Yes" and decrypted_data["data"]["wife_first_marriage"]=="Yes":
            response={
                "screen":"other_info_detail",
                "data":{
                    "wife_husband_first_marriage_or_not":False
                }
            }
        else:
            response={
                "screen":"other_info_detail",
                "data":{
                    "wife_husband_first_marriage_or_not":True
                }
            }
    elif decrypted_data["data"]["trigger"]=="anybody_grant_earlier":
        print("i am executed")
        print(decrypted_data["data"]["is_grant_earlier"])
        if decrypted_data["data"]["is_grant_earlier"]=="Yes":
            response={
                "screen":"other_info_detail",
                "data":{
                    "received_grant_earlier":True,
                    "date_grant_earlier":f"{datetime.now().year}/{datetime.now().month}/1"
                }
            }
        else:
            response={
                "screen":"other_info_detail",
                "data":{
                    "received_grant_earlier":False,
                    "message":"success"
                }
            }
    
    elif decrypted_data["data"]["trigger"]=="other_information_page_detail":
        all_data=decrypted_data["data"]["all_data"]
        decrypted_data["data"].pop("trigger")
        del decrypted_data["data"]["all_data"]
        all_data.update(decrypted_data["data"])
        response={
            "screen":"Bank_Information_Details",
            "data":{
                "all_data":all_data,
                "bank_names":all_banks,
                "show_branch":False,
                "show_ifsc_code":False,
                "ifsc_code_value":""
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="bank_name_selected":
        response={
            "screen":"Bank_Information_Details",
            "data":{
                "show_branch":True,
                "bank_branch":all_banks_branch[decrypted_data["data"]["bank_name_obtained"]]
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="branch_selected_by_user":
        response={
            "screen":"Bank_Information_Details",
            "data":{
                "show_ifsc_code":True,
                "ifsc_code_value":branch_bank_ifsc_code[decrypted_data["data"]["bank_name"]][decrypted_data["data"]["branch_name"]]
            }
        }
    
    elif decrypted_data["data"]["trigger"]=="go_to_document_page":
        all_data=decrypted_data["data"]["all_data"]
        decrypted_data["data"].pop("trigger")
        del decrypted_data["data"]["all_data"]
        all_data.update(decrypted_data["data"])
        different_operation.add_bydefault_all_requirement(db)
        response={
            "screen":"Upload_Document",
            "data":{
                "all_data":all_data,
                "all_important_documents":different_operation.fetch_all_data_from_db(db)
            }
        }
    elif decrypted_data["data"]["trigger"]=="important_documents_of_user":
        print("document name:- ",decrypted_data["data"]["document_name"])
        response={
            "screen":"Upload_Document",
            "data":{
                "important_documents":decrypted_data["data"]["document_name"]
            }
        }
    elif decrypted_data["data"]["trigger"]=="upload_document_page_details":
        all_data=decrypted_data["data"]["all_data"]
        if decrypted_data["data"]["important_documents"]=="joint_photo":
            all_data.update({"joint photo of husband and wife":decrypted_data["data"]["joint_photo_of_h_w"]})
            different_operation.cut_one_user(db,"joint_photo")
            if different_operation.check_entries(db):
                print("truuuuueeeeeeeeeeeeeee")
                response={
                    "screen":"Upload_Document",
                    "data":{
                        "all_data":all_data,
                        "all_important_documents":different_operation.fetch_all_data_from_db(db)
                    }
                }
            else:
                    different_operation.write_all_data_to_json(all_data)
                    response={
                        "screen":"final_page",
                        "data":{
                            "message":"success"
                        }
                     }
        
        elif decrypted_data["data"]["important_documents"]=="applicant_caste_certificate":
            print("bhai tu asuchu ta")
            all_data.update({"applicant caste certificate":decrypted_data["data"]["applicant_caste_certificate"]})
            different_operation.cut_one_user(db,"applicant_caste_certificate")
            if different_operation.check_entries(db):
                print("trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee i am applicant caste certificate ")
                response={
                    "screen":"Upload_Document",
                    "data":{
                        "all_data":all_data,
                        "all_important_documents":different_operation.fetch_all_data_from_db(db)
                    }
                }
            else:
                    different_operation.write_all_data_to_json(all_data)
                    response={
                        "screen":"final_page",
                        "data":{
                            "message":"success"
                        }
                     }
        
        elif decrypted_data["data"]["important_documents"]=="spouse_caste_certificate":
            all_data.update({"spouse caste certificate":decrypted_data["data"]["spouse_caste_certificate"]})
            different_operation.cut_one_user(db,"spouse_caste_certificate")
            if different_operation.check_entries(db):
                print("truuuuueeeeeeeeeeeeeee")
                response={
                    "screen":"Upload_Document",
                    "data":{
                        "all_data":all_data,
                        "all_important_documents":different_operation.fetch_all_data_from_db(db)
                    }
                }
            else:
                    different_operation.write_all_data_to_json(all_data)
                    response={
                        "screen":"final_page",
                        "data":{
                            "message":"success"
                        }
                     }

        elif decrypted_data["data"]["important_documents"]=="applicant_birth_certificate":
            all_data.update({"applicant birth certificate":decrypted_data["data"]["applicant_birth_certificate"]})
            different_operation.cut_one_user(db,"applicant_birth_certificate")
            print("truuuuueeeeeeeeeeeeeee")
            if different_operation.check_entries(db):
                response={
                    "screen":"Upload_Document",
                    "data":{
                        "all_data":all_data,
                        "all_important_documents":different_operation.fetch_all_data_from_db(db)
                    }
                }
            else:
                different_operation.write_all_data_to_json(all_data)
                response={
                    "screen":"final_page",
                    "data":{
                        "message":"success"
                    }
                }
        

    elif decrypted_data["data"]["trigger"]=="send_documents":
        print("I am executed!!!!!!!!!!!!!!!>.................")
        different_operation.send_all_the_details_to_number(decrypted_data["data"]["contact_number"])
        different_operation.send_the_documents(decrypted_data["data"]["contact_number"])
        print("all set")
        response={
            "screen":"final_page",
            "data":{
                "message":"success"
            }
        }

    print(response, type(response))
    encrypted_response = encrypt_response(response, aes_key, iv)
    return PlainTextResponse(content=encrypted_response, media_type='text/plain')