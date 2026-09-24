import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Mechanical Engineering Portal",
    page_icon="⚙️",
    layout="centered"
)

# ----------------- CUSTOM CSS & 3D BUTTON STYLING ----------------- #
st.markdown("""
<style>
    /* Dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Student Badge Card */
    .student-badge {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.95));
        border: 2px solid #38bdf8;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.25);
        text-align: center;
    }
    .student-badge h2 {
        color: #38bdf8;
        margin: 0;
        font-size: 1.5rem;
        letter-spacing: 1px;
    }
    .student-badge p {
        margin: 4px 0 0 0;
        color: #94a3b8;
        font-size: 0.95rem;
        font-weight: 500;
    }

    /* 3D Button Styling */
    div.stButton > button {
        background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
        color: #ffffff;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        border-bottom: 4px solid #1e40af;
        padding: 0.5rem 1rem;
        transition: all 0.1s ease-in-out;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
    }
    div.stButton > button:hover {
        background: linear-gradient(180deg, #3b82f6 0%, #2563eb 100%);
        color: #ffffff;
        border-bottom: 4px solid #1d4ed8;
    }
    div.stButton > button:active {
        transform: translateY(3px);
        border-bottom: 1px solid #1e40af;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.4);
    }

    /* Formula & Result card styling */
    div[data-testid="stMetricValue"] {
        color: #38bdf8;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE MANAGEMENT ----------------- #
if "module" not in st.session_state:
    st.session_state.module = "🏠 Home Menu"

if "history" not in st.session_state:
    st.session_state.history = []

def add_history(calc_name, result_str):
    st.session_state.history.append(f"{calc_name}: {result_str}")
    if len(st.session_state.history) > 5:
        st.session_state.history.pop(0)

def go_home():
    st.session_state.module = "🏠 Home Menu"

def set_module(name):
    st.session_state.module = name


# ----------------- STUDENT INFORMATION CARD ----------------- #
st.markdown("""
<div class="student-badge">
    <h2>⚙️ P . MANOHAR</h2>
    <p><b>Roll No:</b> 2505A31016 &nbsp;|&nbsp; <b>Branch:</b> Mechanical Engineering &nbsp;|&nbsp; <b>Year:</b> 1st Year</p>
</div>
""", unsafe_allow_html=True)


# ----------------- CALCULATION FUNCTIONS ----------------- #
def calc_force(mass, acceleration): return mass * acceleration
def calc_work(force, distance): return force * distance
def calc_power(work, time): return work / time if time > 0 else None
def calc_kinetic_energy(mass, velocity): return 0.5 * mass * (velocity ** 2)

def calc_stress(force, area): return force / area if area > 0 else None
def calc_strain(delta_l, original_l): return delta_l / original_l if original_l > 0 else None
def calc_youngs_modulus(stress, strain): return stress / strain if strain > 0 else None

def calc_heat_transfer(mass, specific_heat, delta_t): return mass * specific_heat * delta_t
def calc_work_done_isobaric(pressure, delta_v): return pressure * delta_v
def calc_thermal_efficiency(work_net, heat_in): return (work_net / heat_in) * 100 if heat_in > 0 else None

def calc_pressure(force, area): return force / area if area > 0 else None
def calc_reynolds(density, velocity, diameter, viscosity): return (density * velocity * diameter) / viscosity if viscosity > 0 else None
def calc_flow_velocity(discharge, area): return discharge / area if area > 0 else None
def calc_discharge(area, velocity): return area * velocity

def calc_conduction(k, area, delta_t, thickness): return (k * area * delta_t) / thickness if thickness > 0 else None
def calc_cop(desired_effect, work_input): return desired_effect / work_input if work_input > 0 else None
def calc_heat_engine_eff(t_high, t_low): return (1 - (t_low / t_high)) * 100 if t_high > 0 else None

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


# ----------------- SIDEBAR NAVIGATION & HISTORY ----------------- #
module_options = [
    "🏠 Home Menu",
    "🧮 General Calculator",
    "🛠️ Mechanical Student Tools",
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

st.sidebar.divider()
st.sidebar.subheader("🕒 Last 5 Calculations")
if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.sidebar.caption(f"• {item}")
else:
    st.sidebar.caption("No calculations recorded yet.")


# ----------------- MAIN PAGES ----------------- #
if st.session_state.module != "🏠 Home Menu":
    if st.button("⬅️ Back to Main Menu", key="top_back"):
        go_home()
        st.rerun()
    st.divider()

# --- HOME DASHBOARD ---
if st.session_state.module == "🏠 Home Menu":
    st.markdown("### 📌 Select a Module")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧮 General Calculator", use_container_width=True): set_module("🧮 General Calculator"); st.rerun()
        if st.button("1. Mechanics", use_container_width=True): set_module("1. Mechanics"); st.rerun()
        if st.button("2. Strength of Materials", use_container_width=True): set_module("2. Strength of Materials"); st.rerun()
        if st.button("3. Thermodynamics", use_container_width=True): set_module("3. Thermodynamics"); st.rerun()
    with col2:
        if st.button("🛠️ Mech Student Tools", use_container_width=True): set_module("🛠️ Mechanical Student Tools"); st.rerun()
        if st.button("4. Fluid Mechanics", use_container_width=True): set_module("4. Fluid Mechanics"); st.rerun()
        if st.button("5. Thermal Engineering", use_container_width=True): set_module("5. Thermal Engineering"); st.rerun()
        if st.button("6. Machine Design", use_container_width=True): set_module("6. Machine Design"); st.rerun()

# --- GENERAL CALCULATOR MODE ---
elif st.session_state.module == "🧮 General Calculator":
    st.header("🧮 General Arithmetic Calculator")
    op = st.selectbox("Operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (xʸ)", "Square Root (√x)"])
    
    if op in ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (xʸ)"]:
        num1 = st.number_input("Enter First Number (A)", value=0.0, step=1.0)
        num2 = st.number_input("Enter Second Number (B)", value=0.0, step=1.0)
        if st.button("Compute"):
            if op == "Addition (+)":
                res = num1 + num2
                st.latex(f"{num1} + {num2} = {res}")
            elif op == "Subtraction (-)":
                res = num1 - num2
                st.latex(f"{num1} - {num2} = {res}")
            elif op == "Multiplication (×)":
                res = num1 * num2
                st.latex(f"{num1} \\times {num2} = {res}")
            elif op == "Division (÷)":
                if num2 == 0:
                    st.error("Error: Division by zero is undefined.")
                    res = None
                else:
                    res = num1 / num2
                    st.latex(f"\\frac{{{num1}}}{{{num2}}} = {res}")
            elif op == "Power (xʸ)":
                res = num1 ** num2
                st.latex(f"{num1}^{{{num2}}} = {res}")
            if res is not None:
                st.success(f"**Result = {res}**")
                add_history("General Calc", f"{res}")
    else:
        num = st.number_input("Enter Value (x)", min_value=0.0, value=16.0, step=1.0)
        if st.button("Compute"):
            res = math.sqrt(num)
            st.latex(f"\\sqrt{{{num}}} = {res}")
            st.success(f"**Result = {res}**")
            add_history("Square Root", f"{res}")

# --- MECHANICAL STUDENT BASIC TOOLS ---
elif st.session_state.module == "🛠️ Mechanical Student Tools":
    st.header("🛠️ Basic Mechanical Tools")
    tool = st.selectbox("Select Tool", ["Pressure Unit Converter", "Standard Steel Bar Weight (IS)"])

    if tool == "Pressure Unit Converter":
        st.write("Convert between Bar, Pascal, and PSI:")
        p_val = st.number_input("Pressure Value", min_value=0.0, value=1.0)
        unit_from = st.selectbox("From", ["bar", "Pascal (Pa)", "psi"])
        if unit_from == "bar":
            pa, psi = p_val * 1e5, p_val * 14.5038
            st.info(f"**{p_val} bar** = {pa:.2f} Pa | {psi:.3f} psi")
        elif unit_from == "Pascal (Pa)":
            bar, psi = p_val / 1e5, p_val * 0.000145038
            st.info(f"**{p_val} Pa** = {bar:.6f} bar | {psi:.6f} psi")
        elif unit_from == "psi":
            bar, pa = p_val / 14.5038, p_val * 6894.76
            st.info(f"**{p_val} psi** = {bar:.4f} bar | {pa:.2f} Pa")

    elif tool == "Standard Steel Bar Weight (IS)":
        st.write("Calculate weight of circular steel bars ($W = \\frac{D^2}{162} \\text{ kg/m}$):")
        st.latex(r"W = \frac{D^2}{162} \times L")
        dia = st.number_input("Diameter of Bar (D) [mm]", min_value=1.0, value=12.0)
        length = st.number_input("Length of Bar (L) [m]", min_value=0.1, value=1.0)
        if st.button("Calculate Weight"):
            w_per_meter = (dia ** 2) / 162
            total_w = w_per_meter * length
            st.success(f"**Unit Weight:** {w_per_meter:.3f} kg/m\n\n**Total Weight:** {total_w:.3f} kg")
            add_history("Steel Bar Weight", f"{total_w:.2f} kg")

# --- 1. MECHANICS ---
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
            add_history("Force", f"{res:.2f} N")

    elif sub == "Work":
        st.latex(r"W = F \times d")
        f = st.number_input("Force (F) [N]", value=50.0, step=1.0)
        d = st.number_input("Displacement (d) [m]", value=5.0, step=0.5)
        if st.button("Calculate"):
            res = calc_work(f, d)
            st.success(f"**Work Done (W) = {res:.4f} J**")
            add_history("Work", f"{res:.2f} J")

    elif sub == "Power":
        st.latex(r"P = \frac{W}{t}")
        w = st.number_input("Work (W) [J]", value=500.0, step=10.0)
        t = st.number_input("Time (t) [s]", min_value=0.0001, value=10.0, step=0.5)
        if st.button("Calculate"):
            res = calc_power(w, t)
            st.success(f"**Power (P) = {res:.4f} W**")
            add_history("Power", f"{res:.2f} W")

    elif sub == "Kinetic Energy":
        st.latex(r"KE = \frac{1}{2} m v^2")
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=2.0, step=0.1)
        v = st.number_input("Velocity (v) [m/s]", value=10.0, step=0.5)
        if st.button("Calculate"):
            res = calc_kinetic_energy(m, v)
            st.success(f"**Kinetic Energy (KE) = {res:.4f} J**")
            add_history("Kinetic Energy", f"{res:.2f} J")

# --- 2. STRENGTH OF MATERIALS ---
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
            add_history("Stress", f"{res:.2f} Pa")

    elif sub == "Strain":
        st.latex(r"\varepsilon = \frac{\Delta L}{L_0}")
        dl = st.number_input("Change in Length (ΔL) [mm]", value=0.5, step=0.05)
        l0 = st.number_input("Original Length (L₀) [mm]", min_value=0.001, value=100.0, step=1.0)
        if st.button("Calculate"):
            res = calc_strain(dl, l0)
            st.success(f"**Strain (ε) = {res:.6f} (dimensionless)**")
            add_history("Strain", f"{res:.5f}")

    elif sub == "Young's Modulus":
        st.latex(r"E = \frac{\sigma}{\varepsilon}")
        stress = st.number_input("Stress (σ) [Pa]", value=200000000.0, step=1000000.0)
        strain = st.number_input("Strain (ε)", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate"):
            res = calc_youngs_modulus(stress, strain)
            st.success(f"**Young's Modulus (E) = {res / 1e9:.3f} GPa ({res:.2f} Pa)**")
            add_history("Young's Modulus", f"{res / 1e9:.2f} GPa")

# --- 3. THERMODYNAMICS ---
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
            add_history("Heat Transfer", f"{res:.2f} J")

    elif sub == "Work Done (Constant P)":
        st.latex(r"W = P \times \Delta V")
        p = st.number_input("Pressure (P) [Pa]", min_value=0.0, value=101325.0)
        dv = st.number_input("Change in Volume (ΔV) [m³]", value=0.05, format="%.4f")
        if st.button("Calculate"):
            res = calc_work_done_isobaric(p, dv)
            st.success(f"**Work Done (W) = {res:.2f} J**")
            add_history("Work Done", f"{res:.2f} J")

    elif sub == "Thermal Efficiency":
        st.latex(r"\eta = \left(\frac{W_{\text{net}}}{Q_{\text{in}}}\right) \times 100\%")
        wnet = st.number_input("Net Work Output (W_net) [J or kJ]", min_value=0.0, value=400.0)
        qin = st.number_input("Heat Input (Q_in) [J or kJ]", min_value=0.001, value=1000.0)
        if st.button("Calculate"):
            res = calc_thermal_efficiency(wnet, qin)
            st.success(f"**Thermal Efficiency (η) = {res:.2f} %**")
            add_history("Thermal Eff.", f"{res:.2f} %")

# --- 4. FLUID MECHANICS ---
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
            add_history("Pressure", f"{res:.2f} Pa")

    elif sub == "Reynolds Number":
        st.latex(r"Re = \frac{\rho \times v \times D}{\mu}")
        rho = st.number_input("Fluid Density (ρ) [kg/m³]", min_value=0.0, value=1000.0)
        v = st.number_input("Flow Velocity (v) [m/s]", min_value=0.0, value=1.5)
        d = st.number_input("Pipe Diameter (D) [m]", min_value=0.0, value=0.05)
        mu = st.number_input("Dynamic Viscosity (μ) [Pa·s]", min_value=0.000001, value=0.001, format="%.6f")
        if st.button("Calculate"):
            re = calc_reynolds(rho, v, d, mu)
            regime = "Laminar Flow (Re < 2300)" if re < 2300 else ("Turbulent Flow (Re > 4000)" if re > 4000 else "Transitional Flow")
            st.success(f"**Reynolds Number (Re) = {re:.2f}**\n\n*Flow Regime:* {regime}")
            add_history("Reynolds No", f"{re:.1f}")

    elif sub == "Flow Velocity":
        st.latex(r"v = \frac{Q}{A}")
        q = st.number_input("Discharge (Q) [m³/s]", min_value=0.0, value=0.05)
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.0001, value=0.02)
        if st.button("Calculate"):
            res = calc_flow_velocity(q, a)
            st.success(f"**Flow Velocity (v) = {res:.4f} m/s**")
            add_history("Flow Velocity", f"{res:.2f} m/s")

    elif sub == "Discharge":
        st.latex(r"Q = A \times v")
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.0, value=0.02)
        v = st.number_input("Velocity (v) [m/s]", min_value=0.0, value=2.5)
        if st.button("Calculate"):
            res = calc_discharge(a, v)
            st.success(f"**Discharge (Q) = {res:.4f} m³/s**")
            add_history("Discharge", f"{res:.2f} m3/s")

# --- 5. THERMAL ENGINEERING ---
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
            add_history("Conduction", f"{res:.2f} W")

    elif sub == "COP (Refrigeration / Heat Pump)":
        st.latex(r"COP = \frac{\text{Desired Effect}}{\text{Work Input}}")
        effect = st.number_input("Desired Effect (Cooling or Heating Q) [kW]", min_value=0.0, value=7.5)
        work = st.number_input("Work Input (W) [kW]", min_value=0.001, value=2.5)
        if st.button("Calculate"):
            res = calc_cop(effect, work)
            st.success(f"**Coefficient of Performance (COP) = {res:.2f}**")
            add_history("COP", f"{res:.2f}")

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
                add_history("Carnot Eff.", f"{res:.2f} %")

# --- 6. MACHINE DESIGN ---
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
            add_history("Torque", f"{res:.2f} N-m")

    elif sub == "Shaft Power":
        st.latex(r"P = T \times \omega = \frac{2 \pi N T}{60}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=99.5)
        n = st.number_input("Rotational Speed (N) [RPM]", min_value=0.0, value=1440.0)
        if st.button("Calculate"):
            res = calc_shaft_power(t, n)
            st.success(f"**Shaft Power (P) = {res:.2f} W ({res / 1000:.3f} kW)**")
            add_history("Shaft Power", f"{res:.2f} W")

    elif sub == "Shaft Diameter (Torsion)":
        st.latex(r"d = \left(\frac{16 T}{\pi \tau}\right)^{\frac{1}{3}}")
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=250.0)
        tau = st.number_input("Allowable Shear Stress (τ) [MPa]", min_value=0.01, value=45.0)
        if st.button("Calculate"):
            tau_pa = tau * 1e6
            d = calc_shaft_diameter(t, tau_pa)
            d_mm = d * 1000
            st.success(f"**Required Shaft Diameter (d) = {d_mm:.2f} mm ({d:.4f} m)**")
            add_history("Shaft Dia", f"{d_mm:.2f} mm")
