Some analysis of the association rules
-----------




```
install.packages("arules")
install.packages("arulesViz")

d <- fromJSON(file="/tmp/Morrowind_taglist.json")

tr = as(d, "transactions")
#two examples
rules <- apriori(tr, parameter= list(supp=0.006, conf=0.9))
plot(rules,method="graph", control=list(type="items"))
rules <- apriori(tr, parameter= list(supp=0.02, conf=0.2))
plot(rules,method="graph", control=list(type="items"))
```
