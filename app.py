import streamlit as st
import math

# Page setup
st.set_page_config(
    page_title="P. MANOHAR - Mechanical Portal",
    page_icon="⚙️",
    layout="centered"
)

# ----------------- SESSION STATE & 10-ITEM HISTORY ----------------- #
if "module" not in st.session_state:
    st.session_state.module = "🏠 Home Menu"

if "calc_history" not in st.session_state:
    st.session_state.calc_history = []

def add_history(entry_text):
    st.session_state.calc_history.insert(0, entry_text)
    if len(st.session_state.calc_history) > 10:
        st.session_state.calc_history.pop()

def go_home():
    st.session_state.module = "🏠 Home Menu"

def set_module(name):
    st.session_state.module = name

# ----------------- 3D STYLING & BACKGROUND CSS ----------------- #
st.markdown("""
<style>
    /* High-Tech Industrial Carbon-Slate Radial Gradient Background */
    .stApp {
        background: radial-gradient(circle at 50% 15%, #1e2638 0%, #0b0f19 100%);
        color: #f1f5f9;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }

    /* Student Profile Badge Card */
    .student-badge {
        background: linear-gradient(135deg, rgba(23, 37, 84, 0.7) 0%, rgba(15, 23, 42, 0.85) 100%);
        border: 2px solid #f59e0b;
        border-radius: 16px;
        padding: 18px 24px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(245, 158, 11, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    .badge-name {
        font-size: 1.45rem;
        font-weight: 800;
        color: #fbbf24;
        letter-spacing: 0.8px;
    }
    .badge-sub {
        font-size: 0.98rem;
        color: #cbd5e1;
        margin-top: 6px;
    }

    /* 3D Tactile Buttons - Industrial Ember Gold / Orange */
    div.stButton > button {
        background: linear-gradient(180deg, #f59e0b 0%, #d97706 50%, #b45309 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 22px !important;
        box-shadow: 0 5px 0 #78350f, 0 10px 18px rgba(0, 0, 0, 0.55) !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.08s ease-in-out !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(180deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%) !important;
        transform: translateY(-1px) !important;
    }
    div.stButton > button:active {
        transform: translateY(4px) !important;
        box-shadow: 0 1px 0 #78350f, 0 3px 6px rgba(0, 0, 0, 0.4) !important;
    }

    /* Visual Demo / Lab Display Card */
    .demo-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 12px;
        padding: 16px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- PROFILE HEADER ----------------- #
st.markdown("""
<div class="student-badge">
    <div class="badge-name">👨‍🎓 P . MANOHAR</div>
    <div class="badge-sub">
        <b>Roll No:</b> 2505A31016 &nbsp;|&nbsp; 
        <b>Branch:</b> Mechanical Engineering &nbsp;|&nbsp; 
        <b>Year:</b> 2nd Year
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- CALCULATION FUNCTIONS ----------------- #

# Mechanics
def calc_force(m, a): return m * a
def calc_work(f, d): return f * d
def calc_power(w, t): return w / t if t > 0 else None
def calc_kinetic_energy(m, v): return 0.5 * m * (v ** 2)

# Strength of Materials
def calc_stress(f, a): return f / a if a > 0 else None
def calc_strain(dl, l0): return dl / l0 if l0 > 0 else None
def calc_youngs(s, e): return s / e if e > 0 else None

# Thermodynamics
def calc_heat(m, c, dt): return m * c * dt
def calc_isobaric(p, dv): return p * dv
def calc_eff(w, q): return (w / q) * 100 if q > 0 else None

# Fluid Mechanics
def calc_pressure(f, a): return f / a if a > 0 else None
def calc_reynolds(rho, v, d, mu): return (rho * v * d) / mu if mu > 0 else None
def calc_flow_vel(q, a): return q / a if a > 0 else None
def calc_discharge(a, v): return a * v

# Thermal Engineering
def calc_conduction(k, a, dt, x): return (k * a * dt) / x if x > 0 else None
def calc_cop(effect, work): return effect / work if work > 0 else None
def calc_carnot(th, tl): return (1 - (tl / th)) * 100 if th > 0 else None

# Machine Design
def calc_torque(p, rpm):
    return (p * 60) / (2 * math.pi * rpm) if rpm > 0 else None
def calc_shaft_power(t, rpm):
    return (2 * math.pi * rpm * t) / 60
def calc_shaft_diameter(t, tau):
    return ((16 * t) / (math.pi * tau)) ** (1 / 3) if tau > 0 else None

# Classroom Simulations
def calc_beam_center_load(load_n, length_m, e_pa, i_m4):
    # Simply supported beam with central point load
    max_deflection = (load_n * (length_m ** 3)) / (48 * e_pa * i_m4) if (e_pa * i_m4) > 0 else None
    max_moment = (load_n * length_m) / 4
    return max_deflection, max_moment

# ----------------- SIDEBAR & NAVIGATION ----------------- #
module_options = [
    "🏠 Home Menu",
    "🏫 Classroom Demos",
    "🔄 Unit Converter Mode",
    "🧮 General Calculator",
    "🛠️ Mech Quick Tools",
    "1. Mechanics",
    "2. Strength of Materials",
    "3. Thermodynamics",
    "4. Fluid Mechanics",
    "5. Thermal Engineering",
    "6. Machine Design"
]

selected_sidebar = st.sidebar.selectbox(
    "Navigation Menu",
    module_options,
    index=module_options.index(st.session_state.module)
)

if selected_sidebar != st.session_state.module:
    st.session_state.module = selected_sidebar
    st.rerun()

if st.session_state.module != "🏠 Home Menu":
    if st.sidebar.button("⬅️ Return to Main Menu", use_container_width=True, key="side_back"):
        go_home()
        st.rerun()

# --- SIDEBAR: 10-STEP HISTORY WITH DOWNLOAD & CLEAR ---
st.sidebar.divider()
st.sidebar.subheader("🕒 History (Last 10)")

if st.session_state.calc_history:
    for idx, item in enumerate(st.session_state.calc_history, 1):
        st.sidebar.caption(f"**{idx}.** {item}")

    # Prepare plain-text string for export
    history_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(st.session_state.calc_history)])
    
    st.sidebar.download_button(
        label="📥 Download History (.txt)",
        data=history_text,
        file_name="p_manohar_calc_history.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    if st.sidebar.button("🗑️ Clear History", use_container_width=True):
        st.session_state.calc_history = []
        st.rerun()
else:
    st.sidebar.caption("No calculations recorded yet.")


# ----------------- MAIN VIEW ROUTING ----------------- #
if st.session_state.module != "🏠 Home Menu":
    if st.button("⬅️ Back to Main Menu", key="top_back"):
        go_home()
        st.rerun()
    st.divider()

# --- 1. HOME DASHBOARD ---
if st.session_state.module == "🏠 Home Menu":
    st.markdown("### 🚀 Engineering Portal Dashboard")
    st.write("Choose any core discipline, classroom live simulator, or conversion module:")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🏫 Classroom Demos", use_container_width=True):
            set_module("🏫 Classroom Demos")
            st.rerun()
        if st.button("🔄 Unit Converter Mode", use_container_width=True):
            set_module("🔄 Unit Converter Mode")
            st.rerun()
        if st.button("🧮 General Calculator", use_container_width=True):
            set_module("🧮 General Calculator")
            st.rerun()
        if st.button("1. Mechanics", use_container_width=True):
            set_module("1. Mechanics")
            st.rerun()
        if st.button("2. Strength of Materials", use_container_width=True):
            set_module("2. Strength of Materials")
            st.rerun()

    with c2:
        if st.button("🛠️ Mech Quick Tools", use_container_width=True):
            set_module("🛠️ Mech Quick Tools")
            st.rerun()
        if st.button("3. Thermodynamics", use_container_width=True):
            set_module("3. Thermodynamics")
            st.rerun()
        if st.button("4. Fluid Mechanics", use_container_width=True):
            set_module("4. Fluid Mechanics")
            st.rerun()
        if st.button("5. Thermal Engineering", use_container_width=True):
            set_module("5. Thermal Engineering")
            st.rerun()
        if st.button("6. Machine Design", use_container_width=True):
            set_module("6. Machine Design")
            st.rerun()

# --- 2. CLASSROOM DEMO SIMULATORS ---
elif st.session_state.module == "🏫 Classroom Demos":
    st.header("🏫 Classroom Interactive Demo Simulator")
    demo_tab1, demo_tab2 = st.tabs(["1. Beam Deflection Simulator", "2. Simple Gear Train Simulator"])

    with demo_tab1:
        st.subheader("Simply Supported Beam (Point Load at Center)")
        st.latex(r"\delta_{\max} = \frac{F \cdot L^3}{48 \cdot E \cdot I}, \quad M_{\max} = \frac{F \cdot L}{4}")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            f_load = st.slider("Applied Force (F) [N]", min_value=100.0, max_value=50000.0, value=5000.0, step=100.0)
            l_beam = st.slider("Span Length (L) [m]", min_value=0.5, max_value=10.0, value=2.5, step=0.1)
        with col_d2:
            e_mat = st.selectbox("Beam Material (E)", ["Structural Steel (200 GPa)", "Aluminum (69 GPa)", "Cast Iron (110 GPa)"])
            e_val = 200e9 if "Steel" in e_mat else (69e9 if "Aluminum" in e_mat else 110e9)
            i_val = st.number_input("Area Moment of Inertia (I) [cm⁴]", min_value=0.1, value=450.0) * 1e-8

        if st.button("Simulate Beam"):
            defl_m, m_max = calc_beam_center_load(f_load, l_beam, e_val, i_val)
            defl_mm = defl_m * 1000
            add_history(f"Demo Beam: Load={f_load}N, Defl={defl_mm:.3f}mm")
            
            st.markdown(f"""
            <div class="demo-card">
                <h4>📊 Simulation Output</h4>
                <p><b>Maximum Bending Moment:</b> {m_max:.2f} N·m</p>
                <p><b>Central Deflection (δ_max):</b> <span style="color:#fbbf24; font-size:1.2rem; font-weight:bold;">{defl_mm:.3f} mm</span></p>
            </div>
            """, unsafe_allow_html=True)
            st.progress(min(defl_mm / 15.0, 1.0), text="Deflection Stress Visualizer")

    with demo_tab2:
        st.subheader("Simple Spur Gear Transmission")
        st.latex(r"i = \frac{N_1}{N_2} = \frac{T_2}{T_1}, \quad \tau_2 = \tau_1 \times i")
        
        g1, g2 = st.columns(2)
        with g1:
            z1 = st.number_input("Driver Gear Teeth (T₁)", min_value=8, value=20)
            n1 = st.number_input("Driver Speed (N₁) [RPM]", min_value=1.0, value=1500.0)
            t1 = st.number_input("Driver Torque (τ₁) [N·m]", min_value=0.1, value=30.0)
        with g2:
            z2 = st.number_input("Driven Gear Teeth (T₂)", min_value=8, value=60)
        
        if st.button("Simulate Gear Ratio"):
            ratio = z2 / z1
            n2 = n1 / ratio
            t2 = t1 * ratio
            add_history(f"Gear Train: Ratio={ratio:.2f}:1, Driven={n2:.1f}RPM")
            
            st.markdown(f"""
            <div class="demo-card">
                <h4>⚙️ Gearbox Output</h4>
                <p><b>Gear Ratio (i):</b> {ratio:.2f} : 1</p>
                <p><b>Driven Speed (N₂):</b> <span style="color:#38bdf8; font-weight:bold;">{n2:.2f} RPM</span></p>
                <p><b>Output Torque (τ₂):</b> <span style="color:#fbbf24; font-weight:bold;">{t2:.2f} N·m</span></p>
            </div>
            """, unsafe_allow_html=True)

# --- 3. DEDICATED UNIT CONVERTER MODE ---
elif st.session_state.module == "🔄 Unit Converter Mode":
    st.header("🔄 Comprehensive Mechanical Unit Converter")
    conv_category = st.selectbox(
        "Choose Engineering Property", 
        ["Pressure", "Power", "Force", "Length", "Dynamic Viscosity", "Thermal Conductivity"]
    )

    if conv_category == "Pressure":
        st.latex(r"1\text{ bar} = 10^5\text{ Pa} = 0.1\text{ MPa} = 14.5038\text{ psi}")
        val_p = st.number_input("Input Value (in Bar)", value=1.0)
        st.info(f"""
        - **{val_p * 1e5:.2f}** Pascals (Pa)
        - **{val_p * 100:.2f}** Kilopascals (kPa)
        - **{val_p * 0.1:.4f}** Megapascals (MPa)
        - **{val_p * 14.5038:.3f}** Pounds per sq. inch (psi)
        - **{val_p * 0.986923:.4f}** Atmospheres (atm)
        """)
        if st.button("Log Pressure Conversion"):
            add_history(f"Converted {val_p} bar ➔ {val_p * 0.1:.2f} MPa")
            st.success("Logged to history!")

    elif conv_category == "Power":
        st.latex(r"1\text{ kW} = 1000\text{ W} = 1.34102\text{ HP}")
        val_pw = st.number_input("Input Value (in Kilowatts - kW)", value=5.0)
        st.info(f"""
        - **{val_pw * 1000:.2f}** Watts (W)
        - **{val_pw * 1.34102:.3f}** Mechanical Horsepower (HP)
        - **{val_pw * 859.845:.2f}** Kilocalories/hour (kcal/h)
        - **{val_pw * 3412.14:.2f}** BTU/hour
        """)
        if st.button("Log Power Conversion"):
            add_history(f"Converted {val_pw} kW ➔ {val_pw * 1.34102:.2f} HP")
            st.success("Logged to history!")

    elif conv_category == "Force":
        st.latex(r"1\text{ kN} = 1000\text{ N} = 224.809\text{ lbf} = 101.97\text{ kgf}")
        val_f = st.number_input("Input Value (in Kilonewtons - kN)", value=2.0)
        st.info(f"""
        - **{val_f * 1000:.2f}** Newtons (N)
        - **{val_f * 224.809:.2f}** Pound-force (lbf)
        - **{val_f * 101.972:.2f}** Kilogram-force (kgf)
        """)
        if st.button("Log Force Conversion"):
            add_history(f"Converted {val_f} kN ➔ {val_f * 1000:.0f} N")
            st.success("Logged to history!")

    elif conv_category == "Length":
        val_l = st.number_input("Input Value (in Millimeters - mm)", value=50.8)
        st.info(f"""
        - **{val_l / 1000:.4f}** Meters (m)
        - **{val_l / 10:.2f}** Centimeters (cm)
        - **{val_l / 25.4:.4f}** Inches (in)
        - **{val_l / 304.8:.4f}** Feet (ft)
        """)

    elif conv_category == "Dynamic Viscosity":
        st.latex(r"1\text{ Pa}\cdot\text{s} = 1\text{ kg/(m}\cdot\text{s)} = 10\text{ Poise} = 1000\text{ cP}")
        val_mu = st.number_input("Input Dynamic Viscosity (Pa·s)", value=0.001, format="%.5f")
        st.info(f"""
        - **{val_mu * 1000:.2f}** Centipoise (cP)
        - **{val_mu * 10:.3f}** Poise (P)
        - **{val_mu * 0.671969:.5f}** lb/(ft·s)
        """)

    elif conv_category == "Thermal Conductivity":
        st.latex(r"1\text{ W/(m}\cdot\text{K)} = 0.5778\text{ BTU/(hr}\cdot\text{ft}\cdot^\circ\text{F)}")
        val_k = st.number_input("Input k [W/(m·K)]", value=45.0)
        st.info(f"""
        - **{val_k * 0.85984:.3f}** kcal/(hr·m·°C)
        - **{val_k * 0.5778:.3f}** BTU/(hr·ft·°F)
        """)

# --- 4. GENERAL CALCULATOR MODE ---
elif st.session_state.module == "🧮 General Calculator":
    st.header("🧮 General & Scientific Mode")
    c_mode = st.radio("Select Domain", ["Basic Math (+, -, ×, ÷)", "Scientific Exponents / Roots", "Trigonometric"], horizontal=True)

    if c_mode == "Basic Math (+, -, ×, ÷)":
        b1, b2, b3 = st.columns([2, 1, 2])
        with b1: n1 = st.number_input("Operand 1", value=12.0)
        with b2: oper = st.selectbox("Op", ["+", "-", "×", "÷"])
        with b3: n2 = st.number_input("Operand 2", value=4.0)

        if st.button("Solve Arithmetic"):
            if oper == "+": res = n1 + n2
            elif oper == "-": res = n1 - n2
            elif oper == "×": res = n1 * n2
            elif oper == "÷": res = n1 / n2 if n2 != 0 else "Error: Div/0"

            if isinstance(res, (int, float)):
                add_history(f"{n1} {oper} {n2} = {res:.4f}")
                st.success(f"**Result:** {res:.4f}")
            else:
                st.error(res)

    elif c_mode == "Scientific Exponents / Roots":
        sc_choice = st.selectbox("Function", ["Square Root (√x)", "Power (xʸ)", "Natural Log (ln x)", "Log Base 10"])
        x_in = st.number_input("Input (x)", value=25.0)
        y_in = 2.0
        if sc_choice == "Power (xʸ)":
            y_in = st.number_input("Exponent (y)", value=3.0)

        if st.button("Solve Scientific"):
            if sc_choice == "Square Root (√x)":
                ans = math.sqrt(x_in) if x_in >= 0 else None
                tag = f"√({x_in}) = {ans:.4f}"
            elif sc_choice == "Power (xʸ)":
                ans = x_in ** y_in
                tag = f"{x_in}^{y_in} = {ans:.4f}"
            elif sc_choice == "Natural Log (ln x)":
                ans = math.log(x_in) if x_in > 0 else None
                tag = f"ln({x_in}) = {ans:.4f}"
            elif sc_choice == "Log Base 10":
                ans = math.log10(x_in) if x_in > 0 else None
                tag = f"log10({x_in}) = {ans:.4f}"

            if ans is not None:
                add_history(tag)
                st.success(f"**Result:** {ans:.6f}")
            else:
                st.error("Mathematical domain error!")

    elif c_mode == "Trigonometric":
        deg = st.number_input("Angle θ (Degrees)", value=30.0)
        fn_trig = st.selectbox("Function", ["sin(θ)", "cos(θ)", "tan(θ)"])
        if st.button("Solve Trigonometry"):
            rad = math.radians(deg)
            if fn_trig == "sin(θ)": out = math.sin(rad)
            elif fn_trig == "cos(θ)": out = math.cos(rad)
            elif fn_trig == "tan(θ)": out = math.tan(rad) if (deg % 180 != 90) else "Undefined"

            if isinstance(out, float):
                add_history(f"{fn_trig} @ {deg}° = {out:.4f}")
                st.success(f"**Result:** {out:.4f}")
            else:
                st.error(out)

# --- 5. MECH QUICK TOOLS ---
elif st.session_state.module == "🛠️ Mech Quick Tools":
    st.header("🛠️ Mechanical Student Reference Tools")
    t_tab1, t_tab2 = st.tabs(["📋 Standard Materials Database", "💧 Saturated Steam Snippet"])

    with t_tab1:
        st.subheader("Common Metals & Alloy Reference")
        st.markdown("""
        | Material | Density (kg/m³) | Young's Modulus (GPa) | Yield Strength (MPa) | Thermal Cond. (W/mK) |
        | :--- | :--- | :--- | :--- | :--- |
        | **Structural Mild Steel** | 7850 | 200 | 250 | 45 |
        | **Stainless Steel 304** | 8000 | 193 | 215 | 16.2 |
        | **Aluminum 6061-T6** | 2700 | 69 | 276 | 167 |
        | **Gray Cast Iron** | 7200 | 110 | 130 | 50 |
        | **Titanium Gr. 5** | 4430 | 114 | 880 | 6.7 |
        | **High Brass** | 8500 | 97 | 310 | 115 |
        """)

    with t_tab2:
        st.subheader("Saturated Water / Steam Table (Gauge Guide)")
        st.markdown("""
        | Temp (°C) | Pressure (kPa) | Enthalpy Liquid $h_f$ (kJ/kg) | Enthalpy Evap $h_{fg}$ (kJ/kg) | Enthalpy Steam $h_g$ (kJ/kg) |
        | :--- | :--- | :--- | :--- | :--- |
        | **100** | 101.3 | 419.1 | 2257.0 | 2676.1 |
        | **120** | 198.5 | 503.7 | 2202.6 | 2706.3 |
        | **150** | 475.8 | 632.2 | 2114.3 | 2746.5 |
        | **180** | 1002.7 | 763.2 | 2015.0 | 2778.2 |
        | **200** | 1553.8 | 852.4 | 1940.7 | 2793.2 |
        """)

# --- MODULE 1: MECHANICS ---
elif st.session_state.module == "1. Mechanics":
    st.header("1. Mechanics")
    sub = st.selectbox("Select Calculation", ["Force", "Work", "Power", "Kinetic Energy"])

    if sub == "Force":
        st.latex(r"F = m \times a")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=10.0)
        a = st.number_input("Acceleration (a) [m/s²]", value=9.81)
        if st.button("Calculate Force"):
            res = calc_force(m, a)
            add_history(f"Force: m={m}kg, a={a}m/s² ➔ {res:.2f} N")
            st.success(f"**Force (F) = {res:.4f} N**")

    elif sub == "Work":
        st.latex(r"W = F \times d")
        f = st.number_input("Force (F) [N]", value=50.0)
        d = st.number_input("Displacement (d) [m]", value=5.0)
        if st.button("Calculate Work"):
            res = calc_work(f, d)
            add_history(f"Work: F={f}N, d={d}m ➔ {res:.2f} J")
            st.success(f"**Work Done (W) = {res:.4f} J**")

    elif sub == "Power":
        st.latex(r"P = \frac{W}{t}")
        w = st.number_input("Work (W) [J]", value=500.0)
        t = st.number_input("Time (t) [s]", min_value=0.0001, value=10.0)
        if st.button("Calculate Power"):
            res = calc_power(w, t)
            add_history(f"Power: W={w}J, t={t}s ➔ {res:.2f} W")
            st.success(f"**Power (P) = {res:.4f} W**")

    elif sub == "Kinetic Energy":
        st.latex(r"KE = \frac{1}{2} m v^2")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=2.0)
        v = st.number_input("Velocity (v) [m/s]", value=10.0)
        if st.button("Calculate KE"):
            res = calc_kinetic_energy(m, v)
            add_history(f"KE: m={m}kg, v={v}m/s ➔ {res:.2f} J")
            st.success(f"**Kinetic Energy (KE) = {res:.4f} J**")

