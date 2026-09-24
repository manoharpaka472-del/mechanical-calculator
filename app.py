import streamlit as st
import math

# Page setup
st.set_page_config(
    page_title="Mechanical Engineering Portal",
    page_icon="⚙️",
    layout="centered"
)

# ----------------- SESSION STATE & HISTORY ----------------- #
if "module" not in st.session_state:
    st.session_state.module = "🏠 Home Menu"

if "calc_history" not in st.session_state:
    st.session_state.calc_history = []

def add_history(entry_text):
    st.session_state.calc_history.insert(0, entry_text)
    if len(st.session_state.calc_history) > 5:
        st.session_state.calc_history.pop()

def go_home():
    st.session_state.module = "🏠 Home Menu"

def set_module(name):
    st.session_state.module = name

# ----------------- CUSTOM 3D CSS & DARK STYLING ----------------- #
st.markdown("""
<style>
    /* Dark Metallic Background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Student Profile Badge */
    .student-badge {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }
    .badge-name {
        font-size: 1.35rem;
        font-weight: 700;
        color: #38bdf8;
        letter-spacing: 0.5px;
    }
    .badge-sub {
        font-size: 0.95rem;
        color: #94a3b8;
        margin-top: 4px;
    }

    /* 3D Tactile Buttons */
    div.stButton > button {
        background: linear-gradient(180deg, #3b82f6 0%, #1d4ed8 100%) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        box-shadow: 0 4px 0 #1e40af, 0 8px 12px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.1s ease-in-out !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(180deg, #60a5fa 0%, #2563eb 100%) !important;
        transform: translateY(-1px);
    }
    div.stButton > button:active {
        transform: translateY(4px) !important;
        box-shadow: 0 0 0 #1e40af, 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- PROFILE BANNER ----------------- #
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

# ----------------- SIDEBAR & NAVIGATION ----------------- #
module_options = [
    "🏠 Home Menu",
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

# Sidebar: Rolling Calculation History (Last 5)
st.sidebar.divider()
st.sidebar.subheader("🕒 Last 5 Calculations")
if st.session_state.calc_history:
    for idx, item in enumerate(st.session_state.calc_history, 1):
        st.sidebar.caption(f"**{idx}.** {item}")
    if st.sidebar.button("Clear History", use_container_width=True):
        st.session_state.calc_history = []
        st.rerun()
else:
    st.sidebar.caption("No recent calculations yet.")


# ----------------- MAIN VIEW ROUTING ----------------- #
if st.session_state.module != "🏠 Home Menu":
    if st.button("⬅️ Back to Main Menu", key="top_back"):
        go_home()
        st.rerun()
    st.divider()

# --- HOME DASHBOARD ---
if st.session_state.module == "🏠 Home Menu":
    st.markdown("### 🚀 Engineering Modules & Tools")
    st.write("Select a module below to launch formulas and automated solving:")

    colA, colB = st.columns(2)
    with colA:
        if st.button("🧮 General Calculator", use_container_width=True):
            set_module("🧮 General Calculator")
            st.rerun()
        if st.button("1. Mechanics", use_container_width=True):
            set_module("1. Mechanics")
            st.rerun()
        if st.button("2. Strength of Materials", use_container_width=True):
            set_module("2. Strength of Materials")
            st.rerun()
        if st.button("3. Thermodynamics", use_container_width=True):
            set_module("3. Thermodynamics")
            st.rerun()

    with colB:
        if st.button("🛠️ Mech Quick Tools", use_container_width=True):
            set_module("🛠️ Mech Quick Tools")
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

# --- GENERAL CALCULATOR MODE ---
elif st.session_state.module == "🧮 General Calculator":
    st.header("🧮 General & Scientific Calculator")
    calc_type = st.radio("Operation Type", ["Basic Arithmetic (+, -, ×, ÷)", "Scientific Powers & Roots", "Trigonometry"], horizontal=True)

    if calc_type == "Basic Arithmetic (+, -, ×, ÷)":
        c1, c2, c3 = st.columns([2, 1, 2])
        with c1:
            num1 = st.number_input("Number 1", value=0.0)
        with c2:
            op = st.selectbox("Operator", ["+", "-", "×", "÷"])
        with c3:
            num2 = st.number_input("Number 2", value=0.0)

        if st.button("Calculate Result"):
            if op == "+": res = num1 + num2
            elif op == "-": res = num1 - num2
            elif op == "×": res = num1 * num2
            elif op == "÷": res = num1 / num2 if num2 != 0 else "Error: Division by 0"

            if isinstance(res, (int, float)):
                record = f"{num1} {op} {num2} = {res:.4f}"
                add_history(record)
                st.success(f"**Result:** {res:.4f}")
            else:
                st.error(res)

    elif calc_type == "Scientific Powers & Roots":
        sub_sc = st.selectbox("Function", ["Square Root (√x)", "Power (xʸ)", "Natural Log (ln x)", "Base-10 Log (log₁₀ x)"])
        x_val = st.number_input("Value (x)", value=9.0)
        y_val = 0.0
        if sub_sc == "Power (xʸ)":
            y_val = st.number_input("Power (y)", value=2.0)

        if st.button("Calculate Result"):
            if sub_sc == "Square Root (√x)":
                res = math.sqrt(x_val) if x_val >= 0 else None
                rec_str = f"√({x_val}) = {res:.4f}" if res is not None else "Math Error"
            elif sub_sc == "Power (xʸ)":
                res = x_val ** y_val
                rec_str = f"{x_val}^{y_val} = {res:.4f}"
            elif sub_sc == "Natural Log (ln x)":
                res = math.log(x_val) if x_val > 0 else None
                rec_str = f"ln({x_val}) = {res:.4f}" if res is not None else "Math Error"
            elif sub_sc == "Base-10 Log (log₁₀ x)":
                res = math.log10(x_val) if x_val > 0 else None
                rec_str = f"log10({x_val}) = {res:.4f}" if res is not None else "Math Error"

            if res is not None:
                add_history(rec_str)
                st.success(f"**Result:** {res:.6f}")
            else:
                st.error("Input out of domain!")

    elif calc_type == "Trigonometry":
        angle_deg = st.number_input("Angle (in Degrees)", value=45.0)
        trig_fn = st.selectbox("Function", ["sin(θ)", "cos(θ)", "tan(θ)"])
        if st.button("Calculate Result"):
            rad = math.radians(angle_deg)
            if trig_fn == "sin(θ)": res = math.sin(rad)
            elif trig_fn == "cos(θ)": res = math.cos(rad)
            elif trig_fn == "tan(θ)": res = math.tan(rad) if (angle_deg % 180 != 90) else "Undefined"

            if isinstance(res, float):
                record = f"{trig_fn} @ {angle_deg}° = {res:.4f}"
                add_history(record)
                st.success(f"**Result:** {res:.4f}")
            else:
                st.error(res)

# --- QUICK TOOLS (CONVERTERS & MATERIAL PROPS) ---
elif st.session_state.module == "🛠️ Mech Quick Tools":
    st.header("🛠️ Engineering Student Quick Tools")
    tool_tab1, tool_tab2 = st.tabs(["🔄 Unit Converters", "📋 Material Properties Table"])

    with tool_tab1:
        st.subheader("Fast Unit Conversions")
        conv_type = st.selectbox("Conversion Type", ["Pressure", "Power", "Length"])
        if conv_type == "Pressure":
            val = st.number_input("Pressure value in Bar", value=1.0)
            st.info(f"**{val} Bar equals:**\n- **{val * 100000:.2f}** Pascals (Pa)\n- **{val * 100:.2f}** kPa\n- **{val * 0.1:.4f}** MPa\n- **{val * 14.5038:.2f}** psi")
        elif conv_type == "Power":
            val = st.number_input("Power value in Kilowatts (kW)", value=1.0)
            st.info(f"**{val} kW equals:**\n- **{val * 1000:.2f}** Watts (W)\n- **{val * 1.34102:.3f}** Horsepower (HP)\n- **{val * 859.845:.2f}** kcal/h")
        elif conv_type == "Length":
            val = st.number_input("Length in Millimeters (mm)", value=25.4)
            st.info(f"**{val} mm equals:**\n- **{val / 1000:.4f}** Meters (m)\n- **{val / 10:.3f}** Centimeters (cm)\n- **{val / 25.4:.4f}** Inches (in)")

    with tool_tab2:
        st.subheader("Standard Mechanical Properties (Room Temp)")
        st.markdown("""
        | Material | Density (kg/m³) | Young's Modulus (GPa) | Yield Strength (MPa) |
        | :--- | :--- | :--- | :--- |
        | **Structural Steel (A36)** | 7850 | 200 | 250 |
        | **Stainless Steel (304)** | 8000 | 193 | 215 |
        | **Aluminum (6061-T6)** | 2700 | 69 | 276 |
        | **Cast Iron (Gray)** | 7200 | 110 | 130 |
        | **Titanium (Grade 5)** | 4430 | 114 | 880 |
        | **Brass (C36000)** | 8500 | 97 | 310 |
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
