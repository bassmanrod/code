#!/bin/bash

# Pre-generate periodic Xymon reports
#
# This would typically run via cron and xymoncmd. A sample crontab
# to generate daily, weekly and monthly reports would be:
#
#     10 0 * * * /usr/lib/xymon/server/bin/xymoncmd --env=/usr/lib/xymon/server/etc/xymonserver.cfg xymonreports.sh daily
#     10 1 * * 1 /usr/lib/xymon/server/bin/xymoncmd --env=/usr/lib/xymon/server/etc/xymonserver.cfg xymonreports.sh weekly
#     10 2 1 * * /usr/lib/xymon/server/bin/xymoncmd --env=/usr/lib/xymon/server/etc/xymonserver.cfg xymonreports.sh monthly
#
# I.e. daily reports run each day at 0:10 AM, weekly reports run 
# on Monday morning at 1:10 AM, monthly reports run on the first of 
# each month at 2:10 AM.

# This script requires the GNU date utility. Point this
# setting to where you have that installed
GNUDATE=date
export GNUDATE

if [ "$1" == "-?" -o "$1" == "--help" -o $# -eq 0 ]
then
   echo "Usage: $0 {daily,weekly,monthly,annual} [fake reporting-date]"
   echo "The \"fake reporting-date\" defaults to today, meaning"
   echo "that the report runs until yesterday at 23:59:59."
   echo "Thus, to generate a daily report for Dec 1st 2001, use"
   echo "   $0 daily \"2 Dec 2001\""
   echo "NB: Quotes are required for the fake reporting-date"
   exit 1
fi

if [ "$XYMONHOME" = "" ]; then
   echo "Must have Xymon environment set."
   exit 1
fi

# This is the top-level directory for the pre-generated reports.
REPORTTOPDIR="$XYMONWWWDIR/periodic"
REPORTTOPURL="$XYMONWEB/periodic"

REPTYPE=$1
if [ "$REPTYPE" == "" ]
then
   REPTYPE="daily"
fi

TODAY=$2
if [ "$TODAY" == "" ]
then
   TODAY="today"
fi

if [ "$REPTYPE" == "daily" ]
then
   REPDIR=$REPTYPE/`$GNUDATE --date="$TODAY -1 day" +"%Y/%m/%d"`
   set `$GNUDATE --date="$TODAY -1 day" +"%d %b %Y"`
   SDAY=$1; SMON=$2; SYEAR=$3
elif [ "$REPTYPE" == "weekly" ]
then
   REPDIR=$REPTYPE/`$GNUDATE --date="$TODAY -1 week" +"%Y/%V"`
   set `$GNUDATE --date="$TODAY -1 week" +"%d %b %Y"`
   SDAY=$1; SMON=$2; SYEAR=$3
elif [ "$REPTYPE" == "monthly" ]
then
   REPDIR=$REPTYPE/`$GNUDATE --date="$TODAY -1 day" +"%Y/%m"`
   set `$GNUDATE --date="$TODAY -1 month" +"%d %b %Y"`
   SDAY=$1; SMON=$2; SYEAR=$3
else
   echo "Unknown report type : $REPTYPE"
   exit 1
fi

# End date is today, meaning today at 00:00
set `$GNUDATE --date="$TODAY -1 day" +"%d %b %Y"`
EDAY=$1; EMON=$2; EYEAR=$3


STIME=`$GNUDATE +%s --date "$SDAY $SMON $SYEAR 00:00:00"`
ETIME=`$GNUDATE +%s --date "$EDAY $EMON $EYEAR 23:59:59"`

# Create the output directory
mkdir -p $REPORTTOPDIR/$REPDIR || exit 1
XYMONWEB=$REPORTTOPURL/$REPDIR $XYMONHOME/bin/xymongen --reportopts=$STIME:$ETIME:0:nongr $XYMONGENREPOPTS $REPORTTOPDIR/$REPDIR

exit 0

