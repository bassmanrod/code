#!/bin/sh

# Startup script for Xymon
#
# This starts the "xymonlaunch" tool, which in turn starts
# all of the other Xymon server programs.

case "`uname -s`" in
   "SunOS")
   	ID=/usr/xpg4/bin/id
	;;
   *)
   	ID=id
	;;
esac

if test `$ID -un` != xymon
then
	echo "Xymon must be started as the xymon user"
	exit 1
fi

case "$1" in
   "start")
	if test -s /var/log/xymon/xymonlaunch.pid
	then
		kill -0 `cat /var/log/xymon/xymonlaunch.pid`
		if test $? -eq 0
		then
			echo "Xymon appears to be running, doing restart"
			$0 stop
		else
			rm -f /var/log/xymon/xymonlaunch.pid
		fi
	fi

	 /usr/lib/xymon/server/bin/xymonlaunch --config=/usr/lib/xymon/server/etc/tasks.cfg --env=/usr/lib/xymon/server/etc/xymonserver.cfg --log=/var/log/xymon/xymonlaunch.log --pidfile=/var/log/xymon/xymonlaunch.pid
	echo "Xymon started"
	;;

   "stop")
	if test -s /var/log/xymon/xymonlaunch.pid
	then
		kill -TERM `cat /var/log/xymon/xymonlaunch.pid`
		echo "Xymon stopped"
	else
		echo "Xymon is not running"
	fi
	rm -f /var/log/xymon/xymonlaunch.pid
	;;

   "status")
	if test -s /var/log/xymon/xymonlaunch.pid
	then
		kill -0 `cat /var/log/xymon/xymonlaunch.pid`
		if test $? -eq 0
		then
			echo "Xymon (xymonlaunch) running with PID `cat /var/log/xymon/xymonlaunch.pid`"
			exit 0
		else
			echo "Xymon not running, removing stale PID file"
			rm -f /var/log/xymon/xymonlaunch.pid
			exit 1
		fi
	else
		echo "Xymon (xymonlaunch) does not appear to be running"
		exit 3
	fi
	;;

   "restart")
	if test -s /var/log/xymon/xymonlaunch.pid
	then
		$0 stop
		sleep 10
		$0 start
	else
		echo "xymonlaunch does not appear to be running, starting it"
		$0 start
	fi
	;;

   "reload")
	if test -s /var/log/xymon/xymond.pid
	then
		kill -HUP `cat /var/log/xymon/xymond.pid`
	else
		echo "xymond not running (no PID file)"
	fi
	;;

   "rotate")
   	for PIDFILE in /var/log/xymon/*.pid
	do
		kill -HUP `cat $PIDFILE`
	done
	;;

   *)
   	echo "Usage: $0 start|stop|restart|reload|status|rotate"
	break;
esac

exit 0

