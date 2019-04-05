set:
	python3.6 main.py special KnNaA >special_base
	python3.6 main.py special KcCbB >special_expand
	sudo mv special_base /usr/share/X11/xkb/symbols/
	sudo mv special_expand /usr/share/X11/xkb/symbols/
	sudo setxkbmap -layout special_base,special_expand -option grp:rctrl_switch
