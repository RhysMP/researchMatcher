res = """
MARIO TAPIA-PACHECO Los Angeles / Santa Barbara, CA • 323-705-9808 • mtap1121@gmail.com • https://www.linkedin.com/in/mariotapiapacheco EDUCATION University of California, Santa Barbara Santa Barbara, CA Bachelor of Science in Statistics and Data Science June 2024 Major GPA: 3.74/4.0, Overall GPA: 3.52/4.0 Relevant coursework: Machine Learning, Regression Analysis, Data Analysis/Visualization, Statistics, Probability, Multivariable Calculus, Linear algebra, Design of Experiments PROJECTS UCSB, Rainbow Six Siege Predictive Modeling | R, Santa Barbara, CA December 2023  Explored 7 machine learning algorithms to find the best performing model on a binary classification problem including random forests, elastic net logistic regression, and support vector machines.  Achieved a classification accuracy of 0.79 and area under the receiver operating curve of 0.75 with final model using 5-fold cross validation and comparisons between various machine learning models. Personal, Austin Animal Center Cats Modeling | Python, Remote December 2023  Constructed 3 feed forward neural networks and benchmarked performance with a random forest model leveraging the Tensorflow and Keras libraries to solve a regression problem.  Performed unsupervised learning with k-means clustering as part of an exploratory data analysis utilizing the scikit-learn library. UCSB, World Happiness Report Data Exploration | Python, Santa Barbara, CA June 2023  Utilized a number of libraries including Altair, Scipy, and Pandas to visualize relationships between variables, perform principal component analysis, and analyze the influence of factors on overall happiness in countries across the world.  Organized results into a readable report using JupyterNotebook, summarized key findings, and narrated the entire process from start to finish to simulate communicating findings to a non-technical crowd. EXPERIENCE House President, SBSHC, Santa Barbara, CA June 2023-Present  Lead bi-weekly house meetings covering a range of topics such as budgets, social events, and member equity to ensure the cooperation of all house members.  Coordinate with other house presidents to maximize member engagement and share different approaches to comply with respective house principles. CAMPUS INVOLVEMENT Member, Data Science Club, UCSB, Santa Barbara, CA September 2022-Present  Engage in weekly meetings that focus on developing programming and statistical skills and networking with data science professionals.  Partnered with other UCSB students on a series of projects in an intermediate group that focuses on applying statistical models to real data sets. Member, Latinx Business Association, UCSB, Santa Barbara, CA February 2023-Present  Engage in weekly professional development workshops to strengthen networking skills and develop a strong work ethic.  Volunteer in monthly community service opportunities that help uplift the Latinx and greater Santa Barbara community. ADDITIONAL INFORMATION Portfolio: https://github.com/mtapia-pacheco Programming: Python, R, SQL in R, Base SAS Libraries: Scikit-learn, Matplotlib, Altair, Pandas, Numpy, Tidymodels, Ggplot, Tidyverse, Dplyr, DBI, RSQLite, Keras Languages: Spanish (Native)
"""

rea = """
Proven work experience as a Computer Scientist or similar role The ability to think through problems and find solutions with various computer technologies
Experience working with leaders in an organization to identify their needs
Strong programming skills in languages such as Python, Java, C++, or others, depending on the specific field of focus
Proficiency in data analysis, machine learning, or artificial intelligence techniques and tools
Knowledge of software development methodologies and practices, including agile methodologies and version control systems
Familiarity with database management systems and SQL for efficient data storage and retrieval
Excellent problem-solving and critical-thinking abilities to tackle complex computational and mathematical challenges
Strong communication and interpersonal skills to collaborate effectively with team members and stakeholders
Ability to adapt to evolving technologies and learn new programming languages and frameworks quickly
Understanding of computer architecture and operating systems principles
Knowledge of cybersecurity principles and practices to ensure the security of computer systems and data
A bachelor’s or master’s degree in computer science or a related field, or equivalent work experience and certifications.
"""

# import necessary packages
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import pandas as pd
import numpy as np

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


cleaned_resume = re.sub(r'[^a-zA-Z\s]', '', res)
cleaned_research = re.sub(r'[^a-zA-Z\s]', '', rea)

print(type(cleaned_research))

# get keywords
stud_keys = get_keywords_student(cleaned_resume)
profe_keys = get_keywords_prof(cleaned_research)

print(stud_keys)

fin_s_keys = [tup[0] for tup in stud_keys if tup[1] >= 0.2]
fin_p_keys = [tup[0] for tup in profe_keys if tup[1] >= 0.2]

# function to get overall cosine similarity between both lists of keywords
def get_sim_score(student_keys, prof_keys):
    student_keys = fin_s_keys
    prof_keys = fin_p_keys

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
    norm_product = np.linalg.norm(vector_list1) * np.linalg.norm(vector_list2)

    # calculate the overall similarity score
    sim_score = dot_product / norm_product if norm_product != 0 else 0.0

    return sim_score

print(get_sim_score(stud_keys, profe_keys))
