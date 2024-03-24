library(readxl)
library(dplyr)

data <- read_excel("raw-data.xlsx") # NOTE: ensure you are in the correct working directory (user_study)

# Prepare a function to run the Mann-Whitney U test for a given task and dependent variable
run_mann_whitney <- function(data, task, dependent_variable) {
  # Filter data for the specific task
  task_data <- data %>% filter(Task == task)
  
  # Convert dependent variable to a formula
  formula <- as.formula(paste("`", dependent_variable, "` ~ `Experience level`", sep=""))
  
  # Perform the Mann-Whitney U test using wilcox.test
  result <- wilcox.test(formula, data = task_data, exact = FALSE)
  return(result)
}

# Initialize a list to store results
results <- list()
tasks <- unique(data$Task)
dependent_variables <- c("Time (s)", "Number of clicks")

# Run tests for each task and dependent variable
for (task in tasks) {
  for (dependent_variable in dependent_variables) {
    results[[paste("Task", task, dependent_variable)]] <- run_mann_whitney(data, task, dependent_variable)
  }
}

# Results
results
