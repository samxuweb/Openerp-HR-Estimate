from openerp.osv import osv, fields

class ProjectManagement(osv.Model):
	_name = "hrestimate.projectmanagement"

	_columns = {
		'test' : fields.char(string="Test", size=256, required=True),
	}