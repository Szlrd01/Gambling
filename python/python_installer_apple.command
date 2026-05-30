clear

if command -v python3 &>/dev/null; then
    goto_install=true
else
    goto_install=false
fi

if [ "$goto_install" = false ]; then
    curl -L -o python_mac.pkg python.org
    if [ ! -f python_mac.pkg ]; then exit 1; fi
    
    sudo installer -pkg python_mac.pkg -target /
    rm python_mac.pkg
fi

python3 -m pip install --upgrade pip
python3 -m pip install colorama
echo "Kesz! Nyomj meg egy gombot a kilepeshez..."
read -n 1