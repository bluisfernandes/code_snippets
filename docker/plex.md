docker run \
-d \
--name plex \
--network=host \
--platform linux/arm64/v8 \
-e TZ="America/Chicago" \
-e PLEX_CLAIM=<CLAIM> \
-v ~/plex/database:/config \
-v ~/plex/temp:/transcode \
-v ~/plex/media:/data \
plexinc/pms-docker



docker run \
-d \
--name plex \
--network=host \
--platform linux/arm64/v8 \
--restart unless-stopped \
-e TZ="America/Chicago" \
-e PLEX_CLAIM="claim" \
-v ~/plex/database:/config \
-v ~/plex/temp:/transcode \
-v ~/plex/media:/data \
lscr.io/linuxserver/plex:latest


scp input.webm USER@IP:/plex/media
