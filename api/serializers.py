from rest_framework import serializers

from api.models import *

# ----------------------------------------------------------------
# ACCOUNT SERIALIZERS
# ----------------------------------------------------------------

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# APPEARANCE SERIALIZERS
# ----------------------------------------------------------------

class AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# SOCIAL SERIALIZERS
# ----------------------------------------------------------------

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        
           
# ----------------------------------------------------------------
# CALENDAR SERIALIZERS
# ----------------------------------------------------------------

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'
        
# ----------------------------------------------------------------
# COMPANYINFO SERIALIZERS
# ----------------------------------------------------------------

class CompanyInfoSerializer(serializers.ModelSerializer):
    id_social = SocialSerializer(required=False)
    
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        
class CompanyInfoPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyInfo
        fields = '__all__'
        

        
# ----------------------------------------------------------------
# IMAGE SERIALIZERS
# ----------------------------------------------------------------

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# CARD SERIALIZERS
# ----------------------------------------------------------------

class CardSerializer(serializers.ModelSerializer):
    
    id_social = SocialSerializer(required=False)
    id_appearance = AppearanceSerializer(required=False)
    id_account = AccountSerializer(required=False)
    id_company_info = CompanyInfoSerializer(required=False)
    id_appearance = AppearanceSerializer(required=False)
    
    class Meta:
        model = Card
        fields = '__all__'
        
class CardSerializerByLink(serializers.ModelSerializer):
    
    id_social = SocialSerializer(required=False)
    id_appearance = AppearanceSerializer(required=False)
    # id_account = AccountSerializer(required=False)
    id_company_info = CompanyInfoSerializer(required=False)
    id_appearance = AppearanceSerializer(required=False)
    
    
    class Meta:
        model = Card
        fields = '__all__'
        
class CardPOSTSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = '__all__'
        
# ----------------------------------------------------------------
# PORTFOLIO SERIALIZERS
# ----------------------------------------------------------------

class PortfolioSerializer(serializers.ModelSerializer):
    # id_card = CardSerializer(required=False)
    class Meta:
        model = Portfolio
        fields = '__all__'
        
class PortfolioPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
    
        
# ----------------------------------------------------------------
# Subscription SERIALIZERS
# ----------------------------------------------------------------
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        

# ----------------------------------------------------------------
# Subscription SERIALIZERS
# ----------------------------------------------------------------
class UserSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubsctibe
        fields = ['id_subscription', 'price', 'card_count']