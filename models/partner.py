from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_beneficiary = fields.Boolean(string="مستفيد", default=False)
    onboarding_status = fields.Selection([
        ('none', 'لم يعبأ النموذج'),
        ('pending', 'انتظار المراجعة'),
        ('approved', 'تم الاعتماد')
    ], default='none', string="حالة الطلب")

    birth_date = fields.Date(string="تاريخ الميلاد")
    trainee_status = fields.Selection([
        ('unemployed', 'باحث عن عمل'),
        ('graduate', 'خريج'),
        ('student', 'طالب'),
        ('employee', 'موظف')
    ], string="حالة المتدرب")

    assigned_path = fields.Selection([
        ('office', 'المسار المكتبي'),
        ('technical', 'المسار الفني'),
        ('handicraft', 'المسار الحرفي')
    ], string="المسار المعتمد")

    selected_skills = fields.Text(string="المهارات المختارة")
