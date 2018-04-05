import json

dsUrl = 'http://google.com'
dsUsername = 'Chris'
dsPassword = 'Password'

datasources_dict = [
    {
        'name'      : 'aqJMSDS',
        'jndi'      : 'aqJMSDS',
        'url'           : dsUrl,
        'username': dsUsername,
        'password': dsPassword,
        'driver'    : 'oracle.jdbc.xa.client.OracleXADataSource'
    },{
        'name'      : 'CWDirectCPDS',
        'jndi'      : 'CWDirectCPDS',
        'url'           : dsUrl,
        'username': dsUsername,
        'password': dsPassword,
        'driver'    : 'oracle.jdbc.OracleDriver'
    },{
        'name'      : 'SerenadeSeamDatasource',
        'jndi'      : 'SerenadeSeamDatasource',
        'url'           : dsUrl,
        'username': dsUsername,
        'password': dsPassword,
        'driver'    : 'oracle.jdbc.OracleDriver'
    }
]

#datasources = json.dumps(datasources_dict, indent=True)
#datasources = json.dumps(datasources_dict)
#print datasources_dict

for ds in datasources_dict:
    print ds
