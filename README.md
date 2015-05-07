# openfire-django
This is django application for openfire user management. 

#Openfire – User Management using Python django

Prerequisites

1. Openfire server installed
2. Openfire user management plugin ( download from http://www.igniterealtime.org/projects/openfire/plugins.jsp)

The configuration for user service plugin can be done in Openfire Admin console under Server > Server Settings > User Service. Once you done with it run the project.

#Installation

1. Create new django project.
3. Dowload and install openfire-django 
4. Add following code to settings.py file ,

```
OPENFIRE_SERVER='http://<server-domain>:9090/'
ADMIN_USERNAME='admin'
ADMIN_PASSWORD='admin'
```

5. edit urls.py file and add following code to it,

```
url(r'^server/', include('openfireapp.urls')),
```

6. Add templates to relative path.
7. Run django project.

