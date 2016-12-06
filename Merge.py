import os
import ctypes
import webbrowser
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

ctypes.windll.kernel32.SetConsoleTitleA(b"PDF Merger")

def PdfMerger():
	files_Directory = input('\n' + 'What directory are the files in?:' + '\n').replace('\\', '/')
	upside_User = str(input('\n' + 'Did your dumbass import the files upside down? (Yes or No)' + '\n').lower())
	pdf_Files = [f for f in os.listdir(files_Directory) if f.endswith("pdf")]
	merger = PdfFileMerger()

	initialization = '\n The following items will be merged:'
	print(initialization)
	print('=' * len(initialization))

	for filename in pdf_Files:
		print(filename)

	proceed = str(input('\nWould you like to continue?: (Yes or No): \n').lower())
	if proceed == "yes":
		for filename in pdf_Files:
			merger.append(PdfFileReader(os.path.join(files_Directory, filename), 'rb'))

		merger.write(os.path.join(files_Directory, "merged_full.pdf"))

		if upside_User == 'no':
			print('\n' + 'Files have been merged, and stored within', os.path.join(files_Directory))
	
		elif upside_User == 'yes':
			pdf_In = open(os.path.join(files_Directory, "merged_full.pdf"), 'rb')
			pdf_Reader = PdfFileReader(pdf_In)
			pdf_Writer = PdfFileWriter()

			for pagenum in range(pdf_Reader.numPages):
				page = pdf_Reader.getPage(pagenum)
				page.rotateClockwise(180)
				pdf_Writer.addPage(page)

			pdf_Output = open(os.path.join(files_Directory, "rotated.pdf"), 'wb')
			pdf_Writer.write(pdf_Output)
			pdf_Output.close()
			pdf_In.close()

			print('\n' + 'Files have been rotated, and stored within', os.path.join(files_Directory))

		navigate_to_Directory = str(input('\nWould you like to navigate to the directory? (Yes or No)\n')).lower()

		if navigate_to_Directory == 'yes':
			webbrowser.open(files_Directory)
		else:
			print("\nAll done!\n")
	else:
		print("\nLet's try this again...\n")
		PdfMerger()

PdfMerger()