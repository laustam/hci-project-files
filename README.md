# Contents

> **_NOTE:_** The final project report can be found in the directory `/experimentation/user_study` and is named `user_study.pdf`

Each section in this `README` file is related to a subdirectory of the project directory. Within each of these sections, more details about the contents of that specific subdirectory is given.


## `use_case_definition`

This directory contains all files relating to creating the initial use case definitions. The following can be found here:

| Filename | Description |
|-|-|
|`persona_brenda.pdf`|Persona Brenda|
|`persona_ramon.pdf`|Persona Ramon|
|`storyboard.pdf`|Storyboard|
|`use_case_description.md`|Use Case Description|
|`user_scenario_ramon.md`|User Scenario for Persona Ramon|
|`use_case_scenario_brenda.md`|Use Case Scenario for Persona Brenda|

## `prototyping`

This directory contains three subdirectories for both lo-fi prototypes v1 and v2 used in the pilot study as well as the hi-fi prototype v1 used in the user study. Additionally, a file outlining the design rationales behind each prototype is provided (`design_rationales.md`).

### Lo-Fi Prototypes (`lo_fi_prototype_v1` and `lo_fi_prototype_v2`)

Both lo-fi prototypes were created using Figma. The subdirectories `lo_fi_prototype_v1` and `lo_fi_prototype_v2` contain screenshots to the different screens created. Note that `lo_fi_prototype_v2` only contains screens related to the timed events because these are the only changes made to the prototype v2. The differences of the lo-fi prototypes were the focus of the pilot study which determined which is preferable.

### Hi-Fi Prototype (`hi_fi_prototype_v1`)

The hi-fi prototype was implemented using SvelteKit. Files inside the `hi_fi_prototype_v1` subdirectory include all relevant files to run the application. To view the application, the following commands can be run to start a server and open the application (running on port `5173` on `localhost`):

```
npm install
npm run dev -- --open
```

## `experimentation`

This directory contains two subdirectories for files related to the pilot study and the user study. Both subdirectories contain similar contents that can be grouped into separate categories. The categories, their description, and filenames specific to the pilot or user study are listed here:

| Category | Description | Filenames in `pilot_study` | Filenames in `user_study` |
|-|-|-|-|
| Consent forms | Scanned version of the consent forms given to each participant | *Not available* | `consent_forms.pdf` | 
| Raw data collected | The raw data collected during the study that includes recorded values for the independent and dependent variables of the experiment (Excel) and the researcher's anonymous observations made of participant performance and feedback (Markdown) | Excel: `raw-data.xlsx`; Research notes: `raw_notes.md`| Excel: `raw-data.xlsx`, Researcher notes: `raw_notes.md` |
| Scripts used to create graphs | Python scripts used to create final data visualizations | Raw data: `graphs-all.py`; Averaged data: `graphs-avg.py` | `generate_graphs.py` |
| Graphs | Two types of graphs saved in PDF version: histograms for raw data and for averaged data | Raw data: `time_taken_histogram.pdf`, `number_of_clicks_histogram.pdf`; Averaged data: `average_time_taken_histogram.pdf`, `average_clicks_histogram.pdf`   | Raw data: `graph_time_taken.pdf`, `graph_clicks.pdf`; Averaged data: `graph_avg_time_taken.pdf`, `graph_avg_clicks.pdf`
| Statistical tests | R script used to conduct relevant statistical tests on data | *Not available* | Mann-Whitney-Wilcoxon Test: `mann_whitney_test.R` |
| Report on Study | Report about the specific study | `pilot_study.pdf` | `user_study.pdf` |