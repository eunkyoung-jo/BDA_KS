#2018/05/08
import nltk

#to get make names and female names as data
f_file = open('data/kfemale.txt')
f_namelist = [(l.strip(), 'female') for l in f_file.readlines()]
f_file.close()
# You should fill out below.

klabeled_names = m_namelist + f_namelist

#to make training data mixed
# You should fill out below.

#to extract the last letter of a name
def gender_kfeatures(word):
    return {'last_letter':word[-1]}

#to make data sets for training, testing(inner validation)
# You should fill out below.

print('training done\n')

#### testing by input ####
name='김요욱'
n_cat=kclassifier.classify(gender_kfeatures(name))
print(name, ':', n_cat)
name='전형준'
n_cat=kclassifier.classify(gender_kfeatures(name))
print(name, ':', n_cat)
name='양소희'
n_cat=kclassifier.classify(gender_kfeatures(name))
print(name, ':', n_cat)

### evaluating ####
# You should fill out below.

# every running result could be different since suffled.
evaluate_cat(kclassifier, f_namelist, 'female')
evaluate_cat(kclassifier, m_namelist, 'male')

