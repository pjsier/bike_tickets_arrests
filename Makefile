pdf_arrests = Documents_for_P062407_part_2.pdf
pdf_tickets = Documents_for_P062407.pdf
tabula_args_arrests = 53.0,49.0,739.97,560.02
tabula_args_tickets = 89.123,80.325,727.133,528.615

all: output/bike_arrests.csv output/bike_tickets.csv
	python3 join_geocoding.py

output/bike_%.csv: output/bike_%_temp.csv
	perl -ne 'print if $$. == 1 || /^\d/' $< > $@

.INTERMEDIATE: output/bike_%_temp.csv
output/bike_%_temp.csv: output/bike_%.pdf tabula-java.jar
	java -jar tabula-java.jar -a $(tabula_args_$*) -p all -o $@ $<

output/bike_%.pdf:
	wget -O $@ https://cdn.muckrock.com/foia_files/2017/06/29/$(pdf_$*)

tabula-java.jar:
	wget -O $@ https://github.com/tabulapdf/tabula-java/releases/download/0.9.2/tabula-0.9.2-jar-with-dependencies.jar

.PHONY: clean

clean:
	rm output/bike*
