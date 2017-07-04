all: output/bike_arrests.csv output/bike_tickets.csv

output/bike_arrests.csv: output/bike_arrests.pdf
	java -jar tabula-java.jar -a 53.0,49.0,739.97,560.02 -p all -o output/bike_arrests_temp.csv output/bike_arrests.pdf && \
	head -n 1 output/bike_arrests_temp.csv > output/bike_arrests.csv && sed -e 1d output/bike_arrests_temp.csv | grep "^\d" >> output/bike_arrests.csv && \
	rm output/bike_arrests_temp.csv

output/bike_tickets.csv: output/bike_tickets.pdf
	java -jar tabula-java.jar -a 89.123,80.325,727.133,528.615 -p all -o output/bike_tickets_temp.csv output/bike_tickets.pdf && \
	head -n 1 output/bike_tickets_temp.csv > output/bike_tickets.csv && sed -e 1d output/bike_tickets_temp.csv | grep "^\d" >> output/bike_tickets.csv && \
	rm output/bike_tickets_temp.csv

output/bike_arrests.pdf: tabula-java.jar
	wget -O output/bike_arrests.pdf https://cdn.muckrock.com/foia_files/2017/06/29/Documents_for_P062407_part_2.pdf

output/bike_tickets.pdf: tabula-java.jar
	wget -O output/bike_tickets.pdf https://cdn.muckrock.com/foia_files/2017/06/29/Documents_for_P062407.pdf

tabula-java.jar:
	wget -O tabula-java.jar https://github.com/tabulapdf/tabula-java/releases/download/0.9.2/tabula-0.9.2-jar-with-dependencies.jar
