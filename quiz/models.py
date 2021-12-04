from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField
# from django.core.validators import MaxValueValidator, MinValueValidator


STATUS = ((0, "Draft"), (1, "Approved"))


class Category(models.Model):
    """Create category"""

    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Set pluaral name for Category"""
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Question(models.Model):
    """Create a question"""

    body = models.TextField(max_length=350, unique=True)
    # option1 = models.CharField(max_length=200)
    # option2 = models.CharField(max_length=200)
    # option3 = models.CharField(max_length=200, blank=True)
    # option4 = models.CharField(max_length=200, blank=True)
    # option5 = models.CharField(max_length=200, blank=True)
    # option6 = models.CharField(max_length=200, blank=True)
    # key = models.IntegerField(help_text='Correct answer',
    #                           validators=[MaxValueValidator(6), 
    #                           MinValueValidator(1)])
    category = models.ManyToManyField(Category,
                                      related_name='question')
    # slug = models.SlugField(max_length=70, unique=True)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    list_filter = 'category'
    search_fields = ('category')

    class Meta:
        """Ordering for questions"""
        ordering = ['id']

    def __str__(self):
        # return f'Question id: {self.question.id} / category: {self.category}'
        return self.body


# Code adapted from:
# https://stackoverflow.com/questions/47867760/django-quiz-app-model-for-multiple-choice-questions#47867939
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.PROTECT)
    option = models.CharField("option", max_length=50)
    position = models.IntegerField("position")
    is_correct = models.BooleanField(default=False)
    feedback_correct = models.CharField(max_length=200, default='You are correct!')
    feedback_incorrect = models.CharField(max_length=220, default='Sorry, you got this wrong.')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            # no duplicated option per question
            ("question", "option"),
            # no duplicated position per question
            ("question", "position")
        ]
        ordering = ["position"]
        verbose_name_plural = 'Answer options'

    def __str__(self):
        return self.option


class QuestionOptions(models.Model):
    """Create question_options object"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    category = models.ManyToManyField(Category)
    correct_answer = models.IntegerField()

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return f'{self.question}'


class Quiz(models.Model):
    """Create a quiz"""

    title = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(Category,
                                 related_name='quiz')
    # slug = models.SlugField(max_length=200, unique=True)
    prepopulated_fields = {"slug": ("title",)}
    description = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder',
                                     blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    """Create quiz_question link"""

    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT,
                             related_name='quiz_question')
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.quiz)} - {str(self.question)}'


class Assessment(models.Model):
    """Crate assessment"""

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='assessment')
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quiz}-{self.user}'


class Answers(models.Model):
    """Create user answer"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answered_question')
    answer = models.IntegerField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE,
                                   related_name='answers')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return f'{self.assessment}-{self.question}-{self.answer}'