from unittest import TestCase, SkipTest


class ExamplesSmokeTestCase(TestCase):
    """
    These are just basic tests that run each example
    to make sure no errors are triggered.
    """

    def test_basic_example(self):
        from examples import basic_example # NOQA

    def test_default_response_example(self):
        from examples import default_response_example # NOQA

    def test_export_example(self):
        raise SkipTest(
            'This is being skipped to avoid '
            'creating files durring tests.'
        )

    def test_gitter_example(self):
        raise SkipTest(
            'This is being skipped because keys for this '
            'API are not included in the public repository.'
        )

    def test_hipchat_bot(self):
        raise SkipTest(
            'This is being skipped because keys for this '
            'API are not included in the public repository.'
        )

    def test_learning_feedback_example(self):
        raise SkipTest(
            'This is being skipped because it contains '
            'a while loop in the code body and will not '
            'terminate on its own.'
        )

    def test_mailgun_example(self):
        raise SkipTest(
            'This is being skipped because keys for this '
            'API are not included in the public repository.'
        )

    def test_math_and_time(self):
        from examples import math_and_time # NOQA

    def test_microsoft_bot(self):
        raise SkipTest(
            'This is being skipped because keys for this '
            'API are not included in the public repository.'
        )

    def test_specific_response_example(self):
        from examples import specific_response_example # NOQA

    def test_terminal_example(self):
        raise SkipTest(
            'This is being skipped because it contains '
            'a while loop in the code body and will not '
            'terminate on its own.'
        )

    def test_terminal_mongo_example(self):
        raise SkipTest(
            'This is being skipped so that we do not have '
            'to check if Mongo DB is running before running '
            'this test.'
        )

    def test_tkinter_gui(self):
        raise SkipTest(
            'This is being skipped so that we do not open up '
            'a GUI durring testing.'
        )

    def test_twitter_training_example(self):
        raise SkipTest(
            'This is being skipped because keys for this '
            'API are not included in the public repository.'
        )

    def test_ubuntu_corpus_training_example(self):
        raise SkipTest(
            'This test is being skipped because it takes '
            'hours to download and train from this corpus.'
        )
