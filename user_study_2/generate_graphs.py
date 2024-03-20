import matplotlib.pyplot as plt
import pandas as pd

TITLE_SIZE = 20
AXES_SIZE = 15
LEGEND_SIZE = 13

def graph_data(dependent_var: str, filename: str):
    # Sort and filter tasks
    tasks = data['Task'].unique()

    fig, axs = plt.subplots(2, 2, figsize=(15, 10), sharey=True)

    # Flatten the axs for easy iteration
    axs = axs.flatten()

    for i, task in enumerate(sorted(tasks)):
        task_data = data[data['Task'] == task].sort_values(by='Participant')
        colors = task_data['Experience level'].apply(lambda x: 'blue' if x == "Some" else 'orange').to_list()
        
        axs[i].bar(task_data['Participant'], task_data[dependent_var], color=colors, alpha=0.75)
        axs[i].set_title(f'Task {task}', fontsize=TITLE_SIZE)
        axs[i].set_xlabel('Participant', fontsize=AXES_SIZE)
        axs[i].set_ylabel(dependent_var, fontsize=AXES_SIZE)
        axs[i].set_xticks(task_data['Participant'])

    # Adding a legend
    labels = ['No Experience', 'Experienced']
    handles = [plt.Rectangle((0,0),1,1, color=color, ec="k") for color in ['orange','blue']]
    plt.figlegend(handles, labels, loc='upper right', borderaxespad=0.1, title="Experience Level", fontsize=LEGEND_SIZE).get_title().set_fontsize(LEGEND_SIZE)

    plt.tight_layout()
    plt.savefig(filename, format='pdf', dpi=300, bbox_inches='tight')  # Save the figure

# Load your data
data_path = 'raw-data.xlsx'  # Make sure to update this path to your actual data file
data = pd.read_excel(data_path)

graph_data("Time (s)", "graph_time_taken.pdf")
graph_data("Number of clicks", "graph_clicks.pdf")
