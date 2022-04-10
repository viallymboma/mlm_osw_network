from django.db import models
from apps.network_settings.models import Packages
from apps.user_accounts.models import ClientsTable, SubadminTable
from apps.network_settings.models import (
    Packages, Rank, CompensationPlan, Product, 
    RetailCommission, ActivationCommission, 
    TokenCreationHelper, Epins, ReferralCommission
)
from django.contrib.auth.models import User

# Create your models here.

# When someone Registers activation commission is triggered 
# and the persons PV is ogmented based on the package 
# they have choosen 

# After registration completed, user will be saved here along with his:
# epin, the package he choose, and all the ret of things related to him
# especially his bonus and pv and amount in dollars ghana cedis and naira
# date when it will be paid from the time it was activated

class ActivationCommissionTransaction (models.Model):
    trans_token_id = models.CharField(max_length=255, null=False, blank=False, unique=True)
    activation_epin = models.ForeignKey(Epins, null=False, blank=False, on_delete=models.CASCADE, related_name="activation_epins")
    activ_commission = models.ForeignKey(ActivationCommission, null=False, blank=False, on_delete=models.CASCADE, related_name="activate_com_t")
    iba = models.ForeignKey(ClientsTable, null=False, blank=False, on_delete=models.CASCADE, related_name="iba_client")
    package = models.ForeignKey(Packages, null=False, blank=False, on_delete=models.CASCADE, related_name="activ_com_pack")
    # The country will be determined in and saved by the code based on the user at hand
    country = models.CharField(max_length=1000, blank=True, null=True)
    # this will be calculated in the code and saved in the below field
    activation_profit = models.IntegerField(blank=True, null=True, help_text="activation profit")

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)


class ReferralCommissionTransaction (models.Model):
    # activation_epin = models.ForeignKey(Epins, null=False, blank=False, on_delete=models.CASCADE, related_name="activation_epins")
    trans_token_id = models.CharField(max_length=255, null=False, blank=False, unique=True)
    iba = models.ForeignKey(ClientsTable, null=False, blank=False, on_delete=models.CASCADE, related_name="iba_receiving_bonus")
    downliner = models.ForeignKey(ClientsTable, null=False, blank=False, on_delete=models.CASCADE, related_name="iba_giving_bonus")
    package = models.ForeignKey(Packages, null=True, blank=True, on_delete=models.CASCADE, related_name="ref_com_pack")
    referral_commission = models.ForeignKey(ReferralCommission, null=False, blank=False, on_delete=models.CASCADE, related_name="referral_com_t")
    pv_assigned_to_upliner = models.IntegerField(blank=False, null=False, help_text="corresponding e-pin")
    # country = models.CharField(max_length=1000, choices=COUNTRY, blank=False, null=False)
    activation_profit = models.IntegerField(blank=True, null=True, help_text="activation profit")

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)


























# class ProductRetailTransaction (models.Model):
#     repurchase_epin = models.ForeignKey(Epins, null=True, blank=False, on_delete=models.CASCADE, related_name="prod_repurchase_epins")
#     # here i call him client because both the iba and the client can do this operation
#     client = models.ForeignKey(ClientsTable, null=False, blank=False, on_delete=models.CASCADE, related_name="client_prod_retail")
#     # country = models.CharField(max_length=1000, blank=False, null=False)
#     # this will be calculated in the code and saved in the below field
#     activation_profit = models.IntegerField(blank=True, null=True, help_text="activation profit")

#     date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
#     date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

# class ProductActivationTransaction (models.Model):
#     activation_epin = models.ForeignKey(Epins, null=True, blank=True, on_delete=models.CASCADE, related_name="prod_activation_epins")
#     # Here i call him iba because only the iba can do this operation
#     iba = models.ForeignKey(ClientsTable, null=False, blank=False, on_delete=models.CASCADE, related_name="iba_prod_activitation")
#     # The country will be determined in and saved by the code based on the user at hand
#     # country = models.CharField(max_length=1000, blank=False, null=False)
#     # this will be calculated in the code and saved in the below field
#     activation_profit = models.IntegerField(blank=True, null=True, help_text="activation profit")

#     date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
#     date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)


# class RetailCommissionTransaction (models.Model):
#     repurchase_epin = models.ForeignKey(Epins, null=False, blank=False, on_delete=models.CASCADE, related_name="repurchase_epins")
#     client = models.ForeignKey(ClientsTable, null=False, blank=False, on_delete=models.CASCADE, related_name="retail_client")
#     # The country will be determined in and saved by the code based on the user at hand
#     country = models.CharField(max_length=1000, blank=False, null=False)
#     # this will be calculated in the code and saved in the below field
#     retail_profit = models.IntegerField(blank=True, null=True, help_text="retail profit")

#     date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
#     date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)






# COUNTRY = (
#     ("Ghana", "Ghana"),
#     ("Nigeria", "Nigeria"),
#     ("Cameroon", "Cameroon"),
#     ("Ivory Coast", "Ivory Coast"),
#     ("Togo", "Togo"),
# )

# STATUS = (
#     ("Used", "Used"),
#     ("Unused", "Unused"),
#     # ("Suspend", "Suspend"),
# )

# USED_FOR = (
#     ("Activation", "Activation"),
#     ("Repurchase", "Repurchase"),
# )

# class BronzeEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Bronze')

# class SilverEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Silver')

# class GoldEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Gold')

# class TitaniumEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Titanium')

# class TitaniumProEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Titanium Pro')

# class DiamondEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Diamond')

# class DiamondProEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Diamond Pro')

# class PresidentialEpinManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(package='Presidential')
    
#     def get_subadmin(self, subadmin):
#         return super().get_queryset().filter(for_subadmin=self.subadmin)

# class Epins (models.Model):
#     e_pin = models.CharField(max_length=100, choices=PACKAGES, blank=False, null=False, unique=True)
#     country = models.CharField(max_length=1000, choices=COUNTRY, blank=False, null=False)
#     package = models.ForeignKey(Packages, null=False, blank=False, on_delete=models.CASCADE, related_name="admin")
#     payement_transaction_proof = models.IntegerField(blank=True, null=True, default=0, help_text="Transaction ID", unique=True)
#     created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="created_by")
#     for_subadmin = models.ForeignKey(SubadminTable, null=False, blank=False, on_delete=models.CASCADE, related_name="subadmin")
#     used_by = models.ManyToManyField(ClientsTable, blank=True, null=True, default=0, help_text="Personal volume attached", unique=True)
#     used_for = models.CharField(max_length=10, choices=USED_FOR, blank=True, null=True)
#     status = models.CharField(max_length=10, choices=STATUS, blank=False, null=False, default="Unused")
#     # iba = models.IntegerField(blank=True, null=True, default=0, help_text="Cedis Amount attached", unique=True)
#     # naira_amount = models.IntegerField(blank=True, null=True, default=0, help_text="Naira Amount attached", unique=True)
#     # products_quantity = models.IntegerField(blank=True, null=True, default=0, help_text="Quantity of Product upon registration")

#     date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
#     date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

#     all_epins = models.Manager()
#     bronze = BronzeEpinManager()
#     # usage example: Epins.bronze.all()
#     silver = SilverEpinManager()
#     gold = GoldEpinManager()
#     titanium = TitaniumEpinManager()
#     titanium_pro = TitaniumProEpinManager()
#     diamond = DiamondEpinManager()
#     diamond_pro = DiamondProEpinManager()
#     prisidential = PresidentialEpinManager()

#     def __str__(self):
#         return self.e_pin