# --- MODULE 2: STRENGTH OF MATERIALS ---
elif st.session_state.module == "2. Strength of Materials":
    st.header("2. Strength of Materials")
    sub = st.selectbox("Select Calculation", ["Stress", "Strain", "Young's Modulus"])

    if sub == "Stress":
        st.latex(r"\sigma = \frac{F}{A}")
        f = st.number_input("Applied Load (F) [N]", value=1000.0)
        a = st.number_input("Area (A) [m²]", min_value=0.000001, value=0.002, format="%.6f")
        if st.button("Calculate Stress"):
            res = calc_stress(f, a)
            add_history(f"Stress: F={f}N, A={a}m² ➔ {res/1e6:.2f} MPa")
            st.success(f"**Stress (σ) = {res:.2f} Pa ({res / 1e6:.4f} MPa)**")

    elif sub == "Strain":
        st.latex(r"\varepsilon = \frac{\Delta L}{L_0}")
        dl = st.number_input("Change in Length (ΔL) [mm]", value=0.5)
        l0 = st.number_input("Original Length (L₀) [mm]", min_value=0.001, value=100.0)
        if st.button("Calculate Strain"):
            res = calc_strain(dl, l0)
            add_history(f"Strain: ΔL={dl}mm, L0={l0}mm ➔ {res:.6f}")
            st.success(f"**Strain (ε) = {res:.6f}**")

    elif sub == "Young's Modulus":
        st.latex(r"E = \frac{\sigma}{\varepsilon}")
        stress = st.number_input("Stress (σ) [Pa]", value=200000000.0)
        strain = st.number_input("Strain (ε)", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate Modulus"):
            res = calc_youngs(stress, strain)
            add_history(f"Young's Modulus: ➔ {res/1e9:.2f} GPa")
            st.success(f"**Young's Modulus (E) = {res / 1e9:.3f} GPa**")

# --- MODULE 3: THERMODYNAMICS ---
elif st.session_state.module == "3. Thermodynamics":
    st.header("3. Thermodynamics")
    sub = st.selectbox("Select Calculation", ["Heat Transfer", "Work Done (Constant P)", "Thermal Efficiency"])

    if sub == "Heat Transfer":
        st.latex(r"Q = m \times c \times \Delta T")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=1.0)
        cp = st.number_input("Specific Heat (c) [J/(kg·K)]", min_value=0.0, value=4184.0)
        dt = st.number_input("Temp Difference (ΔT) [K or °C]", value=20.0)
        if st.button("Calculate Heat"):
            res = calc_heat(m, cp, dt)
            add_history(f"Heat Q: m={m}, ΔT={dt} ➔ {res/1000:.2f} kJ")
            st.success(f"**Heat Transfer (Q) = {res:.2f} J ({res / 1000:.3f} kJ)**")

    elif sub == "Work Done (Constant P)":
        st.latex(r"W = P \times \Delta V")
        p = st.number_input("Pressure (P) [Pa]", min_value=0.0, value=101325.0)
        dv = st.number_input("Change in Volume (ΔV) [m³]", value=0.05, format="%.4f")
        if st.button("Calculate Isobaric Work"):
            res = calc_isobaric(p, dv)
            add_history(f"Work (PΔV): P={p}Pa ➔ {res:.2f} J")
            st.success(f"**Work Done (W) = {res:.2f} J**")

    elif sub == "Thermal Efficiency":
        st.latex(r"\eta = \left(\frac{W_{\text{net}}}{Q_{\text{in}}}\right) \times 100\%")
        wnet = st.number_input("Net Work Output [J]", min_value=0.0, value=400.0)
        qin = st.number_input("Heat Input [J]", min_value=0.001, value=1000.0)
        if st.button("Calculate Efficiency"):
            res = calc_eff(wnet, qin)
            add_history(f"Efficiency: W={wnet}, Q={qin} ➔ {res:.2f}%")
            st.success(f"**Thermal Efficiency (η) = {res:.2f} %**")

