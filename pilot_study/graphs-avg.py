import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FONT_SIZE_LABELS = 14
FONT_SIZE_LEGEND = 16
FONT_SIZE_AXES = 16
FONT_SIZE_TITLE = 20

# Load the data
data = pd.read_excel('a3-data.xlsx')

# Calculate the statistics for time taken
time_stats = data.groupby(['Task', 'UI'])['Time taken (s)'].agg(['mean', 'max', 'min']).reset_index()

# Calculate the statistics for number of clicks
click_stats = data.groupby(['Task', 'UI'])['Number of clicks'].agg(['mean', 'max', 'min']).reset_index()

# Set up for plotting
tasks = sorted(data['Task'].unique())
uis = sorted(data['UI'].unique())
colors = ['skyblue', 'lightgreen']  # Colors for Task 1 and Task 2

# Plotting for Time Taken
fig, ax1 = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(tasks))

for i, ui in enumerate(uis):
    means = time_stats.loc[time_stats['UI'] == ui, 'mean']
    min_errors = means - time_stats.loc[time_stats['UI'] == ui, 'min']
    max_errors = time_stats.loc[time_stats['UI'] == ui, 'max'] - means
    errors = np.abs(np.vstack((min_errors, max_errors)))  # Make sure errors are positive
    ax1.bar(index + bar_width * i, means, bar_width, label=f'UI {ui}', color=colors[i],
            yerr=errors, capsize=5)

ax1.set_xlabel('Task', fontsize=FONT_SIZE_AXES)
ax1.set_ylabel('Average Time Taken (s)', fontsize=FONT_SIZE_AXES)
ax1.set_title('Average Time Taken for Each Task by UI Type', fontsize=FONT_SIZE_TITLE)
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(['Timer Task' if i == 0 else 'Stopwatch Task' for i in index], fontsize=FONT_SIZE_LABELS)
ax1.legend(title='UI Type', fontsize=FONT_SIZE_LEGEND).get_title().set_fontsize(FONT_SIZE_LEGEND)

plt.tight_layout()
plt.savefig("average_time_taken_histogram.pdf", format='pdf', dpi=300, bbox_inches='tight')

# Plotting for Number of Clicks
fig, ax2 = plt.subplots(figsize=(10, 6))

for i, ui in enumerate(uis):
    means = click_stats.loc[click_stats['UI'] == ui, 'mean']
    min_errors = means - click_stats.loc[click_stats['UI'] == ui, 'min']
    max_errors = click_stats.loc[click_stats['UI'] == ui, 'max'] - means
    errors = np.abs(np.vstack((min_errors, max_errors)))  # Make sure errors are positive
    ax2.bar(index + bar_width * i, means, bar_width, label=f'UI {ui}', color=colors[i],
            yerr=errors, capsize=5)

ax2.set_xlabel('Task', fontsize=FONT_SIZE_AXES)
ax2.set_ylabel('Average Number of Clicks', fontsize=FONT_SIZE_AXES)
ax2.set_title('Average Number of Clicks for Each Task by UI Type', fontsize=FONT_SIZE_TITLE)
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(['Timer Task' if i == 0 else 'Stopwatch Task' for i in index], fontsize=FONT_SIZE_LABELS)
ax2.legend(title='UI Type', fontsize=FONT_SIZE_LEGEND).get_title().set_fontsize(FONT_SIZE_LEGEND)

plt.tight_layout()
plt.savefig("average_clicks_histogram.pdf", format='pdf', dpi=300, bbox_inches='tight')