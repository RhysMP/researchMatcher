# import necessary packages
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# create function to use BERT model and extract keywords from students resume
def get_keywords_student(resume):
    # initialize BERT model 
    kw_model = KeyBERT()

    # get keywords 
    keywords = kw_model.extract_keywords(resume, keyphrase_ngram_range=(1, 3), stop_words='english')

    # return keywords
    return keywords

# create function to use BERT model and extract keywords from profs description
def get_keywords_prof(research):
    # initialize BERT model 
    kw_model = KeyBERT()

    # get keywords 
    keywords = kw_model.extract_keywords(research, keyphrase_ngram_range=(1, 2), stop_words='english')

    # return keywords
    return keywords


# # get user input for the file path
# stud_file_path = input("Enter the path to the student.txt file: ")
# prof_file_path = input("Enter the path to the prof.txt file: ")

# # Open the file in read mode
# with open(file_path, 'r') as file:
#     # Read the content of the file into a string
#     file_content = file.read()

# Print or use the content as needed
# print(file_content)



# get resume from user-input (str)
resume = input("> Student text: ")
print(len(resume))
cleaned_resume = re.sub(r'[^a-zA-Z\s]', '', resume)
# get info from user-input (str)
research = input("> Professor text: ")
cleaned_research = re.sub(r'[^a-zA-Z\s]', '', research)

# get keywords
stud_keys = get_keywords_student(cleaned_resume)
profe_keys = get_keywords_prof(cleaned_research)

# final list of keywords after removing scores
# fin_s_keys = []
# fin_p_keys = []

# for tup in stud_keys:
#     if tup[1] >= 0.5:
#         fin_s_keys.append(tup[0])

# for tup in profe_keys:
#     if tup[1] >= 0.5:
#         fin_p_keys.append(tup[0])
fin_s_keys = [tup[0] for tup in stud_keys if tup[1] >= 0.5]
fin_p_keys = [tup[0] for tup in profe_keys if tup[1] >= 0.5]

# function to get overall cosine similarity between both lists of keywords
def get_sim_score(student_keys, prof_keys):
    student_keys = fin_s_keys
    prof_keys = fin_p_keys

    all_keys = fin_s_keys + fin_p_keys

    # create a CountVectorizer to convert the keyword lists into vectors
    vectorizer = CountVectorizer().fit(all_keys)

    # transform each keyword list into a vector
    # vector_list1 = vectorizer.transform(student_keys).toarray()
    # vector_list2 = vectorizer.transform(prof_keys).toarray()
    vector_list1 = vectorizer.transform([student_keys]).toarray()
    vector_list2 = vectorizer.transform([prof_keys]).toarray()

    # calculate cosine similarity between the two vectors
    cosine_sim = cosine_similarity(vector_list1, vector_list2)

    # calculate the overall similarity score
    sim_score = cosine_sim[0][0]

    return sim_score

# print output
print(get_sim_score(stud_keys, profe_keys))