# --- MODULE 4: FLUID MECHANICS ---
elif st.session_state.module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics")
    sub = st.selectbox("Select Calculation", ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"])

    if sub == "Pressure":
        st.latex(r"P = \frac{F}{A}")
        f = st.number_input("Force (F) [N]", value=500.0)
        a = st.number_input("Area (A) [m²]", min_value=0.0001, value=0.05)
        if st.button("Calculate Pressure"):
            res = calc_pressure(f, a)
            add_history(f"Pressure: F={f}, A={a} ➔ {res/1000:.2f} kPa")
            st.success(f"**Pressure (P) = {res:.2f} Pa ({res / 1000:.3f} kPa)**")

    elif sub == "Reynolds Number":
        st.latex(r"Re = \frac{\rho \times v \times D}{\mu}")
        rho = st.number_input("Fluid Density (ρ) [kg/m³]", min_value=0.0, value=1000.0)
        v = st.number_input("Flow Velocity (v) [m/s]", min_value=0.0, value=1.5)
        d = st.number_input("Pipe Diameter (D) [m]", min_value=0.0, value=0.05)
        mu = st.number_input("Dynamic Viscosity (μ) [Pa·s]", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate Re"):
            re = calc_reynolds(rho, v, d, mu)
            regime = "Laminar" if re < 2300 else ("Turbulent" if re > 4000 else "Transitional")
            add_history(f"Reynolds No: Re={re:.0f} ({regime})")
            st.success(f"**Reynolds Number (Re) = {re:.2f}** ({regime} Flow)")

    elif sub == "Flow Velocity":
        st.latex(r"v = \frac{Q}{A}")
        q = st.number_input("Discharge (Q) [m³/s]", min_value=0.0, value=0.05)
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.0001, value=0.02)
        if st.button("Calculate Velocity"):
            res = calc_flow_vel(q, a)
            add_history(f"Flow Velocity: Q={q}, A={a} ➔ {res:.2f} m/s")
            st.success(f"**Flow Velocity (v) = {res:.4f} m/s**")

    elif sub == "Discharge":
        st.latex(r"Q = A \times v")
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.0, value=0.02)
        v = st.number_input("Velocity (v) [m/s]", min_value=0.0, value=2.5)
        if st.button("Calculate Discharge"):
            res = calc_discharge(a, v)
            add_history(f"Discharge: A={a}, v={v} ➔ {res:.4f} m³/s")
            st.success(f"**Discharge (Q) = {res:.4f} m³/s**")

