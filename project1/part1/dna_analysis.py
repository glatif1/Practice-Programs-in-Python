# Name: ...
# CS 110
# Project 1: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
# 
# This program is based on Michael Ernt's assignment on DNA Analysis 

###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print ("You must supply a file name as an argument when running this program.")
    sys.exit(2)


# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
g_count = 0
c_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bp's we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    if bp == 'C':
        c_count = c_count + 1
    if bp == 'G':
        g_count = g_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

# Print the answer
print("")
print ("GC-content:", gc_content)
print("G-content", g_count)
print("C-content:",c_count)
print("")



#the AT content

# Total nucleotides seen so far.
total_countat = 0
# Number of A and T nucleotides seen so far.
at_count = 0
a_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bp's we've seen
    total_countat = total_countat + 1

    # next, if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1
    if bp =="A":
        a_count = a_count+1
    if bp == "T":
        t_count = t_count+1
    lengthofseq = len(seq)
# divide the at_count by the total_count
at_content = float(at_count) / total_countat

sumofcount = a_count + t_count + g_count + c_count

ATGCratio = float(at_count) / gc_count


# Print the answer
print(" ")
print("AT to GC ratio:", ATGCratio)
print(" ")
print ("AT-content:", at_content)
print("A-content:",a_count)
print("T-content:",t_count)
print(" ")
print("Length of Sequence:", lengthofseq)
print("Total Count:",total_count)
print("Sum:", sumofcount)
print(" ")

if gc_content > .6:
    print("This organism has HIGH GC CONTENT")
elif gc_content < .4:
    print("This organism has LOW GC CONTENT")
else:
    print("This organism has MODERATE GC CONTENT")





