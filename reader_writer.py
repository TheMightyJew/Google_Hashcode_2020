class reader_writer():

    def write_solution(self, file_path, dict_result, score):
        file = open(file_path, "w")
        file.write(str(len(dict_result)) + '\n')
        for library_id in dict_result.keys():
            lib_num = str(library_id)
            lib_books = dict_result[library_id]
            size = len(lib_books)
            size = str(size)
            lib_books = (' '.join(map(str, lib_books)))
            file.write(lib_num + " " + size + '\n' + lib_books + '\n')
        file.write('Score: ' + str(score) + '\n')
        file.close()
        return

    def read_file(self, file_path):
        file = open(file_path, "r")
        file_list = file.read().split("\n")
        file.close()
        return file_list

    def sort_by_score(self, line, scores):
        dict = {}
        for book in line:
            dict[book] = scores[book]
        new_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1],reverse=True)}
        line = list(new_dict.keys())
        return line

    def makedict(self, file,book_score_dict):
        dict={}
        lib_index_key=0
        for i in range(0,len(file)-1,2):
            if len(file[i]) == 0:
                break
            line1=file[i].split(" ")
            line2=file[i+1].split(" ")
            lib={}
            lib['book_num']=int(line1[0])
            lib['register_days']=int(line1[1])
            lib['book_per_day']=int(line1[2])
            line2 = list(map(int, line2))
            line2 = self.sort_by_score(line2,book_score_dict)
            lib['books']=line2
            dict[lib_index_key]=lib
            lib_index_key+=1
        return dict

    def read_data(self, file_path):
        file = self.read_file(file_path)
        total_books,total_libraries,total_days=file[0].split(" ")
        total_books=int(total_books)
        total_libraries=int(total_libraries)
        total_days=int(total_days)
        list_keys=list(range(total_books))
        list_values=file[1].split(" ")
        list_values = list(map(int, list_values))
        book_score_dict=dict(zip(list_keys,list_values))
        libraries_dict = self.makedict(file[2:],book_score_dict)
        return total_books, total_libraries, total_days, book_score_dict, libraries_dict