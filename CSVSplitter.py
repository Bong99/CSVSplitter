import sys, getopt

def main(argv):
  argMain ={'i': ' ', 'o':' '}
  inputfile = ''
  outputfile = ''
  lineNoSeperate = 1
  
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print ('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
  #print ('Input file is ', inputfile)
  #print ('Output file is ', outputfile)
  
  argMain['i'] = inputfile
  argMain['o'] = outputfile
  #print(argMain)
  return argMain
   
if __name__ == "__main__":
  argMain = main(sys.argv[1:])

lineNoSeperate = input("Please enter no of line you want to spit: ")  
print('lineNoSeperate = ' + lineNoSeperate)

fin = open(argMain['i'], 'r')

currentFileNum = 0
currentLine = 0

foutname = argMain['o'] + '_' + str(currentFileNum) + '.csv'

print ('Created File [' + foutname + ']')

fout = open(foutname, 'w')

for line in fin:
  fout.write(line)
  currentLine+=1
  
  if currentLine/int(lineNoSeperate) - round(currentLine/int(lineNoSeperate), 0) == 0.0:
    fout.close()
    currentFileNum+=1
    foutname = argMain['o'] + '_' + str(currentFileNum) + '.csv'
    fout = open(foutname, 'w')
    print ('Created File [' + foutname + ']')

print('***Done***') 
fin.close()



