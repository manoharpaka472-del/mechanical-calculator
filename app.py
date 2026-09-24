import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Mechanical Engineering Calculator",
    page_icon="⚙️",
    layout="centered"
)

# Custom Stylish CSS
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        background: linear-gradient(90deg, #1E88E5, #00E676);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .badge-card {
        background: rgba(30, 136, 229, 0.1);
        border: 1px solid #1E88E5;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        margin-bottom: 20px;
        color: #E0E0E0;
    }
    .history-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #00E676;
        padding: 8px 12px;
        margin: 6px 0;
        border-radius: 4px;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE SETUP ----------------- #
if "module" not in st.session_state:
    st.session_state.module = "🏠 Home Menu"

if "history" not in st.session_state:
    st.session_state.history = []

def add_history(calc_str):
    st.session_state.history.append(calc_str)
    if len(st.session_state.history) > 5:
        st.session_state.history.pop(0)

def go_home():
    st.session_state.module = "🏠 Home Menu"

def set_module(name):
    st.session_state.module = name

# ----------------- CALCULATION FUNCTIONS ----------------- #

# 1. Mechanics
def calc_force(mass, acceleration):
    return mass * acceleration

def calc_work(force, distance):
    return force * distance

def calc_power(work, time):
    return work / time if time > 0 else None

def calc_kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

# 2. Strength of Materials
def calc_stress(force, area):
    return force / area if area > 0 else None

def calc_strain(delta_l, original_l):
    return delta_l / original_l if original_l > 0 else None

def calc_youngs_modulus(stress, strain):
    return stress / strain if strain > 0 else None

# 3. Thermodynamics
def calc_heat_transfer(mass, specific_heat, delta_t):
    return mass * specific_heat * delta_t

def calc_work_done_isobaric(pressure, delta_v):
    return pressure * delta_v

def calc_thermal_efficiency(work_net, heat_in):
    return (work_net / heat_in) * 100 if heat_in > 0 else None

# 4. Fluid Mechanics
def calc_pressure(force, area):
    return force / area if area > 0 else None

def calc_reynolds(density, velocity, diameter, viscosity):
    return (density * velocity * diameter) / viscosity if viscosity > 0 else None

def calc_flow_velocity(discharge, area):
    return discharge / area if area > 0 else None

def calc_discharge(area, velocity):
    return area * velocity

# 5. Thermal Engineering
def calc_conduction(k, area, delta_t, thickness):
    return (k * area * delta_t) / thickness if thickness > 0 else None

def calc_cop(desired_effect, work_input):
    return desired_effect / work_input if work_input > 0 else None

def calc_heat_engine_eff(t_high, t_low):
    return (1 - (t_low / t_high)) * 100 if t_high > 0 else None

# 6. Machine Design
def calc_torque(power, speed_rpm):
    if speed_rpm > 0:
        omega = (2 * math.pi * speed_rpm) / 60
        return power / omega
    return None

def calc_shaft_power(torque, speed_rpm):
    omega = (2 * math.pi * speed_rpm) / 60
    return torque * omega

def calc_shaft_diameter(torque, allowable_shear_stress):
    if allowable_shear_stress > 0:
        return ((16 * torque) / (math.pi * allowable_shear_stress)) ** (1 / 3)
    return None


# ----------------- SIDEBAR ----------------- #
st.sidebar.markdown("""
<div class="badge-card">
    <b>Student Project</b><br>
    👨‍🎓 <b>Name:</b> Vignesh<br>
    🆔 <b>Roll No:</b> 2505A31052
</div>
""", unsafe_allow_html=True)

nav_options = [
    "🏠 Home Menu",
    "🧮 General Calculator",
    "🔧 Engineering Tools & Tables",
    "1. Mechanics",
    "2. Strength of Materials",
    "3. Thermodynamics",
    "4. Fluid Mechanics",
    "5. Thermal Engineering",
    "6. Machine Design"
]

