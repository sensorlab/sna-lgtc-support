DTB = am335x-lgtc-wireless.dtb \
      am335x-lgtc-wired.dtb

KERNEL := $(HOME)/src/linux/linux-stable

CPP = /usr/bin/cpp

DTC := $(KERNEL)/scripts/dtc/dtc

CPP_FLAGS = 	-nostdinc \
		-I . \
		-I$(KERNEL)/arch/arm/boot/dts \
		-I$(KERNEL)/arch/arm/boot/dts/include \
		-x assembler-with-cpp \
		-undef -D__DTS__

DTC_FLAGS =	-i$(KERNEL)/arch/arm/boot/dts \
		-b 0 -@
		#-Wno-unit_address_vs_reg

all: $(DTB)

-include $(DTB:.dtb=.d)

%.dtb: %.dts
	$(CPP) $(CPP_FLAGS) -Wp,-MD,$<.pre.d -o $<.pre $<
	$(DTC) $(DTC_FLAGS) -d $<.dtc.d -O dtb -o $@ $<.pre
	sed -e 's/^.*:/$@:/;s/\.dts\.pre/.dts/g' $<.pre.d $<.dtc.d > $(@:.dtb=.d)
	rm $<.pre.d $<.dtc.d $<.pre

clean:
	rm -f *.dtb *.dts.tmp

.PHONY: all clean
