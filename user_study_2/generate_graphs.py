import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

EXPERIENCE_COLOR = "blue"
NO_EXPERIENCE_COLOR = "orange"

def graphs_performance_per_task(dependent_var: str, filename: str):
    TITLE_SIZE = 40
    AXES_SIZE = 30
    LEGEND_SIZE = 28
    TICK_SIZE = 26

    # Sort and filter tasks
    tasks = data['Task'].unique()

    fig, axs = plt.subplots(2, 2, figsize=(15, 15), sharey=True)

    # Flatten the axs for easy iteration
    axs = axs.flatten()

    for i, task in enumerate(sorted(tasks)):
        task_data = data[data['Task'] == task].sort_values(by='Participant')
        colors = task_data['Experience level'].apply(lambda x: EXPERIENCE_COLOR if x == "Some" else NO_EXPERIENCE_COLOR).to_list()
        
        axs[i].bar(task_data['Participant'], task_data[dependent_var], color=colors)
        axs[i].set_title(f'Task {task}', fontsize=TITLE_SIZE)
        axs[i].set_xlabel('Participant', fontsize=AXES_SIZE)
        axs[i].set_ylabel(dependent_var, fontsize=AXES_SIZE)
        axs[i].set_xticks(task_data['Participant'])

        # Adjust tick labels size for each subplot
        axs[i].tick_params(axis='x', labelsize=TICK_SIZE)
        axs[i].tick_params(axis='y', labelsize=TICK_SIZE)

    # Adding a legend
    labels = ['No Experience', 'Some Experience']
    handles = [plt.Rectangle((0,0),1,1, color=color, ec="k") for color in [NO_EXPERIENCE_COLOR,EXPERIENCE_COLOR]]
    plt.figlegend(handles, labels, loc=(0.67, 0.35), borderaxespad=0.1, fontsize=LEGEND_SIZE)

    plt.tight_layout()
    plt.savefig(filename, format='pdf', dpi=300, bbox_inches='tight')  # Save the figure

def graph_average_performance_per_task(dependent_var: str, filename: str):
    AXES_SIZE = 18
    LEGEND_SIZE = 15
    TICK_SIZE = 13

    # Splitting the dataframe based on experience level
    df_exp = data[data['Experience level'] == 'Some']
    df_no_exp = data[data['Experience level'] != 'Some']

    # Calculating averages and error margins for time taken
    time_avg_exp = df_exp.groupby('Task')[dependent_var].mean()
    time_avg_no_exp = df_no_exp.groupby('Task')[dependent_var].mean()

    time_min_exp = df_exp.groupby('Task')[dependent_var].min()
    time_max_exp = df_exp.groupby('Task')[dependent_var].max()

    time_min_no_exp = df_no_exp.groupby('Task')[dependent_var].min()
    time_max_no_exp = df_no_exp.groupby('Task')[dependent_var].max()

    # Error bars (min and max values)
    time_error_exp = [time_avg_exp - time_min_exp, time_max_exp - time_avg_exp]
    time_error_no_exp = [time_avg_no_exp - time_min_no_exp, time_max_no_exp - time_avg_no_exp]

    # Setting up the plot for time taken
    tasks = np.arange(1, len(time_avg_exp) + 1)  # Assuming the same number of tasks for both groups
    bar_width = 0.35  # Width of the bars

    fig, ax = plt.subplots()
    ax.bar(tasks - bar_width/2, time_avg_exp, bar_width, yerr=time_error_exp, 
        label='Some Experience', color=EXPERIENCE_COLOR, capsize=5)
    ax.bar(tasks + bar_width/2, time_avg_no_exp, bar_width, yerr=time_error_no_exp, 
        label='No Experience', color=NO_EXPERIENCE_COLOR, capsize=5)

    # Labels, title and legend
    ax.set_xlabel('Task Number', fontsize=AXES_SIZE)
    ax.set_ylabel(f'Average {dependent_var}', fontsize=AXES_SIZE)
    ax.set_xticks(tasks)
    ax.legend(fontsize=LEGEND_SIZE)

    plt.yticks(fontsize=TICK_SIZE)
    plt.xticks(fontsize=TICK_SIZE)

    plt.tight_layout()
    plt.savefig(filename, format='pdf', dpi=300, bbox_inches='tight')  # Save the figure

# Load your data
data_path = 'raw-data.xlsx'  # Make sure to update this path to your actual data file
data = pd.read_excel(data_path)

graphs_performance_per_task("Time (s)", "graph_time_taken.pdf")
graphs_performance_per_task("Number of clicks", "graph_clicks.pdf")

graph_average_performance_per_task("Time (s)", "graph_avg_time_taken.pdf")
graph_average_performance_per_task("Number of clicks", "graph_avg_clicks.pdf")