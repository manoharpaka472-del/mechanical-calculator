import streamlit as st
import streamlit.components.v1 as components
import math

# Page configuration
st.set_page_config(
    page_title="MechCalc 3D | P. MANOHAR",
    page_icon="⚙️",
    layout="centered"
)

# ----------------- 3D INTERACTIVE CANVAS BACKGROUND ----------------- #
# Injects a lightweight Three.js 3D geometric grid network that moves with the mouse/touch
threejs_canvas = """
<div id="threejs-canvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; pointer-events: none;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    const container = document.getElementById('threejs-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    // Create 3D Geometric Wireframe Torus
    const geometry = new THREE.TorusKnotGeometry(10, 3, 100, 16);
    const material = new THREE.MeshBasicMaterial({ 
        color: 0x00f2fe, 
        wireframe: true, 
        transparent: true, 
        opacity: 0.18 
    });
    const torusKnot = new THREE.Mesh(geometry, material);
    scene.add(torusKnot);

    // Create 3D Floating Particle Sphere
    const particlesGeo = new THREE.BufferGeometry();
    const count = 400;
    const posArray = new Float32Array(count * 3);
    for(let i = 0; i < count * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 50;
    }
    particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const particlesMat = new THREE.PointsMaterial({
        size: 0.25,
        color: 0x38bdf8,
        transparent: true,
        opacity: 0.6
    });
    const particlesMesh = new THREE.Points(particlesGeo, particlesMat);
    scene.add(particlesMesh);

    camera.position.z = 24;

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);
        torusKnot.rotation.x += 0.003;
        torusKnot.rotation.y += 0.005;
        particlesMesh.rotation.y -= 0.001;
        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
</script>
"""
components.html(threejs_canvas, height=0, width=0)

