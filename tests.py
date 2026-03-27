import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# Creating 10 unit tests
def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='Q1', points=-5)
    
    with pytest.raises(Exception):
        Question(title='Q1', points=200)

def test_create_choice_with_no_text():
    with pytest.raises(Exception):
        Question('')

def test_create_choice_with_long_text():
    with pytest.raises(Exception):
        Question('In sem justo, commodo ut, suscipit at, pharetra vitae, orci. Duis sapien nunc, ' \
        'commodo et, interdum suscipit, sollicitudin et, dolor. Pellentesque habitant morbi tristique ' \
        'senectus et netus et malesuada fames ac turpis egestas. Aliquam id dolor. Class aptent taciti ' \
        'sociosqu ad litora')

def test_set_correct_choices():
    question = Question(title='q1', max_selections=2)
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)
    choice3 = question.add_choice('c', False)
    choice4 = question.add_choice('d', True)

    question.set_correct_choices([choice2.id, choice4.id])
    assert not question.choices[0].is_correct
    assert question.choices[1].is_correct
    assert not question.choices[2].is_correct
    assert question.choices[3].is_correct

def test_correct_choices():
    question1 = Question(title='q1', max_selections=2)
    question1.add_choice('a', False)
    question1.add_choice('b', True)
    question1.add_choice('c', False)
    question1.add_choice('d', True)

    correct_choices = [choice for choice in question1.choices if choice.is_correct]
    assert len(correct_choices) == 2
    assert correct_choices[0].text == 'b'
    assert correct_choices[1].text == 'd'

def test_add_multiple_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)
    question.add_choice('d', True)

    assert len(question.choices) == 4
    assert question.choices[0].text == 'a'
    assert not question.choices[0].is_correct
    assert question.choices[1].text == 'b'
    assert question.choices[1].is_correct
    assert question.choices[2].text == 'c'
    assert not question.choices[2].is_correct
    assert question.choices[3].text =='d'
    assert question.choices[3].is_correct

def test_add_choice_with_empty_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', True)

def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', True)

    question.remove_all_choices()
    assert len(question.choices) == 0

def test_remove_choice_by_id():
    question = Question(title='q1')
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)

    question.remove_choice_by_id(choice1.id)
    assert len(question.choices) == 1
    assert question.choices[0].text == 'b'

def test_remove_choice_by_invalid_id():
    question = Question(title='q1')
    choice = question.add_choice('a', True)

    with pytest.raises(Exception):
        question.remove_choice_by_id('invalid_id')