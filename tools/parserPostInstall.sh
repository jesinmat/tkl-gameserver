wget -O - https://api.github.com/repos/ahmet2mir/wildq/releases/latest | grep "browser_download_url.*linux.*tar.*" |  cut -d '"' -f 4 | wget -qi - && mkdir wildq && tar -zxvf wildq-*.tar.gz -C ./wildq && rm wildq-*.tar.gz
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
