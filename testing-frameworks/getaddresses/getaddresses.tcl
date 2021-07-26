set mapfile [open ../firmware/cf2.map r]
set map [read $mapfile]
set resultfile [open getaddresses/addresses.txt w]
set desiredfile [open getaddresses/desired.txt r]
set desired [read $desiredfile]
close $desiredfile
set addresslist ""
foreach {var obj} $desired {
	regexp "$var\\\.?\[\[:digit:]]*\[\[:space:]]*0x(\[\[:xdigit:]]*) *0x\[\[:xdigit:]]* bin/$obj\\.o" $map matches address
	# puts "Match: $matches\n\twith address 0x[string range $address 8 end]"
	puts $resultfile "$var $obj [string range $address 8 end]"
	append addresslist "$var=0x[string range $address 9 end];"
}
close $mapfile
close $resultfile
# set template [open "cfSitlTemplate.py" r]
# set sitl [open "../testing-frameworks/sitl/cfSitl.py" w]
# puts $sitl [regsub {#REPLACED-BY-ADDRESSES} [read $template] $addresslist]
# close $template
# close $sitl