selected_sidebar = st.sidebar.selectbox(
    "Navigation Menu",
    nav_options,
    index=nav_options.index(st.session_state.module)
)

if selected_sidebar != st.session_state.module:
    st.session_state.module = selected_sidebar
    st.rerun()

if st.session_state.module != "🏠 Home Menu":
    st.sidebar.divider()
    if st.sidebar.button("⬅️ Return to Main Menu", use_container_width=True, key="side_back"):
        go_home()
        st.rerun()

# Sidebar: Last 5 Calculations History
st.sidebar.divider()
st.sidebar.subheader("🕒 History (Last 5)")
if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.sidebar.markdown(f'<div class="history-card">{item}</div>', unsafe_allow_html=True)
    if st.sidebar.button("Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
else:
    st.sidebar.caption("No calculations recorded yet.")


# ----------------- TOP BAR ----------------- #
if st.session_state.module != "🏠 Home Menu":
    if st.button("⬅️ Back to Main Menu", key="top_back"):
        go_home()
        st.rerun()
    st.divider()

# ----------------- HOME DASHBOARD ----------------- #
if st.session_state.module == "🏠 Home Menu":
    st.markdown('<p class="main-title">⚙️ Mechanical Engineering Hub</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="badge-card">
        <b>Designed & Developed by:</b> Vignesh | <b>Roll No:</b> 2505A31052
    </div>
    """, unsafe_allow_html=True)

    st.write("Select any tool or engineering module below:")

    col_a, col_b = st.columns(2)
    with col_a:
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

    with col_b:
        if st.button("🔧 Engineering Tools & Tables", use_container_width=True):
            set_module("🔧 Engineering Tools & Tables")
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

# ----------------- GENERAL CALCULATOR ----------------- #
elif st.session_state.module == "🧮 General Calculator":
    st.header("🧮 General Arithmetic Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter First Number (A)", value=0.0, step=1.0)
    with col2:
        num2 = st.number_input("Enter Second Number (B)", value=0.0, step=1.0)

    operation = st.selectbox(
        "Operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Modulus (%)", "Power (A^B)"]
    )

    if st.button("Compute Result", use_container_width=True):
        res = 0
        symbol = "+"
        valid = True

        if operation == "Addition (+)":
            res = num1 + num2
            symbol = "+"
        elif operation == "Subtraction (-)":
            res = num1 - num2
            symbol = "-"
        elif operation == "Multiplication (×)":
            res = num1 * num2
            symbol = "×"
        elif operation == "Division (÷)":
            if num2 != 0:
                res = num1 / num2
                symbol = "÷"
            else:
                st.error("Cannot divide by zero.")
                valid = False
        elif operation == "Modulus (%)":
            if num2 != 0:
                res = num1 % num2
                symbol = "%"
            else:
                st.error("Cannot perform modulus by zero.")
                valid = False
        elif operation == "Power (A^B)":
            res = num1 ** num2
            symbol = "^"

        if valid:
            st.success(f"**Result:** {num1} {symbol} {num2} = **{res}**")
            add_history(f"{num1} {symbol} {num2} = {res:.2f}")

# ----------------- MECHANICAL TOOLS & CONVERTER ----------------- #
elif st.session_state.module == "🔧 Engineering Tools & Tables":
    st.header("🔧 Mechanical Tools & Reference")

    tab1, tab2 = st.tabs(["Unit Converter", "Standard Engineering Constants"])
    
    with tab1:
        tool = st.selectbox("Select Conversion Type", ["Pressure", "Power", "Length", "Energy"])

        if tool == "Pressure":
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["bar", "Pascal (Pa)", "psi", "atm"])
            u_to = st.selectbox("To", ["Pascal (Pa)", "bar", "psi", "atm"])
            
            # Base unit: Pascal
            to_pa = {"bar": 1e5, "Pascal (Pa)": 1.0, "psi": 6894.76, "atm": 101325.0}
            res_val = (val * to_pa[u_from]) / to_pa[u_to]
            st.info(f"**{val} {u_from} = {res_val:.4e} {u_to}**")
            add_history(f"{val} {u_from} -> {res_val:.2f} {u_to}")

        elif tool == "Power":
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["Kilowatt (kW)", "Horsepower (HP)", "Watt (W)"])
            u_to = st.selectbox("To", ["Watt (W)", "Kilowatt (kW)", "Horsepower (HP)"])
            
            to_w = {"Kilowatt (kW)": 1000.0, "Horsepower (HP)": 745.7, "Watt (W)": 1.0}
            res_val = (val * to_w[u_from]) / to_w[u_to]
            st.info(f"**{val} {u_from} = {res_val:.4f} {u_to}**")
            add_history(f"{val} {u_from} -> {res_val:.2f} {u_to}")

        elif tool == "Length":
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["Meter (m)", "Millimeter (mm)", "Inch (in)", "Foot (ft)"])
            u_to = st.selectbox("To", ["Millimeter (mm)", "Meter (m)", "Inch (in)", "Foot (ft)"])

            to_m = {"Meter (m)": 1.0, "Millimeter (mm)": 0.001, "Inch (in)": 0.0254, "Foot (ft)": 0.3048}
            res_val = (val * to_m[u_from]) / to_m[u_to]
            st.info(f"**{val} {u_from} = {res_val:.4f} {u_to}**")
            add_history(f"{val} {u_from} -> {res_val:.2f} {u_to}")

        elif tool == "Energy":
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["Joule (J)", "Kilojoule (kJ)", "Calorie (cal)", "Kilowatt-hour (kWh)"])
            u_to = st.selectbox("To", ["Kilojoule (kJ)", "Joule (J)", "Calorie (cal)", "Kilowatt-hour (kWh)"])

            to_j = {"Joule (J)": 1.0, "Kilojoule (kJ)": 1000.0, "Calorie (cal)": 4.184, "Kilowatt-hour (kWh)": 3.6e6}
            res_val = (val * to_j[u_from]) / to_j[u_to]
            st.info(f"**{val} {u_from} = {res_val:.4f} {u_to}**")
            add_history(f"{val} {u_from} -> {res_val:.2f} {u_to}")

    with tab2:
        st.markdown("""
        | Constant Name | Symbol | Standard Value | Unit |
        | :--- | :--- | :--- | :--- |
        | Acceleration due to Gravity | $g$ | 9.80665 | $\\text{m/s}^2$ |
        | Standard Atmospheric Pressure | $P_{\\text{atm}}$ | 101,325 | $\\text{Pa}$ |
        | Universal Gas Constant | $R_u$ | 8.314 | $\\text{J/(mol}\\cdot\\text{K)}$ |
        | Characteristic Gas Constant (Air) | $R_{\\text{air}}$ | 287 | $\\text{J/(kg}\\cdot\\text{K)}$ |
        | Density of Pure Water ($4^\\circ\\text{C}$) | $\\rho_w$ | 1000 | $\\text{kg/m}^3$ |
        | Specific Heat of Water | $c_p$ | 4.184 | $\\text{kJ/(kg}\\cdot\\text{K)}$ |
        """)

# --- MODULE 1: MECHANICS ---
elif st.session_state.module == "1. Mechanics":
    st.header("1. Mechanics")
    sub = st.selectbox("Select Calculation", ["Force", "Work", "Power", "Kinetic Energy"])

    if sub == "Force":
        st.latex(r"F = m \times a")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=10.0, step=0.1)
        a = st.number_input("Acceleration (a) [m/s²]", value=9.81, step=0.1)
        if st.button("Calculate"):
            res = calc_force(m, a)
            st.success(f"**Force (F) = {res:.4f} N**")
            add_history(f"Force: {res:.2f} N")

    elif sub == "Work":
        st.latex(r"W = F \times d")
        f = st.number_input("Force (F) [N]", value=50.0, step=1.0)
        d = st.number_input("Displacement (d) [m]", value=5.0, step=0.5)
        if st.button("Calculate"):
            res = calc_work(f, d)
            st.success(f"**Work Done (W) = {res:.4f} J**")
            add_history(f"Work: {res:.2f} J")

    elif sub == "Power":
        st.latex(r"P = \frac{W}{t}")
        w = st.number_input("Work (W) [J]", value=500.0, step=10.0)
        t = st.number_input("Time (t) [s]", min_value=0.0001, value=10.0, step=0.5)
        if st.button("Calculate"):
            res = calc_power(w, t)
            st.success(f"**Power (P) = {res:.4f} W**")
            add_history(f"Power: {res:.2f} W")

    elif sub == "Kinetic Energy":
        st.latex(r"KE = \frac{1}{2} m v^2")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=2.0, step=0.1)
        v = st.number_input("Velocity (v) [m/s]", value=10.0, step=0.5)
        if st.button("Calculate"):
            res = calc_kinetic_energy(m, v)
            st.success(f"**Kinetic Energy (KE) = {res:.4f} J**")
            add_history(f"KE: {res:.2f} J")

# --- MODULE 2: STRENGTH OF MATERIALS ---
elif st.session_state.module == "2. Strength of Materials":
    st.header("2. Strength of Materials")
    sub = st.selectbox("Select Calculation", ["Stress", "Strain", "Young's Modulus"])

    if sub == "Stress":
        st.latex(r"\sigma = \frac{F}{A}")
        f = st.number_input("Applied Load / Force (F) [N]", value=1000.0, step=50.0)
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.000001, value=0.002, format="%.6f")
        if st.button("Calculate"):
            res = calc_stress(f, a)
            st.success(f"**Stress (σ) = {res:.2f} Pa ({res / 1e6:.4f} MPa)**")
            add_history(f"Stress: {res/1e6:.2f} MPa")

    elif sub == "Strain":
        st.latex(r"\varepsilon = \frac{\Delta L}{L_0}")
        dl = st.number_input("Change in Length (ΔL) [mm]", value=0.5, step=0.05)
        l0 = st.number_input("Original Length (L₀) [mm]", min_value=0.001, value=100.0, step=1.0)
        if st.button("Calculate"):
            res = calc_strain(dl, l0)
            st.success(f"**Strain (ε) = {res:.6f} (dimensionless)**")
            add_history(f"Strain: {res:.5f}")

    elif sub == "Young's Modulus":
        st.latex(r"E = \frac{\sigma}{\varepsilon}")
        stress = st.number_input("Stress (σ) [Pa]", value=200000000.0, step=1000000.0)
        strain = st.number_input("Strain (ε)", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate"):
            res = calc_youngs_modulus(stress, strain)
            st.success(f"**Young's Modulus (E) = {res / 1e9:.3f} GPa ({res:.2f} Pa)**")
            add_history(f"Young's Mod: {res/1e9:.2f} GPa")

# --- MODULE 3: THERMODYNAMICS ---
elif st.session_state.module == "3. Thermodynamics":
    st.header("3. Thermodynamics")
    sub = st.selectbox("Select Calculation", ["Heat Transfer", "Work Done (Constant P)", "Thermal Efficiency"])

    if sub == "Heat Transfer":
        st.latex(r"Q = m \times c \times \Delta T")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=1.0)
        cp = st.number_input("Specific Heat Capacity (c) [J/(kg·K)]", min_value=0.0, value=4184.0)
        dt = st.number_input("Temperature Difference (ΔT) [K or °C]", value=20.0)
        if st.button("Calculate"):
            res = calc_heat_transfer(m, cp, dt)
            st.success(f"**Heat Transfer (Q) = {res:.2f} J ({res / 1000:.3f} kJ)**")
            add_history(f"Heat: {res/1000:.2f} kJ")

    elif sub == "Work Done (Constant P)":
        st.latex(r"W = P \times \Delta V")
        p = st.number_input("Pressure (P) [Pa]", min_value=0.0, value=101325.0)
        dv = st.number_input("Change in Volume (ΔV) [m³]", value=0.05, format="%.4f")
        if st.button("Calculate"):
            res = calc_work_done_isobaric(p, dv)
            st.success(f"**Work Done (W) = {res:.2f} J**")
            add_history(f"Isobaric W: {res:.2f} J")

    elif sub == "Thermal Efficiency":
        st.latex(r"\eta = \left(\frac{W_{\text{net}}}{Q_{\text{in}}}\right) \times 100\%")
        wnet = st.number_input("Net Work Output (W_net) [J or kJ]", min_value=0.0, value=400.0)
        qin = st.number_input("Heat Input (Q_in) [J or kJ]", min_value=0.001, value=1000.0)
        if st.button("Calculate"):
            res = calc_thermal_efficiency(wnet, qin)
            st.success(f"**Thermal Efficiency (η) = {res:.2f} %**")
            add_history(f"Thermal Eff: {res:.2f}%")

# --- MODULE 4: FLUID MECHANICS ---
elif st.session_state.module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics")
    sub = st.selectbox("Select Calculation", ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"])

    if sub == "Pressure":
        st.latex(r"P = \frac{F}{A}")
        f = st.number_input("Normal Force (F) [N]", value=500.0)
        a = st.number_input("Area (A) [m²]", min_value=0.0001, value=0.05)
        if st.button("Calculate"):
            res = calc_pressure(f, a)
            st.success(f"**Pressure (P) = {res:.2f} Pa ({res / 1000:.3f} kPa)**")
            add_history(f"Pressure: {res:.2f} Pa")

    elif sub == "Reynolds Number":
        st.latex(r"Re = \frac{\rho \times v \times D}{\mu}")
        rho = st.number_input("Fluid Density (ρ) [kg/m³]", min_value=0.0, value=1000.0)
        v = st.number_input("Flow Velocity (v) [m/s]", min_value=0.0, value=1.5)
        d = st.number_input("Pipe Diameter (D) [m]", min_value=0.0, value=0.05)
        mu = st.number_input("Dynamic Viscosity (μ) [Pa·s]", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate"):
            re = calc_reynolds(rho, v, d, mu)
            regime = "Laminar" if re < 2300 else ("Turbulent" if re > 4000 else "Transitional")
            st.success(f"**Reynolds Number (Re) = {re:.2f}**\n\n*Flow Regime:* {regime}")
            add_history(f"Re: {re:.1f} ({regime})")

    elif sub == "Flow Velocity":
        st.latex(r"v = \frac{Q}{A}")
        q = st.number_input("Discharge (Q) [m³/s]", min_value=0.0, value=0.05)
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.0001, value=0.02)
        if st.button("Calculate"):
            res = calc_flow_velocity(q, a)
            st.success(f"**Flow Velocity (v) = {res:.4f} m/s**")
            add_history(f"Flow Vel: {res:.3f} m/s")

    elif sub == "Discharge":
        st.latex(r"Q = A \times v")
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.0, value=0.02)
        v = st.number_input("Velocity (v) [m/s]", min_value=0.0, value=2.5)
        if st.button("Calculate"):
            res = calc_discharge(a, v)
            st.success(f"**Discharge (Q) = {res:.4f} m³/s**")
            add_history(f"Discharge: {res:.3f} m³/s")

# --- MODULE 5: THERMAL ENGINEERING ---
elif st.session_state.module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering")
    sub = st.selectbox("Select Calculation", ["Heat Conduction (Fourier's Law)", "COP (Refrigeration / Heat Pump)", "Heat Engine Efficiency (Carnot)"])

    if sub == "Heat Conduction (Fourier's Law)":
        st.latex(r"Q = \frac{k \times A \times \Delta T}{x}")
        k = st.number_input("Thermal Conductivity (k) [W/(m·K)]", min_value=0.0, value=45.0)
        a = st.number_input("Surface Area (A) [m²]", min_value=0.0, value=2.0)
        dt = st.number_input("Temperature Difference (ΔT) [K or °C]", value=50.0)
        dx = st.number_input("Wall Thickness (x) [m]", min_value=0.0001, value=0.1)
        if st.button("Calculate"):
            res = calc_conduction(k, a, dt, dx)
            st.success(f"**Rate of Heat Conduction (Q_cond) = {res:.2f} W**")
            add_history(f"Conduction: {res:.2f} W")

    elif sub == "COP (Refrigeration / Heat Pump)":
        st.latex(r"COP = \frac{\text{Desired Effect}}{\text{Work Input}}")
        effect = st.number_input("Desired Effect (Cooling or Heating Q) [kW]", min_value=0.0, value=7.5)
        work = st.number_input("Work Input (W) [kW]", min_value=0.001, value=2.5)
        if st.button("Calculate"):
            res = calc_cop(effect, work)
            st.success(f"**Coefficient of Performance (COP) = {res:.2f}**")
            add_history(f"COP: {res:.2f}")

    elif sub == "Heat Engine Efficiency (Carnot)":
        st.latex(r"\eta_{\text{Carnot}} = \left(1 - \frac{T_{\text{low}}}{T_{\text{high}}}\right) \times 100\%")
        th = st.number_input("Source Temperature (T_high) [Kelvin]", min_value=0.1, value=600.0)
        tl = st.number_input("Sink Temperature (T_low) [Kelvin]", min_value=0.0, value=300.0)
        if tl >= th:
            st.error("Sink Temperature (T_low) must be lower than Source Temperature (T_high).")
        else:
            if st.button("Calculate"):
                res = calc_heat_engine_eff(th, tl)
                st.success(f"**Carnot Efficiency (η_max) = {res:.2f} %**")
                add_history(f"Carnot Eff: {res:.2f}%")

# --- MODULE 6: MACHINE DESIGN ---
elif st.session_state.module == "6. Machine Design":
    st.header("6. Machine Design")
    sub = st.selectbox("Select Calculation", ["Torque from Power & RPM", "Shaft Power", "Shaft Diameter (Torsion)"])

    if sub == "Torque from Power & RPM":
        st.latex(r"T = \frac{P}{\omega} = \frac{60 \times P}{2 \pi N}")
        p = st.number_input("Power (P) [Watts]", min_value=0.0, value=15000.0, step=100.0)
        n = st.number_input("Rotational Speed (N) [RPM]", min_value=0.1, value=1440.0, step=10.0)
        if st.button("Calculate"):
            res = calc_torque(p, n)
            st.success(f"**Torque (T) = {res:.2f} N·m**")
            add_history(f"Torque: {res:.2f} N·m")

    elif sub == "Shaft Power":
        st.latex(r"P = T \times \omega = \frac{2 \pi N T}{60}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=99.5)
        n = st.number_input("Rotational Speed (N) [RPM]", min_value=0.0, value=1440.0)
        if st.button("Calculate"):
            res = calc_shaft_power(t, n)
            st.success(f"**Shaft Power (P) = {res:.2f} W ({res / 1000:.3f} kW)**")
            add_history(f"Shaft Power: {res/1000:.2f} kW")

    elif sub == "Shaft Diameter (Torsion)":
        st.latex(r"d = \left(\frac{16 T}{\pi \tau}\right)^{\frac{1}{3}}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=250.0)
        tau = st.number_input("Allowable Shear Stress (τ) [MPa]", min_value=0.01, value=45.0)
        if st.button("Calculate"):
            tau_pa = tau * 1e6
            d = calc_shaft_diameter(t, tau_pa)
            d_mm = d * 1000
            st.success(f"**Required Shaft Diameter (d) = {d_mm:.2f} mm ({d:.4f} m)**")
            add_history(f"Shaft Dia: {d_mm:.2f} mm")
