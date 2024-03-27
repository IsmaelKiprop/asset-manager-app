from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.contrib.auth import logout
from .models import CustomUser, InventoryItem, Expense, IntangibleAsset, Machinery, ComputerHardware, Furniture, Investment, FixedAsset, Contract, Savings, Budget, BankIntegration, Bill, FinancialGrowth
from .serializers import CustomUserSerializer, InventoryItemSerializer, ExpenseSerializer, IntangibleAssetSerializer, MachinerySerializer, HardwareSoftwareSerializer, FurnitureSerializer, InvestmentSerializer, FixedAssetSerializer, ContractSerializer, SavingsSerializer, BudgetSerializer, BankIntegrationSerializer, BillSerializer, FinancialReportSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            'user': CustomUserSerializer(user, context=self.get_serializer_context()).data,
            'token': token
        })

class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user:
            _, token = AuthToken.objects.create(user)
            serializer = CustomUserSerializer(user)
            # Include user's first name in the response data
            return Response({'user': serializer.data, 'token': token})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

class LogoutAPI(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        # Invalidate the user's token
        request.auth.delete()
        # Logout the user
        logout(request)
        return Response({'success': 'Successfully logged out'}, status=200)

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user

# Views for Inventory Management

class InventoryItemListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryItemDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

# Views for Expense Management

class ExpenseListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# Views for Intangible Assets

class IntangibleAssetListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = IntangibleAsset.objects.all()
    serializer_class = IntangibleAssetSerializer

class IntangibleAssetDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = IntangibleAsset.objects.all()
    serializer_class = IntangibleAssetSerializer

# Views for Machinery and Vehicles

class MachineryListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer

class MachineryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer


# Views for Hardware and Software

class HardwareSoftwareListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = ComputerHardware.objects.all()
    serializer_class = HardwareSoftwareSerializer

class HardwareSoftwareDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = ComputerHardware.objects.all()
    serializer_class = HardwareSoftwareSerializer

# Views for Furniture

class FurnitureListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

class FurnitureDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

# Views for Investments

class InvestmentListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

# Views for Fixed Assets

class FixedAssetListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = FixedAsset.objects.all()
    serializer_class = FixedAssetSerializer

class FixedAssetDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = FixedAsset.objects.all()
    serializer_class = FixedAssetSerializer

# Views for Contract Management

class ContractListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ContractDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

# Views for Financial Management

class ExpenseListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class SavingsListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer

class SavingsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer

class BudgetListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BankIntegrationListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = BankIntegration.objects.all()
    serializer_class = BankIntegrationSerializer

class BankIntegrationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = BankIntegration.objects.all()
    serializer_class = BankIntegrationSerializer

class BillListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class FinancialReportListAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = FinancialGrowth.objects.all()
    serializer_class = FinancialReportSerializer

class FinancialReportDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = FinancialGrowth.objects.all()
    serializer_class = FinancialReportSerializer
