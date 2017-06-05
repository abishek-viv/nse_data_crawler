"""__Main_code__,Basic functionalities for extracting the data from NSE and processing it. Nothing much but to imporve the code oops can be applied to 
	imporve the modularity and better functioning. Feel free to modify the code and git it."""

import datetime
import requests
import os, zipfile
from os import listdir
from os.path import isfile, join

month = 'MAY'
month_in_num=5

file_path=os.getcwd()

###getting the current dir path and adding "/bhav_cpy" is to create a desired dir name. Path file was created with linux while
###developing, do change it accordingly to your OS.

directory_to_bhav = file_path + "/BHAV_CPY"			#update the path file according to the OS
directory_to_oi = file_path + "/OI"				#update the path file according to the OS
directory_to_vol = file_path + "/VOLATILITY"			#update the path file according to the OS
###testing the creation of the current dir thing is working

"""print (directory)							 	
	if not os.path.exists(directory):
		os.mkdir(directory)"""

holidays=[1,6,7,13,14,20,21,27,28]
###function for fetching the data
def Monthly_bhav(directory_bhav):
	###checks the desired dir exists else creates a new dir								
	try:
		if not os.listdir(directory_bhav):				
			os.rmkdir(directory_bhav)
	except:
		if not os.path.exists(directory_bhav):				
			os.mkdir(directory_bhav)			###shifting through the days
			for i in range(1,32):
				if i not in holidays:					
					if (i<=9):
							url='http://www.nseindia.com/content/historical/DERIVATIVES/2017/{}/fo0{}{}2017bhav.csv.zip'
							r = requests.get(url.format(month,i,month))	
							file_name="fo0{}{}2017bhav.zip"
							modified_f_name=file_name.format(i,month)

							###os.path.join is used to merge the creating .zip files into the current /bhav_cpy dir
							with open(os.path.join(directory_bhav,modified_f_name), "wb") as code: 
									code.write(r.content)  
					else:
							url='http://www.nseindia.com/content/historical/DERIVATIVES/2017/{}/fo{}{}2017bhav.csv.zip'
							r = requests.get(url.format(month,i,month))	
							file_name="fo{}{}2017bhav.zip"
							modified_f_name=file_name.format(i,month)
							with open(os.path.join(directory_bhav,modified_f_name), "wb") as code:
									code.write(r.content)
				else:
					pass



def Open_interest(directory_oi):
	try:
		if not os.listdir(directory_oi):				
			os.rmkdir(directory_oi)
	except:
		if not os.path.exists(directory_oi):				
			os.mkdir(directory_oi)			###shifting through the days
			for i in range(1,32):
				if i not in holidays:					
					if (i<=9):
							url='https://www.nseindia.com/archives/nsccl/mwpl/nseoi_0{}0{}2017.zip'
							r = requests.get(url.format(i,month_in_num))	
							file_name="nseoi_0{}0{}2017.zip"
							modified_f_name=file_name.format(i,month_in_num)

							###os.path.join is used to merge the creating .zip files into the current /bhav_cpy dir
							with open(os.path.join(directory_oi,modified_f_name), "wb") as code: 
									code.write(r.content)  
					else:
							url='https://www.nseindia.com/archives/nsccl/mwpl/nseoi_{}0{}2017.zip'
							r = requests.get(url.format(i,month_in_num))	
							file_name="nseoi_{}0{}2017.zip"
							modified_f_name=file_name.format(i,month_in_num)
							with open(os.path.join(directory_oi,modified_f_name), "wb") as code:
									code.write(r.content)
				else:
					pass

def Volatility(directory_vol):
	try:
		if not os.listdir(directory_vol):				
			os.rmkdir(directory_vol)
	except:
		if not os.path.exists(directory_vol):				
			os.mkdir(directory_vol)			###shifting through the days
			for day in range(1,32):
				if day not in holidays:					
					if (day<=9):
							url='https://www.nseindia.com/archives/nsccl/volt/FOVOLT_0{}0{}2017.csv'
							r = requests.get(url.format(day,month_in_num))	
							file_name="fovolt_0{}0{}2017.csv"
							modified_f_name=file_name.format(day,month_in_num)

							###os.path.join is used to merge the creating .zip files into the current /bhav_cpy dir
							with open(os.path.join(directory_vol,modified_f_name), "wb") as code: 
									code.write(r.content)  
					else:
							url='https://www.nseindia.com/archives/nsccl/volt/FOVOLT_{}0{}2017.csv'
							r = requests.get(url.format(day,month_in_num))	
							file_name="fovolt_{}0{}2017.csv"
							modified_f_name=file_name.format(day,month_in_num)
							with open(os.path.join(directory_vol,modified_f_name), "wb") as code:
									code.write(r.content)
				else:
					pass


###function to extract all the zip files							
def Unzipper(unzip_directory):
	file_path=os.getcwd()
	###listdir is used to list the contents of a directory
	onlyfiles = os.listdir(unzip_directory)
	#print (unzip_directory)
	#print (onlyfiles)
	for i in onlyfiles:
	#if o.endswith(".zip"):
		path_to_zipfile= unzip_directory + "/{}".format(i)
		#print (path_to_zipfile)
		###refer zipfile doc for more info about the underlying function
		zip = zipfile.ZipFile(path_to_zipfile, 'r')
		zip.extractall(unzip_directory)
		zip.close()

###main function to define the working of the project
if __name__ == '__main__':
	print "======"*10
	print "Extracting the Bhav copy\n" 
	Monthly_bhav(directory_to_bhav)
	print "unzippping...\n"
	Unzipper(directory_to_bhav)
	print "Bhav copy extraction complete\n"
	print "======"*10
	print "Extracting the OI\n"
	Open_interest(directory_to_oi)
	print "unzippping...\n"
	Unzipper(directory_to_oi)
	print "OI extraction complete\n"
	print "======"*10
	print "Extracting the Volatility file\n"
	Volatility(directory_to_vol)
	print "Volatility file extraction complete"
