def format_currency(value):
    return f"KSh {value:,.0f}"

def get_status_icon(category):
    icons = {"LOW": "✅ Approved", "MEDIUM": "⚠️ Review Required", "HIGH": "❌ Rejected"}
    return icons.get(category, "❓ Unknown")