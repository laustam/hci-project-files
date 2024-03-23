library(readxl)
data <- read_excel("raw-data.xlsx") # NOTE: ensure you are in the correct working directory (user_study)

# Mann Whitney Test for Time(s)
wilcox.test(`Time (s)` ~ `Experience level`, data = data, exact = FALSE)

# Mann Whitney Test for Number of clicks
wilcox.test(`Number of clicks` ~ `Experience level`, data = data, exact = FALSE)
