Файл main.py:

import numpy as np

class Risk:
    def __init__(self, name, description, probability, impact, business_type):
        self.name = name
        self.description = description
        self.probability = probability
        self.impact = impact
        self.business_type = business_type
        self.priority = self.calculate_priority()
        
    def calculate_priority(self):
        weight_prob, weight_impact = self.get_weights()
        priority = self.probability * weight_prob + self.impact * weight_impact
        return priority
    
    def get_weights(self):
        if self.business_type == 'banking':
            return 0.6, 0.4
        elif self.business_type == 'retail':
            return 0.5, 0.5
        elif self.business_type == 'it':
            return 0.4, 0.6
        else:
            return 0.5, 0.5

class RiskAssessment:
    def __init__(self):
        self.risks = []

    def add_risk(self, risk):
        self.risks.append(risk)

    def evaluate_risks(self):
        for risk in self.risks:
            risk.priority = risk.calculate_priority()

    def get_risks_report(self):
        report = []
        for risk in self.risks:
            report.append({
                'name': risk.name,
                'description': risk.description,
                'probability': risk.probability,
                'impact': risk.impact,
                'priority': risk.priority,
                'business_type': risk.business_type
            })
        return report

# Пример использования системы для оценки рисков
if __name__ == "__main__":
    assessment = RiskAssessment()
    
    risk1 = Risk('Data Breach', 'Potential data breach affecting customer data', 0.7, 0.9, 'banking')
    risk2 = Risk('Supply Chain Disruption', 'Disruption in supply chain affecting product availability', 0.5, 0.7, 'retail')
    risk3 = Risk('Software Bug', 'Critical bug in software affecting operations', 0.8, 0.6, 'it')
    
    assessment.add_risk(risk1)
    assessment.add_risk(risk2)
    assessment.add_risk(risk3)
    
    assessment.evaluate_risks()

    risks_report = assessment.get_risks_report()
    
    for risk in risks_report:
        print(f"Name: {risk['name']}")
        print(f"Description: {risk['description']}")
        print(f"Probability: {risk['probability']}")
        print(f"Impact: {risk['impact']}")
        print(f"Priority: {risk['priority']}")
        print(f"Business Type: {risk['business_type']}")
        print("="*40)
