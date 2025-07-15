import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import io
import base64
from IPython.display import display, HTML
from matplotlib.patches import Rectangle

# Set style for better visualizations
plt.style.use('seaborn-v0_8-whitegrid')

# Function to generate VNG test visualizations
def create_vng_visualization(test_type, data, title, findings, normal_range=None):
    """
    Create a visualization of VNG test results
    
    Parameters:
    -----------
    test_type : str
        Type of VNG test (e.g., "Caloric", "Oculomotor")
    data : dict
        Dictionary containing test data
    title : str
        Title of the visualization
    findings : str
        Clinical findings/interpretation
    normal_range : tuple, optional
        Tuple indicating normal range (min, max)
    """
    fig = plt.figure(figsize=(12, 7))
    gs = GridSpec(3, 1, height_ratios=[1, 3, 1])
    
    # Title section
    ax_title = plt.subplot(gs[0])
    ax_title.axis('off')
    ax_title.text(0.5, 0.5, title, fontsize=16, fontweight='bold', ha='center')
    
    # Test data plot
    ax_plot = plt.subplot(gs[1])
    
    # Plot data based on test type
    if test_type == "Caloric":
        times = data['time']
        for side in ['right', 'left']:
            for temp in ['warm', 'cool']:
                ax_plot.plot(times, data[f'{side}_{temp}'], 
                             label=f"{side.capitalize()} ear ({temp})",
                             linewidth=2)
        
        ax_plot.set_ylabel("Slow Phase Velocity (°/s)")
        ax_plot.set_xlabel("Time (seconds)")
        
        if normal_range:
            ax_plot.axhspan(normal_range[0], normal_range[1], alpha=0.2, color='green', label='Normal Range')
            
    elif test_type == "Saccade":
        # Plot saccadic eye movements
        for direction in ['horizontal', 'vertical']:
            ax_plot.plot(data['time'], data[direction], 
                         label=f"{direction.capitalize()} saccades",
                         linewidth=2)
        
        ax_plot.set_ylabel("Eye Position (°)")
        ax_plot.set_xlabel("Time (seconds)")
        
    elif test_type == "Smooth Pursuit":
        # Plot smooth pursuit tracking
        ax_plot.plot(data['time'], data['target'], 'k--', label='Target', alpha=0.5)
        ax_plot.plot(data['time'], data['actual'], label='Eye Movement', linewidth=2)
        
        ax_plot.set_ylabel("Eye Position (°)")
        ax_plot.set_xlabel("Time (seconds)")
        
    elif test_type == "Optokinetic":
        # Plot optokinetic nystagmus
        ax_plot.plot(data['time'], data['response'], linewidth=2)
        
        ax_plot.set_ylabel("Slow Phase Velocity (°/s)")
        ax_plot.set_xlabel("Time (seconds)")
        
    elif test_type == "Positional":
        # Plot positional nystagmus
        for position in data['positions']:
            start = data['position_times'][position][0]
            end = data['position_times'][position][1]
            segment = np.logical_and(data['time'] >= start, data['time'] <= end)
            
            ax_plot.plot(data['time'][segment], data['spv'][segment], 
                         label=position, linewidth=2)
            
            # Add position labels
            ax_plot.axvspan(start, end, alpha=0.1, color='gray')
            ax_plot.text((start + end)/2, ax_plot.get_ylim()[1]*0.9, 
                         position, ha='center')
            
        ax_plot.set_ylabel("Slow Phase Velocity (°/s)")
        ax_plot.set_xlabel("Time (seconds)")
    
    ax_plot.legend(loc='upper right')
    ax_plot.grid(True, linestyle='--', alpha=0.7)
    
    # Findings section
    ax_findings = plt.subplot(gs[2])
    ax_findings.axis('off')
    
    # Create a box for findings
    box = Rectangle((0.05, 0.05), 0.9, 0.9, fill=True, 
                   alpha=0.1, color='blue', transform=ax_findings.transAxes)
    ax_findings.add_patch(box)
    
    ax_findings.text(0.5, 0.8, "CLINICAL FINDINGS:", fontsize=12, 
                   fontweight='bold', ha='center', transform=ax_findings.transAxes)
    ax_findings.text(0.5, 0.5, findings, fontsize=11, ha='center', 
                   wrap=True, transform=ax_findings.transAxes)
    
    plt.tight_layout()
    return fig

