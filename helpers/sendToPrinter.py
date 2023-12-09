import cups
import sys


def send_to_printer():
	conn = cups.Connection()
	printers = conn.getPrinters()

	available_printers = list(printers.keys())
	print_using = available_printers[3]
	photo_dict = {"PageSize":"4x6", "MediaType":"photographic-glossy", "cupsPrintQuality":"High"}
	plain_dict = {"PageSize":"Letter", "MediaType":"stationary", "cupsPrintQuality":"High"}
	filename = "./test-5.png"

	try:
	    """Print the file."""
	    conn.printFile(print_using, filename, "title", photo_dict)
	except:
	    sys.exit("Error")

"""
Home_Inkjet dnssd://Brother%20MFC-J6530DW._ipp._tcp.local./?uuid=e3248000-80ce-11db-8000-3c2af40b2b01
ColorModel/Color Mode: Gray *RGB
cupsPrintQuality/Quality: *Normal High
Duplex/2-Sided Printing: None *DuplexNoTumble DuplexTumble
PageSize/Media Size: 215x345mm 3.5x5 3.5x5.Fullbleed 4x6 4x6.Fullbleed 5x7 5x7.Fullbleed 5x8 5x8.Fullbleed A3 A3.Fullbleed A4 A4.Fullbleed A5 A6 A6.Fullbleed Env10 EnvC5 EnvDL EnvMonarch Executive FanFoldGermanLegal Legal *Letter Letter.Fullbleed Oficio Tabloid Tabloid.Fullbleed Custom.WIDTHxHEIGHT
MediaType/MediaType: stationery photographic-glossy stationery-inkjet *any
"""
