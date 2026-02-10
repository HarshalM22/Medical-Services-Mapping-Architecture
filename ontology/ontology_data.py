
# -----------------------------
# ABBREVIATIONS / SHORTHANDS
# -----------------------------
ABBREVIATIONS = {
    # procedure related
    "flx": "flexible",
    "rig": "rigid",
    "dx": "diagnostic",
    "tx": "therapeutic",
    "scr": "screening",

    # billing noise
    "hc": "",
    "lvl": "",
    "chg": "",
    "proc": "procedure",
    "svc": "service",
    "w/": "with",
    "w/o": "without",

    # technique
    "lap": "laparoscopic",
    "endo": "endoscopic",
    "op": "open",

    # anatomy shorthand
    "gi": "gastrointestinal",
    "abd": "abdominal",
    "lt": "left",
    "rt": "right",
    "bil": "bilateral",

    # misc
    "nos": "unspecified",
    "unspec": "unspecified"
}

# -----------------------------
# SYNONYMS / TERM NORMALIZATION
# -----------------------------
SYNONYMS = {
    # GI
    "large intestine": "colon",
    "bowel": "colon",
    "colonic": "colon",
    "sigmoid colon": "sigmoid",
    "rectum": "rectal",

    # upper GI
    "food pipe": "esophagus",
    "oesophagus": "esophagus",

    # procedures
    "scope": "endoscopy",
    "scopy": "endoscopy",
    "visual exam": "inspection",

    # pathology / lab
    "culture": "lab_culture",
    "specimen": "sample",
    "histology": "pathology",

    # imaging
    "ct scan": "ct",
    "cat scan": "ct",
    "mri scan": "mri",
    "x ray": "xray",

    # misc
    "removal": "excision",
    "cutting": "excision"
}

# -----------------------------
# BODY PARTS / ANATOMY
# -----------------------------
BODY_PARTS = {

    # =========================
    # GASTROINTESTINAL (GI)
    # =========================
    "esophagus": ["upper", "mid", "lower"],
    "stomach": ["fundus", "body", "antrum", "pylorus"],
    "duodenum": ["first portion", "second portion"],
    "jejunum": [],
    "ileum": [],
    "small_intestine": ["duodenum", "jejunum", "ileum"],
    "colon": ["cecum", "ascending", "transverse", "descending", "sigmoid"],
    "rectum": [],
    "anus": [],

    # =========================
    # HEPATOBILIARY / PANCREAS
    # =========================
    "liver": ["left lobe", "right lobe"],
    "gallbladder": [],
    "bile_duct": ["common bile duct", "intrahepatic"],
    "pancreas": ["head", "body", "tail"],
    "spleen": [],

    # =========================
    # RESPIRATORY
    # =========================
    "nose": [],
    "sinus": ["maxillary", "ethmoid", "frontal", "sphenoid"],
    "pharynx": [],
    "larynx": [],
    "trachea": [],
    "bronchus": ["left", "right"],
    "lung": ["left", "right", "upper lobe", "middle lobe", "lower lobe"],
    "pleura": [],

    # =========================
    # CARDIOVASCULAR
    # =========================
    "heart": ["atrium", "ventricle"],
    "coronary_artery": ["left", "right"],
    "aorta": ["thoracic", "abdominal"],
    "vein": ["central", "peripheral"],
    "artery": ["central", "peripheral"],

    # =========================
    # URINARY / RENAL
    # =========================
    "kidney": ["left", "right", "renal pelvis"],
    "ureter": ["left", "right"],
    "bladder": [],
    "urethra": [],

    # =========================
    # REPRODUCTIVE (FEMALE)
    # =========================
    "uterus": ["cervix", "endometrium"],
    "ovary": ["left", "right"],
    "fallopian_tube": ["left", "right"],
    "vagina": [],

    # =========================
    # REPRODUCTIVE (MALE)
    # =========================
    "prostate": [],
    "testis": ["left", "right"],
    "epididymis": [],
    "penis": [],

    # =========================
    # MUSCULOSKELETAL
    # =========================
    "bone": [
        "skull", "spine", "rib", "pelvis",
        "femur", "tibia", "fibula",
        "humerus", "radius", "ulna"
    ],
    "joint": [
        "shoulder", "elbow", "wrist",
        "hip", "knee", "ankle"
    ],
    "muscle": [],
    "tendon": [],
    "ligament": [],

    # =========================
    # NEUROLOGICAL
    # =========================
    "brain": ["cerebrum", "cerebellum", "brainstem"],
    "spinal_cord": ["cervical", "thoracic", "lumbar"],
    "nerve": ["peripheral", "cranial"],

    # =========================
    # ENDOCRINE
    # =========================
    "thyroid": [],
    "parathyroid": [],
    "adrenal_gland": ["left", "right"],
    "pituitary": [],

    # =========================
    # EYE / ENT
    # =========================
    "eye": ["retina", "cornea", "lens"],
    "ear": ["external", "middle", "inner"],

    # =========================
    # SKIN / SOFT TISSUE
    # =========================
    "skin": ["scalp", "face", "trunk", "extremity"],
    "subcutaneous_tissue": [],
    "soft_tissue": [],

    # =========================
    # BREAST
    # =========================
    "breast": ["left", "right"],

    # =========================
    # GENERAL / MULTI-SYSTEM
    # =========================
    "abdomen": [],
    "pelvis": [],
    "chest": [],
    "whole_body": []
}

