grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades: " , grades


def print_grades(gradez):
    for grade in gradez:
        print grade
print "-----------------"
print_grades(grades)

print "Let's compute some stats!"

def grades_sum(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum

print grades_sum(grades)

def grades_average(scores):
    return grades_sum(scores)/float(len(scores))

print "average is: ", grades_average(grades)

print "Time to conquer the variance!"

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) **2

    return variance/float(len(scores))

print "variance is: ", grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5 

variance = grades_variance(grades)

print "standard deviation is: ", grades_std_deviation(variance)

print grades_std_deviation(grades_variance(grades))
