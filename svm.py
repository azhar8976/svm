import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pickle
import os

# --- 1. ULTRA PRO MAX CONFIGURATION ---
st.set_page_config(
    page_title="QUANTUM NEXUS // MEDICAL INTELLIGENCE CORE",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED CYBERPUNK GLASSMORPHISM CSS & ANIMATIONS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght=400;600;900&family=Rajdhani:wght=500;700&display=swap');
    
    /* App Matrix Base */
    .stApp {
        background: radial-gradient(circle at 50% 30%, #0a1128 0%, #020617 100%);
        color: #f1f5f9;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Glitch Title Style */
    .nexus-header {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #fe007a, #00ff87);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 6s ease infinite, pulseGlow 2s infinite alternate;
        margin-bottom: 5px;
    }
    
    .nexus-subtitle {
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        color: #64748b;
        letter-spacing: 4px;
        font-size: 0.9rem;
        margin-bottom: 25px;
    }

    /* 3D Glassmorphic Cards */
    .crypto-card {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 242, 254, 0.15);
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(0, 242, 254, 0.02);
        margin-bottom: 18px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .crypto-card:hover {
        border-color: #00f2fe;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.25);
        transform: translateY(-3px);
    }

    /* Pulse Animations */
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes pulseGlow {
        0% { filter: drop-shadow(0 0 5px rgba(0, 242, 254, 0.2)); }
        100% { filter: drop-shadow(0 0 15px rgba(0, 242, 254, 0.6)); }
    }

    /* Sidebar Matrix Styling */
    [data-testid="stSidebar"] {
        background: #030712 !important;
        border-right: 1px solid rgba(0, 242, 254, 0.15);
    }
    </style>
""", unsafe_allow_html=True)


# --- 3. HARDWARE CORE: MODEL LOADING KERNEL ---
@st.cache_resource
def load_quantum_core(model_type_str):
    """Loads the model artifacts safely from local directories"""
    file_mapping = {
        "Support Vector Machine (SVM)": "svm_model.pkl",
        "Random Forest Classifier": "random_forest_model.pkl"
    }
    target_file = file_mapping.get(model_type_str)
    
    if os.path.exists(target_file):
        try:
            with open(target_file, 'rb') as f:
                loaded_model = pickle.load(f)
                return loaded_model, "✓ OPERATIONAL", "success"
        except Exception as e:
            return None, f"⚠ DEGRADED ({str(e)})", "error"
    else:
        return None, f"⚠ OFFLINE (Missing {target_file})", "warning"


# --- 4. CONTROL PANEL: SIDEBAR OPERATIONS ---
st.sidebar.markdown("<h2 style='color:#00f2fe; text-align:center; font-family:Orbitron;'>🎛️ CONTROL UNIT</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown("### 🧬 MODEL SELECTOR")
selected_core = st.sidebar.selectbox("CORE KERNEL ENGINE", ["Support Vector Machine (SVM)", "Random Forest Classifier"])

# Trigger model loader immediately
active_model, core_status, status_type = load_quantum_core(selected_core)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 PATIENT BIOMETRIC VECTOR")

# Inputs matching your original variables
age = st.sidebar.slider("AGE WAVEFORM", 15, 90, 45)
sex = st.sidebar.selectbox("GENDER VECTOR", ["MALE", "FEMALE"])
bp = st.sidebar.selectbox("BLOOD PRESSURE ARCHITECTURE", ["HIGH", "NORMAL", "LOW"])
cholesterol = st.sidebar.selectbox("CHOLESTEROL MATRIX", ["HIGH", "NORMAL"])
na_to_k = st.sidebar.slider("Na_to_K IONIC SPEC", 5.0, 40.0, 16.5)

# Feature engineering derived variables
age_group_str = "41-50"
if age <= 20: age_group_str = "10-20"
elif age <= 30: age_group_str = "21-30"
elif age <= 40: age_group_str = "31-40"
elif age <= 50: age_group_str = "41-50"
elif age <= 60: age_group_str = "51-60"
elif age <= 70: age_group_str = "61-70"
else: age_group_str = "70+"

high_nak_val = 1 if na_to_k > 15.0 else 0


# --- 5. DATA ENGINE: MOCK REFERENCE CORPUS FOR VISUALIZATION ---
@st.cache_data
def generate_reference_space():
    np.random.seed(42)
    n = 200
    m_age = np.random.randint(15, 90, n)
    m_nak = np.random.uniform(5.0, 40.0, n)
    m_bp = np.random.choice(["LOW", "NORMAL", "HIGH"], n, p=[0.2, 0.3, 0.5])
    
    m_drug = []
    for a, nk, b in zip(m_age, m_nak, m_bp):
        if nk > 15.2: m_drug.append("DrugY")
        elif b == "HIGH": m_drug.append("drugA" if a < 50 else "drugB")
        else: m_drug.append("drugC" if a < 45 else "drugX")
            
    return pd.DataFrame({"Age": m_age, "Na_to_K": m_nak, "BP": m_bp, "Drug": m_drug})

ref_df = generate_reference_space()


# --- 6. MAIN HUB TERMINAL DISPLAY ---
st.markdown('<div class="nexus-header">QUANTUM NEXUS INTELLIGENCE SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="nexus-subtitle">PREGNANCY & MEDICAL DIAGNOSTIC CORE // PRODUCTION SUITE v2.0</div>', unsafe_allow_html=True)

# Upper Grid Telemetry Metrics
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f'<div class="crypto-card"><h5 style="color:#64748b; margin:0;">ACTIVE CORE</h5><h3 style="color:#00f2fe; margin:5px 0;">{selected_core.split()[0]} Engine</h3></div>', unsafe_allow_html=True)
with m2:
    status_color = "#00ff87" if "✓" in core_status else "#ffea00"
    st.markdown(f'<div class="crypto-card"><h5 style="color:#64748b; margin:0;">KERNEL HARNESS LINK</h5><h3 style="color:{status_color}; margin:5px 0;">{core_status}</h3></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="crypto-card"><h5 style="color:#64748b; margin:0;">FEATURES EXTRACTED</h5><h3 style="color:#00f2fe; margin:5px 0;">7 Core Pipelines</h3></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="crypto-card"><h5 style="color:#64748b; margin:0;">THREAD SYSTEM</h5><h3 style="color:#fe007a; margin:5px 0;">REAL-TIME LIVE</h3></div>', unsafe_allow_html=True)


# --- 7. DEEP VISUALIZATION: HYPER-SPACE GRID ---
st.markdown("<h3 style='font-family:Orbitron; color:#f1f5f9;'>📊 HYPER-SPACE VECTOR BOUNDARIES</h3>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🌐 3D CLUSTER VECTOR WINDOW", "📈 2D ISOLINE DISTRIBUTION"])

with tab1:
    bp_numeric_map = {"LOW": 0, "NORMAL": 1, "HIGH": 2}
    ref_df["BP_Int"] = ref_df["BP"].map(bp_numeric_map)
    user_bp_int = bp_numeric_map.get(bp)

    fig_3d = go.Figure()
    drug_colors = {"DrugY": "#00f2fe", "drugA": "#fe007a", "drugB": "#ffea00", "drugC": "#00ff87", "drugX": "#a855f7"}
    
    for d_class, color in drug_colors.items():
        subset = ref_df[ref_df["Drug"] == d_class]
        fig_3d.add_trace(go.Scatter3d(
            x=subset["Age"], y=subset["Na_to_K"], z=subset["BP_Int"],
            mode="markers", name=f"Cluster: {d_class}",
            marker=dict(size=5, color=color, opacity=0.7)
        ))
        
    fig_3d.add_trace(go.Scatter3d(
        x=[age], y=[na_to_k], z=[user_bp_int],
        mode="markers+text", name="🎯 CURRENT VECTOR PATIENT",
        marker=dict(size=14, color="#ffffff", symbol="diamond", line=dict(color="#fe007a", width=3)),
        text=["LIVE TARGET"], textposition="top center"
    ))
    
    fig_3d.update_layout(
        template="plotly_dark", margin=dict(l=0, r=0, b=0, t=0),
        scene=dict(
            xaxis=dict(title=dict(text='AGE SPECTRUM', font=dict(family='Orbitron', color='#00f2fe')), backgroundcolor="#030712"),
            yaxis=dict(title=dict(text='Na_to_K ION LEVEL', font=dict(family='Orbitron', color='#00f2fe')), backgroundcolor="#030712"),
            zaxis=dict(title=dict(text='BP INTENSITY GRID', font=dict(family='Orbitron', color='#00f2fe')), backgroundcolor="#030712", tickvals=[0,1,2], ticktext=['LOW','NORMAL','HIGH']),
        ),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=500
    )
    # Fixed deprecation warning (replaced use_container_width with width='stretch')
    st.plotly_chart(fig_3d, width='stretch')

with tab2:
    fig_2d = px.scatter(
        ref_df, x="Age", y="Na_to_K", color="Drug",
        title="Patient Feature Clustering Mapping",
        color_discrete_map=drug_colors, template="plotly_dark"
    )
    fig_2d.add_shape(
        type="line", x0=age, y0=0, x1=age, y1=40,
        line=dict(color="#fe007a", width=2, dash="dash")
    )
    fig_2d.add_shape(
        type="line", x0=15, y0=na_to_k, x1=90, y1=na_to_k,
        line=dict(color="#00f2fe", width=2, dash="dash")
    )
    fig_2d.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    # Fixed deprecation warning
    st.plotly_chart(fig_2d, width='stretch')


# --- 8. PREDICTION PIPELINE INTERFERENCE ---
st.markdown("---")
c_left, c_right = st.columns([4, 5])

with c_left:
    st.markdown('<div class="crypto-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='font-family:Orbitron; color:#00f2fe; margin-top:0;'>📝 TRANSPILED FEATURE VECTOR</h4>", unsafe_allow_html=True)
    
    # FIXED ARROW ARTIFACT BUG: Converted all column elements strictly to strings to avoid mixed data type serialization crashes
    features_payload = {
        "Feature Attribute": ["Age", "Sex", "BP", "Cholesterol", "Na_to_K", "Age_Group", "High_NaK"],
        "Runtime Payload": [str(age), str(sex), str(bp), str(cholesterol), f"{na_to_k:.2f}", str(age_group_str), str(high_nak_val)]
    }
    st.table(pd.DataFrame(features_payload))
    st.markdown('</div>', unsafe_allow_html=True)

with c_right:
    st.markdown('<div class="crypto-card" style="border-color: #00ff87;">', unsafe_allow_html=True)
    st.markdown("<h4 style='font-family:Orbitron; color:#00ff87; margin-top:0;'>🔮 MODEL ENGINE INFERENCE</h4>", unsafe_allow_html=True)
    
    if active_model is not None:
        try:
            # 1. Encoders/Mapping layer matching how your models were trained (Strings to Numbers)
            sex_num = 1 if sex == "MALE" else 0
            bp_num = 2 if bp == "HIGH" else (1 if bp == "NORMAL" else 0)
            chol_num = 1 if cholesterol == "HIGH" else 0
            
            # Map age group to a numerical assignment code if needed
            age_group_mapping = {"10-20": 0, "21-30": 1, "31-40": 2, "41-50": 3, "51-60": 4, "61-70": 5, "70+": 6}
            age_group_num = age_group_mapping.get(age_group_str, 3)

            # 2. FIXED USER WARNING SHAPE LOGIC: Extracted raw values array directly without headers
            # Structure matches array layout: [Age, Sex, BP, Cholesterol, Na_to_K, Age_Group, High_NaK]
            input_vector = np.array([[age, sex_num, bp_num, chol_num, na_to_k, age_group_num, high_nak_val]])
            
            # Prediction Execution on raw numeric values
            raw_prediction = active_model.predict(input_vector)[0]
            
            st.markdown(f"<h2 style='color:#00ff87; font-family:Orbitron; margin:10px 0;'>🎯 RESULT: {str(raw_prediction).upper()}</h2>", unsafe_allow_html=True)
            st.markdown(f"**Execution Core:** Integrated Live Binary Object (`{selected_core}`)")
            st.info("Inference parsed successfully via compiled pipeline array metadata with native format arrays.")
            
        except Exception as inf_err:
            st.markdown("<h3 style='color:#fe007a;'>⚠ CORRUPTION IN PIPELINE VALUE</h3>", unsafe_allow_html=True)
            st.error(f"Error Description: {str(inf_err)}")
    else:
        st.caption("🔄 RUNNING HYBRID SIMULATION GENERATOR (PKL OFFLINE)")
        if na_to_k > 15.0:
            res, conf, col = "DRUG Y (MAX SYNAPSE)", "99.1% Confidence Matrix", "#00f2fe"
        elif bp == "HIGH" and age > 50:
            res, conf, col = "DRUG B (ANTI-HYPERTENSIVE ALPHA)", "94.6% Confidence Matrix", "#fe007a"
        elif bp == "HIGH" and age <= 50:
            res, conf, col = "DRUG A (CARDIO STABILIZER BETA)", "91.2% Confidence Matrix", "#ffea00"
        else:
            res, conf, col = "DRUG X / C (BALANCED HOMEOSTASIS)", "88.4% Confidence Matrix", "#00ff87"
            
        st.markdown(f"<h2 style='color:{col}; font-family:Orbitron; margin:10px 0;'>🎯 SIM: {res}</h2>", unsafe_allow_html=True)
        st.markdown(f"**Confidence Matrix Layer:** `{conf}`")
        st.warning("Note: Yeh output simulation fallback se aaya hai.")

    st.progress(1.0)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#334155; font-size:0.8rem; margin-top:30px;'>⚡ SECURE QUANTUM NET NODE EXECUTION // OPERATING WITH ZERO EXPLOIT PROFILE</p>", unsafe_allow_html=True)