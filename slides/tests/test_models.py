from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from slides.models import Slide, Question, Person, Help, Done


class TestModels(TestCase):
    def setUp(self):
        self.a_student = Person.objects.create_user("Niki", "niki@rocketu.com","password")
        self.a_slide = Slide.objects.create(name="mySlide")

    def test_slide(self):
        self.assertEqual(self.a_slide.name, "mySlide")

    def test_question(self):
        a_question = Question.objects.create(student=self.a_student, answered=False, text="what the heck")
        self.assertEqual(a_question.answered, False)
        self.assertEqual(a_question.text, "what the heck")

    def test_help(self):
        a_help = Help.objects.create(student=self.a_student, slide=self.a_slide, helped=False)
        self.assertFalse(a_help.helped)

    # def test_done(self):
    #     a_done = Done.objects.create(student=self.a_student, slide=self.a_slide, done=False)
    #     self.assertEqual(a_done.done)

class QuestionListTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.a_student = Person.objects.create_user("Niki", "niki@rocketu.com","password")
        self.a_slide = Slide.objects.create(name="mySlide")

    def test_question_response(self):
        response = self.c.get('/question/')
        self.assertEqual(response.status_code, 200)

    # def test_question_create(self):
    #     response = self.c.get(reverse('question_create'))
    #     self.assertEqual(response.status_code, 302)
    #
    #     self.c.login(username='test', password='test')
    #     response = self.c.get(reverse('question_create'))
    #     self.assertEqual(response.status_code, 200)

    # def test_question_template_context(self):
    #     Question.objects.create(student=self.a_student, answered=False, text="what the heck")
    #     Question.objects.create(student=self.a_student, answered=False, text="dang this is hard")
    #     response = self.c.get(reverse('question'))
    #     self.assertEqual(len(response.context['question']), 2)

# class StaticTest(TestCase):
#     def test_images(self):
#         abs_path = finders.find('static/img/Assets/Exclamation-HOLLOW.png')
#         self.assertTrue(staticfiles_storage.exists(abs_path))

