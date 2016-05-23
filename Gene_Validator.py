#!/usr/bin/python
# Written by Adrian Bubie (git hub: https://github.com/Apb58)
#Gene Name Validation checker for new test panels:
#Checks Gene name from the list of genes from the genes index against the genes
#listed in the test regions.

Gene_list = open('Genes_List.txt','r')
Raw_Genes = Gene_list.readlines()
Genes = list()
for item in Raw_Genes:
    item = item.replace('\n','')
    Genes.append(item)


file_name = raw_input('Name of Test Regions file: ')
test_genes = open(file_name, 'r')
raw_test_regions = test_genes.readlines()
test_regions = list()
for item in raw_test_regions:
    item = item.replace('\n','')
    test_regions.append(item)
    

for gene in test_regions:
    if gene not in Genes:
        print ("error: " + gene + " not in genes index")
    else:
        print (gene + " is in genes index")

count = len(test_regions)
print "Genes in the Test Regions:", count
    
