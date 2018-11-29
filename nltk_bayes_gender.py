#2018/11
#gender identification
from nltk.corpus import names
import nltk

#have a look at '~/nltk_data/corpora/names/[male.txt, female.txt]'
m_names = [(name, 'male') for name in names.words('male.txt')]
f_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = m_names + f_names

#to make training data mixed
import random
random.shuffle(labeled_names)
print(labeled_names)
print('all:', len(labeled_names))
print('# of male,', len(m_names))
print('# of female,', len(f_names))

#to extract the last letter of a name
def gender_features(word):
    return {'last_letter':word[-1]}

#to make data sets for training, testing(inner validation)
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
n_classifier = nltk.NaiveBayesClassifier.train(train_set)
print('all:', len(featuresets))
print('# of train:', len(train_set))
print('# of test:', 500, round(500/len(featuresets),2))
print('training done\nyour testing is....')

#### testing by input ####
neo_cat=n_classifier.classify(gender_features('Neo'))
print('Neo:',neo_cat)
tri_cat=n_classifier.classify(gender_features('Shrek'))
print('Shrek:',tri_cat)
tri_cat=n_classifier.classify(gender_features('Emma'))
print('Emma:',tri_cat)

### evaluating ####
def evaluate_cat(classifier, names, gender):
    n_s = 0
    for (name, gender) in names:
        n_cat = classifier.classify(gender_features(name))
        if n_cat == gender:
            n_s += 1

    n_names = len(names)
    acc_f = n_s/n_names
    print('[%s] all' %gender , 'success', 'fail')
    print(n_names, n_s, n_names-n_s)
    print('accuracy:', acc_f)

# every running result could be different since suffled.
evaluate_cat(n_classifier, m_names, 'male')
evaluate_cat(n_classifier, f_names, 'female')


