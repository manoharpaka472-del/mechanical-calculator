import streamlit as st
import pandas as pd
import urllib.parse
import math

# Page configuration
st.set_page_config(
    page_title="MechCalc Pro Suite | P. MANOHAR",
    page_icon="⚙️",
    layout="centered"
)

# ----------------- ATTRACTIVE WALLPAPER & VIBRANT BUTTONS CSS ----------------- #
st.markdown("""
    <style>
    /* Industrial Mechanical High-Tech Background */
    .stApp {
        background: linear-gradient(rgba(10, 14, 26, 0.88), rgba(6, 10, 20, 0.94)), 
                    url('https://images.unsplash.com/photo-1504917599217-d4dc5ebe6122?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #F8FAFC;
    }

    /* 3D Glassmorphic Student Header */
    .student-badge-3d {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(14, 165, 233, 0.28));
        border: 1px solid rgba(245, 158, 11, 0.55);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.75), inset 0 1px 0 rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 22px;
    }

    /* VIBRANT CONTRASTING BUTTONS (Electric Gold & Amber Glow) */
    div.stButton > button {
        background: linear-gradient(145deg, #f59e0b, #d97706) !important;
        color: #0f172a !important;
        border: 1px solid #fde68a !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        letter-spacing: 0.4px !important;
        box-shadow: 0 6px 18px rgba(245, 158, 11, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        background: linear-gradient(145deg, #fbbf24, #f59e0b) !important;
        border-color: #ffffff !important;
        box-shadow: 0 10px 25px rgba(245, 158, 11, 0.65), 0 0 15px rgba(251, 191, 36, 0.5) !important;
        color: #000000 !important;
    }
    div.stButton > button:active {
        transform: translateY(1px) scale(0.98);
    }

    /* 3D Inputs */
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid rgba(245, 158, 11, 0.4) !important;
        border-radius: 8px !important;
        color: #f8fafc !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: rgba(10, 15, 28, 0.95) !important;
        backdrop-filter: blur(16px);
        border-right: 1px solid rgba(245, 158, 11, 0.25);
    }

    /* Calculation History Box */
    .history-card {
        background: rgba(15, 23, 42, 0.9);
        border-left: 3px solid #f59e0b;
        border-radius: 6px;
        padding: 8px 10px;
        margin-bottom: 6px;
        font-family: monospace;
        font-size: 0.82rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE & TRACKING ----------------- #
if "module" not in st.session_state:
    st.session_state.module = "🏠 Home Menu"

if "history" not in st.session_state:
    st.session_state.history = []

def add_history(calc_name, formula_val):
    st.session_state.history.insert(0, f"[{calc_name}] {formula_val}")
    if len(st.session_state.history) > 10:
        st.session_state.history.pop()

def go_home():
    st.session_state.module = "🏠 Home Menu"

def set_module(name):
    st.session_state.module = name


# ----------------- CALCULATION FUNCTIONS ----------------- #
# 1. Mechanics
def calc_force(m, a): return m * a
def calc_work(f, d): return f * d
def calc_power(w, t): return w / t if t > 0 else None
def calc_ke(m, v): return 0.5 * m * (v ** 2)

# 2. Strength of Materials
def calc_stress(f, a): return f / a if a > 0 else None
def calc_strain(dl, l0): return dl / l0 if l0 > 0 else None
def calc_youngs(s, e): return s / e if e > 0 else None

# 3. Thermodynamics
def calc_heat(m, c, dt): return m * c * dt
def calc_work_done(p, dv): return p * dv
def calc_thermal_eff(w, q): return (w / q) * 100 if q > 0 else None

# 4. Fluid Mechanics
def calc_pressure(f, a): return f / a if a > 0 else None
def calc_reynolds(rho, v, d, mu): return (rho * v * d) / mu if mu > 0 else None
def calc_velocity(q, a): return q / a if a > 0 else None
def calc_discharge(a, v): return a * v

# 5. Thermal Engineering
def calc_conduction(k, a, dt, x): return (k * a * dt) / x if x > 0 else None
def calc_cop(effect, w): return effect / w if w > 0 else None
def calc_heat_engine_eff(th, tl): return (1 - (tl / th)) * 100 if th > 0 else None

# 6. Machine Design
def calc_torque(p, n): return (60 * p) / (2 * math.pi * n) if n > 0 else None
def calc_shaft_power(t, n): return (2 * math.pi * n * t) / 60
def calc_shaft_dia(t, tau): return ((16 * t) / (math.pi * tau)) ** (1 / 3) if tau > 0 else None

# Specialized Tools
def calc_thermal_expansion(l0, alpha, dt): return l0 * alpha * dt
def calc_weight(volume, density): return volume * density
def calc_hoop_stress(p, d, t): return (p * d) / (2 * t) if t > 0 else None
def calc_longitudinal_stress(p, d, t): return (p * d) / (4 * t) if t > 0 else None
def calc_euler_buckling(E, I, L, end_condition):
    k_factors = {"Both Ends Pinned": 1.0, "Both Ends Fixed": 0.5, "One Fixed, One Free": 2.0, "One Fixed, One Pinned": 0.7}
    k = k_factors.get(end_condition, 1.0)
    effective_length = k * L
    return (math.pi ** 2 * E * I) / (effective_length ** 2)

def calc_spring_stiffness(G, d, D, n): return (G * (d ** 4)) / (8 * (D ** 3) * n) if (D > 0 and n > 0) else None
def calc_spring_shear_stress(W, D, d): return (8 * W * D) / (math.pi * (d ** 3)) if d > 0 else None
def calc_belt_drive(d1, n1, d2):
    n2 = (n1 * d1) / d2 if d2 > 0 else None
    velocity = (math.pi * (d1 / 1000) * n1) / 60
    return n2, velocity

# Additional Mechanical Tools
def calc_flywheel(mass, k_radius, rpm, cs):
    # I = m * k^2, omega = (2*pi*N)/60
    # E_k = 0.5 * I * omega^2,  delta_E = I * omega^2 * Cs
    omega = (2 * math.pi * rpm) / 60
    i_inertia = mass * (k_radius ** 2)
    e_kin = 0.5 * i_inertia * (omega ** 2)
    delta_e = i_inertia * (omega ** 2) * cs
    return i_inertia, e_kin, delta_e

def calc_flange_coupling(d_shaft):
    # Standard empirical proportions for rigid flange coupling
    d_hub = 2 * d_shaft
    l_hub = 1.5 * d_shaft
    d_pitch = 3 * d_shaft
    d_outside = 4 * d_shaft
    t_flange = 0.5 * d_shaft
    return d_hub, l_hub, d_pitch, d_outside, t_flange


# ----------------- SIDEBAR PROFILE & NAVIGATION ----------------- #
st.sidebar.markdown("""
<div style="background: rgba(245, 158, 11, 0.14); padding: 12px; border-radius: 10px; border: 1px solid rgba(245, 158, 11, 0.45);">
    <h4 style="margin:0; color:#fbbf24;">⚙️ STUDENT DETAILS</h4>
    <p style="margin:3px 0 0 0; font-size: 0.9rem;"><b>Name:</b> P . MANOHAR</p>
    <p style="margin:2px 0 0 0; font-size: 0.9rem;"><b>Roll No:</b> 2505A31016</p>
    <p style="margin:2px 0 0 0; font-size: 0.9rem;"><b>Year:</b> 2nd Year</p>
    <p style="margin:2px 0 0 0; font-size: 0.9rem;"><b>Branch:</b> Mechanical Engineering</p>
</div>
""", unsafe_allow_html=True)

nav_options = [
    "🏠 Home Menu",
    "📱 Mobile QR Code Scanner",
    "🎯 Class Live Demo Problems",
    "📊 Engineering Visualizer",
    "🧮 General Calculator",
    "1. Mechanics",
    "2. Strength of Materials",
    "3. Thermodynamics",
    "4. Fluid Mechanics",
    "5. Thermal Engineering",
    "6. Machine Design",
    "🛠️ Mechanical Student Utilities"
]

selected_sidebar = st.sidebar.selectbox(
    "Select Module",
    nav_options,
    index=nav_options.index(st.session_state.module)
)

if selected_sidebar != st.session_state.module:
    st.session_state.module = selected_sidebar
    st.rerun()

# Last 10 Calculations History with Export Option
st.sidebar.divider()
st.sidebar.markdown("### 🕒 Recent History (Last 10)")
if st.session_state.history:
    for idx, item in enumerate(st.session_state.history, start=1):
        st.sidebar.markdown(f"<div class='history-card'>{idx}. {item}</div>", unsafe_allow_html=True)
    
    history_text = "\n".join(st.session_state.history)
    st.sidebar.download_button(
        label="📥 Download History (.txt)",
        data=history_text,
        file_name="mechanical_calc_history.txt",
        mime="text/plain",
        use_container_width=True
    )
    if st.sidebar.button("Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
else:
    st.sidebar.caption("No calculations recorded yet.")

if st.session_state.module != "🏠 Home Menu":
    st.sidebar.divider()
    if st.sidebar.button("⬅️ Return to Main Menu", use_container_width=True, key="side_back"):
        go_home()
        st.rerun()


# ----------------- TOP STUDENT BADGE ----------------- #
st.markdown("""
<div class="student-badge-3d">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff;">P . MANOHAR</div>
            <div style="font-size: 0.9rem; color: #fbbf24; font-weight: 600;">ROLL NO: 2505A31016</div>
        </div>
        <div style="text-align: right; font-size: 0.85rem; color: #cbd5e1;">
            <b>2nd Year</b> | Mechanical Engineering<br>
            <span style="color:#f59e0b;">Turbine Machinery Suite</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

if st.session_state.module != "🏠 Home Menu":
    if st.button("⬅️ Back to Main Menu", key="top_back"):
        go_home()
        st.rerun()
    st.divider()


# ----------------- MODULE PAGES ----------------- #

# 0. HOME MENU
if st.session_state.module == "🏠 Home Menu":
    st.title("⚙️ Engineering Calculator Dashboard")
    st.write("Launch specialized modules, tools, and visualizers below:")

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("📱 Mobile QR Code Scanner", use_container_width=True):
            set_module("📱 Mobile QR Code Scanner"); st.rerun()
    with col_b:
        if st.button("🎯 Class Live Demo Problems", use_container_width=True):
            set_module("🎯 Class Live Demo Problems"); st.rerun()

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Engineering Visualizer", use_container_width=True):
            set_module("📊 Engineering Visualizer"); st.rerun()
        if st.button("🧮 General Calculator", use_container_width=True):
            set_module("🧮 General Calculator"); st.rerun()
        if st.button("1. Mechanics", use_container_width=True):
            set_module("1. Mechanics"); st.rerun()
        if st.button("2. Strength of Materials", use_container_width=True):
            set_module("2. Strength of Materials"); st.rerun()

    with col2:
        if st.button("3. Thermodynamics", use_container_width=True):
            set_module("3. Thermodynamics"); st.rerun()
        if st.button("4. Fluid Mechanics", use_container_width=True):
            set_module("4. Fluid Mechanics"); st.rerun()
        if st.button("5. Thermal Engineering", use_container_width=True):
            set_module("5. Thermal Engineering"); st.rerun()
        if st.button("6. Machine Design", use_container_width=True):
            set_module("6. Machine Design"); st.rerun()

    st.write("")
    if st.button("🛠️ Mechanical Utilities (Flywheels, Couplings, Springs, Vessels)", use_container_width=True):
        set_module("🛠️ Mechanical Student Utilities"); st.rerun()

# 1. LIVE QR CODE
elif st.session_state.module == "📱 Mobile QR Code Scanner":
    st.header("📱 Scan to Open on Smartphone")
    st.write("Display this on the classroom projector screen for quick mobile access:")

    default_url = "https://manoharpaka472-del-mechanical-calculator-app-2n151z.streamlit.app"
    app_url = st.text_input("App URL:", value=default_url)

    encoded_url = urllib.parse.quote(app_url)
    qr_api_link = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={encoded_url}&bgcolor=0b1120&color=f59e0b"

    col_qr1, col_qr2 = st.columns([1, 1])
    with col_qr1:
        st.image(qr_api_link, caption="Live QR Access Code")
    with col_qr2:
        st.markdown(f"""
        ### Instant Sharing:
        1. Open camera on any Android or iOS device.
        2. Scan the QR code to open the calculator.
        3. All modules are 100% mobile-friendly.
        
        **URL:** [{app_url}]({app_url})
        """)

# 2. CLASSROOM DEMO PROBLEMS
elif st.session_state.module == "🎯 Class Live Demo Problems":
    st.header("🎯 Preloaded Textbook Demo Problems")
    demo_choice = st.selectbox(
        "Choose Textbook Scenario",
        [
            "1. Strength of Materials: Mild Steel Tie Rod under Axial Load",
            "2. Fluid Mechanics: Pipe Flow Regime (Reynolds Number)",
            "3. Thermodynamics: Carnot Engine Thermal Efficiency"
        ]
    )

    if demo_choice == "1. Strength of Materials: Mild Steel Tie Rod under Axial Load":
        st.info("**Problem Statement:** A 20 mm diameter steel rod is subjected to an axial pull of 45 kN. Find the induced tensile stress.")
        st.latex(r"\sigma = \frac{F}{A} = \frac{45000}{\frac{\pi}{4}(0.02)^2}")
        if st.button("Solve Step-by-Step"):
            d = 0.02
            area = (math.pi / 4) * (d ** 2)
            force = 45000
            stress = calc_stress(force, area)
            st.success(f"**Calculated Area:** {area:.6f} m²")
            st.success(f"**Resulting Stress (σ):** {stress/1e6:.2f} MPa ({stress:.2f} Pa)")
            add_history("Demo Stress", f"F=45kN, d=20mm -> σ={stress/1e6:.2f}MPa")

    elif demo_choice == "2. Fluid Mechanics: Pipe Flow Regime (Reynolds Number)":
        st.info("**Problem Statement:** Water (ρ = 1000 kg/m³, μ = 0.001 Pa·s) flows at 0.08 m/s through a 25 mm internal diameter tube. Classify the flow regime.")
        st.latex(r"Re = \frac{\rho \times v \times D}{\mu}")
        if st.button("Solve Step-by-Step"):
            re = calc_reynolds(1000, 0.08, 0.025, 0.001)
            regime = "Laminar Flow (Re < 2300)" if re < 2300 else "Turbulent Flow"
            st.success(f"**Reynolds Number (Re):** {re:.2f}")
            st.success(f"**Flow Regime Assessment:** {regime}")
            add_history("Demo Reynolds", f"v=0.08m/s, D=25mm -> Re={re:.1f} ({regime})")

    elif demo_choice == "3. Thermodynamics: Carnot Engine Thermal Efficiency":
        st.info("**Problem Statement:** A heat engine receives heat at 800 K and rejects heat to a reservoir at 300 K. Determine the maximum theoretical efficiency.")
        st.latex(r"\eta_{\text{Carnot}} = \left(1 - \frac{T_L}{T_H}\right) \times 100\%")
        if st.button("Solve Step-by-Step"):
            eff = calc_heat_engine_eff(800.0, 300.0)
            st.success(f"**Maximum Theoretical Efficiency (η):** {eff:.2f} %")
            add_history("Demo Carnot", f"TH=800K, TL=300K -> η={eff:.2f}%")

# 3. ENGINEERING VISUALIZER
elif st.session_state.module == "📊 Engineering Visualizer":
    st.header("📊 Interactive Engineering Visualizer")
    chart_choice = st.selectbox("Select Curve to Plot", [
        "Stress vs. Strain (Hooke's Law)",
        "Isothermal Expansion (P-V Diagram)",
        "Torque vs. Rotational Speed (Constant Power)"
    ])

    if chart_choice == "Stress vs. Strain (Hooke's Law)":
        st.write("Generates linear elastic response curve based on Young's Modulus ($E$).")
        e_gpa = st.slider("Young's Modulus (GPa)", min_value=50, max_value=250, value=200, step=10)
        strains = [i * 0.0002 for i in range(1, 16)]
        stresses = [(s * e_gpa * 1000) for s in strains]
        df = pd.DataFrame({"Strain (ε)": strains, "Stress (MPa)": stresses}).set_index("Strain (ε)")
        st.line_chart(df)

    elif chart_choice == "Isothermal Expansion (P-V Diagram)":
        st.write("Plots pressure reduction across volume expansion ($P \propto 1/V$).")
        c = st.slider("Constant C (P × V)", min_value=100, max_value=1000, value=500, step=50)
        volumes = [v * 0.5 for v in range(1, 21)]
        pressures = [c / v for v in volumes]
        df = pd.DataFrame({"Volume (m³)": volumes, "Pressure (kPa)": pressures}).set_index("Volume (m³)")
        st.line_chart(df)

    elif chart_choice == "Torque vs. Rotational Speed (Constant Power)":
        st.write("Displays inverse relationship between torque and RPM at fixed power.")
        power_kw = st.slider("Rated Shaft Power (kW)", min_value=5, max_value=100, value=25, step=5)
        rpms = [rpm for rpm in range(500, 3100, 100)]
        torques = [calc_torque(power_kw * 1000, rpm) for rpm in rpms]
        df = pd.DataFrame({"Speed (RPM)": rpms, "Torque (N·m)": torques}).set_index("Speed (RPM)")
        st.line_chart(df)

# 4. GENERAL CALCULATOR
elif st.session_state.module == "🧮 General Calculator":
    st.header("🧮 General Purpose Calculator")
    op = st.selectbox("Operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (xʸ)", "Square Root (√x)", "Modulo (%)"])

    if op in ["Square Root (√x)"]:
        num = st.number_input("Enter value (x)", min_value=0.0, value=25.0)
        if st.button("Calculate"):
            res = math.sqrt(num)
            st.success(f"**√{num} = {res:.4f}**")
            add_history("Sqrt", f"√({num}) = {res:.4f}")
    else:
        num1 = st.number_input("Value 1 (x)", value=10.0)
        num2 = st.number_input("Value 2 (y)", value=2.0)
        if st.button("Calculate"):
            if op == "Addition (+)":
                res = num1 + num2
                st.success(f"**{num1} + {num2} = {res}**")
                add_history("Add", f"{num1} + {num2} = {res}")
            elif op == "Subtraction (-)":
                res = num1 - num2
                st.success(f"**{num1} - {num2} = {res}**")
                add_history("Sub", f"{num1} - {num2} = {res}")
            elif op == "Multiplication (×)":
                res = num1 * num2
                st.success(f"**{num1} × {num2} = {res}**")
                add_history("Mult", f"{num1} × {num2} = {res}")
            elif op == "Division (÷)":
                if num2 == 0:
                    st.error("Error: Division by zero!")
                else:
                    res = num1 / num2
                    st.success(f"**{num1} ÷ {num2} = {res:.4f}**")
                    add_history("Div", f"{num1} / {num2} = {res:.4f}")
            elif op == "Power (xʸ)":
                res = num1 ** num2
                st.success(f"**{num1}^{num2} = {res:.4f}**")
                add_history("Pow", f"{num1}^{num2} = {res:.4f}")
            elif op == "Modulo (%)":
                if num2 == 0:
                    st.error("Error: Modulo by zero!")
                else:
                    res = num1 % num2
                    st.success(f"**{num1} % {num2} = {res}**")
                    add_history("Mod", f"{num1} % {num2} = {res}")

