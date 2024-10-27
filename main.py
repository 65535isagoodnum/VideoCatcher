from util import *


json_data = load_source()

response = connect(json_data["urls"][5], headers=get_header())
print(response.status_code)

data = json.loads(response.content)

video_response = connect(data['data']['dash']['video'][0]['base_url'], headers=get_header())
audio_response = connect(data['data']['dash']['audio'][0]['base_url'], headers=get_header())

print(video_response.status_code)
print(audio_response.status_code)

print(video_response.text)

# save("tang6", video_response.content, audio_response.content)
