# clearpass-device-db

A database to manage MAC addresses for MAC-authentication with Aruba ClearPass

Add authentication source:
![img.png](doc/auth_source.png)

Configure Authentication Source with this filter query:
`SELECT mac as user_password,role_id,description FROM devices_device WHERE mac='%{Radius:IETF:User-Name}'`

Set attributes as shown:
![img_1.png](doc/filter_query.png)