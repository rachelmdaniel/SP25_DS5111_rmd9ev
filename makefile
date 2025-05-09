default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

ygainers.html:
	google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=10000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	/home/ubuntu/SP25_DS5111_rmd9ev/env/bin/python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=60000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	/home/ubuntu/SP25_DS5111_rmd9ev/env/bin/python3 -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

normalize:
	/home/ubuntu/SP25_DS5111_rmd9ev/env/bin/python3 get_gainer.py $(SRC)

gainers:
	@echo "Processing gainers for source: $(SRC)"
	@if [ "$(SRC)" = "yahoo" ]; then \
		make ygainers.csv; \
		make normalize SRC=yahoo; \
	elif [ "$(SRC)" = "wsj" ]; then \
		make wsjgainers.csv; \
		make normalize SRC=wsj; \
	else \
		echo "Invalid SRC value. Use 'yahoo' or 'wsj'."; \
		exit 1; \
	fi

clean:
	rm -f ygainers.html ygainers.csv wsjgainers.html wsjgainers.csv

lint:
	- pylint get_gainer.py bin/gainers/*.py bin/normalize_csv.py || true

test: lint
	pytest -vv tests

