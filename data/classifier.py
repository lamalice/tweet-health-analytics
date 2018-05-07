from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics
import json

def get_data():

   training_set = []
   training_target = []
   testing_set = []

   with open('/home/alice/Developer/tweet-health-analytics/data/20180503/sampleTraining.json' ,encoding='utf-8') as data_file:
       data = json.load(data_file)

       for x in range(len(data)):
           training_set.append(data[x]['full_text'])
           training_target.append(str(data[x]['classification']))
   data_file.close()

   with open("/home/alice/Developer/tweet-health-analytics/data/20180503/extracted_tweets11.json", encoding='utf-8') as testing_file:
       test = json.load(testing_file)

   return training_set, training_target, test

def classifier():
    training_set, training_target, test = get_data()
    tfidf_transformer = TfidfVectorizer(
                                       stop_words='english',
                                       analyzer='word',
                                       lowercase=False,
                                       )

    tf_transformer = tfidf_transformer.fit_transform(training_set)

    test_doc = [
        'I’m so sick homework',
        'I called in sick',
        'I am so sick of homework',
        'I have a fever',
        'I got a fever',
        'Yup I got the fever',
       'Ive been sick for a while',
       'too sick to tweet today in fact my mom is typing this I’m just',
       'Been sick this past week',
       'sick of',
       'They done fired them and put them feds in they life SICK',
       ' Too many Minnesotans are working hard without getting ahead. Things like paid family leave and earned sick time would go a…'
    ]
    multNB = MultinomialNB()

    clf = multNB.fit(tf_transformer, training_target)

    with open("/home/alice/Developer/tweet-health-analytics/data/20180503/extracted_tweets11.json", 'w', encoding='utf-8') as classify:

        for y in range(len(test)):
            test_tweet = test[y]['full_text']
            tf_test = tfidf_transformer.transform([test_tweet])
            predict_proba = clf.predict_proba(tf_test)
            predict_class = clf.predict(tf_test)

            for item in predict_class:
                item = str(item).replace("'", "\"")
                predict_class = item
            test[y]['classication'] = predict_class
            test[y]['proba'] = str(predict_proba[0]).replace(" ", ",")
            # print(test_tweet, ': ', test[y]['proba'], ': ', test[y]['classication'])

            classify.seek(0)
            classify.truncate()
        json.dump(test, classify)

    # accuracy(training_target, predicted)

classifier()