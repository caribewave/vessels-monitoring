#!/usr/bin/python

#import os,sys,socket
import aisparser
#import fileinput

#try:
#    f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    f.connect('192.168.2.70',1234)
#    s = f.makefile('r')
#except:
#    sys.stderr.write("Error connecting")
#    raise


with open('log_ais_vhtm.log', 'r') as f:
       s=f.readlines()

ais_state = aisparser.ais_state()


for p in s:
    result = aisparser.assemble_vdm( ais_state, p )
#    print "%s : %s" % (result, p)
    if( result == 0):
        ais_state.msgid = aisparser.get_6bit( ais_state.six_state, 6 )
#        print "msgid = %d" % (ais_state.msgid)

        if ais_state.msgid == 1:
            msg = aisparser.aismsg_1()
            aisparser.parse_ais_1( ais_state, msg )
            (status,lat_dd,long_ddd) = aisparser.pos2ddd(msg.latitude, msg.longitude)

            print "%s,%d,%s,%s" % (p[0:19],msg.userid,lat_dd,long_ddd)
#            print "mmsi     : %d" % (msg.userid)
#            print "latitude : %d" % (msg.latitude)
#            print "longitude: %d" % (msg.longitude)
#            print "lat_dd   : %s" % (lat_dd)
#            print "long_ddd : %s" % (long_ddd)
#            print "pos_acc  : %d" % (ord(msg.pos_acc))

        elif ais_state.msgid == 2:
            msg = aisparser.aismsg_2()
            aisparser.parse_ais_2( ais_state, msg )
            (status,lat_dd,long_ddd) = aisparser.pos2ddd(msg.latitude, msg.longitude)

            print "%s,%d,%s,%s" % (p[0:19],msg.userid,lat_dd,long_ddd)
#            print "mmsi     : %d" % (msg.userid)
#            print "latitude : %d" % (msg.latitude)
#            print "longitude: %d" % (msg.longitude)
#            print "lat_dd   : %s" % (lat_dd)
#            print "long_ddd : %s" % (long_ddd)
#            print "pos_acc  : %d" % (ord(msg.pos_acc))

        elif ais_state.msgid == 3:
            msg = aisparser.aismsg_3()
            aisparser.parse_ais_3( ais_state, msg )
            (status,lat_dd,long_ddd) = aisparser.pos2ddd(msg.latitude, msg.longitude)

            print "%s,%d,%s,%s" % (p[0:19],msg.userid,lat_dd,long_ddd)
#            print "mmsi     : %d" % (msg.userid)
#            print "latitude : %d" % (msg.latitude)
#            print "longitude: %d" % (msg.longitude)
#            print "lat_dd   : %s" % (lat_dd)
#            print "long_ddd : %s" % (long_ddd)
#            print "pos_acc  : %d" % (ord(msg.pos_acc))

        elif ais_state.msgid == 4:
            msg = aisparser.aismsg_4()
            aisparser.parse_ais_4( ais_state, msg )
            (status,lat_dd,long_ddd) = aisparser.pos2ddd(msg.latitude, msg.longitude)

            print "%s,%d,%s,%s" % (p[0:19],msg.userid,lat_dd,long_ddd)
#            print "mmsi     : %d" % (msg.userid)
#            print "latitude : %d" % (msg.latitude)
#            print "longitude: %d" % (msg.longitude)
#            print "lat_dd   : %s" % (lat_dd)
#            print "long_ddd : %s" % (long_ddd)
#            print "pos_acc  : %d" % (ord(msg.pos_acc))

#        elif ais_state.msgid == 5:
#            msg = aisparser.aismsg_5()
#            aisparser.parse_ais_5( ais_state, msg )
#
#            print "mmsi       : %d" % (msg.userid)
#            print "callsign   : %s" % (msg.callsign)
#            print "name       : %s" % (msg.name)
#            print "destination: %s" % (msg.dest)

        elif ais_state.msgid == 8:
	    msg = aisparser.aismsg_8()
	    aisparser.parse_ais_8( ais_state, msg )
			
	    dac = msg.app_id >> 6;
	    fi = msg.app_id & 0x3F;

#	    print "dac       : %d" % (dac)
#	    print "fi        : %d" % (fi)

	    sixbit = msg.data
	    spare = aisparser.get_6bit( sixbit, 2 )
	    msgid = aisparser.get_6bit( sixbit, 6 )
#	    print "msgid     : %d" % (msgid)

	    if fi==1 and msgid==3:
	    	msg1_3 = aisparser.seaway1_3()
	    	aisparser.parse_seaway1_3( sixbit, msg1_3 )
			
	    	for i in xrange(0,6):
		    report = aisparser.get_water_level_report( msg1_3, i)
		    utc_time = report.utc_time
		    print "month     : %d" % (ord(utc_time.month))
		    print "day       : %d" % (ord(utc_time.day))
		    print "hours     : %d" % (ord(utc_time.hours))
		    print "minutes   : %d" % (ord(utc_time.minutes))
		    print "station   : %s" % (report.station_id)
		    print "longitude : %ld" % (report.longitude)
		    print "latitude  : %ld" % (report.latitude)
		    print "type      : %d" % (ord(report.type))
		    print "level     : %d" % (report.level)
		    print "datum     : %d" % (ord(report.datum))
		    print "spare     : %d" % (report.spare)
		    print "\n"

f.closed
True
