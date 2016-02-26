#This script must accept an odd number of command line arguments.
#The first argument must be the name of the csv file to be read from,
#and every pair of arguments after that are to be indices of columns in the
#range of the csv data fram

args = commandArgs(trailingOnly=TRUE)
args_index = 2

getTags <- function(){
    
    tag1 = as.integer(args[args_index])
    tag2 = as.integer(args[args_index+1])
    
    return(c(tag1, tag2))
}

if(length(args) < 1){
    print('not enough arguments')
    quit()
}

data = read.csv(args[1])

while(args_index < length(args)){
    tags = getTags()
    args_index = args_index + 2
    
    print(sprintf('testing %s and %s', colnames(data)[tags[1]], colnames(data)[tags[2]]))
    test = table(data[,tags[1]] == 1, data[,tags[2]] == 1)
    print(fisher.test(test))
}
