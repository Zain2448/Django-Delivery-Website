from allauth.account.adapter import DefaultAccountAdapter

class NoNewUserAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False