# -----------------------------
# MODALITIES / TECHNIQUES
# -----------------------------
MODALITIES = {

    # =========================
    # ENDOSCOPIC / MINIMALLY INVASIVE
    # =========================
    "endoscopy": [
        "scope", "scopy", "endoscopic",
        "colonoscopy", "sigmoidoscopy",
        "egd", "ercp", "bronchoscopy",
        "cystoscopy", "arthroscopy",
        "hysteroscopy", "laparoscopy"
    ],

    # =========================
    # IMAGING / RADIOLOGY
    # =========================
    "imaging": [
        "ct", "computed tomography",
        "mri", "magnetic resonance",
        "xray", "radiograph",
        "fluoroscopy",
        "ultrasound", "usg", "sonography",
        "doppler",
        "mammography",
        "dexa", "bone density",
        "angiography"
    ],

    # =========================
    # NUCLEAR MEDICINE
    # =========================
    "nuclear_medicine": [
        "pet", "pet-ct",
        "spect",
        "nuclear scan",
        "radionuclide",
        "thyroid uptake"
    ],

    # =========================
    # SURGICAL (OPEN / MINIMALLY INVASIVE)
    # =========================
    "surgery": [
        "open", "surgical",
        "laparoscopic", "robotic",
        "excision", "resection",
        "amputation", "repair",
        "fusion", "implant"
    ],

    # =========================
    # INTERVENTIONAL RADIOLOGY / CARDIOLOGY
    # =========================
    "interventional": [
        "catheterization", "cath",
        "angioplasty", "stent",
        "embolization",
        "thrombectomy",
        "ablation",
        "biopsy needle"
    ],

    # =========================
    # CARDIAC DIAGNOSTIC
    # =========================
    "cardiac_diagnostics": [
        "ecg", "ekg",
        "echocardiogram", "echo",
        "stress test",
        "holter",
        "tilt table"
    ],

    # =========================
    # LABORATORY / PATHOLOGY
    # =========================
    "laboratory": [
        "lab", "laboratory",
        "blood test", "urine test",
        "culture", "sensitivity",
        "pathology", "histology",
        "cytology", "biopsy",
        "hematology",
        "chemistry",
        "immunology",
        "microbiology",
        "molecular"
    ],

    # =========================
    # ANESTHESIA / PAIN
    # =========================
    "anesthesia": [
        "anesthesia",
        "general anesthesia",
        "regional anesthesia",
        "local anesthesia",
        "sedation",
        "epidural",
        "spinal block"
    ],

    # =========================
    # RADIATION ONCOLOGY
    # =========================
    "radiation_therapy": [
        "radiation",
        "radiotherapy",
        "external beam",
        "brachytherapy",
        "imrt",
        "stereotactic",
        "radiosurgery"
    ],

    # =========================
    # PHYSICAL MEDICINE / REHAB
    # =========================
    "rehabilitation": [
        "physical therapy", "pt",
        "occupational therapy", "ot",
        "speech therapy",
        "rehab"
    ],

    # =========================
    # RESPIRATORY / PULMONARY
    # =========================
    "respiratory": [
        "pulmonary function test", "pft",
        "spirometry",
        "ventilation",
        "nebulization",
        "oxygen therapy"
    ],

    # =========================
    # OBSTETRICS / NEONATAL
    # =========================
    "obstetrics": [
        "delivery",
        "vaginal delivery",
        "cesarean",
        "c-section",
        "fetal monitoring",
        "amniocentesis"
    ],

    # =========================
    # DIALYSIS / RENAL
    # =========================
    "dialysis": [
        "hemodialysis",
        "peritoneal dialysis",
        "dialysis session"
    ],

    # =========================
    # TRANSFUSION / BLOOD BANK
    # =========================
    "transfusion": [
        "blood transfusion",
        "platelet transfusion",
        "plasma transfusion"
    ],

    # =========================
    # PHARMACY / INFUSION
    # =========================
    "infusion": [
        "iv infusion",
        "chemotherapy",
        "biologic infusion",
        "injection",
        "immunotherapy"
    ],

    # =========================
    # WOUND / DERMATOLOGY
    # =========================
    "wound_care": [
        "debridement",
        "wound care",
        "burn treatment",
        "skin graft"
    ],

    # =========================
    # EMERGENCY / CRITICAL CARE
    # =========================
    "critical_care": [
        "icu",
        "critical care",
        "resuscitation",
        "ventilator management"
    ],

    # =========================
    # DME / THERAPEUTIC DEVICES
    # =========================
    "medical_device": [
        "prosthetic",
        "orthotic",
        "implantable device",
        "pacemaker",
        "defibrillator"
    ],

    # =========================
    # MENTAL HEALTH
    # =========================
    "mental_health": [
        "psychiatric evaluation",
        "psychotherapy",
        "counseling",
        "behavioral therapy"
    ]
}

