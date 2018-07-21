import pandas as pd
import re
import os

class FeatureExtractor:
    def __init__(self):
        complaints = pd.read_csv('/nlp/complaints.csv')
        self.complaints = {}

        for idx, _ in complaints.iterrows():
            complaint_id = _.policy_related_complaint.lower().replace('-', ' ').replace(' ', '_')
            file_name = 'features_' + complaint_id + '.csv'
            if file_name in os.listdir('/nlp'):
                self.complaints[complaint_id] = {
                    'file': file_name,
                    'complaint': _.policy_related_complaint,
                    'interaction': _.interaction_type,
                    'category': _.category,
                    'sub_classification': _.sub_classification
                }

        self.rules = {}
        for key, value in self.complaints.items():
            rules = pd.read_csv('/nlp/' + value['file'])
            self.rules[key] = rules.regex.tolist()


    def label(self, input_string):
        input_string = input_string.lower()
        result = {}
        for key, rules in self.rules.items():
            for rule in rules:
                if re.search(rule, input_string):
                    result[key] = self.complaints[key]
                    result[key]['rule'] = rule

        return result
