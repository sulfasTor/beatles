curl -s -L https://www.calaveras-literarias.com/seccion/$1/page/[1-50:1] | grep --color -o "www.calaveras-literarias.com/$1/.*class" | sed 's/ class//g'
