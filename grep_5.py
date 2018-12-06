string_to_search=input("Enter the String: ")
before=int(input("How many lines to print before string match ? "))
after=int(input("How many lines to print after string match ? "))
file_to_search=input("Enter the file to search: ")

def search_string(string_to_search, before, after, file_to_search):
	with open(file_to_search) as f:
		all_lines = f.readlines()
		last_line_number=len(all_lines)
		for current_line_no, current_line in enumerate(all_lines):
			if string_to_search in current_line:
				start_line_no=max(current_line_no - before, 0)
				end_line_no=min(last_line_number, current_line_no+after+1)
				for i in range(start_line_no, current_line_no):print(all_lines[i])				
				for i in range(current_line_no, end_line_no):print(all_lines[i])
				break
search_string(string_to_search, before, after, file_to_search)