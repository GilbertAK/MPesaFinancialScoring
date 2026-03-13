# System thresholds for Credit Scoring
MIN_SCORE = 300
MAX_SCORE = 850
RISK_LEVELS = {
    "LOW": {"color": "#00ff00", "threshold": 700},
    "MEDIUM": {"color": "#ffcc00", "threshold": 500},
    "HIGH": {"color": "#ff4b4b", "threshold": 0}
}

# Average Kenyan Transaction Benchmarks (Monthly)
BENCHMARKS = {
    "avg_income": 45000, # KSh
    "utility_ratio": 0.15,
    "savings_rate": 0.10
}