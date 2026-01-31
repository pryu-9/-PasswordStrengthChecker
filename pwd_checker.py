import re

def check_strength(password):
    score = 0
    checks = []
    
    if len(password) >= 8: 
        score += 1
        checks.append("✅ Length OK")
    else:
        checks.append("❌ Min 8 chars chahiye")
        
    if re.search(r'[A-Z]', password): 
        score += 1
        checks.append("✅ Uppercase hai")
    else:
        checks.append("❌ Capital letter daalo")
        
    if re.search(r'[a-z]', password): 
        score += 1
        checks.append("✅ Small letters hai")
    else:
        checks.append("❌ Small letters daalo")
        
    if re.search(r'\d', password): 
        score += 1
        checks.append("✅ Number hai")
    else:
        checks.append("❌ Number daalo")
        
    if re.search(r'[!@#$%^&*]', password): 
        score += 1
        checks.append("✅ Special char hai")
    else:
        checks.append("❌ !@#$ daalo")
    
    # Progress bar
    bar = "🟥" * (5-score) + "🟩" * score
    strength = "🟢 STRONG" if score >= 4 else "🟡 MEDIUM" if score >= 3 else "🔴 WEAK"
    
    print(f"\n{bar} {strength} ({score}/5)")
    for check in checks:
        print(f"  {check}")

    if score >= 4: return "🟢 STRONG"
    elif score >= 3: return "🟡 MEDIUM" 
    else: return "🔴 WEAK"

# Main program
while True:
    pw = input("\nEnter password (or 'quit' to exit): ")
    if pw.lower() == 'quit': break
    result = check_strength(pw)
    print(f"Result: {result}")

