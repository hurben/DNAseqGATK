
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


nrow(data_frame)
ncol(data_frame)

sink(out_put)


for (i in 5:ncol(data_frame))
{

	ba_pvalue <- cor.test(ba,data_frame[,i])$p.value
	ba_cor <- cor.test(ba,data_frame[,i])$estimate

	da_pvalue <- cor.test(da,data_frame[,i])$p.value
	da_cor <- cor.test(da,data_frame[,i])$estimate

	pd_pvalue <- cor.test(pd,data_frame[,i])$p.value
	pd_cor <- cor.test(pd,data_frame[,i])$estimate


	if ( is.na(ba_pvalue) == FALSE )
	{
		
		if ( is.na(da_pvalue) == FALSE)
		{	
			if (is.na(pd_pvalue) == FALSE)
			{


				if ( ba_pvalue < 0.05)
				{

					ba.lm <- lm(ba~data_frame[,i])

					gene <- colnames(data_frame)[i]
					pngfile <- paste(gene,"BA.png",sep=".")
					png(filename=pngfile)
					plot(ba~data_frame[,i], pch=19, main=gene, xlab="#Mutations", ylab="BA")
					abline(ba.lm, col="red")
					dev.off()
					print (paste0("BA:", colnames(data_frame)[i], "	", ba_cor, "	", ba_pvalue), quote="FALSE")


				}

			############

				if ( da_pvalue < 0.05)
				{
					da.lm <- lm(da~data_frame[,i])

					gene <- colnames(data_frame)[i]
					pngfile <- paste(gene,"DA.png",sep=".")
					png(filename=pngfile)
					plot(da~data_frame[,i], pch=19, main=gene,  xlab="#Mutations", ylab="DA")
					abline(da.lm, col="red")
					dev.off()
					print (paste0("DA:", colnames(data_frame)[i],  "	", da_cor, "	", da_pvalue), quote="FALSE")


				}

			##############
				if ( pd_pvalue < 0.05)
				{
					pd.lm <- lm(pd~data_frame[,i])

					gene <- colnames(data_frame)[i]
					pngfile <- paste(gene,"PD.png",sep=".")
					png(filename=pngfile)
					plot(pd~data_frame[,i], pch=19, main=gene, xlab="#Mutations", ylab="PD")
					abline(pd.lm, col="red")
					dev.off()
					print (paste0("PD:", colnames(data_frame)[i],  "	", pd_cor, "	", pd_pvalue), quote="FALSE")



				}



			}
		}

	}
}


close(out_put)
