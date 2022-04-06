sed 's/ORIGIN//' prepinsulin.txt
sed 's/ //g'  prepinsulin.txt
sed 's/[0-9]//g' prepinsulin.txt
sed 's/"//"//' prepinsulin.txt

 sed -e 's/ORIGIN//' -e 's/ //g' -e 's/[0-9]//g' -e '4d' -e '1d'  prepinsulin.txt
 

 
 sed -e 's/ORIGIN//' -e 's/ //g' -e 's/[0-9]//g' -e '4d' -e '1d' preproinsulin-seq.txt > preproinsulin-seq-clean.txt
 
 #removes ORIGIN, spaces, numbers, 4th line and 1st line (note deleting 1st line will remove ORIGIN but just left it)
 
  cut -c 1-24 preproinsulin-seq-clean.txt > lsinsulin-seq-clean.txt
  cut -c 25-54 preproinsulin-seq-clean.txt > binsulin-seq-clean.txt
  cut -c 55-89 preproinsulin-seq-clean.txt > cinsulin-seq-clean.txt
  cut -c 90-110 preproinsulin-seq-clean.txt > ainsulin-seq-clean.txt
