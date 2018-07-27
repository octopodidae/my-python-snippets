import configparser as cp

config = cp.ConfigParser()

file = r'.\tmp\Config.ini'

config.read( file )

mail = config.get( 'mail', 'SMTP_server' )

database = config.get( 'database', 'name' )

fmeserver = config.get( 'fmeserver', 'SERVER_FME' )

print( 'mail =', mail )
print( 'database =', database )
print( 'fmeserver =', fmeserver )
