### Author : Harsha Yarravarapu
### Version : V.1.0.0
### Date : Feb -25 - 2024
### Problem statement : Evaluating a person's profession 
### Go throgh README.md file to see how features are collected


# Importing packages
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Normalize features
def normalize_data(inp_value, min_value, max_value):
    return (inp_value - min_value) / (max_value - min_value)

# Applying weights to each feature
def apply_weights(inp_value, weight):
    return inp_value * weight

# Calculating fuzzy score using membership func
def fuzzy_score(x, params):
    a, b, c = params
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)
    else:
        return 0.0

# Defining fuzzy variables and their ranges
# I am taking all features on a scale of 0 to 1.0 except years of experience
# this one is kept as the numerical value received.
years_of_experience = ctrl.Antecedent(np.arange(0, 101, 1), 'years_of_experience')
educational_qualifications = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'educational_qualifications')
skillset = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'skillset')
education_institutes = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'education_institutes')
job_title = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'job_title')
previous_company_reputation = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'previous_company_reputation')
innovation_and_technology = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'innovation_and_technology')
impact_on_projects = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'impact_on_projects')
num_successful_projects = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'num_successful_projects')
size_of_teams = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'size_of_teams')
revenue_generated = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'revenue_generated')

professional_value = ctrl.Consequent(np.arange(0, 101, 1), 'professional_value')


# Creating fuzzy sets for each of feature
years_of_experience['low'] = fuzz.trimf(years_of_experience.universe, [0, 0, 5])
years_of_experience['medium'] = fuzz.trimf(years_of_experience.universe, [0, 5, 10])
years_of_experience['high'] = fuzz.trimf(years_of_experience.universe, [5, 10, 10])

educational_qualifications['low'] = fuzz.trimf(educational_qualifications.universe, [0, 0, 0.5])
educational_qualifications['medium'] = fuzz.trimf(educational_qualifications.universe, [0, 0.5, 1])
educational_qualifications['high'] = fuzz.trimf(educational_qualifications.universe, [0.5, 1, 1])

skillset['low'] = fuzz.trimf(skillset.universe, [0, 0, 0.5])
skillset['medium'] = fuzz.trimf(skillset.universe, [0, 0.5, 1])
skillset['high'] = fuzz.trimf(skillset.universe, [0.5, 1, 1])

education_institutes['low'] = fuzz.trimf(education_institutes.universe, [0, 0, 0.5])
education_institutes['medium'] = fuzz.trimf(education_institutes.universe, [0, 0.5, 1])
education_institutes['high'] = fuzz.trimf(education_institutes.universe, [0.5, 1, 1])

job_title['low'] = fuzz.trimf(job_title.universe, [0, 0, 0.5])
job_title['medium'] = fuzz.trimf(job_title.universe, [0, 0.5, 1])
job_title['high'] = fuzz.trimf(job_title.universe, [0.5, 1, 1])

previous_company_reputation['low'] = fuzz.trimf(previous_company_reputation.universe, [0, 0, 0.5])
previous_company_reputation['medium'] = fuzz.trimf(previous_company_reputation.universe, [0, 0.5, 1])
previous_company_reputation['high'] = fuzz.trimf(previous_company_reputation.universe, [0.5, 1, 1])

innovation_and_technology['low'] = fuzz.trimf(innovation_and_technology.universe, [0, 0, 0.5])
innovation_and_technology['medium'] = fuzz.trimf(innovation_and_technology.universe, [0, 0.5, 1])
innovation_and_technology['high'] = fuzz.trimf(innovation_and_technology.universe, [0.5, 1, 1])

impact_on_projects['low'] = fuzz.trimf(impact_on_projects.universe, [0, 0, 0.5])
impact_on_projects['medium'] = fuzz.trimf(impact_on_projects.universe, [0, 0.5, 1])
impact_on_projects['high'] = fuzz.trimf(impact_on_projects.universe, [0.5, 1, 1])

