DTB = am335x-lgtc-wireless.dtb \
      am335x-lgtc-wired.dtb

KERNEL := $(HOME)/src/linux/linux-stable

CPP = /usr/bin/cpp

DTC := $(KERNEL)/scripts/dtc/dtc

CPP_FLAGS = 	-nostdinc \
		-I$(KERNEL)/arch/arm/boot/dts \
		-I$(KERNEL)/arch/arm/boot/dts/include \
		-x assembler-with-cpp \
		-undef -D__DTS__

DTC_FLAGS =	-i$(KERNEL)/arch/arm/boot/dts \
		-b 0 -@
		#-Wno-unit_address_vs_reg

all: $(DTB)

%.dts.tmp: %.dts
	$(CPP) $(CPP_FLAGS) -o $@ $<

%.dtb: %.dts.tmp
	$(DTC) $(DTC_FLAGS) -O dtb -o $@ $<

%.d: %.dts
	$(CPP) $(CPP_FLAGS) -Wp,-MD,$@.pre.tmp -o $(patsubst %.d,%.dts.tmp,$@) $<
	$(DTC) $(DTC_FLAGS) -d $@.dtc.tmp -O dtb -o /dev/null $(patsubst %.d,%.dts.tmp,$@)
	sed -e 's/^.*:/$(patsubst %.d,%.dts.tmp,$@):/' $@.pre.tmp > $@
	sed -e 's/^.*:/$(patsubst %.d,%.dtb,$@):/' $@.dtc.tmp >> $@
	rm $@.pre.tmp $@.dtc.tmp $(patsubst %.d,%.dts.tmp,$@)

clean:
	rm -f *.dtb *.dts.tmp

include $(patsubst %.dtb,%.d,$(DTB))

.PHONY: all clean
