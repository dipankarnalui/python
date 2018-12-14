marker_today="marker123"
result = "cat /tmp/abcd.conf | grep -o '{}.*' | cut -f1 -d'}}'"
print(result.format(marker_today))