import openai
import json
class GetOpinionTopics:
    def __init__(self, theme):
        openai.api_key = "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"
        self.response = json.loads(str(openai.Completion.create( engine="davinci-instruct-beta-v3", prompt="Get the 8 most popular questions about "+theme+" and number them without answers:",   max_tokens=500,  temperature=0.7, presence_penalty=1, frequency_penalty=1)))["choices"][0]["text"]