num_successful_projects['low'] = fuzz.trimf(num_successful_projects.universe, [0, 0, 0.5])
num_successful_projects['medium'] = fuzz.trimf(num_successful_projects.universe, [0, 0.5, 1])
num_successful_projects['high'] = fuzz.trimf(num_successful_projects.universe, [0.5, 1, 1])

size_of_teams['low'] = fuzz.trimf(size_of_teams.universe, [0, 0, 0.5])
size_of_teams['medium'] = fuzz.trimf(size_of_teams.universe, [0, 0.5, 1])
size_of_teams['high'] = fuzz.trimf(size_of_teams.universe, [0.5, 1, 1])

revenue_generated['low'] = fuzz.trimf(revenue_generated.universe, [0, 0, 0.5])
revenue_generated['medium'] = fuzz.trimf(revenue_generated.universe, [0, 0.5, 1])
revenue_generated['high'] = fuzz.trimf(revenue_generated.universe, [0.5, 1, 1])



# I have defined the fuzzy rules(limited to 3 in this case)
# We can design the rules based on the evaluation criteria
# Here below i have taken years of experience as the driving feature for a profession evaluation -
# for a CEO role where years of experience plays a key role. So this feature will get a major chunk in determing
# the membership function values
# These followed by the other rules and the priority order of features 
rule1 = ctrl.Rule(
    (years_of_experience['low'] & educational_qualifications['low']) |
    (years_of_experience['medium'] & educational_qualifications['medium']) |
    (years_of_experience['high'] & educational_qualifications['high']),
    professional_value['low']
)

rule2 = ctrl.Rule(
    (skillset['low'] | skillset['medium']) &
    (education_institutes['low'] | education_institutes['medium'] | education_institutes['high']) &
    (job_title['low'] | job_title['medium']) &
    (previous_company_reputation['low'] | previous_company_reputation['medium']) &
    (innovation_and_technology['high'] | innovation_and_technology['medium']) &
    (impact_on_projects['high'] | impact_on_projects['medium']) &
    (num_successful_projects['medium'] | num_successful_projects['high']) &
    (size_of_teams['medium'] | size_of_teams['high']) &
    (revenue_generated['medium'] | revenue_generated['high']),
    professional_value['medium']
)

rule3 = ctrl.Rule(
    (skillset['high']) &
    (education_institutes['high']) &
    (previous_company_reputation['high']) &
    (innovation_and_technology['high']) &
    (impact_on_projects['high']) &
    (num_successful_projects['high']) &
    (size_of_teams['high']) &
    (revenue_generated['high']),
    professional_value['high']
)

# Create the control system
professional_value_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
professional_value_simulation = ctrl.ControlSystemSimulation(professional_value_ctrl)

# Calculating the professional value
def calculate_professional_value(features_values, weights):
    normalized_features = [normalize_data(value, min_val, max_val) for value, min_val, max_val in zip(features_values, min_values, max_values)]

    weighted_features = [apply_weights(value, weight) for value, weight in zip(normalized_features, weights)]

    for i in range(0, len(weighted_features) - 1):
        professional_value_simulation.input[f'feature_{i+1}'] = weighted_features[i]

    professional_value_simulation.compute()

    final_valuation = professional_value_simulation.output['professional_value']
    
    normalized_final_valuation = normalize_data(final_valuation, min_valuation, max_valuation)

    return normalized_final_valuation

# consider below as an example
features_values = [8, 0.8, 0.5, 0.9, 0.4, 0.7, 0.9, 0.8, 0.6, 0.8, 0.7]  # I have taken these values as an exaple
weights = [0.10, 0.08, 0.12, 0.07, 0.09, 0.08, 0.15, 0.13, 0.11, 0.09, 0.07]
min_values = [0,0,0,0,0,0,0,0,0,0,]  
max_values = [10,1,1,1,1,1,1,1,1,1,1] 
min_valuation = 0
max_valuation = 100

result = calculate_professional_value(features_values, weights)
print(f"Final Professional Valuation: {result:.2f}")
