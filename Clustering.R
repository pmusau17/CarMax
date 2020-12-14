Data = read.csv("CaseDataRemodeled.csv",stringsAsFactors = TRUE)

# Look that strings are factors 
str(Data)

## Trying to identify groups of shoppers with similar interests and to the shoppers
## within each group of previous car purchases.
colnames(Data)

dim(Data)

## Lets look at all the different car models (will identify manufacturer)
table(Data[,3])

CarData <- Data[,-c(1,13,14)]
########################### PCA ################################

pr.out = prcomp(CarData)
MFData[,14]

colMeans(Data$purchase_make)




sd.data <- scale(CarData)

data.dist <- dist(CarData)

hclust(CarData)

sum(is.na(CarData))
summary(CarData)

CarData <- na.omit(CarData)
hclust(CarData)

