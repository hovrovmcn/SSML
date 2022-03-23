import json
import base64

# Default data loadout
data = {
    "input" : {
        "ssml":""
    },
    "voice" : {
        "languageCode":"ru-ru",
        "name":"ru-RU-Wavenet-A",
        "ssmlGender":"MALE"
    },
    "audioConfig" : {
        "audioEncoding":"MP3",
    },
}

encode_string = open("mp3_base64.mp3", "rb").read()
wav_file = open("temp.mp3", "wb")
decode_string = base64.b64decode(encode_string)
wav_file.write(decode_string)

plain_text = input()

data['input']['ssml'] = '<speak>' + plain_text + '</speak>'

json_string = json.dumps(data)
print(json_string)