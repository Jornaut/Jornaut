import openai
import json
import random
class GetOpinionFormed:
    def __init__(self, theme, topics):
        self.theme = theme
        self.topics = topics
        self.writers = [0,1,2,3]
        self.response = ""
        openai.api_key = "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"
        self.GetWriter()
        writer = self.writers[random.randint(0, len(self.writers)-1)]
        self.text = json.loads(str(openai.Completion.create( engine="davinci-instruct-beta-v3", prompt='''Write a long op-ed, as you was '''+writer[1]+''', the theme of the op-ed is about '''+self.theme+''', and you need to make an introducion about the theme - with a strong opinion, answer the following numbered (1 up to 8) questions and conclude in the final paragraph the impact of the '''+self.theme+''' to the US :'''+self.topics+'''The op-ed is here:''',   max_tokens=700,  temperature=0.7, presence_penalty=1, frequency_penalty=1)))["choices"][0]["text"]
        self.response = '''<div class="According">'''+"According to "+writer[0]+''':</div><div class="oped">'''+self.text+'''</div>'''
    def GetWriter(self):
        self.writers[0] = ["Manoela","a young lady, left-wing, sports lover, from new york"]
        self.writers[1] = ["Marcelo", "a chatty 35-year-old Texas-born Republican politician"]
        self.writers[2] = ["Natália", "a lesbian 80-year-old California-born conservative astrologer"]
        self.writers[3] = ["Guilherme", "a nerd gamer, 18-year-old Alabama-born anarchist singer"]