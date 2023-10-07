#install.packages("haven")
library("haven")
xpt = read_xpt("/Users/obinnadinneya/Desktop/MY_BIGDATA_PROJECT/MMSA2021.xpt")
write.csv(xpt, file="mydata/MMSA2021.csv")
csv1 = read.csv('MMSA2021.csv')