# -----------------------------
# ACTIONS / OPERATIONS
# -----------------------------
ACTIONS = {

    # =========================
    # DIAGNOSTIC / EVALUATIVE
    # =========================
    "inspection": [
        "exam",
        "evaluation",
        "visualization",
        "screening",
        "assessment",
        "survey"
    ],

    "measurement": [
        "measurement",
        "pressure measurement",
        "manometry",
        "flow measurement"
    ],

    "monitoring": [
        "monitoring",
        "surveillance",
        "telemetry",
        "observation"
    ],

    # =========================
    # SAMPLING / DIAGNOSTIC TISSUE
    # =========================
    "biopsy": [
        "biopsy",
        "sampling",
        "tissue sample",
        "histology",
        "cytology",
        "fine needle aspiration",
        "fna"
    ],

    "culture": [
        "culture",
        "sensitivity",
        "microbial culture"
    ],

    # =========================
    # REMOVAL / DESTRUCTION
    # =========================
    "excision": [
        "removal",
        "resection",
        "polypectomy",
        "excision",
        "amputation",
        "debridement"
    ],

    "ablation": [
        "ablation",
        "cauterization",
        "laser ablation",
        "radiofrequency ablation",
        "cryotherapy"
    ],

    "extraction": [
        "extraction",
        "foreign body removal",
        "stone removal"
    ],

    # =========================
    # REPAIR / RECONSTRUCTION
    # =========================
    "repair": [
        "repair",
        "suturing",
        "closure",
        "anastomosis"
    ],

    "reconstruction": [
        "reconstruction",
        "grafting",
        "skin graft",
        "flap"
    ],

    "fixation": [
        "fixation",
        "stabilization",
        "fusion",
        "internal fixation"
    ],

    # =========================
    # OPENING / ACCESS CREATION
    # =========================
    "incision": [
        "incision",
        "cutdown",
        "otomy",
        "ostomy"
    ],

    "puncture": [
        "puncture",
        "needle insertion"
    ],

    # =========================
    # LUMEN / PASSAGE MODIFICATION
    # =========================
    "dilation": [
        "dilation",
        "stretching",
        "balloon dilation"
    ],

    "stent_placement": [
        "stent",
        "stenting",
        "endoprosthesis placement"
    ],

    # =========================
    # FLUID / PRESSURE MANAGEMENT
    # =========================
    "drainage": [
        "drainage",
        "aspiration",
        "fluid removal"
    ],

    "irrigation": [
        "irrigation",
        "lavage",
        "washout"
    ],

    # =========================
    # INTRODUCTION / ADMINISTRATION
    # =========================
    "injection": [
        "injection",
        "intramuscular injection",
        "subcutaneous injection",
        "intraarticular injection"
    ],

    "infusion": [
        "infusion",
        "iv infusion",
        "chemotherapy",
        "immunotherapy"
    ],

    "implantation": [
        "implant",
        "device insertion",
        "prosthesis placement",
        "pacemaker insertion"
    ],

    # =========================
    # VASCULAR
    # =========================
    "catheterization": [
        "catheterization",
        "line placement",
        "central line",
        "arterial line"
    ],

    "revascularization": [
        "angioplasty",
        "bypass",
        "thrombectomy"
    ],

    "embolization": [
        "embolization",
        "vessel occlusion"
    ],

    # =========================
    # OBSTETRIC / REPRODUCTIVE
    # =========================
    "delivery": [
        "delivery",
        "vaginal delivery",
        "cesarean section",
        "c-section"
    ],

    "fertility_procedure": [
        "insemination",
        "embryo transfer"
    ],

    # =========================
    # RESPIRATORY SUPPORT
    # =========================
    "ventilation": [
        "ventilation",
        "intubation",
        "extubation",
        "airway management"
    ],

    # =========================
    # PAIN / NEURO
    # =========================
    "nerve_block": [
        "nerve block",
        "regional block",
        "epidural",
        "spinal block"
    ],

    # =========================
    # THERAPEUTIC CARE (NON-PROCEDURAL)
    # =========================
    "therapy": [
        "physical therapy",
        "occupational therapy",
        "speech therapy",
        "rehabilitation"
    ],

    # =========================
    # DESTRUCTION / CONTROL
    # =========================
    "hemostasis": [
        "hemostasis",
        "bleeding control",
        "ligation"
    ],

    # =========================
    # TRANSFUSION / REPLACEMENT
    # =========================
    "transfusion": [
        "blood transfusion",
        "platelet transfusion",
        "plasma transfusion"
    ],

    # =========================
    # SUPPORT / MAINTENANCE
    # =========================
    "supportive_care": [
        "supportive care",
        "palliative care"
    ]
}

