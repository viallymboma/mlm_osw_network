from django.db import models
from django.contrib.auth.models import User
from apps.user_accounts.models import ClientsTable, SubadminTable

# Create your models here.
# Here we define the settings of the app as well as the 
# commissions and their different settings
# these value will be used in the transaction or operation
# models in operation app

PACKAGES = (
    ("Bronze", "Bronze"),
    ("Silver", "Silver"),
    ("Gold", "Gold"),
    ("Titanium", "Titanium"),
    ("Titanium Pro", "Titanium Pro"),
    ("Diamond", "Diamond"),
    ("Diamond Pro", "Diamond Pro"),
    ("Presidential", "Presidential"),
)

RANKS = (
    ("Leader", "Leader"),
    ("Coordinator", "Coordinator"),
    ("Manager", "Manager"),
    ("1-Star Manager", "1-Star Manager"),
    ("2-Star Manager", "2-Star Manager"),
    ("3-Star Manager", "3-Star Manager"),
    ("4-Star Manager", "4-Star Manager"),
    ("Director", "Director"),
    ("1-Star Director", "1-Star Director"),
    ("2-Star Director", "2-Star Director"),
    ("3-Star Director", "3-Star Director"),
    ("Prime Minister", "Prime Minister"),
    ("President", "President"),
    ("Senior President", "Senior President"),
)

# RANK_PRIZES = (

# )

COMP_PLAN = (
    ("Retail", "Retail"),
    ("Activation", "Activation"),
    ("Referral", "Referral"),
    ("Team Lead", "Team Lead"),
    ("Income Position", "Income Position"),
    ("Marching", "Marching"),
    ("Business Meeting", "Business Meeting"),
    ("Life Changing", "Life Changing"),
)

COUNTRY = (
    ("Ghana", "Ghana"),
    ("Nigeria", "Nigeria"),
    ("Cameroon", "Cameroon"),
    ("Ivory Coast", "Ivory Coast"),
    ("Togo", "Togo"),
)


RETAIL_PRICES = (
    ("172.00", "172.00"),
    ("342.00", "342.00"),
    ("1,365.00", "1,365.00"),
)

WHOLESALE_PRICES = (
    ("132.00", "132.00"),
    ("263.00", "263.00"),
    ("1,050.00", "1,050.00"),
)

RETAIL_PROFIT = (
    (40.00, 40.00),
    (79.00, 79.00),
    (315.00, 315.00),
)

STATUS = (
    ("Used", "Used"),
    ("Unused", "Unused"),
    # ("Suspend", "Suspend"),
)

USED_FOR = (
    ("Activation", "Activation"),
    ("Repurchase", "Repurchase"),
)

class Packages (models.Model):
    package_name = models.CharField(max_length=100, choices=PACKAGES, blank=False, null=False, unique=True)
    personal_volume = models.IntegerField(blank=True, null=True, default=0, help_text="Personal volume attached", unique=True)
    dollar_amount = models.IntegerField(blank=True, null=True, default=0, help_text="Dollar Amount attached", unique=True)
    cedis_amount = models.IntegerField(blank=True, null=True, default=0, help_text="Cedis Amount attached", unique=True)
    naira_amount = models.IntegerField(blank=True, null=True, default=0, help_text="Naira Amount attached")
    products_quantity = models.IntegerField(blank=True, null=True, default=0, help_text="Quantity of Product upon registration")

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.package_name
    
    def returnID (self):
        return id

# class Rank (models.Model):


class Rank (models.Model):
    rank_name = models.CharField(max_length=255, choices=RANKS, unique=True)
    pv = models.FloatField(blank=True, null=True, unique=True, default=0, help_text="Needed Personal Volume for eligibility")
    lesser_team_volume = models.FloatField(blank=True, null=True, unique=True, default=0, help_text="Volume from the leg built by me")
    sponsor_team_volume = models.FloatField(blank=True, null=True, unique=True, default=0, help_text="Volume from the leg built by upliner")
    max_cummulative_leg = models.FloatField(blank=True, null=True, unique=True, default=0, help_text="Maximum pv needed per on person in a leg")
    earning_in_cedis = models.FloatField(blank=True, null=True, unique=True, default=0, help_text="Maximum pv needed per on person in a leg")
    prizes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.rank_name


class CompensationPlan (models.Model):
    name = models.CharField(max_length=255, unique=True)
    percentage = models.IntegerField(blank=True, null=True, default=0, help_text="Percentage")
    condition = models.CharField(max_length=255, unique=True)

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.name


class Product (models.Model):
    product_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    wholesale_price = models.IntegerField(choices=WHOLESALE_PRICES, blank=True, null=True, help_text="Proce sold by company")
    retail_price = models.IntegerField(choices=RETAIL_PRICES, blank=True, null=True, help_text="retail price")
    # retail_profit = models.IntegerField(choices=RETAIL_PROFIT, blank=True, null=True, help_text="Fixed Line")
    available_quantity = models.IntegerField(blank=True, null=True, default=0, help_text="total quantity of this articles")

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.product_name


