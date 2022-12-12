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
### "xdotool" aracı aşağıdaki şekilde yüklenebilir:
* sudo apt-get update
* sudo apt-get install xdotool

## Tam Ekran Modu İçin Yapılması Gerekenler
* Taskbar'a sağ tıklanır ve "Panel Settings" seçilir.
* Açılan pencerede "Advanced"e tıklanır ve "Minimize panel when not in use" seçeneği işaretlenir.
