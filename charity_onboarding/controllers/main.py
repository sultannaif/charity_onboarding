from odoo import http
from odoo.http import request

class CharityOnboarding(http.Controller):

    @http.route('/beneficiary/onboarding', type='http', auth="user", website=True)
    def onboarding_form(self, **post):
        return request.render('charity_onboarding.onboarding_page_template')

    @http.route('/beneficiary/onboarding/submit', type='http', auth="user", methods=['POST'], website=True)
    def onboarding_submit(self, **post):
        # جمع المهارات المختارة من المصفوفة إلى نص مفصول بفاصلة
        skills_list = request.httprequest.form.getlist('skills')
        skills_text = ", ".join(skills_list)
        
        request.env.user.partner_id.write({
            'birth_date': post.get('birth_date'),
            'trainee_status': post.get('trainee_status'),
            'assigned_path': post.get('path'), # المسار الذي طلبه في النموذج
            'selected_skills': skills_text,
            'onboarding_status': 'pending',
            'is_beneficiary': True
        })
        return request.redirect('/slides')
