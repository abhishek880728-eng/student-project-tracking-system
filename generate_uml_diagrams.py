"""
========================================================================================
VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY, ERODE - 12
DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A
Student: Abhishek.R (732925ITR002)
Script: generate_uml_diagrams.py
Description: Generates UML Component Diagram and Activity Diagram matching the reference
             specifications for the Student Project & Skill Tracking System.
========================================================================================
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Rectangle, Polygon

OUT_DIR = os.path.join(os.path.dirname(__file__), "docs", "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

def draw_component_icon(ax, x, y, w=0.36, h=0.26):
    """Draws standard UML component glyph (rectangle with two protruding tabs)."""
    ax.add_patch(Rectangle((x, y), w, h, facecolor='white', edgecolor='#1a252f', lw=1.2, zorder=10))
    tab_w = w * 0.45
    tab_h = h * 0.25
    ax.add_patch(Rectangle((x - tab_w/2, y + h*0.60), tab_w, tab_h, facecolor='white', edgecolor='#1a252f', lw=1.0, zorder=11))
    ax.add_patch(Rectangle((x - tab_w/2, y + h*0.15), tab_w, tab_h, facecolor='white', edgecolor='#1a252f', lw=1.0, zorder=11))

def draw_ball(ax, x, y, r=0.16, label="", label_pos='below'):
    """Draws Provided Interface (Lollipop / Ball)."""
    ax.add_patch(Circle((x, y), r, facecolor='#5bc0de', edgecolor='#1a252f', lw=1.5, zorder=8))
    if label:
        if label_pos == 'below':
            ax.text(x, y - r - 0.14, label, fontsize=9, fontweight='bold', color='#102a43', ha='center', va='top')
        elif label_pos == 'left':
            ax.text(x - r - 0.12, y, label, fontsize=9, fontweight='bold', color='#102a43', ha='right', va='center')

def draw_socket(ax, x, y, r=0.18, facing='left', label="", label_pos='below'):
    """Draws Required Interface (Socket / Arc)."""
    if facing == 'left':
        theta1, theta2 = 90, 270
    elif facing == 'right':
        theta1, theta2 = 270, 90
    elif facing == 'up':
        theta1, theta2 = 0, 180
    else:
        theta1, theta2 = 180, 360
    
    wedge = Wedge((x, y), r, theta1, theta2, width=0.045, facecolor='#1a252f', edgecolor='#1a252f', zorder=8)
    ax.add_patch(wedge)
    if label:
        if label_pos == 'below':
            ax.text(x, y - r - 0.14, label, fontsize=9, fontweight='bold', color='#102a43', ha='center', va='top')
        elif label_pos == 'right':
            ax.text(x + r + 0.12, y, label, fontsize=9, fontweight='bold', color='#102a43', ha='left', va='center')

def draw_ball_and_socket(ax, x, y, r=0.16, facing='left', label="", label_pos='below'):
    """Draws an assembly connector (ball nested inside socket)."""
    ax.add_patch(Circle((x, y), r * 0.70, facecolor='#5bc0de', edgecolor='#1a252f', lw=1.3, zorder=9))
    if facing == 'left':
        theta1, theta2 = 90, 270
    elif facing == 'right':
        theta1, theta2 = 270, 90
    elif facing == 'up':
        theta1, theta2 = 0, 180
    else:
        theta1, theta2 = 180, 360
    wedge = Wedge((x, y), r * 1.15, theta1, theta2, width=0.045, facecolor='#1a252f', edgecolor='#1a252f', zorder=10)
    ax.add_patch(wedge)
    if label:
        if label_pos == 'below':
            ax.text(x, y - r - 0.14, label, fontsize=8.5, fontweight='bold', color='#102a43', ha='center', va='top')
        elif label_pos == 'above':
            ax.text(x, y + r + 0.12, label, fontsize=8.5, fontweight='bold', color='#102a43', ha='center', va='bottom')
        elif label_pos == 'right':
            ax.text(x + r + 0.14, y, label, fontsize=8.5, fontweight='bold', color='#102a43', ha='left', va='center')


# ========================================================================================
# 1. UML COMPONENT DIAGRAM
# ========================================================================================
def generate_component_diagram():
    fig, ax = plt.subplots(figsize=(13.0, 9.5), dpi=300)
    ax.set_xlim(-0.5, 13.0)
    ax.set_ylim(-0.5, 9.5)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    outer_bg = '#7ee7ff'  # Cyan-blue matching reference image 1
    border_col = '#1a252f'

    # Outer Container Component: <<component>> Terminal -> Student Project Tracking System
    outer_box = FancyBboxPatch((2.2, 0.5), 8.6, 8.0, boxstyle="square,pad=0",
                               facecolor=outer_bg, edgecolor=border_col, lw=2.2, zorder=1)
    ax.add_patch(outer_box)
    draw_component_icon(ax, 10.25, 8.05, w=0.45, h=0.35)

    ax.text(6.5, 8.15, "<<component>>\nStudent Project Tracking System", 
            fontsize=12, fontweight='bold', color='#102a43', ha='center', va='center')

    # ---------------------------------------------------------
    # Inner Components (Direct 1:1 mapping to reference image)
    # ---------------------------------------------------------
    # 1. SafetyInspection -> ProjectTrackingEngine (Center)
    core_w, core_h = 2.6, 3.4
    core_x, core_y = 4.2, 3.3
    ax.add_patch(Rectangle((core_x, core_y), core_w, core_h, facecolor=outer_bg, edgecolor=border_col, lw=1.8, zorder=3))
    draw_component_icon(ax, core_x + core_w - 0.42, core_y + core_h - 0.32, w=0.34, h=0.24)
    ax.text(core_x + core_w/2, core_y + core_h/2, "<<component>>\nProjectTracking\nEngine", 
            fontsize=10.5, fontweight='bold', color='#102a43', ha='center', va='center')

    # 2. Staff -> Student & Faculty Module (Top Right)
    c2_w, c2_h = 2.4, 1.1
    c2_x, c2_y = 8.0, 5.9
    ax.add_patch(Rectangle((c2_x, c2_y), c2_w, c2_h, facecolor=outer_bg, edgecolor=border_col, lw=1.8, zorder=3))
    draw_component_icon(ax, c2_x + c2_w - 0.38, c2_y + c2_h - 0.30, w=0.32, h=0.22)
    ax.text(c2_x + c2_w/2, c2_y + c2_h/2, "<<component>>\nStudent & Faculty\nModule", 
            fontsize=9.5, fontweight='bold', color='#102a43', ha='center', va='center')

    # 3. Defect -> SkillGapAnalyzer (Bottom Left)
    c3_w, c3_h = 2.4, 1.0
    c3_x, c3_y = 4.2, 0.75
    ax.add_patch(Rectangle((c3_x, c3_y), c3_w, c3_h, facecolor=outer_bg, edgecolor=border_col, lw=1.8, zorder=3))
    draw_component_icon(ax, c3_x + c3_w - 0.38, c3_y + c3_h - 0.30, w=0.32, h=0.22)
    ax.text(c3_x + c3_w/2, c3_y + c3_h/2, "<<component>>\nSkillGapAnalyzer", 
            fontsize=9.5, fontweight='bold', color='#102a43', ha='center', va='center')

    # 4. Map -> MilestoneScheduler (Bottom Right)
    c4_w, c4_h = 2.2, 1.0
    c4_x, c4_y = 7.4, 0.75
    ax.add_patch(Rectangle((c4_x, c4_y), c4_w, c4_h, facecolor=outer_bg, edgecolor=border_col, lw=1.8, zorder=3))
    draw_component_icon(ax, c4_x + c4_w - 0.38, c4_y + c4_h - 0.30, w=0.32, h=0.22)
    ax.text(c4_x + c4_w/2, c4_y + c4_h/2, "<<component>>\nMilestone\nScheduler", 
            fontsize=9.5, fontweight='bold', color='#102a43', ha='center', va='center')

    # ---------------------------------------------------------
    # Ports on Boundary
    # ---------------------------------------------------------
    port_size = 0.22
    p_state = (2.2 - port_size/2, 6.1)     # Corresponds to "State" port
    p_details = (2.2 - port_size/2, 4.8)   # Corresponds to "Details" port
    p_item = (2.2 - port_size/2, 2.3)      # Corresponds to "Inspection Item" port
    p_account = (10.8 - port_size/2, 4.8)  # Corresponds to "Account" port
    p_insp_id = (10.8 - port_size/2, 3.4)  # Corresponds to "Inspection ID" port

    for p in [p_state, p_details, p_item, p_account, p_insp_id]:
        ax.add_patch(Rectangle(p, port_size, port_size, facecolor=outer_bg, edgecolor=border_col, lw=1.5, zorder=6))

    # ---------------------------------------------------------
    # Provided Interfaces (External Left: Lollipops)
    # ---------------------------------------------------------
    # State / Student Info
    ax.plot([1.4, 2.2], [6.1 + port_size/2, 6.1 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_ball(ax, 1.4, 6.1 + port_size/2, r=0.17, label="Student\nProfile")

    # Details / Project Proposal
    ax.plot([1.4, 2.2], [4.8 + port_size/2, 4.8 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_ball(ax, 1.4, 4.8 + port_size/2, r=0.17, label="Project\nDetails")

    # Inspection Item / Evaluation Rubrics
    ax.plot([1.4, 2.2], [2.3 + port_size/2, 2.3 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_ball(ax, 1.4, 2.3 + port_size/2, r=0.17, label="Evaluation\nRubrics")

    # ---------------------------------------------------------
    # Internal Ball & Socket Interfaces (Matching Reference Exactly)
    # ---------------------------------------------------------
    # Left inside: Sockets on ProjectTrackingEngine for Student Profile & Project Details
    ax.plot([2.2 + port_size/2, 2.9], [6.1 + port_size/2, 6.1 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_socket(ax, 2.9, 6.1 + port_size/2, r=0.17, facing='right', label="Student Profile")
    ax.plot([2.9 + 0.17, core_x], [6.1 + port_size/2, 6.1 + port_size/2], color=border_col, lw=1.8, zorder=4)

    ax.plot([2.2 + port_size/2, 2.9], [4.8 + port_size/2, 4.8 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_socket(ax, 2.9, 4.8 + port_size/2, r=0.17, facing='right', label="Project Details")
    ax.plot([2.9 + 0.17, core_x], [4.8 + port_size/2, 4.8 + port_size/2], color=border_col, lw=1.8, zorder=4)

    # Lower path: from Evaluation Rubrics port across to Defect details (SkillGapAnalyzer)
    ax.plot([2.2 + port_size/2, 5.2], [2.3 + port_size/2, 2.3 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_ball_and_socket(ax, 5.2, 2.3 + port_size/2, r=0.17, facing='up', label="Defect / Gap\ndetails", label_pos='below')
    # From ball-and-socket to core component above
    ax.plot([5.2, 5.2], [core_y, 2.3 + port_size/2 + 0.17], color=border_col, lw=1.8, zorder=4)
    # From ball-and-socket to SkillGapAnalyzer below
    ax.plot([5.2, 5.2], [2.3 + port_size/2 - 0.40, c3_y + c3_h], color=border_col, lw=1.8, zorder=4)

    # Core to Student & Faculty (Staff): Inspector connector
    ax.plot([core_x + core_w, 7.3], [6.4, 6.4], color=border_col, lw=1.8, zorder=4)
    draw_ball_and_socket(ax, 7.3, 6.4, r=0.17, facing='right', label="Faculty Guide /\nInspector", label_pos='below')
    ax.plot([7.3 + 0.17, c2_x], [6.4, 6.4], color=border_col, lw=1.8, zorder=4)

    # Core to Right: Inspection ID connector going to Port
    ax.plot([core_x + core_w, 7.3], [4.9, 4.9], color=border_col, lw=1.8, zorder=4)
    draw_ball_and_socket(ax, 7.3, 4.9, r=0.17, facing='right', label="Project ID /\nInspection ID", label_pos='below')
    ax.plot([7.3 + 0.17, 8.4, 8.4, 10.8], [4.9, 4.9, 3.4 + port_size/2, 3.4 + port_size/2], color=border_col, lw=1.8, zorder=4)

    # Core to MilestoneScheduler (Map): Location / Milestone connector
    ax.plot([core_x + core_w, 7.3], [3.8, 3.8], color=border_col, lw=1.8, zorder=4)
    draw_ball_and_socket(ax, 7.3, 3.8, r=0.17, facing='right', label="Milestones /\nLocation", label_pos='below')
    ax.plot([7.3 + 0.17, 8.5, 8.5], [3.8, 3.8, c4_y + c4_h], color=border_col, lw=1.8, zorder=4)

    # Staff (Student & Faculty) down to Account connector, then to Account port
    ax.plot([c2_x + 1.2, c2_x + 1.2], [c2_y, 5.15], color=border_col, lw=1.8, zorder=4)
    draw_ball_and_socket(ax, c2_x + 1.2, 5.15, r=0.17, facing='down', label="Account /\nUser Role", label_pos='below')
    ax.plot([c2_x + 1.2, 10.8], [4.8 + port_size/2, 4.8 + port_size/2], color=border_col, lw=1.8, zorder=4)

    # ---------------------------------------------------------
    # Required Interfaces (External Right: Sockets)
    # ---------------------------------------------------------
    # Account Socket
    ax.plot([10.8, 11.55], [4.8 + port_size/2, 4.8 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_socket(ax, 11.55, 4.8 + port_size/2, r=0.20, facing='left', label="Account /\nDBMS Auth", label_pos='below')

    # Inspection ID Socket
    ax.plot([10.8, 11.55], [3.4 + port_size/2, 3.4 + port_size/2], color=border_col, lw=1.8, zorder=4)
    draw_socket(ax, 11.55, 3.4 + port_size/2, r=0.20, facing='left', label="Project ID /\nAudit Record", label_pos='below')

    # ---------------------------------------------------------
    # Red Annotation Labels (Identical to Reference Image 1)
    # ---------------------------------------------------------
    red_col = '#e03131'

    # Annotation 1: Component
    ax.text(4.0, 9.15, "Component", fontsize=11, fontweight='bold', color=red_col, ha='center')
    ax.annotate("", xy=(4.0, 8.55), xytext=(4.0, 8.95),
                arrowprops=dict(arrowstyle="->", color=red_col, lw=1.8, ls="--"))

    # Annotation 2: Port
    ax.text(1.8, 7.3, "Port", fontsize=11, fontweight='bold', color=red_col, ha='center')
    ax.annotate("", xy=(2.2, 6.3), xytext=(1.8, 7.1),
                arrowprops=dict(arrowstyle="->", color=red_col, lw=1.8, ls="--"))

    # Annotation 3: Provided Interface
    ax.text(0.4, 7.2, "Provided\nInterface", fontsize=10.5, fontweight='bold', color=red_col, ha='center')
    ax.annotate("", xy=(1.25, 6.3), xytext=(0.6, 6.9),
                arrowprops=dict(arrowstyle="->", color=red_col, lw=1.8, ls="--"))

    # Annotation 4: Required Interface
    ax.text(11.8, 6.2, "Required Interface", fontsize=10.5, fontweight='bold', color=red_col, ha='center')
    ax.annotate("", xy=(11.6, 5.1), xytext=(11.8, 5.9),
                arrowprops=dict(arrowstyle="->", color=red_col, lw=1.8, ls="--"))

    # Header title
    plt.title("UML 2.0 Component Diagram — Student Project and Skill Tracking System\n"
              "Velalar College of Engineering and Technology | Class: 25IT3A | Abhishek.R (732925ITR002)",
              fontsize=11.5, fontweight='bold', pad=18, color='#102a43')

    plt.tight_layout()
    png_path = os.path.join(OUT_DIR, "component_diagram.png")
    svg_path = os.path.join(OUT_DIR, "component_diagram.svg")
    plt.savefig(png_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.savefig(svg_path, format='svg', facecolor='white', bbox_inches='tight')
    plt.close()
    print(f"[✓] Saved Component Diagram to: {png_path} & {svg_path}")


# ========================================================================================
# 2. UML ACTIVITY DIAGRAM
# ========================================================================================
def generate_activity_diagram():
    fig, ax = plt.subplots(figsize=(10.0, 13.0), dpi=300)
    ax.set_xlim(-0.5, 10.0)
    ax.set_ylim(-0.5, 13.0)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    action_bg = '#7ee7ff'  # Cyan-blue matching reference image 2
    border_col = '#102a43'
    text_col = '#102a43'

    def draw_action(x, y, w, h, text):
        box = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.12,rounding_size=0.25",
                             facecolor=action_bg, edgecolor=border_col, lw=1.6, zorder=4)
        ax.add_patch(box)
        ax.text(x, y, text, fontsize=10, fontweight='bold', color=text_col, ha='center', va='center', zorder=5)

    def draw_diamond(x, y, w, h):
        pts = [[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]]
        poly = Polygon(pts, facecolor=action_bg, edgecolor=border_col, lw=1.6, zorder=4)
        ax.add_patch(poly)

    def draw_fork_join_bar(x, y, w, h=0.20):
        rect = Rectangle((x - w/2, y - h/2), w, h, facecolor='black', edgecolor='black', zorder=6)
        ax.add_patch(rect)

    # 1. Initial Node (Solid black circle ●)
    init_y = 12.2
    ax.add_patch(Circle((4.75, init_y), 0.28, facecolor='black', edgecolor='black', zorder=5))

    # Arrow to First Action
    act1_y = 10.85
    ax.annotate("", xy=(4.75, act1_y + 0.45), xytext=(4.75, init_y - 0.28),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # 2. First Action: "Receive Project Proposal" (Receive Order equivalent)
    draw_action(4.75, act1_y, 3.2, 0.9, "Receive Project\nProposal")

    # Arrow to Fork Bar
    fork_y = 9.5
    ax.annotate("", xy=(4.75, fork_y + 0.10), xytext=(4.75, act1_y - 0.45),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # 3. Synchronization Fork Bar (Thick horizontal black bar)
    draw_fork_join_bar(4.75, fork_y, w=6.4, h=0.20)

    # ---------------------------------------------------------
    # LEFT PARALLEL THREAD (Fill Order equivalent)
    # ---------------------------------------------------------
    left_x = 2.4
    # Arrow from Fork to Left Action
    ax.annotate("", xy=(left_x, 8.55), xytext=(left_x, fork_y - 0.10),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Left Action: "Verify Tech Stack & Skills" (Fill Order equivalent)
    act_left1_y = 8.1
    draw_action(left_x, act_left1_y, 2.7, 0.9, "Verify Tech Stack\n& Skills")

    # Arrow to Decision Diamond
    dec_y = 6.8
    ax.annotate("", xy=(left_x, dec_y + 0.35), xytext=(left_x, act_left1_y - 0.45),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Decision Diamond
    draw_diamond(left_x, dec_y, w=0.85, h=0.7)

    # Branch 1 [skill gap found] (rush order equivalent) -> Left Action
    act_sub_l_x = 1.2
    act_sub_y = 5.2
    ax.plot([left_x - 0.425, act_sub_l_x], [dec_y, dec_y], color='black', lw=1.8)
    ax.annotate("", xy=(act_sub_l_x, act_sub_y + 0.45), xytext=(act_sub_l_x, dec_y),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))
    ax.text(left_x - 0.5, dec_y + 0.22, "[skill gap found]", fontsize=9, fontweight='bold', color='#102a43', ha='right')
    draw_action(act_sub_l_x, act_sub_y, 2.1, 0.9, "Flag Remedial\nMentoring")

    # Branch 2 [else] (else equivalent) -> Right Action
    act_sub_r_x = 3.6
    ax.plot([left_x + 0.425, act_sub_r_x], [dec_y, dec_y], color='black', lw=1.8)
    ax.annotate("", xy=(act_sub_r_x, act_sub_y + 0.45), xytext=(act_sub_r_x, dec_y),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))
    ax.text(left_x + 0.5, dec_y + 0.22, "[skills verified]", fontsize=9, fontweight='bold', color='#102a43', ha='left')
    draw_action(act_sub_r_x, act_sub_y, 2.1, 0.9, "Approve Technical\nFeasibility")

    # Merge Diamond
    merge_y = 3.6
    ax.plot([act_sub_l_x, act_sub_l_x], [act_sub_y - 0.45, merge_y], color='black', lw=1.8)
    ax.annotate("", xy=(left_x - 0.425, merge_y), xytext=(act_sub_l_x, merge_y),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    ax.plot([act_sub_r_x, act_sub_r_x], [act_sub_y - 0.45, merge_y], color='black', lw=1.8)
    ax.annotate("", xy=(left_x + 0.425, merge_y), xytext=(act_sub_r_x, merge_y),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    draw_diamond(left_x, merge_y, w=0.85, h=0.7)

    # ---------------------------------------------------------
    # RIGHT PARALLEL THREAD (Send Invoice & Receive Payment equivalent)
    # ---------------------------------------------------------
    right_x = 7.1
    # Arrow from Fork to Right Action 1
    ax.annotate("", xy=(right_x, 8.55), xytext=(right_x, fork_y - 0.10),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Right Action 1: "Auto-Provision 5 Milestones" (Send Invoice equivalent)
    act_right1_y = 8.1
    draw_action(right_x, act_right1_y, 2.8, 0.9, "Auto-Provision 5\nAcademic Milestones")

    # Arrow to Right Action 2
    act_right2_y = 5.2
    ax.annotate("", xy=(right_x, act_right2_y + 0.45), xytext=(right_x, act_right1_y - 0.45),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Right Action 2: "Assign Faculty Review Committee" (Receive Payment equivalent)
    draw_action(right_x, act_right2_y, 2.8, 0.9, "Assign Faculty\nReview Committee")

    # ---------------------------------------------------------
    # SYNCHRONIZATION JOIN BAR & FINAL NODE
    # ---------------------------------------------------------
    join_y = 2.2
    # Arrow from Left Merge Diamond to Join Bar
    ax.annotate("", xy=(left_x, join_y + 0.10), xytext=(left_x, merge_y - 0.35),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Arrow from Right Action 2 to Join Bar
    ax.annotate("", xy=(right_x, join_y + 0.10), xytext=(right_x, act_right2_y - 0.45),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Solid black Join Bar
    draw_fork_join_bar(4.75, join_y, w=6.4, h=0.20)

    # Arrow from Join Bar to Final Node
    final_y = 0.9
    ax.annotate("", xy=(4.75, final_y + 0.32), xytext=(4.75, join_y - 0.10),
                arrowprops=dict(arrowstyle="->", color='black', lw=1.8))

    # Activity Final Node (Bullseye ◉)
    ax.add_patch(Circle((4.75, final_y), 0.30, facecolor='white', edgecolor='black', lw=2.0, zorder=5))
    ax.add_patch(Circle((4.75, final_y), 0.19, facecolor='black', edgecolor='black', zorder=6))

    plt.title("UML 2.0 Activity Diagram — Project Registration & Evaluation Workflow\n"
              "Velalar College of Engineering and Technology | Class: 25IT3A | Abhishek.R (732925ITR002)",
              fontsize=11.5, fontweight='bold', pad=18, color='#102a43')

    plt.tight_layout()
    png_path = os.path.join(OUT_DIR, "activity_diagram.png")
    svg_path = os.path.join(OUT_DIR, "activity_diagram.svg")
    plt.savefig(png_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.savefig(svg_path, format='svg', facecolor='white', bbox_inches='tight')
    plt.close()
    print(f"[✓] Saved Activity Diagram to: {png_path} & {svg_path}")

if __name__ == "__main__":
    generate_component_diagram()
    generate_activity_diagram()
    print("All diagrams regenerated successfully!")
