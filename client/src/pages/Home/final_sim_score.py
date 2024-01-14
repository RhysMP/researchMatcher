res = """
MARIO TAPIA-PACHECO Los Angeles / Santa Barbara, CA • 323-705-9808 • mtap1121@gmail.com • https://www.linkedin.com/in/mariotapiapacheco EDUCATION University of California, Santa Barbara Santa Barbara, CA Bachelor of Science in Statistics and Data Science June 2024 Major GPA: 3.74/4.0, Overall GPA: 3.52/4.0 Relevant coursework: Machine Learning, Regression Analysis, Data Analysis/Visualization, Statistics, Probability, Multivariable Calculus, Linear algebra, Design of Experiments PROJECTS UCSB, Rainbow Six Siege Predictive Modeling | R, Santa Barbara, CA December 2023  Explored 7 machine learning algorithms to find the best performing model on a binary classification problem including random forests, elastic net logistic regression, and support vector machines.  Achieved a classification accuracy of 0.79 and area under the receiver operating curve of 0.75 with final model using 5-fold cross validation and comparisons between various machine learning models. Personal, Austin Animal Center Cats Modeling | Python, Remote December 2023  Constructed 3 feed forward neural networks and benchmarked performance with a random forest model leveraging the Tensorflow and Keras libraries to solve a regression problem.  Performed unsupervised learning with k-means clustering as part of an exploratory data analysis utilizing the scikit-learn library. UCSB, World Happiness Report Data Exploration | Python, Santa Barbara, CA June 2023  Utilized a number of libraries including Altair, Scipy, and Pandas to visualize relationships between variables, perform principal component analysis, and analyze the influence of factors on overall happiness in countries across the world.  Organized results into a readable report using JupyterNotebook, summarized key findings, and narrated the entire process from start to finish to simulate communicating findings to a non-technical crowd. EXPERIENCE House President, SBSHC, Santa Barbara, CA June 2023-Present  Lead bi-weekly house meetings covering a range of topics such as budgets, social events, and member equity to ensure the cooperation of all house members.  Coordinate with other house presidents to maximize member engagement and share different approaches to comply with respective house principles. CAMPUS INVOLVEMENT Member, Data Science Club, UCSB, Santa Barbara, CA September 2022-Present  Engage in weekly meetings that focus on developing programming and statistical skills and networking with data science professionals.  Partnered with other UCSB students on a series of projects in an intermediate group that focuses on applying statistical models to real data sets. Member, Latinx Business Association, UCSB, Santa Barbara, CA February 2023-Present  Engage in weekly professional development workshops to strengthen networking skills and develop a strong work ethic.  Volunteer in monthly community service opportunities that help uplift the Latinx and greater Santa Barbara community. ADDITIONAL INFORMATION Portfolio: https://github.com/mtapia-pacheco Programming: Python, R, SQL in R, Base SAS Libraries: Scikit-learn, Matplotlib, Altair, Pandas, Numpy, Tidymodels, Ggplot, Tidyverse, Dplyr, DBI, RSQLite, Keras Languages: Spanish (Native)
"""

rea = """
Our campus has an immediate opening for an History Teacher. This position provides a student centered, supportive classroom that promotes compassion and tolerance, emotional security, resourcefulness, and independent critical thinking while addressing the individual academic and emotional needs of each student through Fusion's differentiated approach.

Key Responsibilities Include:

Provide a one-to-one teaching experience in the areas of World and U.S. History, Government, and Economics at grade levels 6-12.

Show evidence of adapting and differentiated instruction for all students and a classroom forum for holistic growth.

Maintain complete and accurate records.

Develop and maintain genuine, positive and consistent communication with parents.

Contribute to and benefit from the campus community.

Practice professionalism through ongoing professional development, reflection and continuous improvement.

In addition to subject matter tutoring and teaching, this position includes significant student mentoring.

Other duties as assigned.
"""

# import necessary packages
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
import re
import numpy as np
from fuzzywuzzy import fuzz

def fuzzy_keyword_similarity(keyword1, keyword2):
    return fuzz.token_sort_ratio(keyword1, keyword2) / 100.0

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


cleaned_resume = re.sub(r'[^a-zA-Z\s]', '', res)
cleaned_research = re.sub(r'[^a-zA-Z\s]', '', rea)

# get keywords
stud_keys = get_keywords_student(cleaned_resume)
profe_keys = get_keywords_prof(cleaned_research)


fin_s_keys = [tup[0] for tup in stud_keys if tup[1] >= 0.2]
fin_p_keys = [tup[0] for tup in profe_keys if tup[1] >= 0.2]


# function to get overall cosine similarity between both lists of keywords
def get_sim_score(student_keys, prof_keys):

    # Extract keywords from tuples
    student_keywords = [tup[0] for tup in student_keys if tup[1] >= 0.2]
    prof_keywords = [tup[0] for tup in prof_keys if tup[1] >= 0.2]

    # Check if either set of keywords is empty
    if not student_keywords or not prof_keywords:
        return 0.0

    # Calculate average similarity between each pair of keywords using fuzzy matching
    similarities = []
    for student_kw in student_keywords:
        for prof_kw in prof_keywords:
            similarities.append(fuzzy_keyword_similarity(student_kw, prof_kw))

    # Calculate the average similarity score
    if similarities:
        sim_score = sum(similarities) / len(similarities)
    else:
        sim_score = 0.0

    return sim_score

print(get_sim_score(stud_keys, profe_keys))

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
