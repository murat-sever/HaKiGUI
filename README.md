# HaKiGUI
## Config Dosyası Adları: 
* narrowConf.conf
* wideConf.conf
* ismConf.conf

## Config Dosya Dizini: `/home/.config/gqrx`

## Gui'nin Otomatik Açılması İçin Yapılması Gerekenler:
* Terminalde 'gnome-session-properties' yazılır.
* Add butonuna basılır ve Command kısmına 'sh *path/to/GUI*/autoStart.sh' yazılır 
* "autoStart.sh" dosyasının içi, Gui dosyasının dizinine göre düzenlenir.

## Yüklenmesi Gereken Araçlar
1) ### "xdotool" aracı aşağıdaki şekilde kurulabilir:
* sudo apt-get update
* sudo apt-get install xdotool
2) ### "dump-1090" aşağıdaki şekilde kurulabilir:
* Github reposundan "dump-1090" indirilir.
* İndirilen dizine girilir ve "make" komutu çalıştırılır.
* Proje dizininin içindeki "launchDump.sh" dosyasının içindeki path, indirilen "dump-1090" pathine göre düzenlenir.

## Tam Ekran Modu İçin Yapılması Gerekenler
* Taskbar'a sağ tıklanır ve "Panel Settings" seçilir.
* Açılan pencerede "Advanced"e tıklanır ve "Minimize panel when not in use" seçeneği işaretlenir.
