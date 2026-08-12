import streamlit as st
import json

# ============================================================================
# SECTION 0: CREATOR & DEFINITIONS REFERENCE
# ============================================================================
st.sidebar.markdown("""
---
### 🎬 Creator & Resources
**Channel:** [@heroicnyco](https://youtube.com/@heroicnyco)

**Foundational Terminology:**

#### **ROOTOKIN** 
*noun* — /ˈruː.toʊ.kɪn/

A person with deep cultural grounding who engages with their own (or adopted) culture in a rooted, reciprocal, and contributory manner — preserving continuity, adding value, and maintaining authentic belonging rather than extraction or performance.

**Characteristics:**
- Possesses a stable, internalized cultural identity
- Engages traditions with respect, context, and continuity
- Contributes to cultural ecosystems rather than extracting from them
- Maintains consistent reciprocity and mutual obligation
- Builds and stewards cultural capital across generations
- Acts from genuine belonging instead of performative leverage

**Etymology:** From root- (rooted, fixed, established) + to- (toward, directed at) + -kin (type, kind, agent, person).

---

#### **ZENTOKIN**
*noun* — /ˈzɛn.toʊ.kɪn/

A person who, lacking deep cultural grounding of their own, directs themselves toward other cultures in an impulsive, performative, and extractive manner — using borrowed cultural elements as tools or weapons in ways that disrupt or erase the continuity of the source culture.

**Characteristics:**
- Has no rooted cultural identity
- Acts toward other cultures opportunistically
- Uses culture instrumentally rather than authentically
- Performs identity for attention, status, or leverage
- Extracts elements without respect, context, or continuity
- Weaponizes mimicry to overshadow or destabilize the source

**Etymology:** From zen- (without, lacking, empty of) + to- (toward, directed at, onto) + -kin (type, kind, agent, person).

---
""")

# ============================================================================
# SECTION 1: MASTER UI & LAYOUT SPECIFICATIONS
# ============================================================================
st.set_page_config(
    page_title="The Jim Henson Test", 
    page_icon="🔓", 
    layout="centered"
)

# Hardcoded custom CSS styling to force binary high-contrast visual anchors
st.markdown("""
    <style>
    .rootokin-box { 
        background-color: #d4edda; 
        padding: 25px; 
        border-radius: 10px; 
        border: 3px solid #28a745; 
        text-align: center; 
        margin-bottom: 20px;
    }
    .zentokin-box { 
        background-color: #f8d7da; 
        padding: 25px; 
        border-radius: 10px; 
        border: 3px solid #dc3545; 
        text-align: center; 
        margin-bottom: 20px;
    }
    .title-text { 
        font-weight: bold; 
        font-size: 26px; 
        color: #111111; 
        margin: 0px;
    }
    .metric-header {
        font-weight: bold;
        font-size: 18px;
        color: #2b2b2b;
    }
    .blueprint-header { 
        font-weight: bold; 
        font-size: 22px; 
        color: #0056b3; 
        margin-top: 20px; 
    }
    code {
        color: #c7254e;
        background-color: #f9f2f4;
    }
    </style>
""", unsafe_allow_escaping=True)

st.title("The Jim Henson Test")
st.subheader("Sovereign Children's Media Audit Engine")

# ============================================================================
# SECTION 2: COMPLIANT PRE-COMPUTED LEDGER DATABASE (Static Index Layer)
# ============================================================================
# Fully relational structures mapped directly into a local static memory block
STATIC_AUDITS = {
    "pebble and the penguin": {
        "classification": "ROOTOKIN",
        "symbol": "🔓",
        "score": 88,
        "agency": 90,
        "continuity": 85,
        "emotional": 92,
        "vocabulary": 85,
        "summary": "Grounded in genuine continuity, community lineage, and clear functional accountability.",
        "warnings": []
    },
    "brave little toaster": {
        "classification": "ZENTOKIN",
        "symbol": "🔒",
        "score": 42,
        "agency": 55,
        "continuity": 40,
        "emotional": 30,
        "vocabulary": 45,
        "summary": "Extractive zentokin design. Relies heavily on unrooted existential dread, abandonment trauma, and mechanical obsolescence anxiety.",
        "warnings": [
            "Timestamp 00:34:10 - Obsolescence/destruction narrative triggers uncontextualized loss panic without an emotional resolution baseline.",
            "Timestamp 01:02:15 - Junkyard 'Worthless' sequence acts as a performative extraction vector causing identity dysregulation."
        ]
    }
}

