#install.packages("haven")
library("haven")
xpt = read_xpt("/Users/obinnadinneya/Desktop/MY_BIGDATA_PROJECT/mydata/MMSA2021.xpt")
write.csv(xpt, file="/Users/obinnadinneya/Desktop/MY_BIGDATA_PROJECT/mydata/MMSA2021.csv")

xpt = read_xpt("/Users/obinnadinneya/Desktop/MY_BIGDATA_PROJECT/mydata/MMSA2019.xpt")
write.csv(xpt, file="/Users/obinnadinneya/Desktop/MY_BIGDATA_PROJECT/mydata/MMSA2019.csv")