# 📱 M-Pesa API Integration Service (MPSA)

## 📌 Overview
MPSA is a robust Python-based integration layer designed to facilitate seamless transactions via the **Safaricom M-Pesa API**. This project demonstrates an enterprise-grade approach to Fintech connectivity, focusing on security, transaction logging, and real-time status monitoring.

Developed with a focus on the East African digital economy, it handles the complexities of Daraja API authentication and STK Push (LNM) flows.

## 🚀 Features
- **OAuth2 Authentication:** Automated token management and lifecycle handling.
- **C2B/B2C Workflows:** Full support for Customer-to-Business and Business-to-Customer transactions.
- **STK Push (LNM):** Instant payment triggers for mobile users.
- **Secure Telemetry:** Real-time logging of API responses and transaction states.
- **Interactive Dashboard:** A Streamlit-powered interface for monitoring payment flows and success rates.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Frontend/Monitoring:** Streamlit
- **API Communication:** Requests / OAuth2
- **Data Handling:** Pandas & NumPy

## 📂 Project Structure
```text
├── app.py              # Main Entry Point (Portfolio Hub)
├── pages/
│   └── 4_M-Pesa_Payment_Service.py  # MPSA Core Logic & UI
├── assets/             # Logos and static files
└── requirements.txt    # Project dependencies