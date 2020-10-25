 

#!/bin/bash

for ip in $(seq 200 210); do
ping -c 1 192.168.21.$ip
done