# 5. MECHANICS
elif st.session_state.module == "1. Mechanics":
    st.header("1. Mechanics")
    sub = st.selectbox("Select Calculation", ["Force", "Work", "Power", "Kinetic Energy"])

    if sub == "Force":
        st.latex(r"F = m \times a")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=10.0)
        a = st.number_input("Acceleration (a) [m/s²]", value=9.81)
        if st.button("Calculate"):
            res = calc_force(m, a)
            st.success(f"**Force (F) = {res:.4f} N**")
            add_history("Force", f"m={m}kg, a={a}m/s² -> F={res:.2f}N")

    elif sub == "Work":
        st.latex(r"W = F \times d")
        f = st.number_input("Force (F) [N]", value=50.0)
        d = st.number_input("Displacement (d) [m]", value=5.0)
        if st.button("Calculate"):
            res = calc_work(f, d)
            st.success(f"**Work Done (W) = {res:.4f} J**")
            add_history("Work", f"F={f}N, d={d}m -> W={res:.2f}J")

    elif sub == "Power":
        st.latex(r"P = \frac{W}{t}")
        w = st.number_input("Work (W) [J]", value=500.0)
        t = st.number_input("Time (t) [s]", min_value=0.0001, value=10.0)
        if st.button("Calculate"):
            res = calc_power(w, t)
            st.success(f"**Power (P) = {res:.4f} W**")
            add_history("Power", f"W={w}J, t={t}s -> P={res:.2f}W")

    elif sub == "Kinetic Energy":
        st.latex(r"KE = \frac{1}{2} m v^2")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=2.0)
        v = st.number_input("Velocity (v) [m/s]", value=10.0)
        if st.button("Calculate"):
            res = calc_ke(m, v)
            st.success(f"**Kinetic Energy (KE) = {res:.4f} J**")
            add_history("KE", f"m={m}kg, v={v}m/s -> KE={res:.2f}J")

