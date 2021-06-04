from django.db import models



# model for proposal objects
class Proposal(models.Model):
    # model field for the customer's name, should never be blank, max length of 60
    customer_name = models.CharField(blank=False, max_length=60)


    # this is how an object's name will be formatted
    def __str__(self):
            return self.customer_name
    # this is how an object will represent itself (as a string)
    def __repr__(self):
            return str("Proposal for " + self.customer_name)


# model for proposal category objects
class ProposalLineCategory(models.Model):
    # model field for the customer's name, should never be blank, max length of 60
    name = models.CharField(blank=False, max_length=60)

    class Meta:
        verbose_name_plural = "Proposal Line Categories"
    def __str__(self):
            return self.name
    # this is how an object will represent itself (as a string)
    def __repr__(self):
            return str("Category: " + self.name)



# model for proposal line objects
class ProposalLine(models.Model):
    # field for the number of units per line item.  default to one, should never be blank
    quantity = models.FloatField(blank=False, default=1.0)
    # field to override the default price of the line item object.  if blank, should be NULL
    override = models.FloatField(blank=True, null=True)
    #
    category = models.ForeignKey(ProposalLineCategory, null=True, on_delete=models.CASCADE)
    #
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Proposal Lines"

    # this is how an object will print its name (as a string)
    def __str__(self):
            return "Proposal {}: Line #{}".format(self,proposal, self.pk)
    # this is how an object will represent itself (as a string)
    def __repr__(self):
            return "Proposal {}: Line #{}".format(self,proposal, self.pk)




# model for proposal objects
# class ProposalLineItem(models.Model):
#     # model field for the customer's name, should never be blank, max length of 60
#     customer_name = models.CharField(blank=False, max_length=60)
