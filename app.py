from pafy import new

# url of video

import requests
from flask import Flask,request,jsonify
# instant created
#video = pafy.new(url)

# print title
app=Flask(__name__)
@app.route('/' ,methods=['POST'])
def helloworld():
    data = request.get_json()

    link = str(data['queryResult']['queryText'])
    video = new(link)
    a = video.getbestaudio()
    print(a.url)
    a1=a.url
    title=video.title
    b = video.getbestvideo()
    print(b.url)
    b1=b.url
    #api_key = "17efd5015e4a69d287611d9121378a8fb1068"
    #api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    #print(api_url)
    # or
    # api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
    # make the request
    #data = requests.get(api_url).json()["url"]
    #if data["status"] == 7:
        # OK, get shortened URL
     #   shortened_url = data["shortLink"]
      #  print("Shortened URL:", shortened_url)
    #else:
     #   print("[!] Error Shortening URL:", data)

    response = {
        "fulfillmentText": "{}                      Audio: {}     Video: {} due to security isssues the link gets invalid in 10 min but you can send me the link again here- @Youtube_audi0_video_bot :currently the bot is in development stage please keep using it".format(title,a1,b1)
    }
    return jsonify(response)

if __name__ == "__main__":
        app.run(debug=True)


video= new("https://youtu.be/a7-x4RfPnQI")
print(video.streams)

print("a=",video.audiostreams)
# print viewcount
b=video.getbestvideo()
print(b.url)
#print(myaudio.url)
print(video.viewcount)

# print author & video length
print(video.author, video.length)

# print duration, likes, dislikes & description
print(video.duration, video.likes, video.description)


