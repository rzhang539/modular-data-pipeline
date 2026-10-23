from pydantic import BaseModel, model_validator 

class raw_data_cleanup(BaseModel):

    user_id: int 
    tenure_months: int
    monthly_charges: float
    total_support_tix: int
    is_churned: int 

    @model_validator(mode='before')
    @classmethod
    def data_check(cls, data: dict) -> dict:

        user_id_actual = data.get("user_id") or data.get("account_id")
        if user_id_actual in ['NA', 'na', 'N/A', 'n/a', None, 'null', 'Null']:
            raise ValueError("Invalid user_id")
        if not isinstance(user_id_actual, int): 
            try:
                user_id_actual = int(user_id_actual)
            except:
                raise ValueError("Invalid user_id")

        tenure_month_actual = data.get("tenure_months") or data.get("months_active") 
        if tenure_month_actual in ['NA', 'na', 'N/A', 'n/a', None, 'null', 'Null']:
            raise ValueError("Invalid tenure_month")
        if not isinstance(tenure_month_actual, int):
            try:
                tenure_month_actual = int(tenure_month_actual)
            except: 
                raise ValueError("Invalid tenure_month")

        monthly_charges_actual = data.get("monthly_charges")
        if monthly_charges_actual in ['NA', 'na', 'N/A', 'n/a', None, 'null', 'Null']:
            raise ValueError("Invalid monthly charge")       
        if not isinstance(monthly_charges_actual, float):
            try:
                monthly_charges_actual = float(monthly_charges_actual)
            except:
                raise ValueError("Invalid monthly charge")
        if monthly_charges_actual < 0:
            raise ValueError("Invalid monthly charge: cannot be negative")

        support_tix_actual = data.get("total_support_tickets")
        if support_tix_actual in ['NA', 'na', 'N/A', 'n/a', None, 'null', 'Null']:
            raise ValueError("Invalid total_support_tickets")       
        if not isinstance(support_tix_actual, int):
            try: 
                support_tix_actual = int(support_tix_actual)
            except:
                raise ValueError("Invalid total_support_tickets")    
        if support_tix_actual < 0:
            raise ValueError("Invalid total_support_tickets: cannot be negative")

        is_churned_actual = data.get("is_churned")
        if is_churned_actual in ['NA', 'na', 'N/A', 'n/a', None, 'null', 'Null']:
            raise ValueError("Invalid is_churn")
        if not isinstance(is_churned_actual, int):
            try:
                is_churned_actual = int(is_churned_actual)
            except:
                raise ValueError("Invalid is_churn")
        if is_churned_actual not in (0,1):
            raise ValueError("Invalid is_churn: must be 0 or 1")

        return {
            "user_id": user_id_actual,
            "tenure_months": tenure_month_actual,
            "monthly_charges": monthly_charges_actual, 
            "total_support_tix": support_tix_actual,
            "is_churned": is_churned_actual
        }

