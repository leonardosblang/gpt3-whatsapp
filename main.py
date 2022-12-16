from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    openai.api_key = "your api key"
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    r = openai.Completion.create(
        model="text-davinci-003",
        prompt=incoming_msg,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    r = r['choices'][0]['text'].replace('\\n', ' ')
    msg.body(r)
    return str(resp)


if __name__ == '__main__':
    app.run()
