def display_gif(fn):
    return '<img src="{}">'.format(fn)


def test_question_1(clusters):
    if clusters == 4:
        print("That's right!  There are 4 clusters in this dataset.")
    elif clusters < 4:
        print("Oops!  We were thinking there were actually more clusters than what you suggested. Try again.  A cluster is a group of points that are closer together and separated from other points in the dataset.")
    else:
        print("Oops!  We were thinking there were fewer clusters than what you suggested. Try again.  A cluster is a group of points that are closer together and separated from other points in the dataset.")


def test_question_2(clusters):
    if clusters == 2:
        print("That's right!  There are 2 clusters in this dataset.")
    else:
        print("Oops!  That doesn't look like what we expected for the number of clusters.  Try again.  A cluster is a group of points that are closer together and separated from other points in the dataset.")

def test_question_3(clusters):
    print("{} is a reasonable guess for a the number of clusters here.  In the next question, you will see a different angle of this data.".format(clusters))

def test_question_4(clusters):
    print("This data is actually the same as the data used in question 3.  Isn't it crazy how looking at data from a different angle can make us believe there are a different number of clusters in the data!  We will look at how to address this in the upcoming parts of this lesson.")
    return display_gif('http://www.reactiongifs.com/wp-content/uploads/2013/03/mind-blown.gif')
