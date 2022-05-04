```
server {
    listen       80;
    server_name  localhost;

    location / {
        # See documentation here: http://nginx.org/en/docs/http/ngx_http_auth_request_module.html
        auth_request /auth;
        root   /usr/share/nginx/html;
        index  index.html;
    }

    location = /auth {
        # Proxy through to Node backend
        proxy_pass http://auth_backend:3000/;
        proxy_pass_request_body off;
        proxy_set_header Content-Length "";
        proxy_set_header X-Original-URI $request_uri;
    }
}
```

