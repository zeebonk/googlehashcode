.PHONY: main logo right_angle learn_and_teach clean

main: logo right_angle learn_and_teach

logo:
	python3 main.py data/logo.in $(ALGO) > data/logo.out

right_angle:
	python3 main.py data/right_angle.in $(ALGO) > data/right_angle.out

learn_and_teach:
	python3 main.py data/learn_and_teach.in $(ALGO) > data/learn_and_teach.out

clean:
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