# 1. Normal VNG test results
time = np.linspace(0, 30, 300)

# Generate data for normal caloric test
normal_data = {
    'time': time,
    'right_warm': 12 + np.sin(time/5) + np.random.normal(0, 0.5, len(time)),
    'right_cool': -12 + np.sin(time/5) + np.random.normal(0, 0.5, len(time)),
    'left_warm': 11 + np.cos(time/5) + np.random.normal(0, 0.5, len(time)),
    'left_cool': -11 + np.cos(time/5) + np.random.normal(0, 0.5, len(time))
}

normal_findings = """
- Symmetrical responses between right and left ears
- Normal peak slow phase velocities
- No significant directional preponderance
- Normal vestibular function
"""

fig1 = create_vng_visualization(
    "Caloric", 
    normal_data, 
    "Normal VNG Caloric Test Results", 
    normal_findings,
    normal_range=(-15, 15)
)

# 2. Right-sided vestibulopathy
right_vestib_data = {
    'time': time,
    'right_warm': 4 + np.sin(time/5) + np.random.normal(0, 0.5, len(time)),
    'right_cool': -4 + np.sin(time/5) + np.random.normal(0, 0.5, len(time)),
    'left_warm': 12 + np.cos(time/5) + np.random.normal(0, 0.5, len(time)),
    'left_cool': -12 + np.cos(time/5) + np.random.normal(0, 0.5, len(time))
}

right_vestib_findings = """
- Reduced responses from right ear (warm and cool)
- Normal responses from left ear
- Right directional preponderance
- Findings consistent with right-sided vestibulopathy
"""

fig2 = create_vng_visualization(
    "Caloric", 
    right_vestib_data, 
    "Right-Sided Vestibulopathy VNG Results", 
    right_vestib_findings,
    normal_range=(-15, 15)
)

# 3. Abnormal saccadic eye movements
saccade_time = np.linspace(0, 10, 200)
target_positions = np.concatenate([np.ones(25)*angle for angle in [-20, 20, -10, 10, -15, 15, -5, 5]])
normal_saccades = np.zeros(len(saccade_time))