class RetailCommission (models.Model):
    retail_name = models.CharField(max_length=255, unique=True)
    bonus_type = models.ForeignKey(CompensationPlan, null=False, blank=False, on_delete=models.CASCADE, related_name="comp_plan_retail")
    product_quantity = models.IntegerField(blank=True, null=True, default=0, help_text="Percentage")
    # product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name="retail_product")
    percentage = models.IntegerField(blank=True, null=True, default=0, help_text="Percentage")
    # retail_profit = models.IntegerField(choices=RETAIL_PROFIT, blank=True, null=True, help_text="retail profit")
    condition = models.CharField(max_length=255, unique=True)
    reward = models.CharField(max_length=255, unique=True)

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.name


class ActivationCommission (models.Model):
    activation_name = models.CharField(max_length=255, unique=True)
    bonus_type = models.ForeignKey(CompensationPlan, null=False, blank=False, on_delete=models.CASCADE, related_name="comp_plan_activation")
    package = models.ForeignKey(Packages, null=False, blank=False, on_delete=models.CASCADE, related_name="pack_activation_com")
    # product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name="admin")
    product_quantity = models.IntegerField(blank=True, null=True, default=0, help_text="Percentage")
    percentage = models.IntegerField(blank=True, null=True, default=0, help_text="Percentage")
    # retail_profit = models.IntegerField(choices=RETAIL_PROFIT, blank=True, null=True, help_text="retail profit")
    condition = models.CharField(max_length=255, unique=True)
    reward = models.CharField(max_length=255, unique=True)

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.activation_name


class ReferralCommission (models.Model):
    ref_name = models.CharField(max_length=255, unique=True)
    bonus_type = models.ForeignKey(CompensationPlan, null=False, blank=False, on_delete=models.CASCADE, related_name="comp_plan_referral")
    package = models.ForeignKey(Packages, null=False, blank=False, on_delete=models.CASCADE, related_name="pack_referral_com")
    # product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name="admin")
    percentage = models.IntegerField(blank=True, null=True, default=0, help_text="Percentage")
    # retail_profit = models.IntegerField(choices=RETAIL_PROFIT, blank=True, null=True, help_text="retail profit")
    condition = models.CharField(max_length=255, unique=True)
    reward = models.CharField(max_length=255, unique=True)

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.ref_name


class TokenCreationHelper(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number = models.IntegerField(blank=True, null=True, default=0, help_text="token_number_helper")

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.name



class BronzeEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Bronze')

class SilverEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Silver')

class GoldEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Gold')

class TitaniumEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Titanium')

class TitaniumProEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Titanium Pro')

class DiamondEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Diamond')

class DiamondProEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Diamond Pro')

class PresidentialEpinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(package='Presidential')
    
    def get_subadmin(self, subadmin):
        return super().get_queryset().filter(for_subadmin=self.subadmin)


class Epins (models.Model):
    e_pin = models.CharField(max_length=100, choices=PACKAGES, blank=False, null=False, unique=True)
    country = models.CharField(max_length=1000, choices=COUNTRY, blank=True, null=True)
    package = models.ForeignKey(Packages, null=False, blank=False, on_delete=models.CASCADE, related_name="admin")
    payement_transaction_proof = models.IntegerField(blank=True, null=True, default=0, help_text="Transaction ID", unique=True)
    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="created_by")
    for_subadmin = models.ForeignKey(SubadminTable, null=False, blank=False, on_delete=models.CASCADE, related_name="subadmin")
    used_by = models.ForeignKey(ClientsTable, blank=True, null=True, on_delete=models.CASCADE, default=0, help_text="Personal volume attached")
    used_for = models.CharField(max_length=10, choices=USED_FOR, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, blank=False, null=False, default="Unused")
    # iba = models.IntegerField(blank=True, null=True, default=0, help_text="Cedis Amount attached", unique=True)
    # naira_amount = models.IntegerField(blank=True, null=True, default=0, help_text="Naira Amount attached", unique=True)
    # products_quantity = models.IntegerField(blank=True, null=True, default=0, help_text="Quantity of Product upon registration")

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    all_epins = models.Manager()
    bronze = BronzeEpinManager()
    # usage example: Epins.bronze.all()
    silver = SilverEpinManager()
    gold = GoldEpinManager()
    titanium = TitaniumEpinManager()
    titanium_pro = TitaniumProEpinManager()
    diamond = DiamondEpinManager()
    diamond_pro = DiamondProEpinManager()
    prisidential = PresidentialEpinManager()

    def __str__(self):
        return self.e_pin















