docker pull jellyfin/jellyfin:latest  # or docker pull ghcr.io/jellyfin/jellyfin:latest

mkdir -p /srv/jellyfin/{config,cache}

docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media:/media --net=host jellyfin/jellyfin:latest