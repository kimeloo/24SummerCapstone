from static import rm0708
from admin_page.models import UserAccount
def refresh_recommendations():
    users = UserAccount.objects.all()
    for user in users:
        rm0708.main(user.id)