# -----------------------------
# INTENT / CLINICAL PURPOSE
# -----------------------------
INTENT_KEYWORDS = {

    # =========================
    # DIAGNOSTIC (FIND / CONFIRM)
    # =========================
    "diagnostic": [
        "diagnostic",
        "evaluation",
        "evaluate",
        "investigation",
        "investigate",
        "rule out",
        "r/o",
        "assessment",
        "workup",
        "confirm",
        "determine cause",
        "initial evaluation"
    ],

    # =========================
    # SCREENING (ASYMPTOMATIC)
    # =========================
    "screening": [
        "screening",
        "preventive",
        "prevention",
        "early detection",
        "routine",
        "annual",
        "baseline",
        "asymptomatic",
        "wellness",
        "health maintenance",
        "surveillance (screening context)"
    ],

    # =========================
    # THERAPEUTIC (TREAT / FIX)
    # =========================
    "therapeutic": [
        "therapeutic",
        "treatment",
        "treat",
        "therapy",
        "intervention",
        "management",
        "removal",
        "resection",
        "repair",
        "correction",
        "control",
        "alleviation",
        "curative",
        "palliative treatment"
    ],

    # =========================
    # FOLLOW-UP / MONITORING
    # =========================
    "follow_up": [
        "follow up",
        "follow-up",
        "recheck",
        "monitor",
        "monitoring",
        "surveillance",
        "post procedure",
        "postoperative",
        "status check",
        "interval evaluation",
        "repeat evaluation"
    ],

    # =========================
    # STAGING / SEVERITY ASSESSMENT
    # =========================
    "staging": [
        "staging",
        "severity assessment",
        "extent evaluation",
        "grading",
        "risk stratification",
        "tumor staging"
    ],

    # =========================
    # CONFIRMATORY / SECONDARY
    # =========================
    "confirmatory": [
        "confirmatory",
        "confirmation",
        "verification",
        "second look",
        "secondary evaluation"
    ],

    # =========================
    # PRE-OPERATIVE / CLEARANCE
    # =========================
    "preoperative": [
        "pre-op",
        "preoperative",
        "pre surgery",
        "surgical clearance",
        "procedure clearance",
        "pre anesthesia"
    ],

    # =========================
    # POST-OPERATIVE / RECOVERY
    # =========================
    "postoperative": [
        "post-op",
        "postoperative",
        "after surgery",
        "recovery evaluation",
        "healing assessment"
    ],

    # =========================
    # PALLIATIVE / SUPPORTIVE
    # =========================
    "palliative": [
        "palliative",
        "comfort care",
        "symptom relief",
        "supportive care",
        "pain relief",
        "quality of life"
    ],

    # =========================
    # EMERGENT / URGENT
    # =========================
    "emergent": [
        "emergency",
        "emergent",
        "urgent",
        "stat",
        "life saving",
        "acute",
        "critical"
    ],

    # =========================
    # ELECTIVE / PLANNED
    # =========================
    "elective": [
        "elective",
        "planned",
        "scheduled",
        "non emergent",
        "optional"
    ],

    # =========================
    # REHABILITATIVE
    # =========================
    "rehabilitative": [
        "rehabilitation",
        "functional recovery",
        "mobility improvement",
        "strengthening",
        "post injury rehab"
    ],

    # =========================
    # PROPHYLACTIC (PREVENT FUTURE ISSUE)
    # =========================
    "prophylactic": [
        "prophylactic",
        "preventive treatment",
        "risk reduction",
        "precautionary"
    ]
}