# --- MODULE 5: THERMAL ENGINEERING ---
elif st.session_state.module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering")
    sub = st.selectbox("Select Calculation", ["Heat Conduction", "COP", "Heat Engine Efficiency (Carnot)"])

    if sub == "Heat Conduction":
        st.latex(r"Q = \frac{k \times A \times \Delta T}{x}")
        k = st.number_input("Thermal Conductivity (k) [W/(m·K)]", min_value=0.0, value=45.0)
        a = st.number_input("Surface Area (A) [m²]", min_value=0.0, value=2.0)
        dt = st.number_input("Temperature Difference (ΔT) [K or °C]", value=50.0)
        dx = st.number_input("Thickness (x) [m]", min_value=0.0001, value=0.1)
        if st.button("Calculate Conduction"):
            res = calc_conduction(k, a, dt, dx)
            add_history(f"Conduction Q: k={k}, ΔT={dt} ➔ {res:.2f} W")
            st.success(f"**Rate of Conduction = {res:.2f} W**")

    elif sub == "COP":
        st.latex(r"COP = \frac{\text{Desired Effect}}{\text{Work Input}}")
        effect = st.number_input("Desired Effect [kW]", min_value=0.0, value=7.5)
        work = st.number_input("Work Input [kW]", min_value=0.001, value=2.5)
        if st.button("Calculate COP"):
            res = calc_cop(effect, work)
            add_history(f"COP: Effect={effect}, Work={work} ➔ {res:.2f}")
            st.success(f"**COP = {res:.2f}**")

    elif sub == "Heat Engine Efficiency (Carnot)":
        st.latex(r"\eta_{\text{Carnot}} = \left(1 - \frac{T_{\text{low}}}{T_{\text{high}}}\right) \times 100\%")
        th = st.number_input("Source Temp (T_high) [K]", min_value=0.1, value=600.0)
        tl = st.number_input("Sink Temp (T_low) [K]", min_value=0.0, value=300.0)
        if tl >= th:
            st.error("T_low must be less than T_high!")
        else:
            if st.button("Calculate Carnot η"):
                res = calc_carnot(th, tl)
                add_history(f"Carnot η: Th={th}K, Tl={tl}K ➔ {res:.2f}%")
                st.success(f"**Carnot Efficiency = {res:.2f} %**")

