# DM4P Monitor Server
**mo-server** is a simple server for monitor and notify.
## Usage
```
docker pull mo-server:[tags]
docker run -d -p 9999:9999 -v /opt/mo-server/:/usr/src/app/configs/ mo-server:[tags]
```