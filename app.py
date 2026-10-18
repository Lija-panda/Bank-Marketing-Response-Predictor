
import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Marketing Intelligence",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("marketing_response_model.pkl")


model = load_model()

# Optimized threshold
THRESHOLD = 0.70


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(99,102,241,0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(139,92,246,0.10),
            transparent 30%
        ),
        #080b14;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

.hero {
    padding: 30px;
    border-radius: 24px;
    background:
        linear-gradient(
            135deg,
            rgba(79,70,229,0.25),
            rgba(124,58,237,0.12)
        );
    border: 1px solid rgba(139,92,246,0.25);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 17px;
    color: #aab0c0;
}

.metric-card {
    background: rgba(25,29,43,0.9);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    min-height: 120px;
}

.metric-title {
    color: #9299aa;
    font-size: 14px;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
}

.section-title {
    font-size: 25px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 15px;
}

.footer {
    text-align: center;
    color: #6f7688;
    padding: 30px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎯 AI Marketing")

    st.markdown("---")

    st.markdown("### 🧠 Final Model")

    st.info(
        """
        **Logistic Regression**

        Selected because it provides better recall for identifying
        potential campaign responders.
        """
    )

    st.markdown("### ⚙️ Decision Threshold")

    st.metric(
        "Response Threshold",
        "70%"
    )

    st.caption(
        "Probability ≥ 70% is classified as a likely responder."
    )

    st.markdown("---")

    st.markdown("### 📊 Validation Results")

    st.metric("Accuracy", "83.16%")
    st.metric("Precision", "36.17%")
    st.metric("Recall", "64.66%")
    st.metric("F1 Score", "46.39%")

    st.markdown("---")

    st.caption(
        "Marketing Response Prediction System"
    )


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🎯 AI-Powered Marketing Intelligence
</div>

<div class="hero-subtitle">
Predict customer response before spending your marketing budget.
Use machine learning to identify high-potential customers and
prioritize campaign outreach.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# TOP METRICS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">MODEL</div>
        <div class="metric-value">Logistic ML</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">ACCURACY</div>
        <div class="metric-value">83.16%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">RECALL</div>
        <div class="metric-value">64.66%</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">BEST F1</div>
        <div class="metric-value">50.07%</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3 = st.tabs([
    "🎯 Customer Prediction",
    "📊 Model Intelligence",
    "ℹ️ About Project"
])


# ============================================================
# TAB 1 — CUSTOMER PREDICTION
# ============================================================

with tab1:

    st.markdown(
        '<div class="section-title">👤 Customer Profile</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    # --------------------------------------------------------
    # CUSTOMER INFORMATION
    # --------------------------------------------------------

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

        job = st.selectbox(
            "Job",
            [
                "admin.",
                "blue-collar",
                "entrepreneur",
                "housemaid",
                "management",
                "retired",
                "self-employed",
                "services",
                "student",
                "technician",
                "unemployed",
                "unknown"
            ]
        )

        marital = st.selectbox(
            "Marital Status",
            [
                "divorced",
                "married",
                "single",
                "unknown"
            ]
        )

        education = st.selectbox(
            "Education",
            [
                "basic.4y",
                "basic.6y",
                "basic.9y",
                "high.school",
                "illiterate",
                "professional.course",
                "university.degree",
                "unknown"
            ]
        )

    # --------------------------------------------------------
    # FINANCIAL INFORMATION
    # --------------------------------------------------------

    with col2:

        default = st.selectbox(
            "Credit Default",
            ["no", "yes", "unknown"]
        )

        housing = st.selectbox(
            "Housing Loan",
            ["no", "yes", "unknown"]
        )

        loan = st.selectbox(
            "Personal Loan",
            ["no", "yes", "unknown"]
        )

        contact = st.selectbox(
            "Contact Type",
            ["cellular", "telephone"]
        )

    # --------------------------------------------------------
    # CAMPAIGN INFORMATION
    # --------------------------------------------------------

    with col3:

        month = st.selectbox(
            "Last Contact Month",
            [
                "jan",
                "feb",
                "mar",
                "apr",
                "may",
                "jun",
                "jul",
                "aug",
                "sep",
                "oct",
                "nov",
                "dec"
            ]
        )

        day_of_week = st.selectbox(
            "Day of Week",
            ["mon", "tue", "wed", "thu", "fri"]
        )

        campaign = st.number_input(
            "Campaign Contacts",
            min_value=1,
            max_value=50,
            value=1
        )


    # ========================================================
    # PREVIOUS CAMPAIGN
    # ========================================================

    st.markdown(
        '<div class="section-title">📞 Previous Campaign Intelligence</div>',
        unsafe_allow_html=True
    )

    p1, p2, p3 = st.columns(3)

    with p1:

        pdays = st.number_input(
            "Days Since Previous Contact",
            min_value=0,
            max_value=1000,
            value=999
        )

    with p2:

        previous = st.number_input(
            "Previous Contacts",
            min_value=0,
            max_value=50,
            value=0
        )

    with p3:

        poutcome = st.selectbox(
            "Previous Campaign Outcome",
            [
                "failure",
                "nonexistent",
                "success"
            ]
        )


    # ========================================================
    # ECONOMIC DATA
    # ========================================================

    st.markdown(
        '<div class="section-title">📈 Economic Environment</div>',
        unsafe_allow_html=True
    )

    e1, e2, e3 = st.columns(3)

    with e1:

        emp_var_rate = st.number_input(
            "Employment Variation Rate",
            value=1.1
        )

    with e2:

        cons_price_idx = st.number_input(
            "Consumer Price Index",
            value=93.994
        )

    with e3:

        cons_conf_idx = st.number_input(
            "Consumer Confidence Index",
            value=-36.4
        )

    e4, e5 = st.columns(2)

    with e4:

        euribor3m = st.number_input(
            "Euribor 3 Month",
            value=4.857
        )

    with e5:

        nr_employed = st.number_input(
            "Number of Employees",
            value=5191.0
        )


    st.markdown("")


    # ========================================================
    # PREDICT BUTTON
    # ========================================================

    predict = st.button(
        "🚀 ANALYZE CUSTOMER",
        use_container_width=True,
        type="primary"
    )


    # ========================================================
    # PREDICTION
    # ========================================================

    if predict:

        # ----------------------------------------------------
        # CREATE INPUT DATA
        # ----------------------------------------------------

        input_data = pd.DataFrame({

            "age": [age],

            "job": [job],

            "marital": [marital],

            "education": [education],

            "default": [default],

            "housing": [housing],

            "loan": [loan],

            "contact": [contact],

            "month": [month],

            "day_of_week": [day_of_week],

            "campaign": [campaign],

            "pdays": [pdays],

            "previous": [previous],

            "poutcome": [poutcome],

            "emp.var.rate": [emp_var_rate],

            "cons.price.idx": [cons_price_idx],

            "cons.conf.idx": [cons_conf_idx],

            "euribor3m": [euribor3m],

            "nr.employed": [nr_employed]

        })


        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        probability = model.predict_proba(
            input_data
        )[0][1]

        probability_percentage = probability * 100


        # ----------------------------------------------------
        # CLASSIFICATION
        # ----------------------------------------------------

        if probability >= THRESHOLD:

            prediction = 1

        else:

            prediction = 0


        # ----------------------------------------------------
        # LEAD SCORE
        # ----------------------------------------------------

        lead_score = round(probability_percentage)


        if lead_score >= 70:

            lead_status = "🔥 HOT LEAD"

        elif lead_score >= 40:

            lead_status = "🟡 WARM LEAD"

        else:

            lead_status = "🔵 COLD LEAD"


        # ====================================================
        # AI DECISION
        # ====================================================

        st.markdown("---")

        st.markdown("## 🎯 AI Decision")


        result_col, score_col = st.columns([2, 1])


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        with result_col:

            if prediction == 1:

                st.success(
                    f"""
                    ## ✅ LIKELY TO RESPOND

                    ### {probability_percentage:.2f}%

                    This customer has a high predicted probability
                    of responding to the marketing campaign.
                    """
                )

            else:

                st.error(
                    f"""
                    ## ❌ UNLIKELY TO RESPOND

                    ### {probability_percentage:.2f}%

                    This customer has a low predicted probability
                    of responding to the marketing campaign.
                    """
                )


        # ----------------------------------------------------
        # LEAD SCORE
        # ----------------------------------------------------

        with score_col:

            st.metric(
                "🎯 Lead Score",
                f"{lead_score} / 100"
            )

            if lead_score >= 70:

                st.success("🔥 HOT LEAD")

            elif lead_score >= 40:

                st.warning("🟡 WARM LEAD")

            else:

                st.info("🔵 COLD LEAD")


        # ====================================================
        # PROBABILITY
        # ====================================================

        st.markdown("### 📊 Response Probability")

        st.progress(
            float(probability)
        )

        st.caption(
            f"Model probability: {probability_percentage:.2f}%"
        )

        st.caption(
            f"Decision threshold: {THRESHOLD * 100:.0f}%"
        )


        # ====================================================
        # AI RECOMMENDATION
        # ====================================================

        st.markdown("### 💡 AI Marketing Recommendation")


        if lead_score >= 70:

            st.success(
                """
                **HIGH-PRIORITY CUSTOMER**

                🔥 Prioritize this customer immediately.

                • Use personalized communication  
                • Consider a targeted offer  
                • Contact through the preferred channel  
                • Allocate higher campaign priority
                """
            )

        elif lead_score >= 40:

            st.warning(
                """
                **MEDIUM-PRIORITY CUSTOMER**

                🟡 This customer shows moderate response potential.

                • Use personalized messaging  
                • Test different offers  
                • Monitor engagement  
                • Avoid excessive repeated contact
                """
            )

        else:

            st.info(
                """
                **LOW-PRIORITY CUSTOMER**

                🔵 This customer has lower predicted response potential.

                • Reduce unnecessary outreach  
                • Focus budget on higher-scoring customers  
                • Use lower-cost communication
                """
            )


        # ====================================================
        # CUSTOMER SNAPSHOT
        # ====================================================

        st.markdown("### 📋 Customer Snapshot")

        s1, s2, s3, s4 = st.columns(4)

        with s1:

            st.metric(
                "Age",
                age
            )

        with s2:

            st.metric(
                "Job",
                job
            )

        with s3:

            st.metric(
                "Contact",
                contact
            )

        with s4:

            st.metric(
                "Previous Outcome",
                poutcome
            )


        # ====================================================
        # CAMPAIGN STRATEGY
        # ====================================================

        st.markdown("### 🚀 Suggested Campaign Strategy")


        if lead_score >= 70:

            st.success(
                """
                **🔥 HIGH-PRIORITY STRATEGY**

                Personalized communication  
                Immediate campaign outreach  
                Tailored promotional offer  
                Preferred contact channel
                """
            )

        elif lead_score >= 40:

            st.warning(
                """
                **🟡 MEDIUM-PRIORITY STRATEGY**

                Personalized messaging  
                Test offer variations  
                Monitor customer engagement
                """
            )

        else:

            st.info(
                """
                **🔵 LOW-PRIORITY STRATEGY**

                Reduce unnecessary outreach  
                Focus resources on higher-scoring customers  
                Use broader, lower-cost communication
                """
            )


# ============================================================
# TAB 2 — MODEL INTELLIGENCE
# ============================================================

with tab2:

    st.markdown(
        '<div class="section-title">🧠 Model Intelligence</div>',
        unsafe_allow_html=True
    )

    st.write(
        "The project compares multiple machine-learning approaches "
        "and selects the model based on the marketing objective."
    )


    m1, m2 = st.columns(2)


    # --------------------------------------------------------
    # LOGISTIC REGRESSION
    # --------------------------------------------------------

    with m1:

        st.markdown("### 🧠 Logistic Regression")

        st.metric(
            "Accuracy",
            "83.16%"
        )

        st.metric(
            "Recall",
            "64.66%"
        )

        st.metric(
            "F1 Score",
            "46.39%"
        )

        st.success(
            "🏆 SELECTED FOR DEPLOYMENT"
        )


    # --------------------------------------------------------
    # RANDOM FOREST
    # --------------------------------------------------------

    with m2:

        st.markdown("### 🌲 Random Forest")

        st.metric(
            "Accuracy",
            "89.48%"
        )

        st.metric(
            "Recall",
            "28.13%"
        )

        st.metric(
            "F1 Score",
            "37.58%"
        )

        st.warning(
            "Higher accuracy, but much lower recall"
        )


    st.markdown("---")


    # ========================================================
    # WHY LOGISTIC REGRESSION
    # ========================================================

    st.markdown("### ⚖️ Why Logistic Regression?")


    st.info(
        """
        Random Forest achieved higher overall accuracy.

        However, this project is not simply about predicting the
        majority class.

        The business objective is to identify customers who may
        respond to the campaign.

        Logistic Regression achieved substantially higher recall
        for the response class.

        Therefore, Logistic Regression was selected as the more
        suitable model for this marketing problem.
        """
    )


    # ========================================================
    # THRESHOLD OPTIMIZATION
    # ========================================================

    st.markdown("### 🎚️ Threshold Optimization")


    threshold_data = pd.DataFrame({

        "Threshold": [
            "0.30",
            "0.40",
            "0.50",
            "0.60",
            "0.70"
        ],

        "Precision (%)": [
            15.98,
            25.97,
            36.17,
            41.72,
            47.19
        ],

        "Recall (%)": [
            86.75,
            73.49,
            64.66,
            61.10,
            53.34
        ],

        "F1 Score (%)": [
            26.97,
            38.38,
            46.39,
            49.58,
            50.07
        ]

    })


    st.dataframe(
        threshold_data,
        use_container_width=True,
        hide_index=True
    )


    st.success(
        "🏆 0.70 was selected because it produced the highest F1 score among the tested thresholds."
    )


# ============================================================
# TAB 3 — ABOUT PROJECT
# ============================================================

with tab3:

    st.markdown(
        '<div class="section-title">ℹ️ About This Project</div>',
        unsafe_allow_html=True
    )


    st.markdown("""
    ## 🎯 Project Objective

    This system predicts whether a customer is likely to respond
    to a marketing campaign using historical customer,
    campaign and economic information.


    ## 🔄 Machine Learning Pipeline

    **Customer Data**

    ↓

    **Data Preprocessing**

    ↓

    **Categorical Encoding**

    ↓

    **Model Training**

    ↓

    **Logistic Regression**

    ↓

    **Probability Prediction**

    ↓

    **Threshold Optimization**

    ↓

    **Marketing Decision**


    ## 📊 Dataset

    The project uses the **Bank Marketing dataset**.

    The dataset contains customer demographics, campaign history
    and economic indicators.


    ## 💼 Real-World Application

    Instead of contacting every customer equally, businesses can
    use predicted response probability to prioritize customers.

    This can help reduce unnecessary outreach and allocate
    marketing resources more efficiently.


    ## 🧠 Key Insight

    **Accuracy alone is not enough.**

    Because the response class is smaller than the non-response
    class, metrics such as recall, precision and F1-score are
    important when evaluating the model.
    """)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

🎯 AI-Powered Marketing Response Prediction System

<br><br>

Built using Python • Pandas • Scikit-learn • Streamlit

<br><br>

Machine Learning for Smarter Marketing Decisions

</div>
""", unsafe_allow_html=True)