# --- MODULE 6: MACHINE DESIGN ---
elif st.session_state.module == "6. Machine Design":
    st.header("6. Machine Design")
    sub = st.selectbox("Select Calculation", ["Torque from Power & RPM", "Shaft Power", "Shaft Diameter (Torsion)"])

    if sub == "Torque from Power & RPM":
        st.latex(r"T = \frac{P}{\omega} = \frac{60 \times P}{2 \pi N}")
        p = st.number_input("Power (P) [Watts]", min_value=0.0, value=15000.0)
        n = st.number_input("Rotational Speed (N) [RPM]", min_value=0.1, value=1440.0)
        if st.button("Calculate Torque"):
            res = calc_torque(p, n)
            add_history(f"Torque: P={p}W, N={n}RPM ➔ {res:.2f} N·m")
            st.success(f"**Torque (T) = {res:.2f} N·m**")

    elif sub == "Shaft Power":
        st.latex(r"P = T \times \omega = \frac{2 \pi N T}{60}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=99.5)
        n = st.number_input("Rotational Speed (N) [RPM]", min_value=0.0, value=1440.0)
        if st.button("Calculate Shaft Power"):
            res = calc_shaft_power(t, n)
            add_history(f"Shaft Power: T={t}Nm, N={n}RPM ➔ {res/1000:.2f} kW")
            st.success(f"**Shaft Power (P) = {res:.2f} W ({res / 1000:.3f} kW)**")

    elif sub == "Shaft Diameter (Torsion)":
        st.latex(r"d = \left(\frac{16 T}{\pi \tau}\right)^{\frac{1}{3}}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=250.0)
        tau = st.number_input("Allowable Shear Stress (τ) [MPa]", min_value=0.01, value=45.0)
        if st.button("Calculate Diameter"):
            d = calc_shaft_diameter(t, tau * 1e6)
            d_mm = d * 1000
            add_history(f"Shaft Dia: T={t}Nm, τ={tau}MPa ➔ {d_mm:.2f} mm")
            st.success(f"**Required Diameter (d) = {d_mm:.2f} mm**")
