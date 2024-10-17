VBoxManage list runningvms

VBoxManage startvm umbrel2 --type headless  

VBoxManage controlvm umbrel2 acpipowerbutton  



to mount the VDI file:
Install qemu-utils
sudo apt-get install qemu-utils

Load the network block device kernel module
sudo modprobe nbd

Connect the VDI file to a network block device
sudo qemu-nbd --connect=/dev/nbd0 /path/to/your.vdi

Identify the partitions on the virtual disk
sudo fdisk -l /dev/nbd0

Mount the partition
sudo mount /dev/nbd0p1 /mnt

undload nbd
sudo modprobe -r nbd