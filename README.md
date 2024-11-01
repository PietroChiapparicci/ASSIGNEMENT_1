Chiapparicci Pietro, 2145440

This is my assignement. Files containing commands like this one (input_str1='' /n A = list(map(int, input_str1.split()))) are made to transform the string from the Rosalind dataset (which should be copied and paste into "input_str1", in most cases) into a usable list to then be used in the different functions. 
Commands like the one below are made to transform the output list into a string that can be copied and pasted into the Rosalind "answer box". The creation of a new file containing the output is due to the fact that, for the majority of cases, the terminal did not print the whole output, but just a small portion. 

C=def()
with open("file_name.txt", "w") as f:
    f.write(' '.join(map(str, C)))