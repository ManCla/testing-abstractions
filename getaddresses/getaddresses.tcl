set mapfile [open ../firmware/cf2.map r]
set map [read $mapfile]
set resultfile [open addresses.txt w]
set desiredfile [open desired.txt r]
set desired [read $desiredfile]
close $desiredfile
foreach {var obj} $desired {
	regexp "$var\\\.?\[\[:digit:]]*\[\[:space:]]*0x(\[\[:xdigit:]]*) *0x\[\[:xdigit:]]* bin/$obj\\.o" $map matches address
	puts "Match: $matches\n\twith address 0x[string range $address 8 end]"
	puts $resultfile "$var $obj [string range $address 8 end]"
}
close $mapfile
close $resultfile
