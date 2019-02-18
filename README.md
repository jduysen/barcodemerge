# barcodemerge
Watches a windows directory for jpg images containing barcodes.  Merges all images after each barcode into multi-page pdf files.

watchfile.py contains all of the python code.  You will need to designate a path_to_watch, converted_path, and merge_path.  There are sample jpgs that I have used for testing.  1.jpg and 5.jpg contain barcodes.  If you run watchfile.py and then copy the jpgs into your path_to_watch, you should get 2 merged pdfs in your merge_path that are organized by the barcode pages each page follows.
