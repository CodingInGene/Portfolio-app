from core.models import VisitorInfo, ProjectVisitInfo

def site_visits(req):
    '''
    1st - proxy ip, 2nd - fall back if 1st not used(without proxy). Split in-case user using proxy and returns multiple ip
    '''
    ip_addr = req.META.get('HTTP_X_FORWARDED_FOR', req.META.get('REMOTE_ADDR')).split(',')[0]
    user_agent = req.META.get("HTTP_USER_AGENT", "unknown")

    if ip_addr:
        # Check user
        existing = VisitorInfo.objects.filter(ip_address=ip_addr).exists()

        if not existing:
            # Store
            new_user = VisitorInfo(ip_address=ip_addr)
            if user_agent:
                new_user.user_agent = user_agent

            new_user.save()

def project_visits(req, project_obj):
    '''
    1st - proxy ip, 2nd - fall back if 1st not used(without proxy). Split in-case user using proxy and returns multiple ip
    '''
    ip_addr = req.META.get('HTTP_X_FORWARDED_FOR', req.META.get('REMOTE_ADDR')).split(',')[0]
    user_agent = req.META.get("HTTP_USER_AGENT", "unknown")

    if ip_addr:
        # Check user
        existing = ProjectVisitInfo.objects.filter(ip_address=ip_addr).exists()

        if not existing:
            # Store
            new_user = ProjectVisitInfo(project=project_obj, ip_address=ip_addr)
            if user_agent:
                new_user.user_agent = user_agent

            new_user.save()