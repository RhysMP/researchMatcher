res = """
MARIO TAPIA-PACHECO Los Angeles / Santa Barbara, CA • 323-705-9808 • mtap1121@gmail.com • https://www.linkedin.com/in/mariotapiapacheco EDUCATION University of California, Santa Barbara Santa Barbara, CA Bachelor of Science in Statistics and Data Science June 2024 Major GPA: 3.74/4.0, Overall GPA: 3.52/4.0 Relevant coursework: Machine Learning, Regression Analysis, Data Analysis/Visualization, Statistics, Probability, Multivariable Calculus, Linear algebra, Design of Experiments PROJECTS UCSB, Rainbow Six Siege Predictive Modeling | R, Santa Barbara, CA December 2023  Explored 7 machine learning algorithms to find the best performing model on a binary classification problem including random forests, elastic net logistic regression, and support vector machines.  Achieved a classification accuracy of 0.79 and area under the receiver operating curve of 0.75 with final model using 5-fold cross validation and comparisons between various machine learning models. Personal, Austin Animal Center Cats Modeling | Python, Remote December 2023  Constructed 3 feed forward neural networks and benchmarked performance with a random forest model leveraging the Tensorflow and Keras libraries to solve a regression problem.  Performed unsupervised learning with k-means clustering as part of an exploratory data analysis utilizing the scikit-learn library. UCSB, World Happiness Report Data Exploration | Python, Santa Barbara, CA June 2023  Utilized a number of libraries including Altair, Scipy, and Pandas to visualize relationships between variables, perform principal component analysis, and analyze the influence of factors on overall happiness in countries across the world.  Organized results into a readable report using JupyterNotebook, summarized key findings, and narrated the entire process from start to finish to simulate communicating findings to a non-technical crowd. EXPERIENCE House President, SBSHC, Santa Barbara, CA June 2023-Present  Lead bi-weekly house meetings covering a range of topics such as budgets, social events, and member equity to ensure the cooperation of all house members.  Coordinate with other house presidents to maximize member engagement and share different approaches to comply with respective house principles. CAMPUS INVOLVEMENT Member, Data Science Club, UCSB, Santa Barbara, CA September 2022-Present  Engage in weekly meetings that focus on developing programming and statistical skills and networking with data science professionals.  Partnered with other UCSB students on a series of projects in an intermediate group that focuses on applying statistical models to real data sets. Member, Latinx Business Association, UCSB, Santa Barbara, CA February 2023-Present  Engage in weekly professional development workshops to strengthen networking skills and develop a strong work ethic.  Volunteer in monthly community service opportunities that help uplift the Latinx and greater Santa Barbara community. ADDITIONAL INFORMATION Portfolio: https://github.com/mtapia-pacheco Programming: Python, R, SQL in R, Base SAS Libraries: Scikit-learn, Matplotlib, Altair, Pandas, Numpy, Tidymodels, Ggplot, Tidyverse, Dplyr, DBI, RSQLite, Keras Languages: Spanish (Native)
"""

rea = """
Scaling up training datasets and model parameters have benefited neural network-based language models, but also present challenges like distributed compute, input data bottlenecks and reproducibility of results. We introduce two simple and scalable software libraries that simplify these issues: t5x enables training large language models at scale, while seqio enables reproducible input and evaluation pipelines. These open-source libraries have been used to train models with hundreds of billions of parameters on multiterabyte datasets. Configurations and instructions for T5-like and GPT-like models are also provided. The libraries can be found at https://github.com/google-research/t5x and https://github.com/google/seqio. Keywords: Large language models, data parallelism, model parallelism, data processing
"""

# import necessary packages
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import pandas as pd

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

fin_s_keys = [tup[0] for tup in stud_keys if tup[1] >= 0.3]
fin_p_keys = [tup[0] for tup in profe_keys if tup[1] >= 0.3]

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
    sim_score = cosine_sim.mean()

    return sim_score

# print output
print(get_sim_score(stud_keys, profe_keys))