# 6. STRENGTH OF MATERIALS
elif st.session_state.module == "2. Strength of Materials":
    st.header("2. Strength of Materials")
    sub = st.selectbox("Select Calculation", ["Stress", "Strain", "Young's Modulus"])

    if sub == "Stress":
        st.latex(r"\sigma = \frac{F}{A}")
        f = st.number_input("Load (F) [N]", value=1000.0)
        a = st.number_input("Area (A) [m²]", min_value=0.000001, value=0.002, format="%.6f")
        if st.button("Calculate"):
            res = calc_stress(f, a)
            st.success(f"**Stress (σ) = {res:.2f} Pa ({res/1e6:.4f} MPa)**")
            add_history("Stress", f"F={f}N, A={a}m² -> σ={res/1e6:.2f}MPa")

    elif sub == "Strain":
        st.latex(r"\varepsilon = \frac{\Delta L}{L_0}")
        dl = st.number_input("Change in Length (ΔL) [mm]", value=0.5)
        l0 = st.number_input("Original Length (L₀) [mm]", min_value=0.001, value=100.0)
        if st.button("Calculate"):
            res = calc_strain(dl, l0)
            st.success(f"**Strain (ε) = {res:.6f} (dimensionless)**")
            add_history("Strain", f"ΔL={dl}mm, L0={l0}mm -> ε={res:.6f}")

    elif sub == "Young's Modulus":
        st.latex(r"E = \frac{\sigma}{\varepsilon}")
        stress = st.number_input("Stress (σ) [Pa]", value=200000000.0)
        strain = st.number_input("Strain (ε)", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate"):
            res = calc_youngs(stress, strain)
            st.success(f"**Young's Modulus (E) = {res/1e9:.3f} GPa**")
            add_history("Young's Mod", f"σ={stress}Pa, ε={strain} -> E={res/1e9:.2f}GPa")

# 7. THERMODYNAMICS
elif st.session_state.module == "3. Thermodynamics":
    st.header("3. Thermodynamics")
    sub = st.selectbox("Select Calculation", ["Heat Transfer", "Work Done (Constant P)", "Thermal Efficiency"])

    if sub == "Heat Transfer":
        st.latex(r"Q = m \times c \times \Delta T")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=1.0)
        c = st.number_input("Specific Heat (c) [J/(kg·K)]", min_value=0.0, value=4184.0)
        dt = st.number_input("Temp Change (ΔT) [K or °C]", value=20.0)
        if st.button("Calculate"):
            res = calc_heat(m, c, dt)
            st.success(f"**Heat Transfer (Q) = {res:.2f} J ({res/1000:.3f} kJ)**")
            add_history("Heat", f"m={m}, ΔT={dt} -> Q={res/1000:.2f}kJ")

    elif sub == "Work Done (Constant P)":
        st.latex(r"W = P \times \Delta V")
        p = st.number_input("Pressure (P) [Pa]", min_value=0.0, value=101325.0)
        dv = st.number_input("Volume Change (ΔV) [m³]", value=0.05, format="%.4f")
        if st.button("Calculate"):
            res = calc_work_done(p, dv)
            st.success(f"**Work Done (W) = {res:.2f} J**")
            add_history("Work (PΔV)", f"P={p}Pa, ΔV={dv}m³ -> W={res:.2f}J")

    elif sub == "Thermal Efficiency":
        st.latex(r"\eta = \left(\frac{W_{\text{net}}}{Q_{\text{in}}}\right) \times 100\%")
        w = st.number_input("Net Work Output [J]", min_value=0.0, value=400.0)
        q = st.number_input("Heat Input [J]", min_value=0.001, value=1000.0)
        if st.button("Calculate"):
            res = calc_thermal_eff(w, q)
            st.success(f"**Thermal Efficiency (η) = {res:.2f} %**")
            add_history("Eff", f"W={w}J, Q={q}J -> η={res:.2f}%")