# ----------------- 3D GLASSMORPHISM & NEON CSS ----------------- #
st.markdown("""
    <style>
    /* Dark Deep-Space Background with 3D Depth */
    .stApp {
        background: radial-gradient(ellipse at 50% 0%, #0d1b2a 0%, #050811 100%) !important;
        color: #f1f5f9;
    }
    
    /* 3D Floating Glass Badge for Student Details */
    .student-badge-3d {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.25), rgba(99, 102, 241, 0.25));
        border: 1px solid rgba(56, 189, 248, 0.4);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 24px;
        transform: perspective(600px) translateZ(10px);
        transition: transform 0.3s ease;
    }
    .student-badge-3d:hover {
        transform: perspective(600px) translateZ(20px);
    }

    /* 3D Interactive Buttons */
    div.stButton > button {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        border-color: #38bdf8 !important;
        box-shadow: 0 10px 25px rgba(14, 165, 233, 0.35), 0 0 10px rgba(56, 189, 248, 0.5) !important;
        color: #ffffff !important;
    }
    div.stButton > button:active {
        transform: translateY(1px) scale(0.98);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
    }

    /* 3D Input & Select Boxes */
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: rgba(15, 23, 42, 0.75) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    /* 3D Sidebar Panel */
    section[data-testid="stSidebar"] {
        background: rgba(10, 15, 26, 0.85) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(56, 189, 248, 0.15);
    }
    
    /* Sleek Calculation Log */
    .history-card-3d {
        background: rgba(15, 23, 42, 0.65);
        border-left: 3px solid #00f2fe;
        border-radius: 8px;
        padding: 10px 14px;
        margin-bottom: 8px;
        font-family: monospace;
        font-size: 0.88rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE SETUP ----------------- #
if "module" not in st.session_state:
    st.session_state.module = "🏠 Home Menu"

if "history" not in st.session_state:
    st.session_state.history = []

def add_history(calc_name, formula_val):
    st.session_state.history.insert(0, f"[{calc_name}] {formula_val}")
    if len(st.session_state.history) > 5:
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


# ----------------- SIDEBAR HEADER & NAVIGATION ----------------- #
st.sidebar.markdown("""
<div style="background: rgba(14, 165, 233, 0.12); padding: 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.35); box-shadow: 0 4px 15px rgba(0,0,0,0.4);">
    <h4 style="margin:0; color:#38bdf8; letter-spacing:1px;">⚙️ MECH PROJECT</h4>
    <p style="margin:4px 0 0 0; font-size: 0.95rem;"><b>Developer:</b> P . MANOHAR</p>
    <p style="margin:2px 0 0 0; font-size: 0.95rem;"><b>Roll No:</b> 2505A31016</p>
</div>
""", unsafe_allow_html=True)

nav_options = [
    "🏠 Home Menu",
    "🧮 General Calculator",
    "1. Mechanics",
    "2. Strength of Materials",
    "3. Thermodynamics",
    "4. Fluid Mechanics",
    "5. Thermal Engineering",
    "6. Machine Design",
    "🛠️ Student Toolset & Units"
]

selected_sidebar = st.sidebar.selectbox(
    "Select Module",
    nav_options,
    index=nav_options.index(st.session_state.module)
)

if selected_sidebar != st.session_state.module:
    st.session_state.module = selected_sidebar
    st.rerun()

# Last 5 Calculations History
st.sidebar.divider()
st.sidebar.markdown("### 🕒 Recent History (Last 5)")
if st.session_state.history:
    for item in st.session_state.history:
        st.sidebar.markdown(f"<div class='history-card-3d'>{item}</div>", unsafe_allow_html=True)
    if st.sidebar.button("Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
else:
    st.sidebar.caption("No calculations saved yet.")

if st.session_state.module != "🏠 Home Menu":
    st.sidebar.divider()
    if st.sidebar.button("⬅️ Return to Main Menu", use_container_width=True, key="side_back"):
        go_home()
        st.rerun()


# ----------------- TOP STUDENT 3D BADGE ----------------- #
st.markdown("""
<div class="student-badge-3d">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-size: 1.2rem; font-weight: 800; color: #ffffff; letter-spacing: 0.5px;">P . MANOHAR</div>
            <div style="font-size: 0.88rem; color: #38bdf8; font-weight: 600;">ROLL NO: 2505A31016</div>
        </div>
        <div style="text-align: right; font-size: 0.8rem; color: #94a3b8;">
            Mechanical Engineering<br><span style="color:#00f2fe;">3D Interactive Edition</span>
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
    st.title("⚙️ Engineering Calculator")
    st.write("Select a module below to begin calculations:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧮 General Calculator", use_container_width=True):
            set_module("🧮 General Calculator"); st.rerun()
        if st.button("1. Mechanics", use_container_width=True):
            set_module("1. Mechanics"); st.rerun()
        if st.button("2. Strength of Materials", use_container_width=True):
            set_module("2. Strength of Materials"); st.rerun()
        if st.button("3. Thermodynamics", use_container_width=True):
            set_module("3. Thermodynamics"); st.rerun()

    with col2:
        if st.button("4. Fluid Mechanics", use_container_width=True):
            set_module("4. Fluid Mechanics"); st.rerun()
        if st.button("5. Thermal Engineering", use_container_width=True):
            set_module("5. Thermal Engineering"); st.rerun()
        if st.button("6. Machine Design", use_container_width=True):
            set_module("6. Machine Design"); st.rerun()
        if st.button("🛠️ Student Toolset & Units", use_container_width=True):
            set_module("🛠️ Student Toolset & Units"); st.rerun()

# 1. GENERAL CALCULATOR
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

# 2. MECHANICS
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

# 3. STRENGTH OF MATERIALS
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

# 4. THERMODYNAMICS
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

# 5. FLUID MECHANICS
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
            regime = "Laminar" if re < 2300 else ("Turbulent" if re > 4000 else "Transitional")
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

# 6. THERMAL ENGINEERING
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

# 7. MACHINE DESIGN
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

# 8. STUDENT TOOLSET & UNITS
elif st.session_state.module == "🛠️ Student Toolset & Units":
    st.header("🛠️ Mechanical Student Utilities")

    tab1, tab2 = st.tabs(["🔄 Unit Converter", "📖 Material Properties Sheet"])

    with tab1:
        st.subheader("Fast Unit Converter")
        tool = st.selectbox("Convert Type", ["Pressure (bar ↔ kPa ↔ psi)", "Power (kW ↔ HP)", "Length (inch ↔ mm)"])

        if tool == "Pressure (bar ↔ kPa ↔ psi)":
            val = st.number_input("Pressure value in Bar", value=1.0)
            st.info(f"**{val} Bar** = **{val * 100:.2f} kPa** = **{val * 14.5038:.2f} psi**")

        elif tool == "Power (kW ↔ HP)":
            val = st.number_input("Power in Kilowatts (kW)", value=1.0)
            st.info(f"**{val} kW** = **{val * 1.34102:.3f} Metric HP (Horsepower)**")

        elif tool == "Length (inch ↔ mm)":
            val = st.number_input("Length in Inches", value=1.0)
            st.info(f"**{val} in** = **{val * 25.4:.2f} mm**")

    with tab2:
        st.subheader("Common Engineering Materials")
        st.markdown("""
        | Material | Density (kg/m³) | Young's Modulus (E) | Yield Strength (MPa) |
        | :--- | :--- | :--- | :--- |
        | **Structural Steel** | 7850 | 200 GPa | 250 |
        | **Aluminum (6061-T6)**| 2700 | 69 GPa | 276 |
        | **Cast Iron** | 7200 | 110 GPa | 130 |
        | **Titanium Alloy** | 4430 | 114 GPa | 830 |
        | **Copper** | 8960 | 117 GPa | 70 |
        """)
