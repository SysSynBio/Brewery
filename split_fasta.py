# Brewery: prediction of 1D protein structure annotations (https://github.com/mircare/Brewery)
# Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use it for purposes not permitted by the CC BY-NC-SA 4.0.

# split fasta file with multiple sequences into multiple fasta files with 1 sequence each
import os
import sys

# check arguments
if len(sys.argv) < 2:
    print("\nUsage:",sys.argv[0]," path_to_fasta\n")
    exit()


# catch big fasta
fasta = open(sys.argv[1], "r").readlines()

# create new directory to save outcome
os.mkdir("Fastas")
os.chdir("Fastas")

# fix formatting
i = 0
while i < len(fasta):
    pid = fasta[i].replace(">", "").split()[0]
    if os.path.isfile(pid):
        j = 0
        while os.path.isfile(pid+str(j)):
            j += 1
        pid += str(j) 
    i+=1
    aa = ">"+pid+"\n"
    while i < len(fasta) and fasta[i][0] != ">":
        aa = aa + fasta[i].strip()
        i+=1
    f = open(pid,"w")
    f.write(aa+"\n")

f.close()

print("Done. You can find the splitted fasta files inside Fastas/. Please run multiple_fasta.py now. E.g., python3 multiple_fasta.py -i Fastas --cpu 4 --parallel 2.")
