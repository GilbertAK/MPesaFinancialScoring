import numpy as np

class ScoringEngine:
    """Core logic for calculating Credit Scores from M-Pesa logs."""
    
    @staticmethod
    def calculate_base_score(income, expenses, bill_history):
        """
        Uses a weighted formula: 
        Score = (Income Stability * 0.4) + (Bill Payment Consistency * 0.4) + (Savings * 0.2)
        """
        # Feature 1: Debt-to-Income Ratio
        dti = (expenses / income) if income > 0 else 1.0
        dti_score = max(0, 1 - dti) * 400
        
        # Feature 2: Utility Consistency (Simulated binary history)
        bill_score = (sum(bill_history) / len(bill_history)) * 400 if bill_history else 0
        
        # Combine and scale to 300-850 range
        final_score = 300 + (dti_score + bill_score) * (550/800)
        return round(min(850, max(300, final_score)))

    @staticmethod
    def get_risk_category(score):
        if score >= 700: return "LOW"
        if score >= 500: return "MEDIUM"
        return "HIGH"