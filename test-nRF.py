#!/usr/bin/python

import spi

# This is a very simple script that uses the rPi SPI port to read out the various registers in a nRF24L01+ device
# connected to the rPI SPI port 0
# It should be pretty self-explanitory

ret = spi.openSPI(speed=1000000)
print "openSPI returns: ", ret
fd = ret ["fd"]
print "fd = ", fd

print "Reading nRF24L01 status registers:"

for x in range(28):
	dat = spi.transfer(fd, (x, 0))
	print "nRF Register 0x%X: %X" % (x, dat[1])

spi.closeSPI (fd)
