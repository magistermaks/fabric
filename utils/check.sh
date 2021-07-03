#!/bin/bash

exceptions=`cat exceptions.dict`

cd ../

function print_error {
	while read -r data; do
		if [[ "$exceptions" != *$data* ]]; then
			echo -e "\033[0;31merror:\033[0m ${data}"
			echo $data >> errors.txt
		fi
  	done
}

function check_file {
	# I tried with `awk '{gsub(/(``)?\`.*?\`(``)?/,"");}1'` but it didn't work
	echo $file_path | xargs cat | python3 -c "import sys;import re;print(re.sub(r'(\`\`)?\`.*?\`(\`\`)?','',sys.stdin.read(),flags=re.S))" | aspell --lang=en_US list | tr [A-Z] [a-z] | sort | uniq | print_error
}

find -name "*.md" | while read file_path;
	do echo -e "\n\033[1;36m${file_path}\033[0m" && check_file $file_path;
done

errors=$(cat errors.txt | sort | uniq | wc -l)

rm errors.txt
echo -e "\nFound ${errors} unique errors."

if [[ $errors > 0 ]]; then
	exit 1
else
	exit 0
fi

