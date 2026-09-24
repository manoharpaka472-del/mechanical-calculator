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

def set_module(name):
    st.session_state.module = name

def clear_history():
    st.session_state.calc_history = []

# ----------------- RELIABLE 3D CSS & BACKGROUND ----------------- #
st.markdown("""
<style>
    /* Dark Slate Background */
    .stApp {
        background-color: #0f172a;
        background: radial-gradient(circle at 50% 15%, #1e293b 0%, #090d16 100%);
        color: #f8fafc;
    }

    /* Student Profile Badge Card */
    .student-badge {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 2px solid #f59e0b;
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
    }
    .badge-name {
        font-size: 1.4rem;
        font-weight: 800;
        color: #fbbf24;
        letter-spacing: 0.5px;
    }
    .badge-sub {
        font-size: 0.95rem;
        color: #cbd5e1;
        margin-top: 4px;
    }

    /* Reliable 3D Gold/Orange Buttons (No pointer-blocking transforms) */
    div.stButton > button {
        background: linear-gradient(180deg, #f59e0b 0%, #d97706 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: 1px solid #b45309 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 0 #78350f, 0 8px 12px rgba(0, 0, 0, 0.4) !important;
        cursor: pointer !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(180deg, #fbbf24 0%, #d97706 100%) !important;
        color: #ffffff !important;
    }
    div.stButton > button:active {
        box-shadow: 0 1px 0 #78350f !important;
    }

    /* Simulation Output Box */
    .demo-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 10px;
        padding: 14px;
        margin: 12px 0px;
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
def calc_force(m, a): return m * a
def calc_work(f, d): return f * d
def calc_power(w, t): return w / t if t > 0 else None
def calc_kinetic_energy(m, v): return 0.5 * m * (v ** 2)

def calc_stress(f, a): return f / a if a > 0 else None
def calc_strain(dl, l0): return dl / l0 if l0 > 0 else None
def calc_youngs(s, e): return s / e if e > 0 else None

def calc_heat(m, c, dt): return m * c * dt
def calc_isobaric(p, dv): return p * dv
def calc_eff(w, q): return (w / q) * 100 if q > 0 else None

def calc_pressure(f, a): return f / a if a > 0 else None
def calc_reynolds(rho, v, d, mu): return (rho * v * d) / mu if mu > 0 else None
def calc_flow_vel(q, a): return q / a if a > 0 else None
def calc_discharge(a, v): return a * v

def calc_conduction(k, a, dt, x): return (k * a * dt) / x if x > 0 else None
def calc_cop(effect, work): return effect / work if work > 0 else None
def calc_carnot(th, tl): return (1 - (tl / th)) * 100 if th > 0 else None

def calc_torque(p, rpm):
    return (p * 60) / (2 * math.pi * rpm) if rpm > 0 else None
def calc_shaft_power(t, rpm):
    return (2 * math.pi * rpm * t) / 60
def calc_shaft_diameter(t, tau):
    return ((16 * t) / (math.pi * tau)) ** (1 / 3) if tau > 0 else None

def calc_beam_center_load(load_n, length_m, e_pa, i_m4):
    max_deflection = (load_n * (length_m ** 3)) / (48 * e_pa * i_m4) if (e_pa * i_m4) > 0 else None
    max_moment = (load_n * length_m) / 4
    return max_deflection, max_moment

# ----------------- SIDEBAR CONTROLS ----------------- #
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

# Sidebar Dropdown sync
current_idx = module_options.index(st.session_state.module) if st.session_state.module in module_options else 0
chosen = st.sidebar.selectbox("Navigation Menu", module_options, index=current_idx)
if chosen != st.session_state.module:
    st.session_state.module = chosen
    st.rerun()

if st.session_state.module != "🏠 Home Menu":
    st.sidebar.button("⬅️ Return to Main Menu", on_click=set_module, args=("🏠 Home Menu",), use_container_width=True, key="side_back")

# History Panel
st.sidebar.divider()
st.sidebar.subheader("🕒 History (Last 10)")
if st.session_state.calc_history:
    for idx, item in enumerate(st.session_state.calc_history, 1):
        st.sidebar.caption(f"**{idx}.** {item}")

    history_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(st.session_state.calc_history)])
    st.sidebar.download_button(
        label="📥 Download History (.txt)",
        data=history_text,
        file_name="p_manohar_calc_history.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.sidebar.button("🗑️ Clear History", on_click=clear_history, use_container_width=True)
else:
    st.sidebar.caption("No calculations recorded yet.")

# ----------------- MAIN VIEW ----------------- #
if st.session_state.module != "🏠 Home Menu":
    st.button("⬅️ Back to Main Menu", on_click=set_module, args=("🏠 Home Menu",), key="main_back")
    st.divider()

# --- HOME DASHBOARD ---
if st.session_state.module == "🏠 Home Menu":
    st.markdown("### 🚀 Engineering Portal Dashboard")
    st.write("Click any module below to open its calculator and formulas:")

    c1, c2 = st.columns(2)
    with c1:
        st.button("🏫 Classroom Demos", on_click=set_module, args=("🏫 Classroom Demos",), use_container_width=True)
        st.button("🔄 Unit Converter Mode", on_click=set_module, args=("🔄 Unit Converter Mode",), use_container_width=True)
        st.button("🧮 General Calculator", on_click=set_module, args=("🧮 General Calculator",), use_container_width=True)
        st.button("1. Mechanics", on_click=set_module, args=("1. Mechanics",), use_container_width=True)
        st.button("2. Strength of Materials", on_click=set_module, args=("2. Strength of Materials",), use_container_width=True)

    with c2:
        st.button("🛠️ Mech Quick Tools", on_click=set_module, args=("🛠️ Mech Quick Tools",), use_container_width=True)
        st.button("3. Thermodynamics", on_click=set_module, args=("3. Thermodynamics",), use_container_width=True)
        st.button("4. Fluid Mechanics", on_click=set_module, args=("4. Fluid Mechanics",), use_container_width=True)
        st.button("5. Thermal Engineering", on_click=set_module, args=("5. Thermal Engineering",), use_container_width=True)
        st.button("6. Machine Design", on_click=set_module, args=("6. Machine Design",), use_container_width=True)

# --- CLASSROOM DEMOS ---
elif st.session_state.module == "🏫 Classroom Demos":
    st.header("🏫 Classroom Interactive Demo Simulator")
    demo_tab1, demo_tab2 = st.tabs(["1. Beam Deflection Simulator", "2. Simple Gear Train Simulator"])

    with demo_tab1:
        st.latex(r"\delta_{\max} = \frac{F \cdot L^3}{48 \cdot E \cdot I}, \quad M_{\max} = \frac{F \cdot L}{4}")
        f_load = st.number_input("Applied Load (F) [N]", min_value=10.0, value=5000.0, step=100.0)
        l_beam = st.number_input("Span Length (L) [m]", min_value=0.1, value=2.5, step=0.1)
        e_mat = st.selectbox("Beam Material (E)", ["Structural Steel (200 GPa)", "Aluminum (69 GPa)", "Cast Iron (110 GPa)"])
        e_val = 200e9 if "Steel" in e_mat else (69e9 if "Aluminum" in e_mat else 110e9)
        i_val = st.number_input("Area Moment of Inertia (I) [cm⁴]", min_value=0.1, value=450.0) * 1e-8

        if st.button("Simulate Beam Deflection"):
            defl_m, m_max = calc_beam_center_load(f_load, l_beam, e_val, i_val)
            defl_mm = defl_m * 1000
            add_history(f"Beam: F={f_load}N, L={l_beam}m ➔ Defl={defl_mm:.3f}mm")
            st.success(f"**Max Bending Moment:** {m_max:.2f} N·m | **Central Deflection:** {defl_mm:.3f} mm")

    with demo_tab2:
        st.latex(r"i = \frac{T_2}{T_1}, \quad N_2 = \frac{N_1}{i}, \quad \tau_2 = \tau_1 \times i")
        z1 = st.number_input("Driver Gear Teeth (T₁)", min_value=1, value=20)
        z2 = st.number_input("Driven Gear Teeth (T₂)", min_value=1, value=60)
        n1 = st.number_input("Driver Speed (N₁) [RPM]", min_value=1.0, value=1500.0)
        t1 = st.number_input("Driver Torque (τ₁) [N·m]", min_value=0.1, value=30.0)

        if st.button("Simulate Gearbox"):
            ratio = z2 / z1
            n2 = n1 / ratio
            t2 = t1 * ratio
            add_history(f"Gears: Ratio={ratio:.2f}:1, Driven Speed={n2:.1f} RPM")
            st.success(f"**Ratio:** {ratio:.2f}:1 | **Driven Speed (N₂):** {n2:.2f} RPM | **Output Torque (τ₂):** {t2:.2f} N·m")

# --- UNIT CONVERTER MODE ---
elif st.session_state.module == "🔄 Unit Converter Mode":
    st.header("🔄 Mechanical Unit Converter")
    conv_category = st.selectbox("Property", ["Pressure", "Power", "Force", "Length"])

    if conv_category == "Pressure":
        st.latex(r"1\text{ bar} = 10^5\text{ Pa} = 0.1\text{ MPa} = 14.5038\text{ psi}")
        val_p = st.number_input("Value in Bar", value=1.0)
        st.info(f"**{val_p} Bar =** {val_p * 1e5:.2f} Pa | {val_p * 0.1:.4f} MPa | {val_p * 14.5038:.3f} psi")
        if st.button("Save to History"):
            add_history(f"{val_p} bar ➔ {val_p * 0.1:.2f} MPa")
            st.success("Logged!")

    elif conv_category == "Power":
        st.latex(r"1\text{ kW} = 1000\text{ W} = 1.34102\text{ HP}")
        val_pw = st.number_input("Value in kW", value=5.0)
        st.info(f"**{val_pw} kW =** {val_pw * 1000:.2f} W | {val_pw * 1.34102:.3f} HP | {val_pw * 859.845:.2f} kcal/h")
        if st.button("Save to History"):
            add_history(f"{val_pw} kW ➔ {val_pw * 1.34102:.2f} HP")
            st.success("Logged!")

    elif conv_category == "Force":
        st.latex(r"1\text{ kN} = 1000\text{ N} = 224.809\text{ lbf}")
        val_f = st.number_input("Value in kN", value=2.0)
        st.info(f"**{val_f} kN =** {val_f * 1000:.2f} N | {val_f * 224.809:.2f} lbf | {val_f * 101.972:.2f} kgf")
        if st.button("Save to History"):
            add_history(f"{val_f} kN ➔ {val_f * 1000:.0f} N")
            st.success("Logged!")

    elif conv_category == "Length":
        val_l = st.number_input("Value in mm", value=25.4)
        st.info(f"**{val_l} mm =** {val_l / 1000:.4f} m | {val_l / 10:.2f} cm | {val_l / 25.4:.4f} in")
        if st.button("Save to History"):
            add_history(f"{val_l} mm ➔ {val_l / 25.4:.3f} in")
            st.success("Logged!")

# --- GENERAL CALCULATOR ---
elif st.session_state.module == "🧮 General Calculator":
    st.header("🧮 General & Scientific Calculator")
    c_mode = st.radio("Operation", ["Basic Math", "Powers / Roots", "Trigonometry"], horizontal=True)

    if c_mode == "Basic Math":
        col1, col2, col3 = st.columns([2, 1, 2])
        with col1: n1 = st.number_input("Num 1", value=10.0)
        with col2: oper = st.selectbox("Op", ["+", "-", "×", "÷"])
        with col3: n2 = st.number_input("Num 2", value=2.0)

        if st.button("Compute"):
            if oper == "+": res = n1 + n2
            elif oper == "-": res = n1 - n2
            elif oper == "×": res = n1 * n2
            elif oper == "÷": res = n1 / n2 if n2 != 0 else "Error: Div by 0"

            if isinstance(res, (int, float)):
                add_history(f"{n1} {oper} {n2} = {res:.4f}")
                st.success(f"**Result:** {res:.4f}")
            else:
                st.error(res)

    elif c_mode == "Powers / Roots":
        sc_choice = st.selectbox("Select", ["Square Root (√x)", "Power (xʸ)", "Natural Log (ln x)"])
        x_in = st.number_input("Value (x)", value=16.0)
        y_in = 2.0
        if sc_choice == "Power (xʸ)":
            y_in = st.number_input("Power (y)", value=2.0)

        if st.button("Compute"):
            if sc_choice == "Square Root (√x)":
                ans = math.sqrt(x_in) if x_in >= 0 else None
                rec = f"√({x_in}) = {ans:.4f}"
            elif sc_choice == "Power (xʸ)":
                ans = x_in ** y_in
                rec = f"{x_in}^{y_in} = {ans:.4f}"
            elif sc_choice == "Natural Log (ln x)":
                ans = math.log(x_in) if x_in > 0 else None
                rec = f"ln({x_in}) = {ans:.4f}"

            if ans is not None:
                add_history(rec)
                st.success(f"**Result:** {ans:.4f}")
            else:
                st.error("Invalid domain")

    elif c_mode == "Trigonometry":
        deg = st.number_input("Angle in Degrees", value=45.0)
        fn_trig = st.selectbox("Function", ["sin", "cos", "tan"])
        if st.button("Compute"):
            rad = math.radians(deg)
            if fn_trig == "sin": out = math.sin(rad)
            elif fn_trig == "cos": out = math.cos(rad)
            elif fn_trig == "tan": out = math.tan(rad) if (deg % 180 != 90) else "Undefined"

            if isinstance(out, float):
                add_history(f"{fn_trig}({deg}°) = {out:.4f}")
                st.success(f"**Result:** {out:.4f}")
            else:
                st.error(out)

# --- MECH QUICK TOOLS ---
elif st.session_state.module == "🛠️ Mech Quick Tools":
    st.header("🛠️ Mechanical Quick Reference")
    st.markdown("""
    | Material | Density (kg/m³) | Young's Modulus (GPa) | Yield Strength (MPa) |
    | :--- | :--- | :--- | :--- |
    | **Mild Steel** | 7850 | 200 | 250 |
    | **Stainless Steel (304)** | 8000 | 193 | 215 |
    | **Aluminum (6061-T6)** | 2700 | 69 | 276 |
    | **Gray Cast Iron** | 7200 | 110 | 130 |
    | **Titanium Gr. 5** | 4430 | 114 | 880 |
    | **Brass** | 8500 | 97 | 310 |
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
