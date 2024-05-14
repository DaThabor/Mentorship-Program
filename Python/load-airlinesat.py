# Load Airline Satisfaction data into SQL Server Database table

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('pyodbc')
install_and_import('pandas')

data = pandas.read_csv(r"D:\DaThabor\Repositories\Mentorship\Mentorship-Program\airline_passenger_satisfaction.csv") # type: ignore
df = pandas.DataFrame(data) # type: ignore

conn = pyodbc.connect( # type: ignore
    "Driver={SQL Server};"
    "Server=DESKTOP-DATHABO\MSSQLDATHABOR19;"
    "Database=airlinesatisfaction;"
    "Trusted_Connection=yes;"
)

SQL_QUERY = """
SELECT * FROM airlinesat;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

for row in cursor.fetchall():
    print('row = %r' % (row,))

conn.close()