# 8. FLUID MECHANICS
elif st.session_state.module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics")
    sub = st.selectbox("Select Calculation", ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"])

    if sub == "Pressure":
        st.latex(r"P = \frac{F}{A}")
        f = st.number_input("Force (F) [N]", value=500.0)
        a = st.number_input("Area (A) [m²]", min_value=0.0001, value=0.05)
        if st.button("Calculate"):
            res = calc_pressure(f, a)
            st.success(f"**Pressure (P) = {res:.2f} Pa ({res/1000:.3f} kPa)**")
            add_history("Pressure", f"F={f}N, A={a}m² -> P={res/1000:.2f}kPa")

    elif sub == "Reynolds Number":
        st.latex(r"Re = \frac{\rho \times v \times D}{\mu}")
        rho = st.number_input("Density (ρ) [kg/m³]", min_value=0.0, value=1000.0)
        v = st.number_input("Velocity (v) [m/s]", min_value=0.0, value=1.5)
        d = st.number_input("Pipe Diameter (D) [m]", min_value=0.0, value=0.05)
        mu = st.number_input("Viscosity (μ) [Pa·s]", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate"):
            re = calc_reynolds(rho, v, d, mu)
            regime = "Laminar Flow (Re < 2300)" if re < 2300 else ("Turbulent Flow (Re > 4000)" if re > 4000 else "Transitional Flow")
            st.success(f"**Reynolds Number (Re) = {re:.2f} ({regime})**")
            add_history("Reynolds", f"v={v}m/s, D={d}m -> Re={re:.1f}")

    elif sub == "Flow Velocity":
        st.latex(r"v = \frac{Q}{A}")
        q = st.number_input("Discharge (Q) [m³/s]", min_value=0.0, value=0.05)
        a = st.number_input("Area (A) [m²]", min_value=0.0001, value=0.02)
        if st.button("Calculate"):
            res = calc_velocity(q, a)
            st.success(f"**Velocity (v) = {res:.4f} m/s**")
            add_history("Flow Vel", f"Q={q}m³/s, A={a}m² -> v={res:.2f}m/s")

    elif sub == "Discharge":
        st.latex(r"Q = A \times v")
        a = st.number_input("Area (A) [m²]", min_value=0.0, value=0.02)
        v = st.number_input("Velocity (v) [m/s]", min_value=0.0, value=2.5)
        if st.button("Calculate"):
            res = calc_discharge(a, v)
            st.success(f"**Discharge (Q) = {res:.4f} m³/s**")
            add_history("Discharge", f"A={a}m², v={v}m/s -> Q={res:.4f}m³/s")

# 9. THERMAL ENGINEERING
elif st.session_state.module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering")
    sub = st.selectbox("Select Calculation", ["Heat Conduction", "COP (Refrigeration)", "Carnot Efficiency"])

    if sub == "Heat Conduction":
        st.latex(r"Q = \frac{k \times A \times \Delta T}{x}")
        k = st.number_input("Conductivity (k) [W/m·K]", min_value=0.0, value=45.0)
        a = st.number_input("Area (A) [m²]", min_value=0.0, value=2.0)
        dt = st.number_input("Temp Diff (ΔT) [K]", value=50.0)
        x = st.number_input("Thickness (x) [m]", min_value=0.0001, value=0.1)
        if st.button("Calculate"):
            res = calc_conduction(k, a, dt, x)
            st.success(f"**Conduction Heat (Q) = {res:.2f} W**")
            add_history("Conduction", f"k={k}, A={a} -> Q={res:.1f}W")

    elif sub == "COP (Refrigeration)":
        st.latex(r"COP = \frac{\text{Desired Effect}}{\text{Work Input}}")
        effect = st.number_input("Effect [kW]", min_value=0.0, value=7.5)
        work = st.number_input("Work [kW]", min_value=0.001, value=2.5)
        if st.button("Calculate"):
            res = calc_cop(effect, work)
            st.success(f"**COP = {res:.2f}**")
            add_history("COP", f"Effect={effect}kW, W={work}kW -> COP={res:.2f}")

    elif sub == "Carnot Efficiency":
        st.latex(r"\eta_{\text{Carnot}} = \left(1 - \frac{T_L}{T_H}\right) \times 100\%")
        th = st.number_input("Source Temp (T_H) [K]", min_value=0.1, value=600.0)
        tl = st.number_input("Sink Temp (T_L) [K]", min_value=0.0, value=300.0)
        if tl >= th:
            st.error("Sink Temperature (T_L) must be lower than Source (T_H).")
        else:
            if st.button("Calculate"):
                res = calc_heat_engine_eff(th, tl)
                st.success(f"**Carnot Efficiency = {res:.2f} %**")
                add_history("Carnot", f"TH={th}K, TL={tl}K -> η={res:.1f}%")

# 10. MACHINE DESIGN
elif st.session_state.module == "6. Machine Design":
    st.header("6. Machine Design")
    sub = st.selectbox("Select Calculation", ["Torque from Power & RPM", "Shaft Power", "Shaft Diameter"])

    if sub == "Torque from Power & RPM":
        st.latex(r"T = \frac{60 \times P}{2 \pi N}")
        p = st.number_input("Power (P) [Watts]", min_value=0.0, value=15000.0)
        n = st.number_input("Speed (N) [RPM]", min_value=0.1, value=1440.0)
        if st.button("Calculate"):
            res = calc_torque(p, n)
            st.success(f"**Torque (T) = {res:.2f} N·m**")
            add_history("Torque", f"P={p}W, N={n}RPM -> T={res:.2f}Nm")

    elif sub == "Shaft Power":
        st.latex(r"P = \frac{2 \pi N T}{60}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=99.5)
        n = st.number_input("Speed (N) [RPM]", min_value=0.0, value=1440.0)
        if st.button("Calculate"):
            res = calc_shaft_power(t, n)
            st.success(f"**Shaft Power (P) = {res:.2f} W ({res/1000:.3f} kW)**")
            add_history("Shaft Power", f"T={t}Nm, N={n}RPM -> P={res/1000:.2f}kW")

    elif sub == "Shaft Diameter":
        st.latex(r"d = \left(\frac{16 T}{\pi \tau}\right)^{\frac{1}{3}}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=250.0)
        tau = st.number_input("Allowable Shear Stress (τ) [MPa]", min_value=0.01, value=45.0)
        if st.button("Calculate"):
            d = calc_shaft_dia(t, tau * 1e6)
            st.success(f"**Diameter (d) = {d*1000:.2f} mm**")
            add_history("Shaft Dia", f"T={t}Nm, τ={tau}MPa -> d={d*1000:.2f}mm")

# 11. ADVANCED MECHANICAL UTILITIES (EXPANDED SUITE)
elif st.session_state.module == "🛠️ Mechanical Student Utilities":
    st.header("🛠️ Advanced Mechanical Student Utilities")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🔄 Unit Converter", 
        "🎡 Flywheel Energy",
        "🔩 Flange Coupling",
        "🌀 Helical Spring", 
        "⚙️ Belt Drive",
        "🏛️ Column Buckling", 
        "🛢️ Pressure Vessels"
    ])

    # Tool 1: Unit Converter
    with tab1:
        st.subheader("Unit Converter")
        tool = st.selectbox("Conversion Mode", ["Pressure", "Power", "Length", "Torque"])
        if tool == "Pressure":
            val = st.number_input("Pressure in Bar", value=1.0)
            st.info(f"**{val} Bar** = **{val * 100:.2f} kPa** = **{val * 14.5038:.2f} psi** = **{val * 0.9869:.3f} atm**")
        elif tool == "Power":
            val = st.number_input("Power in Kilowatts (kW)", value=1.0)
            st.info(f"**{val} kW** = **{val * 1.34102:.3f} HP (Horsepower)** = **{val * 1000:.1f} W**")
        elif tool == "Length":
            val = st.number_input("Length in Inches", value=1.0)
            st.info(f"**{val} in** = **{val * 25.4:.2f} mm** = **{val * 0.0254:.4f} m**")
        elif tool == "Torque":
            val = st.number_input("Torque in N·m", value=10.0)
            st.info(f"**{val} N·m** = **{val * 0.73756:.3f} lbf·ft** = **{val * 8.8507:.2f} lbf·in**")

    # Tool 2: Flywheel Energy Storage
    with tab2:
        st.subheader("Flywheel Kinetic Energy & Energy Fluctuation")
        st.latex(r"E = \frac{1}{2} I \omega^2, \quad \Delta E = I \omega^2 C_s")
        m_fly = st.number_input("Flywheel Mass (m) [kg]", min_value=1.0, value=250.0)
        k_fly = st.number_input("Radius of Gyration (k) [meters]", min_value=0.01, value=0.45)
        rpm_fly = st.number_input("Mean Rotational Speed (N) [RPM]", min_value=1.0, value=720.0)
        cs_fly = st.number_input("Coefficient of Speed Fluctuation (C_s)", min_value=0.001, max_value=0.5, value=0.03, step=0.005)

        if st.button("Calculate Flywheel Energy"):
            i_val, e_tot, delta_e = calc_flywheel(m_fly, k_fly, rpm_fly, cs_fly)
            st.success(f"**Mass Moment of Inertia (I):** {i_val:.3f} kg·m²")
            st.success(f"**Stored Kinetic Energy (E):** {e_tot/1000:.2f} kJ ({e_tot:.1f} J)")
            st.info(f"**Maximum Energy Fluctuation (ΔE):** {delta_e/1000:.2f} kJ")
            add_history("Flywheel", f"m={m_fly}kg, N={rpm_fly}RPM -> E={e_tot/1000:.1f}kJ, ΔE={delta_e/1000:.2f}kJ")

    # Tool 3: Rigid Flange Coupling Dimensions
    with tab3:
        st.subheader("Protected Rigid Flange Coupling Proportioner")
        st.write("Calculates empirical standard design dimensions from shaft diameter ($d$):")
        st.latex(r"D = 2d, \quad L = 1.5d, \quad D_1 = 3d, \quad D_2 = 4d, \quad t_f = 0.5d")
        d_shaft = st.number_input("Shaft Diameter (d) [mm]", min_value=5.0, value=40.0)

        if st.button("Determine Coupling Proportions"):
            d_hub, l_hub, d_pitch, d_outside, t_flange = calc_flange_coupling(d_shaft)
            st.markdown(f"""
            - **Hub Outside Diameter ($D = 2d$):** `{d_hub:.1f} mm`
            - **Hub Length ($L = 1.5d$):** `{l_hub:.1f} mm`
            - **Pitch Circle Diameter of Bolts ($D_1 = 3d$):** `{d_pitch:.1f} mm`
            - **Outside Flange Diameter ($D_2 = 4d$):** `{d_outside:.1f} mm`
            - **Thickness of Flange ($t_f = 0.5d$):** `{t_flange:.1f} mm`
            """)
            add_history("Flange Coupling", f"d={d_shaft}mm -> Hub D={d_hub}mm, PCD={d_pitch}mm")

    # Tool 4: Helical Spring
    with tab4:
        st.subheader("Helical Compression Spring Design")
        st.latex(r"k = \frac{G \cdot d^4}{8 \cdot D^3 \cdot n}, \quad \tau = \frac{8 \cdot W \cdot D}{\pi \cdot d^3}")
        g_gpa = st.number_input("Shear Modulus (G) [GPa]", min_value=1.0, value=79.0)
        w_load = st.number_input("Axial Load (W) [N]", min_value=0.1, value=500.0)
        d_wire = st.number_input("Wire Diameter (d) [mm]", min_value=0.1, value=5.0)
        d_mean = st.number_input("Mean Coil Diameter (D) [mm]", min_value=1.0, value=40.0)
        n_coils = st.number_input("Number of Active Coils (n)", min_value=1, value=10)

        if st.button("Calculate Spring Parameters"):
            g_pa = g_gpa * 1e9
            d_m = d_wire / 1000.0
            d_mean_m = d_mean / 1000.0
            k_stiffness = calc_spring_stiffness(g_pa, d_m, d_mean_m, n_coils)
            tau_stress = calc_spring_shear_stress(w_load, d_mean_m, d_m)
            c_index = d_mean / d_wire
            st.success(f"**Spring Stiffness (k):** {k_stiffness/1000:.2f} N/mm ({k_stiffness:.1f} N/m)")
            st.success(f"**Torsional Shear Stress (τ):** {tau_stress/1e6:.2f} MPa")
            st.info(f"**Spring Index (C = D/d):** {c_index:.2f}")
            add_history("Spring", f"W={w_load}N, k={k_stiffness/1000:.2f}N/mm -> τ={tau_stress/1e6:.2f}MPa")

    # Tool 5: Belt Drive
    with tab5:
        st.subheader("Belt Drive Speed Ratio & Velocity")
        st.latex(r"N_2 = \frac{N_1 \cdot D_1}{D_2}, \quad v = \frac{\pi \cdot D_1 \cdot N_1}{60}")
        d1 = st.number_input("Driver Pulley Diameter (D₁) [mm]", min_value=1.0, value=250.0)
        n1 = st.number_input("Driver Speed (N₁) [RPM]", min_value=1.0, value=1440.0)
        d2 = st.number_input("Driven Pulley Diameter (D₂) [mm]", min_value=1.0, value=500.0)

        if st.button("Calculate Belt Transmission"):
            n2, belt_vel = calc_belt_drive(d1, n1, d2)
            ratio = d2 / d1
            st.success(f"**Driven Shaft Speed (N₂):** {n2:.2f} RPM")
            st.success(f"**Linear Belt Velocity (v):** {belt_vel:.2f} m/s")
            st.info(f"**Velocity Ratio (D₂/D₁):** {ratio:.2f} : 1")
            add_history("Belt Drive", f"D1={d1}mm, N1={n1}RPM -> N2={n2:.1f}RPM, v={belt_vel:.2f}m/s")

    # Tool 6: Column Buckling
    with tab6:
        st.subheader("Euler's Critical Buckling Load (P_cr)")
        st.latex(r"P_{cr} = \frac{\pi^2 E I}{L_e^2}")
        e_val = st.number_input("Modulus of Elasticity (E) [GPa]", min_value=1.0, value=200.0)
        i_val = st.number_input("Moment of Inertia (I) [cm⁴]", min_value=0.01, value=150.0)
        col_l = st.number_input("Column Length (L) [meters]", min_value=0.1, value=3.0)
        end_cond = st.selectbox("End Conditions", ["Both Ends Pinned", "Both Ends Fixed", "One Fixed, One Free", "One Fixed, One Pinned"])
        
        if st.button("Calculate Buckling Load"):
            e_pa = e_val * 1e9
            i_m4 = i_val * 1e-8
            p_cr = calc_euler_buckling(e_pa, i_m4, col_l, end_cond)
            st.success(f"**Critical Buckling Load (P_cr):** {p_cr/1000:.2f} kN ({p_cr:.2f} N)")
            add_history("Buckling", f"L={col_l}m, {end_cond} -> P_cr={p_cr/1000:.2f}kN")

    # Tool 7: Pressure Vessels
    with tab7:
        st.subheader("Thin-Walled Pressure Vessel Stresses")
        st.latex(r"\sigma_h = \frac{P \cdot d}{2t}, \quad \sigma_l = \frac{P \cdot d}{4t}")
        p_in = st.number_input("Internal Pressure (P) [MPa]", min_value=0.01, value=2.0)
        d_in = st.number_input("Internal Diameter (d) [mm]", min_value=1.0, value=500.0)
        t_in = st.number_input("Wall Thickness (t) [mm]", min_value=0.1, value=10.0)

        if st.button("Calculate Vessel Stresses"):
            sigma_h = calc_hoop_stress(p_in, d_in, t_in)
            sigma_l = calc_longitudinal_stress(p_in, d_in, t_in)
            st.success(f"**Hoop (Circumferential) Stress (σ_h):** {sigma_h:.2f} MPa")
            st.success(f"**Longitudinal Stress (σ_l):** {sigma_l:.2f} MPa")
            add_history("Vessel Stress", f"P={p_in}MPa, d={d_in}mm -> σ_h={sigma_h:.2f}MPa")