# -----------------------------
# MODIFIERS / QUALIFIERS
# -----------------------------
MODIFIERS = {
    "with_biopsy": ["with biopsy"],
    "without_biopsy": ["without biopsy"],
    "with_contrast": ["with contrast"],
    "without_contrast": ["without contrast"],
    "bilateral": ["bilateral", "both sides"],
    "left": ["left", "lt"],
    "right": ["right", "rt"]
}

# -----------------------------
# PARENT / HIERARCHY
# -----------------------------
ONTOLOGY_PARENT = {
    # anatomy
    "colon": "gastrointestinal",
    "stomach": "gastrointestinal",
    "esophagus": "gastrointestinal",
    "rectum": "gastrointestinal",

    # modalities
    "endoscopy": "procedure",
    "imaging": "procedure",
    "surgery": "procedure",
    "laboratory": "procedure",

    # actions
    "biopsy": "diagnostic_action",
    "inspection": "diagnostic_action",
    "excision": "therapeutic_action"
}

# -----------------------------
# STOPWORDS (REMOVE NOISE)
# -----------------------------
STOPWORDS = {
    "the", "and", "or", "of", "for", "to",
    "service", "procedure", "level", "charge",
    "facility", "professional", "technical"
}

# -----------------------------
# CANONICAL PROCEDURE PATTERNS
# (Used for scoring & mapping)
# -----------------------------
CANONICAL_PATTERNS = {
    "colonoscopy": {
        "body_part": "colon",
        "modality": "endoscopy",
        "default_intent": "diagnostic"
    },
    "egd": {
        "body_part": "stomach",
        "modality": "endoscopy",
        "default_intent": "diagnostic"
    },
    "ct_abdomen": {
        "body_part": "abdominal",
        "modality": "imaging",
        "default_intent": "diagnostic"
    }
}