# Create staircase pattern for targets
for i in range(len(target_positions)):
    idx_start = i * (len(saccade_time) // len(target_positions))
    idx_end = (i+1) * (len(saccade_time) // len(target_positions))
    normal_saccades[idx_start:idx_end] = target_positions[i]

# Add a slight delay to represent abnormal saccades
abnormal_horizontal = np.zeros_like(normal_saccades)
for i in range(1, len(normal_saccades)):
    target = normal_saccades[i]
    current = abnormal_horizontal[i-1]
    # Slower to reach target with overshoot
    if abs(current - target) > 0.1:
        abnormal_horizontal[i] = current + (target - current) * 0.3 * (1 + 0.5*np.sin(i/10))
    else:
        abnormal_horizontal[i] = target
        
# Vertical saccades with different abnormality
abnormal_vertical = np.zeros_like(normal_saccades)
for i in range(1, len(normal_saccades)):
    target = normal_saccades[i] * 0.8  # Lower amplitude for vertical
    current = abnormal_vertical[i-1]
    # More irregular pattern
    if abs(current - target) > 0.1:
        abnormal_vertical[i] = current + (target - current) * 0.2 * (1 + 0.3*np.cos(i/5))
    else:
        abnormal_vertical[i] = target

saccade_data = {
    'time': saccade_time,
    'horizontal': abnormal_horizontal,
    'vertical': abnormal_vertical
}

saccade_findings = """
- Dysmetric saccades with overshooting and correction
- Slowed saccadic velocity
- Irregular accuracy in target acquisition
- Findings consistent with cerebellar dysfunction
"""

fig3 = create_vng_visualization(
    "Saccade", 
    saccade_data, 
    "Abnormal Saccadic Eye Movements", 
    saccade_findings
)

# 4. Benign Paroxysmal Positional Vertigo (BPPV)
bppv_time = np.linspace(0, 180, 1800)  # 3 minutes of recording
bppv_spv = np.zeros_like(bppv_time)

# Define the positions and their timings
positions = ['Sitting', 'Supine', 'Head Right', 'Sitting', 'Head Left', 'Sitting']
position_times = {
    'Sitting': (0, 30),
    'Supine': (30, 60),
    'Head Right': (60, 90),
    'Sitting (2)': (90, 120),
    'Head Left': (120, 150),
    'Sitting (3)': (150, 180)
}

# Create positional nystagmus pattern typical for BPPV
for i, t in enumerate(bppv_time):
    if 60 <= t < 63:  # Head Right position - onset of nystagmus
        bppv_spv[i] = 18 * np.exp(-(t-60)/2)  # Strong, quick decay
    elif 63 <= t < 75:  # Head Right - dissipating nystagmus
        bppv_spv[i] = 5 * np.exp(-(t-63)/10)
    elif 120 <= t < 123:  # Head Left position - mild nystagmus
        bppv_spv[i] = 5 * np.exp(-(t-120)/2)
    else:
        bppv_spv[i] = np.random.normal(0, 0.8)  # Background noise

bppv_data = {
    'time': bppv_time,
    'spv': bppv_spv,
    'positions': positions,
    'position_times': {
        'Sitting': (0, 30),
        'Supine': (30, 60),
        'Head Right': (60, 90),
        'Sitting (2)': (90, 120),
        'Head Left': (120, 150),
        'Sitting (3)': (150, 180)
    }
}

bppv_findings = """
- Transient positional nystagmus in right Dix-Hallpike position
- Latency of 2-3 seconds before nystagmus onset
- Crescendo-decrescendo pattern with fatigability
- Findings consistent with right posterior canal BPPV
"""

fig4 = create_vng_visualization(
    "Positional", 
    bppv_data, 
    "Benign Paroxysmal Positional Vertigo (BPPV)", 
    bppv_findings
)

# 5. Abnormal Smooth Pursuit (Broken Pursuit)
pursuit_time = np.linspace(0, 15, 300)
# Target movement (sinusoidal)
target_movement = 15 * np.sin(2 * np.pi * 0.2 * pursuit_time)

# Normal pursuit would closely match the target
# Abnormal pursuit shows catch-up saccades and poor tracking
abnormal_pursuit = np.zeros_like(target_movement)

for i in range(len(pursuit_time)):
    if i > 0:
        # Add lag and saccadic corrections
        error = target_movement[i] - abnormal_pursuit[i-1]
        if abs(error) > 3:
            # Catch-up saccade
            abnormal_pursuit[i] = target_movement[i] - np.sign(error) * 1.5
        else:
            # Smooth pursuit with poor gain
            abnormal_pursuit[i] = abnormal_pursuit[i-1] + error * 0.3
            
    # Add some noise
    abnormal_pursuit[i] += np.random.normal(0, 0.4)

pursuit_data = {
    'time': pursuit_time,
    'target': target_movement,
    'actual': abnormal_pursuit
}

pursuit_findings = """
- Broken pursuit with catch-up saccades
- Reduced gain (ratio of eye velocity to target velocity)
- Asymmetric tracking between leftward and rightward movement
- Findings suggestive of central vestibular dysfunction
"""

fig5 = create_vng_visualization(
    "Smooth Pursuit", 
    pursuit_data, 
    "Abnormal Smooth Pursuit Test Results", 
    pursuit_findings
)

# Display all figures (in a notebook this would display them)
plt.show()

# In a script, you would save the figures
fig1.savefig('normal_vng_results.png', dpi=300, bbox_inches='tight')
fig2.savefig('right_vestibulopathy_vng.png', dpi=300, bbox_inches='tight')
fig3.savefig('abnormal_saccades_vng.png', dpi=300, bbox_inches='tight')
fig4.savefig('bppv_vng_results.png', dpi=300, bbox_inches='tight')
fig5.savefig('abnormal_smooth_pursuit_vng.png', dpi=300, bbox_inches='tight')

print("VNG test visualizations have been created and saved.")