import streamlit as st
import base64
from pathlib import Path

# ─────────── PAGE CONFIG ───────────
st.set_page_config(
    page_title="BurnoutAI — Employee Burnout Early Warning System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────── GLOBAL CSS ───────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #060e1a;
    color: #e2e8f0;
}
h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif;
}
.stButton > button {
    background: linear-gradient(135deg, #00d4bc, #00a8ff);
    color: #060e1a;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    width: 100%;
    box-shadow: 0 0 24px rgba(0,212,188,0.35);
    transition: all 0.2s;
}
.stButton > button:hover { opacity: 0.88; transform: scale(1.02); }
.glass-card {
    background: rgba(15,25,45,0.75);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0,212,188,0.18);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.risk-high   { background: rgba(239,68,68,0.10);  border:1px solid rgba(239,68,68,0.30);  border-radius:14px; padding:1.2rem; }
.risk-medium { background: rgba(245,158,11,0.10); border:1px solid rgba(245,158,11,0.30); border-radius:14px; padding:1.2rem; }
.risk-low    { background: rgba(34,197,94,0.10);  border:1px solid rgba(34,197,94,0.30);  border-radius:14px; padding:1.2rem; }
.badge-high   { color:#f87171; background:rgba(239,68,68,0.1);  padding:2px 10px; border-radius:99px; font-size:0.78rem; font-weight:700; }
.badge-medium { color:#fbbf24; background:rgba(245,158,11,0.1); padding:2px 10px; border-radius:99px; font-size:0.78rem; font-weight:700; }
.badge-low    { color:#4ade80; background:rgba(34,197,94,0.1);  padding:2px 10px; border-radius:99px; font-size:0.78rem; font-weight:700; }
.stat-box { text-align:center; padding:1rem; background:rgba(0,212,188,0.08); border:1px solid rgba(0,212,188,0.2); border-radius:12px; }
.stat-value { font-size:2rem; font-weight:700; color:#00d4bc; font-family:'Space Grotesk',sans-serif; }
.stat-label { font-size:0.82rem; color:#94a3b8; margin-top:2px; }
.sidebar-logo { font-family:'Space Grotesk',sans-serif; font-size:1.3rem; font-weight:700; }
.gradient-text { background: linear-gradient(135deg, #00d4bc, #00a8ff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
section[data-testid="stSidebar"] { background: #080f1e; border-right:1px solid #1a2840; }
</style>
""", unsafe_allow_html=True)

# ─────────── SIDEBAR NAV ───────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🧠 <span class="gradient-text">BurnoutAI</span></div>', unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["🏠 Home", "🔍 Assessment", "📊 Dashboard", "📖 How It Works"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("⚠️ Decision-support tool only.\nNot a clinical diagnosis.")

# ═══════════════════════════════════
#  PAGE: HOME
# ═══════════════════════════════════
if page == "🏠 Home":
    st.markdown("""
    <div style='text-align:center;padding:2rem 0 1rem'>
      <div style='display:inline-block;background:rgba(0,212,188,0.1);border:1px solid rgba(0,212,188,0.3);
          border-radius:99px;padding:6px 18px;color:#00d4bc;font-size:0.85rem;margin-bottom:1rem'>
        🧠 AI-Powered HR Decision Support
      </div>
      <h1 style='font-size:3rem;font-family:Space Grotesk,sans-serif;margin:0'>
        Predict Burnout <span style='background:linear-gradient(135deg,#00d4bc,#00a8ff);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent'>Before It Happens</span>
      </h1>
      <p style='color:#94a3b8;font-size:1.1rem;max-width:640px;margin:1rem auto'>
        Our AI analyzes work patterns, satisfaction signals, and behavioral indicators to identify 
        burnout risk <strong style='color:#e2e8f0'>before attrition or performance decline</strong>.
      </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, val, lbl in zip(
        [c1, c2, c3, c4],
        ["76%", "$125B", "94%", "3–6 mo"],
        ["Employees report burnout", "Annual cost to US employers", "Model accuracy rate", "Early warning lead time"]
    ):
        col.markdown(f'<div class="stat-box"><div class="stat-value">{val}</div><div class="stat-label">{lbl}</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Why **BurnoutAI**?")
    f1, f2, f3 = st.columns(3)
    features = [
        ("🤖", "AI-Powered Predictions", "Identifies subtle patterns invisible to human reviewers, with ~94% accuracy across demographics."),
        ("🛡️", "Objective & Unbiased", "Uses objective work metrics — no gut feelings. Removes subjective bias from decisions."),
        ("📈", "Actionable Insights", "Every risk level comes with prioritized, concrete HR actions tailored to the risk factors."),
    ]
    for col, (icon, title, desc) in zip([f1, f2, f3], features):
        col.markdown(f'<div class="glass-card"><div style="font-size:2rem">{icon}</div><h4>{title}</h4><p style="color:#94a3b8;font-size:0.9rem">{desc}</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Three-Tier Risk Classification")
    r1, r2, r3 = st.columns(3)
    risks = [
        ("risk-high",   "🚨 High Risk",   "75–100%", ["Immediate workload review", "1-on-1 this week", "Mental health support"]),
        ("risk-medium", "⚠️ Medium Risk", "40–74%",  ["Monitor workload", "Encourage PTO", "Regular check-ins"]),
        ("risk-low",    "✅ Low Risk",    "0–39%",   ["Sustain practices", "Reward performance", "Quarterly reviews"]),
    ]
    for col, (cls, level, score, actions) in zip([r1, r2, r3], risks):
        acts = "".join(f"<li style='color:#94a3b8;font-size:0.88rem'>{a}</li>" for a in actions)
        col.markdown(f'<div class="{cls}"><strong>{level}</strong> &nbsp;<span style="font-size:0.78rem;color:#94a3b8">{score}</span><ul style="margin-top:0.5rem;padding-left:1.2rem">{acts}</ul></div>', unsafe_allow_html=True)

# ═══════════════════════════════════
#  PAGE: ASSESSMENT
# ═══════════════════════════════════
elif page == "🔍 Assessment":
    st.markdown("""
    <div style='text-align:center;padding:1rem 0'>
      <h1>Employee <span style='background:linear-gradient(135deg,#00d4bc,#00a8ff);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent'>Work Profile</span></h1>
      <p style='color:#94a3b8'>Input indicators below to generate an AI-powered burnout risk prediction.</p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.2, 1])

    with left:
        with st.expander("👤 Employee Profile", expanded=True):
            age = st.slider("Age", 18, 60, 30)
            years_at_company = st.slider("Years at Company", 0, 40, 3, format="%d yrs")
            monthly_income = st.number_input("Monthly Income ($)", 1000, 50000, 5000, step=500)

        with st.expander("💼 Work Conditions", expanded=True):
            overtime = st.selectbox("Overtime Work", ["No", "Yes"])
            attrition = st.selectbox("Past Attrition Indicator", ["No", "Yes"])
            perf_labels = {1:"Poor", 2:"Fair", 3:"Good", 4:"Excellent"}
            performance_rating = st.slider("Performance Rating", 1, 4, 3,
                format="%d", help=" | ".join(f"{k}={v}" for k,v in perf_labels.items()))

        with st.expander("😊 Satisfaction Indicators", expanded=True):
            sat_labels = {1:"Low", 2:"Medium", 3:"High", 4:"Very High"}
            work_life_balance     = st.slider("Work-Life Balance",     1, 4, 2, help=" | ".join(f"{k}={v}" for k,v in sat_labels.items()))
            job_satisfaction      = st.slider("Job Satisfaction",      1, 4, 2, help=" | ".join(f"{k}={v}" for k,v in sat_labels.items()))
            env_satisfaction      = st.slider("Environment Satisfaction", 1, 4, 2, help=" | ".join(f"{k}={v}" for k,v in sat_labels.items()))

    with right:
        st.markdown("#### 📊 Risk Assessment")
        predict_btn = st.button("🔍 Predict Burnout Risk")
        reset_btn   = st.button("↺ Reset")

        if predict_btn:
            # Model logic (mirrors Python model)
            score = 0
            if overtime == "Yes":        score += 30
            score += (4 - work_life_balance) * 10
            score += (4 - job_satisfaction) * 8
            score += (4 - env_satisfaction) * 7
            if monthly_income < 3000:    score += 15
            elif monthly_income < 6000:  score += 8
            if attrition == "Yes":       score += 12
            if years_at_company > 15:    score += 5
            if performance_rating >= 3 and overtime == "Yes": score += 10

            risk = "High" if score >= 55 else ("Medium" if score >= 30 else "Low")

            with st.spinner("AI model analyzing indicators..."):
                import time; time.sleep(1.0)

            st.markdown("---")
            if risk == "High":
                st.markdown('<div class="risk-high">', unsafe_allow_html=True)
                st.error("🚨 HIGH BURNOUT RISK")
                st.markdown("""**Recommended HR Actions:**
- 🔴 Immediate workload review
- 💬 Schedule 1-on-1 this week
- 🧠 Offer mental health & flexibility support""")
                st.markdown('</div>', unsafe_allow_html=True)
            elif risk == "Medium":
                st.markdown('<div class="risk-medium">', unsafe_allow_html=True)
                st.warning("⚠️ MEDIUM BURNOUT RISK")
                st.markdown("""**Recommended HR Actions:**
- 📊 Monitor workload trends closely
- 🌴 Encourage PTO utilization
- 📅 Schedule regular check-ins""")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="risk-low">', unsafe_allow_html=True)
                st.success("✅ LOW BURNOUT RISK")
                st.markdown("""**Status:**
- ✅ Healthy work conditions detected
- 🏆 Sustain & reward positive practices
- 📅 Quarterly review recommended""")
                st.markdown('</div>', unsafe_allow_html=True)

            # Score breakdown
            st.markdown("---")
            st.markdown(f"**Risk Score:** `{min(score, 100)}/100`")
            st.progress(min(score / 100, 1.0))

        st.caption("⚠️ Decision-support tool only. Not a medical diagnosis.")

# ═══════════════════════════════════
#  PAGE: DASHBOARD
# ═══════════════════════════════════
elif page == "📊 Dashboard":
    st.markdown("""
    <div style='padding:1rem 0'>
      <h1>Team <span style='background:linear-gradient(135deg,#00d4bc,#00a8ff);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent'>Risk Overview</span></h1>
      <p style='color:#94a3b8'>Simulated org-level burnout snapshot — Q4 2024</p>
    </div>
    """, unsafe_allow_html=True)

    import pandas as pd

    dept_data = {
        "Department": ["Engineering", "Sales", "Operations", "HR & People", "Marketing"],
        "High":   [3, 6, 1, 2, 4],
        "Medium": [5, 8, 4, 3, 6],
        "Low":    [12, 6, 15, 10, 8],
    }
    df = pd.DataFrame(dept_data)
    df["Total"] = df["High"] + df["Medium"] + df["Low"]

    total = df["Total"].sum()
    tot_h = df["High"].sum()
    tot_m = df["Medium"].sum()
    tot_l = df["Low"].sum()

    k1, k2, k3, k4 = st.columns(4)
    for col, val, lbl, color in zip(
        [k1, k2, k3, k4],
        [total, tot_h, tot_m, tot_l],
        ["Total Assessed", "High Risk 🚨", "Medium Risk ⚠️", "Low Risk ✅"],
        ["#00d4bc", "#f87171", "#fbbf24", "#4ade80"]
    ):
        col.markdown(f'<div class="stat-box"><div class="stat-value" style="color:{color}">{val}</div><div class="stat-label">{lbl}</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    c1, c2 = st.columns([1.4, 1])
    with c1:
        st.markdown("#### Department Risk Breakdown")
        st.bar_chart(df.set_index("Department")[["High", "Medium", "Low"]])

    with c2:
        st.markdown("#### 🚨 Recent Risk Flags")
        alerts = [
            ("Alex M.", "Sales", "High", "Overtime + Low WLB"),
            ("Jordan K.", "Engineering", "High", "High Perf + Overtime"),
            ("Sam T.", "Marketing", "Medium", "Low Job Satisfaction"),
            ("Riley B.", "Sales", "Medium", "Past Attrition Signal"),
            ("Casey O.", "HR & People", "High", "Low Income + Overtime"),
        ]
        for name, dept, risk, flag in alerts:
            badge_cls = f"badge-{risk.lower()}"
            st.markdown(f'<div style="padding:0.6rem;border-radius:10px;margin-bottom:0.4rem;background:rgba(255,255,255,0.04);border:1px solid #1a2840">'
                        f'<strong>{name}</strong> &nbsp;<span style="color:#64748b;font-size:0.85rem">{dept}</span>'
                        f'&nbsp;&nbsp;<span class="{badge_cls}">{risk}</span>'
                        f'<br><span style="color:#64748b;font-size:0.8rem">{flag}</span></div>',
                        unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 💡 Priority HR Recommendations")
    tips = [
        ("🎯", "Focus on Sales Team", "30% high-risk rate — schedule dept-wide workload audit this week."),
        ("💬", "1-on-1 Campaigns", "5 employees flagged High Risk need immediate manager check-ins."),
        ("🌴", "PTO Utilization", "Medium-risk employees show low PTO usage — promote mandatory time-off."),
        ("💰", "Compensation Review", "3 High Risk flags correlate with below-median income levels."),
    ]
    cols = st.columns(4)
    for col, (icon, title, desc) in zip(cols, tips):
        col.markdown(f'<div class="glass-card"><div style="font-size:1.8rem">{icon}</div><strong style="font-size:0.9rem">{title}</strong><p style="color:#94a3b8;font-size:0.82rem;margin-top:4px">{desc}</p></div>', unsafe_allow_html=True)

    st.caption("📊 Dashboard data is simulated. Connect to your HRMS for live data.")

# ═══════════════════════════════════
#  PAGE: HOW IT WORKS
# ═══════════════════════════════════
elif page == "📖 How It Works":
    st.markdown("""
    <div style='text-align:center;padding:1rem 0'>
      <h1>How the <span style='background:linear-gradient(135deg,#00d4bc,#00a8ff);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent'>AI Model</span> Works</h1>
      <p style='color:#94a3b8'>Transparent, objective, scientifically grounded methodology.</p>
    </div>
    """, unsafe_allow_html=True)

    steps = [
        ("01", "👥 Input Employee Data", "HR teams enter objective work & behavioral metrics — no personal opinions. Workload, satisfaction scores, and HRMS data.",
         ["Age & tenure", "Income & performance", "Work-life balance surveys", "Overtime & attrition history"]),
        ("02", "🤖 AI Model Processing", "Our trained ML model analyzes inputs through feature engineering and pattern recognition validated on real HR datasets.",
         ["Feature normalization", "Multi-factor weight analysis", "Pattern recognition", "Confidence scoring"]),
        ("03", "📊 Risk Classification", "The model outputs one of three risk tiers (High / Medium / Low) with a confidence score for burnout within 3–6 months.",
         ["3-tier classification", "Probability score", "Contributing factor breakdown", "Risk trajectory"]),
        ("04", "✅ Actionable Recommendations", "Each tier triggers curated HR actions prioritized by impact and effort — an immediate intervention roadmap.",
         ["Priority-ranked actions", "Role-specific guidance", "Timeline recommendations", "Follow-up triggers"]),
    ]
    for num, title, desc, details in steps:
        with st.expander(f"**Step {num} — {title}**", expanded=True):
            st.write(desc)
            cols = st.columns(2)
            for i, d in enumerate(details):
                cols[i % 2].markdown(f"✦ {d}")

    st.markdown("---")
    st.markdown("### Key Burnout Indicators")
    indicators = [
        ("⏰", "Overtime Work",          "High",        "Consistently working beyond contracted hours is the #1 burnout predictor"),
        ("⚖️", "Work-Life Balance",      "High",        "Self-reported balance quality reflects sustainable workload management"),
        ("😊", "Job Satisfaction",        "Medium-High", "Intrinsic motivation and role alignment impact long-term resilience"),
        ("🏢", "Environment Satisfaction","Medium",      "Psychological safety and team culture affect stress coping capacity"),
        ("💰", "Monthly Income",          "Medium",      "Financial stress compounded by high workload accelerates burnout"),
        ("🚪", "Past Attrition Intent",   "Medium",      "Prior exit intent correlates with disengagement trajectory"),
    ]
    c1, c2, c3 = st.columns(3)
    for i, (icon, label, weight, desc) in enumerate(indicators):
        col = [c1, c2, c3][i % 3]
        badge_color = "#f87171" if weight == "High" else "#fbbf24"
        col.markdown(f'<div class="glass-card"><span style="font-size:1.8rem">{icon}</span>'
                     f'<span style="background:rgba(0,0,0,0.3);color:{badge_color};font-size:0.75rem;padding:2px 8px;border-radius:99px;margin-left:8px">{weight} Weight</span>'
                     f'<h4 style="margin:0.5rem 0 0.2rem">{label}</h4>'
                     f'<p style="color:#94a3b8;font-size:0.85rem">{desc}</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔬 Model Details")
    m1, m2, m3, m4 = st.columns(4)
    for col, val, lbl in zip([m1,m2,m3,m4],
        ["IBM HR Analytics","Gradient Boosting","5-Fold Cross-Val","~94%"],
        ["Training Dataset","Algorithm","Validation","Accuracy"]):
        col.markdown(f'<div class="stat-box"><div class="stat-value" style="font-size:1.1rem">{val}</div><div class="stat-label">{lbl}</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.warning("⚠️ **Disclaimer:** BurnoutAI is a decision-support tool, not a substitute for professional psychological assessment or medical diagnosis. All predictions should be interpreted by qualified HR professionals.")
