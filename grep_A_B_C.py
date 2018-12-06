string_to_search=input("Enter the String: ")
before=int(input("How many lines to print before string match ? "))
after=int(input("How many lines to print before string match ? "))
file_to_search=input("Enter the file to search: ")

def search_string(string_to_search, before, after, file_to_search):
	with open(file_to_search) as f:
		all_lines = f.readlines()
		for current_lineno, current_line in enumerate(all_lines):
			if string_to_search in current_line:
				start_line_no = max(current_lineno - before, 0)
				end_line_no=current_lineno + 1
				break
		for i in range(start_line_no, end_line_no):print(all_lines[i])
		for i in range(end_line_no, end_line_no+after):print(all_lines[i])
search_string(string_to_search, before, after, file_to_search)
