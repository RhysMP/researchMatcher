res = """
Driven thinker exploring the boundaries of Computer Science. National Champion and Gold Medalist in the US Academic Decathlon, TECH Club President at Pierce College, love for computers since the age of 12.

Surface level experience in Cybersecurity, Software development, and Networking.

Recognized by a HackHarvard sponsor for developing an AI platform in under 36 hours to help untrained caretakers support loved ones with Dementia / Alzheimer's. Created an application to incentivize communal volunteering with three others at ShellHacks. Soon attending the 38th Annual Association for the Advancement of Artificial Intelligence (AAAI) Conference.

Looking to hone the skillset to change the world.
"""

rea = """
We are seeking a History teacher to join our team of educators as we engage students in the study of history to provide a relevant and impactful educational experience. The political and social challenges of our current moment have disrupted our discipline of history, and, therefore, the Branson School History Department hopes that our future colleague will join us in bravely addressing these challenges head-on.

As Branson teachers, we are committed continually to revisiting and refining our practice as educators. We feel empowered to create the spaces– physical, academic and emotional – that are needed for our students and to collaborate and partner with experts outside of Branson to enhance the learning for our students. Branson’s strategic plan calls for teachers to design cross-departmental courses. Candidates eager to think of themselves as humanities teachers and looking to work alongside multiple departments are strongly encouraged to apply and to communicate how they have already pursued that passion, if applicable.

Candidates will teach 4 sections of history: 9th grade Modern World History or 10th grade US History, and elective seminars to 11th and 12th graders. In the 9th and 10th grade survey course, the candidate would work closely with colleagues in the Department to plan each unit of study and to evaluate and refine assessment practices. All History teachers report to the History Department Chair and collaborate with all members of the Department.


Duties and Responsibilities:

Teach 4 sections of History, with either two or three preparations.
Collaborate closely with the other teachers of each course to develop units, lessons and assessments. Maintain an understanding of the overall scope and sequence of the History curriculum in order to effectively design a curriculum that aligns with the overall goals of Branson’s History program.
Create a safe and inclusive classroom environment. Treat all students equitably, be sincerely interested in them as individuals, and make a priority of responding to their needs.
Give timely, meaningful, and personal feedback on student performance and participation.
Regularly communicate with the department chair, administration and parents about student progress and concerns as they arise. Respond to evaluations from supervisors and students professionally and constructively.
Serve as a faculty advisor to a group of 8-10 students. Attend all assemblies, faculty meetings, department meetings and required school events.
Be available to meet with students outside of class to provide academic support. Be available to meet with students outside of class to provide social, emotional and mentoring support. Be eager to join a robust community and contribute to community building outside the classroom.

Key Qualifications and Skills:

B.A. or B.S. in History, or related field
Prior teaching experience is ideal, but we will give serious consideration to recent graduates with strong academic credentials and a history of working with high school students.
Commitment to academic excellence, interdisciplinary learning, and advancing the Core Values and Strategic Plan of the school.
Consideration will be given to candidates interested in coaching a sports team.
"""

from transformers import BertTokenizer, BertModel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# create function to use BERT model and extract embeddings from students resume
def get_embeddings_student(resume):
    # tokenize and convert to tensor
    inputs = tokenizer(resume, return_tensors="pt")
    # obtain BERT embeddings
    outputs = model(**inputs)
    # extract embeddings for [CLS] token
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
    return embeddings

# create function to use BERT model and extract embeddings from profs description
def get_embeddings_prof(research):
    # tokenize and convert to tensor
    inputs = tokenizer(research, return_tensors="pt")
    # obtain BERT embeddings
    outputs = model(**inputs)
    # extract embeddings for [CLS] token
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
    return embeddings

cleaned_resume = re.sub(r'[^a-zA-Z\s]', '', res)
cleaned_research = re.sub(r'[^a-zA-Z\s]', '', rea)

# get embeddings
stud_embeddings = get_embeddings_student(cleaned_resume)
profe_embeddings = get_embeddings_prof(cleaned_research)

print(stud_embeddings)
print(profe_embeddings)

# function to get cosine similarity between both sets of embeddings
def get_sim_score(student_embeddings, prof_embeddings):
    # calculate cosine similarity between the two vectors
    dot_product = np.dot(student_embeddings, prof_embeddings)
    norm_product = np.linalg.norm(student_embeddings) * np.linalg.norm(prof_embeddings)

    # calculate the overall similarity score
    sim_score = dot_product / norm_product if norm_product != 0 else 0.0
    return sim_score

print(get_sim_score(stud_embeddings, profe_embeddings))
