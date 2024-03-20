import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FONT_SIZE_LABELS = 14
FONT_SIZE_LEGEND = 16
FONT_SIZE_AXES = 16
FONT_SIZE_TITLE = 20

# Load the data from the uploaded Excel file
file_path = 'a3-data.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Define specific color shades for participants and UIs
color_shades = {
    1.0: {'UI_1': 'dodgerblue', 'UI_2': 'skyblue'},
    2.0: {'UI_1': 'darkorange', 'UI_2': 'bisque'},
    3.0: {'UI_1': 'limegreen', 'UI_2': 'palegreen'},
    4.0: {'UI_1': 'hotpink', 'UI_2': 'lightpink'}
}

def add_hierarchical_labels(ax, df):
    participants = df['Participant'].unique()
    tasks = ['Task 1', 'Task 2']
    labels = [f'Participant {int(participant)}' for participant in participants]

    pos = np.arange(len(tasks) * len(participants))
    step = len(tasks) * len(participants) / len(participants)
    mid_step = step / len(tasks) / 2

    for i, label in enumerate(labels):
        ax.text(i * step + mid_step, -ax.get_ylim()[1] * 0.2, label, ha='center', va='top', fontsize=FONT_SIZE_AXES)


# Apply hatching based on UI
def apply_hatching_by_ui(bars, ui):
    hatch = 'x' if ui == 1.0 else 'O'
    for bar in bars:
        bar.set_hatch(hatch)

# Function to plot and save histogram
def plot_and_save_histogram(df, color_shades, value_column, title, ylabel, filename):
    fig, ax = plt.subplots(figsize=(14, 8))
    for (participant, ui), group_data in df.groupby(['Participant', 'UI']):
        color = color_shades[participant]['UI_1'] if ui == 1.0 else color_shades[participant]['UI_2']
        bars = ax.bar(group_data['Task_ID'], group_data[value_column], color=color)
        apply_hatching_by_ui(bars, ui)

    # ax.set_xlabel('Participants and Tasks', fontsize=16)
    ax.set_ylabel(ylabel, fontsize=FONT_SIZE_AXES)
    ax.set_title(title, fontsize=FONT_SIZE_TITLE)
    add_hierarchical_labels(ax, df)

    ax.bar("0", 0, color='grey', label='UI 1 (Darker Shade, X)', hatch='/')
    ax.bar("0", 0, color='lightgrey', label='UI 2 (Lighter Shade, O)', hatch='o')
    ax.legend(title='UI Patterns', fontsize=FONT_SIZE_LEGEND).get_title().set_fontsize(FONT_SIZE_LEGEND)
    
    ax.set_xticks(range(int(len(data_sorted['Task_ID'])/2)))
    ax.set_xticklabels(['Timer\nTask', 'Stopwatch\nTask'] * int(len(data_sorted['Task_ID']) / 4), rotation=45, fontsize=FONT_SIZE_LABELS)

    plt.tight_layout()
    plt.savefig(filename, format='pdf', dpi=300, bbox_inches='tight')  # Save the figure

# Sort and prepare the data
data['Participant']
data['UI']
data['Task_ID'] = data['Participant'].astype(str) + '-' + data['Task'].astype(str)
data_sorted = data.sort_values(by=['Participant', 'Task'])

# Plot and save the 'Time Taken' histogram
plot_and_save_histogram(data_sorted, color_shades, 'Time taken (s)',
                        'Time Taken for Each Task by Participant and UI',
                        'Time taken (s)', 'time_taken_histogram.pdf')

# Plot and save the 'Number of Clicks' histogram
plot_and_save_histogram(data_sorted, color_shades, 'Number of clicks',
                        'Number of Clicks for Each Task by Participant and UI',
                        'Number of clicks', 'number_of_clicks_histogram.pdf')
