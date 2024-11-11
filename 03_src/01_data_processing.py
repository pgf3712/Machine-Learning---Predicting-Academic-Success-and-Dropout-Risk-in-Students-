import pandas as pd


# LIMPIEZA EDA - DATA SET 1, EL MAS IMPORTANTE

def categorize_previous_qualification(value):
    if value < 15:             # Nivel "Bajo"
        return 1
    elif 15 <= value < 30:     # Nivel "Medio" 
        return 2
    else:                     # Nivel "Alto" 
        return 3
    
def categorize_previous_qualification_grade(grade):
    if grade <= 100:
        return 1
    elif 101 <= grade <= 150:
        return 2
    else:
        return 3
    
def categorize_parents_qualification(value):
    if value <= 10:
        return 1
    elif 11 <= value <= 30:
        return 2
    else:
        return 3
    
def categorize_age_at_enrollment(age):
    if age <= 22:
        return 1
    elif 23 <= age <= 35:
        return 2
    else:
        return 3
    


#--------------------------------------------------------------------------------------------------------------------------    

# LIMPIEZA EDA - DATA SET 2

def categorize_exam_score(score):
    if score >= 67:
        return 1  # HIGH
#    elif score >= 65:
#        return 2  # MEDIUM
    else:
        return 0  # LOW

def categorize_quality(Involvement):
    if Involvement == "High":
        return 3  # HIGH
    elif Involvement == "Medium":
        return 2  # MEDIUM
    else:
        return 1  # LOW
    
def categorize_yes_no(answer):
    if answer == "No":
        return 0  # NO
    else:
        return 1  # YES
    
def categorize_school(school):
    if school == "Public":
        return 0  # NO
    else:
        return 1  # YES
    
def categorize_peer_influence(Involvement):
    if Involvement == "Positive":
        return 3  # POSITIVE
    elif Involvement == "Neutral":
        return 2  # NEUTRAL
    else:
        return 1  # NEGATIVE
    
def categorize_Parental_Education_Level(level):
    if level == "Postgraduate":
        return 3  
    elif level == "College":
        return 2  
    else:
        return 1  
    
def categorize_home_distance(distance):
    if distance == "Far":
        return 3  
    elif distance == "Moderate":
        return 2  
    else:
        return 1  
    
def categorize_gender(gender):
    if gender == "Male":
        return 0  # male
    else:
        return 1  # female