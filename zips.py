midterms = [80,91,71]
finals = [98,89,53]
students = ['bear', 'cat', 'lynsay']

#result = [max(pair) for pair in zip(midterms, finals)]

##result = {t[0]:max(t[1], t[2]) for t in zip(students,midterms, finals)}
##
##print(result)
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades)
