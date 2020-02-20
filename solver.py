import copy

from reader_writer import reader_writer


def read_file(file_name):
    pass

class Solver():
    def __init__(self, file_name):
        self.file_name = file_name
        self.reader_writer = reader_writer()
        self.best_score = 0
        self.best_choices = None
        self.total_books, self.total_libraries, self.total_days, self.books_dict, self.libraries_dict = self.reader_writer.read_data(self.file_name + '.txt')

    def solve_problem(self):
        libraries_choices = {}
        books_scanned = set()
        score_so_far = 0
        best_choices, best_score = self.solve(self.total_days, libraries_choices, books_scanned, score_so_far)
        print('\tsolved with score: ' + str(best_score))
        self.reader_writer.write_solution(file_name + '_solution.txt', best_choices, best_score)

    def solve(self, days_left, libraries_choices, books_scanned, score_so_far):
        best_score = 0
        best_inputs = None
        for library_index in range(self.total_libraries):
            register_days = self.libraries_dict[library_index]['register_days']
            inputs = []
            if library_index not in libraries_choices.keys() and register_days < days_left:
                library_choices, library_score = self.library_choice_and_score(library_index, days_left, books_scanned)
                new_libraries_choices = copy.deepcopy(libraries_choices)
                new_libraries_choices[library_index] = library_choices
                new_books_scanned = copy.deepcopy(books_scanned)
                new_books_scanned.update(library_choices)
                inputs.append(days_left-register_days)
                inputs.append(new_libraries_choices)
                inputs.append(new_books_scanned)
                inputs.append(score_so_far+library_score)
                if inputs[3] > best_score:
                    best_score = inputs[3]
                    best_inputs = copy.deepcopy(inputs)
        if best_inputs is not None and score_so_far < best_inputs[3]:
            return self.solve(best_inputs[0], best_inputs[1], best_inputs[2], best_inputs[3])
        else:
            return libraries_choices, score_so_far

    def library_choice_and_score(self, library_index, days_left, books_scanned):
        library_choices = set()
        days_left = days_left - self.libraries_dict[library_index]['register_days']
        books_capacity = days_left * self.libraries_dict[library_index]['book_per_day']
        for book in self.libraries_dict[library_index]['books']:
            if books_capacity == 0:
                break
            if book not in books_scanned:
                library_choices.add(book)
                books_capacity -= 1
        library_score = self.calculate_score(library_choices)
        return library_choices, library_score

    def calculate_score(self, library_choices):
        score = 0
        for book in library_choices:
            score += self.books_dict[book]
        return score
file_names = ['a_example', 'b_read_on', 'c_incunabula' ,'d_tough_choices' ,'e_so_many_books' ,'f_libraries_of_the_world']
for file_name in file_names:
    print('Starting to solve: ' + file_name)
    solver = Solver(file_name)
    solver.solve_problem()
