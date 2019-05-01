
args <- commandArgs(TRUE)

#data <- read.table(args[1], header=T, sep='\t')
data_frame <- read.table(args[1],sep="\t",head=TRUE, row.names=1)
attach(data_frame)

#data_frame
ba <- data_frame[,1]
da <- data_frame[,2]
pd <- data_frame[,3]


out_put <- file("R_linear_regression_summary.txt")



#data_frame.lm <- lm(ba~data_frame[,4])
#png(filename='test.png')
#plot(ba~data_frame[,4], pch=19)
#abline(data_frame.lm, col="red")
#dev.off()



#sink(out_put)


for (i in 4:nrow(data_frame))
{
	print (i)

	ba_pvalue <- cor.test(ba,data_frame[,i])$p.value
	da_pvalue <- cor.test(da,data_frame[,i])$p.value
	pd_pvalue <- cor.test(pd,data_frame[,i])$p.value



	ba.lm <- lm(ba~data_frame[,i])

	gene <- colnames(data_frame)[i]
	pngfile <- paste(gene,"BA.png",sep=".")
	png(filename=pngfile)

	plot(ba~data_frame[,i], pch=19, main=gene)
	abline(ba.lm, col="red")
	dev.off()



	da.lm <- lm(da~data_frame[,i])

	gene <- colnames(data_frame)[i]
	pngfile <- paste(gene,"DA.png",sep=".")
	png(filename=pngfile)

	plot(da~data_frame[,i], pch=19, main=gene)
	abline(da.lm, col="red")
	dev.off()

	pd.lm <- lm(pd~data_frame[,i])

	gene <- colnames(data_frame)[i]
	pngfile <- paste(gene,"PD.png",sep=".")
	png(filename=pngfile)

	plot(pd~data_frame[,i], pch=19, main=gene)
	abline(pd.lm, col="red")
	dev.off()



}


#close(out_put)
