cd /home/visakoe1/Downloads/ev3/robotdownsizing
git pull
cd /home/visakoe1/Downloads/ev3/
scp -r robotdownsizing/*py robot@"$1":~/robotdownsizing
