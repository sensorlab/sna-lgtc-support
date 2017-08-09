DTB = am335x-lgtc-wireless.dtb

KERNEL := $(HOME)/src/linux/linux-stable

CPP = /usr/bin/cpp

DTC := $(HOME)/src/dtc/dtc

CPP_FLAGS = 	-nostdinc \
		-I$(KERNEL)/arch/arm/boot/dts \
		-I$(KERNEL)/arch/arm/boot/dts/include \
		-x assembler-with-cpp \
		-undef -D__DTS__

DTC_FLAGS =	-i$(KERNEL)/arch/arm/boot/dts \
		-b 0 -@ \
		-Wno-unit_address_vs_reg

all: $(DTB)

%.dts.tmp: %.dts
	$(CPP) $(CPP_FLAGS) -o $@ $<

%.dtb: %.dts.tmp
	$(DTC) $(DTC_FLAGS) -O dtb -o $@ $<

clean:
	rm -f *.dtb *.dts.tmp

.PHONY: all clean
