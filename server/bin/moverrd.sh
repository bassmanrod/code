#!/bin/sh

# This script moves or copies rrd files from the flat "all files
# in a single directory" structure used by the traditional LARRD
# tool, to the "one directory per host" structure used by Xymon

# You need to run this tool once, to migrate your RRD files and
# historical data to Xymon.
#
# Set these variables to match your local setup

# The directory where Big Brother+LARRD has your RRD files currently
SRCDIR=/usr/local/bb/bbvar/rrd

# These are the Xymon directories and filenames
XYMONHOME=/usr/lib/xymon/server
HOSTSCFG=$XYMONHOME/etc/hosts.cfg
DSTDIR=/var/lib/xymon/rrd		# Where the files should end up.

OP="cp -f"			# Set to "mv" to move files instead of copying

# You should not need to modify anything below here.

export SRCDIR XYMONHOME HOSTSCFG DSTDIR OP


cd $SRCDIR || (echo "Cannot go to $SRCDIR"; exit 0)

$XYMONHOME/bin/xymoncfg |grep "^[0-9]" | awk '{print $2}' | \
while read HOST
do
	HOSTC=`echo $HOST | sed 's/\./,/g'`
	mkdir $DSTDIR/${HOST}

	DFILES=`echo $HOST.*.rrd`
	if [ "$DFILES" != "$HOST.*.rrd" ]
	then
	   for f in $HOST.*.rrd
	   do
	     $OP $f $DSTDIR/${HOST}/`echo $f | sed "s/^${HOST}\.//"`
	   done
	fi

	CFILES=`echo $HOSTC.*.rrd`
	if [ "$CFILES" != "$HOSTC.*.rrd" ]
	then
	   for f in $HOSTC.*.rrd
	   do
	     $OP $f $DSTDIR/${HOST}/`echo $f | sed "s/^${HOSTC}\.//"`
	   done
	fi
done

