
# Select some columns form mtcars.
input <- mtcars[,c("am","cyl","hp","wt")]

print(input)

am.data = glm(formula = am ~ cyl + hp + wt, data = input, family = binomial)
print(summary(am.data))

a <- data.frame( am= 1)
result <-  predict(am.data,cyl)
print(result)




model <- glm(formula= vs ~ wt + disp, data=mtcars, family=binomial)

newdata = data.frame(wt = 2.1, disp = 180)

predict(model, newdata, type="response")
