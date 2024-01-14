
# import necessary packages
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
import re
import numpy as np

# create function to use BERT model and extract keywords from students resume
def get_keywords_student(resume):
    # initialize BERT model 
    kw_model = KeyBERT(model="distilbert-base-nli-mean-tokens")

    # get keywords 
    keywords = kw_model.extract_keywords(resume, keyphrase_ngram_range=(1, 3), stop_words='english')

    # return keywords
    return keywords

# create function to use BERT model and extract keywords from profs description
def get_keywords_prof(research):
    # initialize BERT model 
    kw_model = KeyBERT(model="distilbert-base-nli-mean-tokens")

    # get keywords 
    keywords = kw_model.extract_keywords(research, keyphrase_ngram_range=(1, 2), stop_words='english')

    # return keywords
    return keywords


#cleaned_resume = re.sub(r'[^a-zA-Z\s]', '', res)
#cleaned_research = re.sub(r'[^a-zA-Z\s]', '', rea)

# get keywords
#stud_keys = get_keywords_student(cleaned_resume)
#profe_keys = get_keywords_prof(cleaned_research)


#fin_s_keys = [tup[0] for tup in stud_keys if tup[1] >= 0.2]
#fin_p_keys = [tup[0] for tup in profe_keys if tup[1] >= 0.2]


# function to get overall cosine similarity between both lists of keywords
def get_sim_score(student_keys, prof_keys):

    # extract keywords from tuples
    student_keys = [tup[0] for tup in student_keys]
    prof_keys = [tup[0] for tup in prof_keys]

    all_keys = student_keys + prof_keys
    
    
    # check if vocabulary is empty or contains only stop words
    if not any(word.isalpha() for word in all_keys):
        return 0.0  

    # create vectors for student and professor keywords
    vector_list1 = np.array([1 if key in student_keys else 0 for key in all_keys])
    vector_list2 = np.array([1 if key in prof_keys else 0 for key in all_keys])

    # calculate cosine similarity between the two vectors
    dot_product = np.dot(vector_list1, vector_list2)
    norm_product = np.linalg.norm(vector_list1) * np.linalg.norm(vector_list2)  # check this

    # calculate the overall similarity score
    sim_score = dot_product / norm_product if norm_product != 0 else 0.0  # this is causing 0.0

    return sim_score

#print(get_sim_score(stud_keys, profe_keys))

# def only_sim_score(student, prof):

#     # student: str of student resume
#     # prof: str of professor abstract
    
#     # clean resume text, get keywords, extract using threshold
#     clean_resume = re.sub(r'[^a-zA-Z\s]', '', student)
#     keys_stud = get_keywords_student(clean_resume)
#     s_keys = [tup[0] for tup in stud_keys if tup[1] >= 0.2]

#     # clean prof text, get keywords, extract using threshold
#     clean_research = re.sub(r'[^a-zA-Z\s]', '', prof)
#     keys_prof = get_keywords_prof(clean_research)
#     p_keys = [tup[0] for tup in profe_keys if tup[1] >= 0.2]

#     return get_sim_score(stud_keys, profe_keys)