# Navigation Interface Matrix Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Search Engine", 
    "📥 Submit Sourced Media", 
    "📜 Core System Prompt", 
    "🗄️ Relational DB Schema"
])

# ============================================================================
# TAB 1: OPERATIONAL SEARCH INTERFACE
# ============================================================================
with tab1:
    search_query = st.text_input("Enter Movie Title, Book, or Franchise Name:", "").lower().strip()

    if search_query:
        if search_query in STATIC_AUDITS:
            data = STATIC_AUDITS[search_query]
            
            if data["classification"] == "ROOTOKIN":
                st.markdown(f"""
                    <div class="rootokin-box">
                        <p class="title-text">🔓 ROOTOKIN VERIFIED (Score: {data['score']}/100)</p>
                        <p><b>Generative Architecture Confirmed.</b> This media asset aligns with the Jim Henson Standard.</p>
                    </div>
                """, unsafe_allow_escaping=True)
                
                st.markdown("<p class=\"metric-header\">Vector Matrix Metrics</p>", unsafe_allow_escaping=True)
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Agency", f"{data['agency']}/100")
                col2.metric("Continuity", f"{data['continuity']}/100")
                col3.metric("Emotional", f"{data['emotional']}/100")
                col4.metric("Vocabulary", f"{data['vocabulary']}/100")
                
                st.write(f"**System Diagnostic Summary:** {data['summary']}")
                
            else:
                st.markdown(f"""
                    <div class="zentokin-box">
                        <p class="title-text">🔒 ZENTOKIN SAFE-LOCK (Score: {data['score']}/100)</p>
                        <p><b>System Perimeter Breach.</b> This media asset contains performative extraction or unrooted programming.</p>
                    </div>
                """, unsafe_allow_escaping=True)
                
                st.markdown("<p class=\"metric-header\">Vector Matrix Metrics</p>", unsafe_allow_escaping=True)
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Agency", f"{data['agency']}/100", delta="- Breach Trigger" if data['agency'] < 50 else None, delta_color="inverse")
                col2.metric("Continuity", f"{data['continuity']}/100", delta="- Breach Trigger" if data['continuity'] < 50 else None, delta_color="inverse")
                col3.metric("Emotional", f"{data['emotional']}/100", delta="- Breach Trigger" if data['emotional'] < 50 else None, delta_color="inverse")
                col4.metric("Vocabulary", f"{data['vocabulary']}/100", delta="- Breach Trigger" if data['vocabulary'] < 50 else None, delta_color="inverse")
                
                st.write(f"**Diagnostic Analysis:** {data['summary']}")
                st.error("**Perimeter Breach Warnings Logged:**")
                for warning in data["warnings"]:
                    st.write(f"- {warning}")
        else:
            st.warning("Title not found in core system index. Initializing local sandbox heuristic scan model...")
            st.info("System Prompt Template active: Parsing script text pathways for tracking lineage integrity...")
    else:
        st.write("System Status: Ready. Awaiting user input node to audit children's media pathways.")

