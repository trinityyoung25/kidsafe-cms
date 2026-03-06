from django.test import TestCase
from cms.models import Content

class ContentIntegrationTest(TestCase):

    def test_content_approval(self):
        content = Content.objects.create(
            title="Science Video",
            description="Science lesson",
            url="https://youtube.com"
        )

        content.approved = True
        content.save()

        self.assertTrue(content.approved)
