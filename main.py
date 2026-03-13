from scoring_engine import ScoringEngine
import utils

def test_admin_logic():
    print("--- M-PESA ADMIN SCORING TEST ---")
    # Simulated Applicant Data
    applicant = {
        "name": "John Doe",
        "income": 55000,
        "expenses": 20000,
        "bills": [1, 1, 0, 1, 1] # 1 = paid on time
    }
    
    score = ScoringEngine.calculate_base_score(applicant['income'], applicant['expenses'], applicant['bills'])
    risk = ScoringEngine.get_risk_category(score)
    
    print(f"Applicant: {applicant['name']}")
    print(f"Credit Score: {score}")
    print(f"Decision: {utils.get_status_icon(risk)}")

if __name__ == "__main__":
    test_admin_logic()