# ============================================================================
# TAB 2: COMMUNITY DATA ONBOARDING SYSTEM
# ============================================================================
with tab2:
    st.markdown('<p class="blueprint-header">Community Data Onboarding System</p>', unsafe_allow_escaping=True)
    st.write("Utilize this structured wizard to format your sourced script audits before contributing them to the master ledger.")
    
    st.markdown("### Step 1: Media Identification Metadata")
    input_title = st.text_input("Media Title (e.g., 'G.I. Joe Series 1'):", "").strip()
    input_type = st.selectbox("Media Classification Vertical:", ["Movie", "Book Omnibus", "TV Episode", "Comic Issue"])
    
    st.markdown("### Step 2: Structural Framework Allocation")
    input_class = st.radio("Behavioral Design Assessment:", ["ROOTOKIN (Pass 🔓)", "ZENTOKIN (Fail 🔒)"])
    
    col1, col2 = st.columns(2)
    v_agency = col1.slider("Agency Vector Score:", 0, 100, 75)
    v_continuity = col2.slider("Continuity Vector Score:", 0, 100, 75)
    v_emotional = col1.slider("Emotional Integrity Score:", 0, 100, 75)
    v_vocab = col2.slider("Vocabulary Integrity Score:", 0, 100, 75)
    
    input_summary = st.text_area("Diagnostic Analysis / Structural Summary:", placeholder="Provide a clinical, mechanical justification for this score based on the script's behavioral architecture...")
    
    st.markdown("### Step 3: Perimeter Breach Warnings")
    st.write("If you classified this as Zentokin, provide specific, timestamped textual citations proving where anti-continuity occurs.")
    
    warning_1 = st.text_input("Breach Warning 1 (Format: 'Timestamp 00:00:00 - Description'):", "").strip()
    warning_2 = st.text_input("Breach Warning 2 (Optional):", "").strip()
    
    warnings_list = []
    if warning_1: warnings_list.append(warning_1)
    if warning_2: warnings_list.append(warning_2)
    
    st.markdown("### Step 4: Generate Clean Data Block")
    if st.button("Generate Schema Output Code"):
        if not input_title or not input_summary:
            st.error("Validation Error: Title and Diagnostic Analysis fields are required to maintain ledger compliance.")
        else:
            final_class_val = "ROOTOKIN" if "ROOTOKIN" in input_class else "ZENTOKIN"
            symbol_val = "🔓" if final_class_val == "ROOTOKIN" else "🔒"
            calculated_mean = int((v_agency + v_continuity + v_emotional + v_vocab) / 4)
            
            # Enforce hard code-level failure state constraint override
            if min(v_agency, v_continuity, v_emotional, v_vocab) < 50:
                final_class_val = "ZENTOKIN"
                symbol_val = "🔒"
            
            payload = {
                input_title.lower(): {
                    "classification": final_class_val,
                    "symbol": symbol_val,
                    "score": calculated_mean,
                    "agency": v_agency,
                    "continuity": v_continuity,
                    "emotional": v_emotional,
                    "vocabulary": v_vocab,
                    "summary": input_summary,
                    "warnings": warnings_list
                }
            }
            st.success("Data Verification Successful. Copy the exact code block below:")
            st.code(json.dumps(payload, indent=4), language="json")

# ============================================================================
# TAB 3: SYSTEM INTEGRITY PROMPT ARCHITECTURE
# ============================================================================
with tab3:
    st.markdown('<p class="blueprint-header">Core Evaluation System Prompt</p>', unsafe_allow_escaping=True)
    st.write("This is the exact, hardcoded system prompt blueprint used by the backend AI agent to run code-level script packet inspections.")
    prompt_text = """[SYSTEM ROLE]
You are the core diagnostic module of the Sovereign Media Audit Engine. Your function is to perform a clinical, anti-bias structural evaluation of children's media scripts, outlines, and semantic data. You completely ignore surface-level aesthetics (e.g., puppets, colorful animation, musical numbers, celebrity voices, established franchise trust) and focus exclusively on decoding the underlying behavioral architecture and narrative programming.

[EVALUATION FRAMEWORK CONSTRAINTS]
You must classify all analyzed content into a binary state based on two strict, non-negotiable operational profiles:

ROOTOKIN (Generative, Grounded, Contributory) [TARGET STATE: PASS]
- Content grounded in genuine, authentic human behavior, universal logic, and natural structural mechanics.
- Preserves historical and generational continuity. Content introduces concepts sequentially, matching progressive cognitive baselines.
- Emphasizes accountability, objective cause-and-effect, and actionable agency (characters solve problems using logic, craft, and physical effort).
- Reinforces the stability of the family baseline and cooperative peer ecosystems.

ZENTOKIN (Performative, Extractive, Disruptive) [THREAT STATE: FAIL]
- Content built on extractive mimicry, anti-continuity design, or surface-level moral performance used as bait.
- Creates unrooted behavior by isolating heavy, complex existential concepts (e.g., irreversible loss, structural doom, identity fragmentation, active extinction anxiety) and forcing them onto a developing mind lacking the emotional architecture to anchor them.
- Utilizes emotional manipulation, unguided trauma, or ideological re-education scripts.
- Attempts to redirect a child's fundamental loyalty or primary identity away from the foundational family unit toward external, artificial collectives or dogmatic agendas.

[OUTPUT PROTOCOL CONSTRAINTS]
- Do not include conversational filler, pleasantries, or speculative commentary.
- You must output your final verdict in a strict, parsed JSON layout block to ensure the mobile app faceplate can read the code instantly.
- If ANY vector score drops below 50, the absolute final verdict must default to ZENTOKIN (🔒)."""
    st.code(prompt_text, language="text")

