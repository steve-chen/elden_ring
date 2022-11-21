# Launching gunicorn + Flask
gunicorn -b 127.0.0.1:5000 --workers=2 app:app

# Nginx configuration
	root /home/jayden/sites/jaydenchen.org/html;
	location / {
		# checks for static file, if not found proxy to app
		try_files $uri @proxy_to_app;
	}

	location @proxy_to_app {
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header Host $http_host;
		# we don't want nginx trying to do something clever with
		# redirects, we set the Host: header above already.
		proxy_redirect off;
		proxy_pass http://127.0.0.1:5000;
	}

