clear

sudo apt update
sudo apt install -y python3 python3-pip python3-venv

python3 -m pip install --upgrade pip --break-system-packages 2>/dev/null || python3 -m pip install --upgrade pip
python3 -m pip install colorama --break-system-packages 2>/dev/null || python3 -m pip install colorama

echo "Sikeres telepites Linuxon!"
read -p "Nyomj Enter-t a kilepeshez..."