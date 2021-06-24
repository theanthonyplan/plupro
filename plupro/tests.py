from django.test import TestCase
from .models import Proposal, ProposalLine, ProposalLineCategory, ProposalLineItem


class ProposalTest(TestCase):
    """ Test module for Proposal model """

    def setUp(self):
        Proposal.objects.create(
            name='Casper', phone_number="323-241-1122", customer_name='Bull Dog', terms_and_conditions='Stuff to follow..')
        Proposal.objects.create(
            name='Jasper', phone_number="423-241-1772", customer_name='Classy Platypus', terms_and_conditions='Stuff to follow..')


    def test_proposal_name(self):
        proposal_casper = Proposal.objects.get(name='Casper')
        proposal_muffin = Proposal.objects.get(name='Jasper')
        self.assertEqual(
            proposal_casper.phone_number, "323-241-1122")
        self.assertEqual(
            proposal_muffin.phone_number, "423-241-1772")
