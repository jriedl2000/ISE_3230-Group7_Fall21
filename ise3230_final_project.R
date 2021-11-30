library(tidyverse)
library(ggplot2)

score <- read.csv("C:/Users/jried/OneDrive/Documents/ISE 3230/Speed Dating Data.csv")

# linear model to predict outcome of date (linear weights of 6 attributes)

new_score <- score %>%
  mutate(age_diff = age - age_o, race_imp = imprace * samerace, diff_attr = attr1_1/100 * attr_o, 
         diff_sinc = sinc1_1/100 * sinc_o, diff_intel = intel1_1/100 * intel_o, diff_fun = fun1_1/100 * fun_o,
         diff_amb = amb1_1/100 * amb_o, diff_shar = shar1_1/100 * shar_o)

new_score[is.na(new_score)] <- 0

lin.mod <- lm(dec ~ order + int_corr + match + age_diff + race_imp + imprelig
             + goal + date + go_out + career_c + exphappy + expnum + diff_attr + 
                diff_sinc + diff_intel + diff_fun + diff_amb + diff_shar, new_score)
summary(lin.mod)

# Testing the model on wave 6 - 5 men and 5 women but constrained to 3 rounds

wave6 <- new_score %>%
  filter(wave == 6) 

sum((wave6['dec'] - predict.lm(lin.mod, wave6))^2)
df <- data.frame(wave6['id'], wave6['partner'],  wave6['order'], wave6['dec'], predict.lm(lin.mod, wave6))
  