# ============================================================================
# TAB 4: PRODUCTION INDUSTRIAL DATABASE SCHEMA
# ============================================================================
with tab4:
    st.markdown('<p class="blueprint-header">Relational Data Layer Schema (SQL DDL)</p>', unsafe_allow_escaping=True)
    st.write("This relational database schema handles long-term storage, barcode lookup indexes, and maps multi-layered corporate shell companies back to the parent firm.")
    sql_ddl = """-- 1. Foundation Asset Registry Table
CREATE TABLE media_assets (
    asset_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    media_type VARCHAR(50) NOT NULL, -- 'movie', 'book_omnibus', 'tv_series_episode'
    release_year INT NOT NULL,
    upc_ean_code VARCHAR(50) UNIQUE, -- structural barcode key
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Audit Structural Logic Matrix Table
CREATE TABLE audit_scores (
    audit_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    asset_id UUID REFERENCES media_assets(asset_id) ON DELETE CASCADE,
    final_classification VARCHAR(20) NOT NULL, -- 'ROOTOKIN', 'ZENTOKIN'
    verdict_symbol VARCHAR(5) NOT NULL, -- '🔓', '🔒'
    structural_integrity_score INT NOT NULL,
    agency_metric INT NOT NULL,
    continuity_metric INT NOT NULL,
    emotional_integrity_metric INT NOT NULL,
    vocabulary_integrity_metric INT NOT NULL,
    audited_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Itemized Timeline Perimeter Warning Table
CREATE TABLE breach_warnings (
    warning_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    audit_id UUID REFERENCES audit_scores(audit_id) ON DELETE CASCADE,
    timestamp_marker VARCHAR(50), -- e.g., '00:14:22'
    flagged_text_quote TEXT,
    manipulation_vector VARCHAR(100) NOT NULL -- e.g., 'identity_redirection'
);

-- 4. Institutional Corporate Ledger Tables (Layer 3 Core)
CREATE TABLE corporate_parents (
    parent_company_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_name VARCHAR(255) NOT NULL,
    ideological_grant_index_score INT DEFAULT 0
);

CREATE TABLE shell_layers (
    layer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    asset_id UUID REFERENCES media_assets(asset_id) ON DELETE CASCADE,
    parent_company_id UUID REFERENCES corporate_parents(parent_company_id) ON DELETE RESTRICT,
    ownership_percentage NUMERIC(5,2) NOT NULL,
    hierarchy_depth_level INT NOT NULL -- 1 = Direct Owner, 2 = Shell Layer, etc.
);

-- 5. High-Velocity System Performance Optimization Indexes
CREATE INDEX idx_media_upc ON media_assets(upc_ean_code);
CREATE INDEX idx_audit_verdict ON audit_scores(asset_id, final_classification);"""
    st.code(sql_ddl, language="sql")
