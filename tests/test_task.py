from datetime import timedelta
import datetime
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

# The CI will run these tests after all the modules are installed,
# not right after installing the one defining it.
@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super(EstateTestCase, cls).setUpClass()

        # create the data for each tests. By doing it in the setUpClass instead
        # of in a setUp or in each test case, we reduce the testing time and
        # the duplication of code.
        cls.properties = cls.env['task'].create({'user_id': 2, 'name': 'Demo Task', 'description': 'Demo task description',
        'duration': 4, 'status': 'draft'})

    def test_creation_task(self):
        """Test that the task is created like it should."""
        self.properties.stop = datetime.datetime.now() + timedelta(days=self.properties.duration)
        self.assertRecordValues(self.properties, [
           {'user_id': 2, 'name': 'Demo Task', 'description': 'Demo task description', 'duration': 4, 'status': 'draft'},
        ])


    def test_action_progress(self):
        """Test that everything behaves like it should when scheduling a task."""
        self.properties.action_progress()
        self.assertRecordValues(self.properties, [
           {'status': 'in_progess',},
        ])
    
    def test_action_complete(self):
        """Test that everything behaves like it should when done with a task."""
        self.properties.action_complete()
        self.assertRecordValues(self.properties, [
           {'status': 'complete'},
        ])
    
#    def test_autopost_expired_entries(self):
#        self.assertEqual(self.properties._autopost_expired_entries()),[{'status': 'expired'}])
