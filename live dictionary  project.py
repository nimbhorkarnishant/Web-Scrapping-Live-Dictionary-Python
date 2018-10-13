import requests
import json
from bs4 import BeautifulSoup
class credential(object):
    def __init__(self,app_id,app_key,source_language,target_language,URL):
        self.__app_id = 'e47f9dd7'
        self.__app_key = 'cdf73b1bd1d71fdcc45fdeafbccf6a1e'
        self.source_language ='en'
        self.target_language = 'es'
        self.URL = "https://en.oxforddictionaries.com/"
    @property
    def app_id(self):
        return self.__app_id
    @app_id.setter
    def app_id(self,app_id):
        self.__app_id='e47f9dd7'
    @property
    def app_key(self):
        return self.__app_key
    @app_key.setter
    def app_key(self,app_key):
        self.__app_key='cdf73b1bd1d71fdcc45fdeafbccf6a1e'


class search(credential):
    def __init__(self,app_id,app_key,source_language,target_language,URL,word_id):
        super(search,self).__init__(app_id,app_key,source_language,target_language,URL)
        self.word_id=raw_input("enter the word which you want search:")

    def word_meaning(self):
        #word_id=raw_input("Enter the word:")
        word_meaning=[]
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + self.source_language + '/' + self.word_id.lower() + '/translations=' + self.target_language

        r = requests.get(url, headers = {'app_id': self.app_id, 'app_key': self.app_key})

        json_data = json.loads(json.dumps(r.json()))
        try:
            target_word_id = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
            for item in target_word_id:
                for item2 in item['translations']:
                    word_meaning.append(item2['text'])
            print "\t\t\tword meaning:"
            for i in word_meaning:
                print "\t\t\t",i
        except:
            print "sorry! word is not present in dictionary "
            print "try another word or search another thing for your word"


    def synonyms(self):
        ##word_id=raw_input("Enter the word:")
        list_of_synonyms=[]


        try:
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + self.source_language + '/' + self.word_id.lower() + '/synonyms;antonyms'

            r = requests.get(url, headers = {'app_id':self.app_id, 'app_key':self.app_key})

            json_data = json.loads(json.dumps(r.json()))
            target_word_syn = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
        #print target_word_syn

            for item in target_word_syn:
                #print item
                for item2 in item['synonyms']:
                    #print item2
            #print(item2['text'])
                    list_of_synonyms.append(item2['text'])
            print "\t\t\t synonyms of given word:"
            for i in list_of_synonyms:
                print "\t\t\t\t",i

        except:
            message="synonyms of word not availaible"
            print message
            print "try another word or search another thing for your word"

    def word_related(self):
        #word_id=raw_input("Enter the word:")
        list_of_related_words=[]
        try:
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + self.source_language + '/' + self.word_id.lower() + '/synonyms;antonyms'

            r = requests.get(url, headers = {'app_id':self.app_id, 'app_key':self.app_key})

            json_data = json.loads(json.dumps(r.json()))
            target_word_syn = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
            for item in target_word_syn:
                for item2 in item['subsenses']:
                    for item3 in item2['synonyms']:
                    #print('- - -', item3['text'], '\n')
                        list_of_related_words.append(item3['text'])
            print "\t\t\t related word"
            for i in list_of_related_words:
                print "\t\t\t\t",i
        except:
            message="related word of given word is  not availaible"
            print message
            print "try another word or search another thing for your word"

    def sentence(self):
        #word_id=raw_input("Enter the word:")
        list_of_sentence=[]
        try:
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + self.source_language + '/' + self.word_id.lower() + '/sentences'

            r = requests.get(url, headers = {'app_id':self.app_id, 'app_key':self.app_key})
            json_data = json.loads(json.dumps(r.json()))

            target_word_id = json_data['results'][0]['lexicalEntries'][0]['sentences'][0]['text']
    #for item in target_word_id:
        #for item2 in item['sentences']:
            #print item['text']
            print "\t\t\t the sentences of given word"
            list_of_sentence.append(target_word_id)
            for i in list_of_sentence:
                print "\t\t\t\t",i
        except:
            message="The sentence for given word is not availaible"
            print message
            print "try another word or search another thing for your word"


class wordsproperty(credential):
    def weekly_word_watch(self):
        try:
            r = requests.get(self.URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            t=soup.h1
            #print "weekly word Watch"
            print "\t\t\t",t.text,"\t\t\t"
        except:
            print "Error while finding weekly word watch "

    def trending_word(self):
        try:
            r = requests.get(self.URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            soup_page=soup.ol
            si=soup_page.findAll('li')
            #print si
            t1=si[0]
            t2=si[1]
            t3=si[2]
            t4=si[3]
            t5=si[4]
            print "\t\t\tTrending words"
            print "\t\t\t1.",t1.text
            print "\t\t\t2.",t2.text
            print "\t\t\t3.",t3.text
            print "\t\t\t4.",t4.text
            print "\t\t\t5.",t5.text
        except:
            print "Error while find trending words"

    def word_of_the_day(self):
        try:
            r = requests.get(self.URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            m=soup.strong
            s=m.a
            print "\t\t\t WORD OF THE DAY \t\t\t"
            print "\t\t\t   ",s.text,"\t\t\t"
        except:
            print "Error to find word of the day"


def main():
    s=search(0,0,0,0,0,0)
    w=wordsproperty(0,0,0,0,0)


    while True:
        print "press 1:for getting a meaning:"
        print "press 2:for getting a synonyms"
        print "press 3:for gettinng a sentence of given word"
        print "press 4:for getting a word related of given word"
        print "press 5:for getting trending words"
        print "press 6:for getting words of the day"
        print "press 7:for wekkly watch word"
        print "any no for exit:"
        choice=input("enter the choice:")
        if choice==1:
            s.word_meaning()
        elif choice==2:
            s.synonyms()
        elif choice==3:
            s.sentence()
        elif choice==4:
            s.word_related()
        elif choice==5:
            w.trending_word()
        elif choice==6:
            w.word_of_the_day()
        elif choice==7:
            w.weekly_word_watch()
        else:
            print "you exit successfully"
            break

if __name__ == '__main__':
        main()
