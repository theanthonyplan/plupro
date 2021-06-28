from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from .models import UserProfile
from .api.serializers import UserSerializer



class TestUserProfileSignals(TestCase):
    """
    Test db signals for UserProfile model.
    """
    def setUp(self):
        # create a user
        self.user = User.objects.create(first_name='Brian', last_name='Fellows', email='BrianFellows@safariplanet.com', username='BryFel')
        # create any other objects you will need


    def test_user_profile_post_save(self):
        p1 = User.objects.filter(username='BryFel')[0] # get our user profie that was created with the user
        assert p1 is not None                               # sanity check
        up1 = p1.userprofile
        assert up1 is not None                              # sanity check

        print(up1)
        up1.phone_number = 7
        up1.title = 'gagafa'
        up1.city = 'Montreal'
        up1.save()

        up1.refresh_from_db()
        self.assertEqual(up1.phone_number, '7')
        self.assertEqual(up1.title, 'gagafa')
        self.assertEqual(up1.city, 'Montreal')

class TestUserProfileAPI(TestCase):
    """
    Test the DRF viewsets and serializers for UserProfile model.
    """
    def setUp(self):
        # use the DRF API testing client
        self.client = APIClient()
        # create a user
        self.user = User.objects.create(first_name='Brian', last_name='Fellows', email='BrianFellows@safariplanet.com', username='BryFel')
        self.user2 = User.objects.create(first_name='Brian2', last_name='Fellows2', email='Brian2Fellows2@safariplanet.com', username='Bry2Fel2')
        self.user3 = User.objects.create(first_name='Brian3', last_name='Fellows3', email='Brian3Fellows3@safariplanet.com', username='Bry3Fel3')
        # force auth
        self.client.force_authenticate(user=self.user)

        # create any extra objects/data we will need for testing
        self.user_id = self.user.id                               # save our user id for later
        self.user.userprofile.title = 'masfaf'                     # update a title
        self.user.userprofile.save()                               # and save it

        self.user2.userprofile.is_active = False                   # set profile 2 to be inactive
        self.user2.userprofile.save()                              # and save it

    def test_get_user_profile(self):
        """
        Create two objects, test the number returned by user-profile-list query.
        """
        # Build a url to retrieve all objects
        url = reverse('account-api:user-profile-list', args=())
        # GET a response
        res = self.client.get(url, data={})
        # Make sure the response is OK
        self.assertEqual(res.status_code, 200)
        # Assert that 3 objects were created and returned
        self.assertEqual(len(res.data), 3)

        # Build a url to get a specific user profile
        url = reverse('account-api:user-profile-detail', args=(self.user_id,))
        res = self.client.get(url, data={})
        self.assertEqual(res.status_code, 200)                                    # make sure we only have 1 response
        self.assertEqual(res.data['title'], 'masfaf')                             # check that we have data access and that its valid




    def test_create_user_profile(self):
        """
        Create an object, GET its list, make sure only 1 is returned.
        """
        # get rid of the user profile for user2
        self.user2.userprofile.delete()

        user_profile_data = {
                "title": "title_here",
                "city": "cityplace",
                "country": "countryland",
                "phone_number": 1235554214,
                "is_active": True,
                "user": self.user2.id
        }


        # Make sure we have 2 instances
        self.assertEqual(UserProfile.objects.all().count(), 2)
        # build the url
        url = reverse('account-api:user-profile-list', args=())
        # POST a request and get a response to create a new profile
        res = self.client.post(url, data=user_profile_data)
        # Make sure the response is OK
        self.assertEqual(res.status_code, 201)
        # Assert that we have 3 profiles
        self.assertEqual(UserProfile.objects.all().count(), 3)


    def test_update_user_profile(self):
        """
        Create an object, check it. Update it. Check again.
        """
        # prepare data
        user_profile_data = {
            "title": "title_here",
            "city": "cityplace",
            "country": "countryland",
            "phone_number": 1235554214,
            "is_active": True,
            "user": self.user3.id
        }
        # Here we are starting out with 3 instances in the DB
        self.assertEqual(UserProfile.objects.all().count(), 3)
        # build the url
        url = reverse('account-api:user-profile-detail', args=(self.user3.id,))
        # get the data
        res = self.client.put(url, data=user_profile_data,format='json')
        print("URL: {}".format(url))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['title'], 'title_here')                       # check that we have data access and that its valid
