from openerp.osv import osv, fields

class mechanical(osv.Model):
	_name = "mechanical"

	def _gap_lead(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_lead - i.x_lead_system_me_load
		return res

	def _gap_senior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_senior - i.optimal_senior
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'project_complexity' : fields.selection([
			('High','High'),
			('Medium','Medium'),
			('Low','Low')],'Project functional complexity ',required=True),
		'x_lead_system_me_load' : fields.related('project_id','x_lead_system_me_load',type='float',string='Optimal Lead',readonly=True),
		'optimal_senior' : fields.float('Optimal Senior'),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior'),
		'projected_junior' : fields.float('Projected Junior'),
		'gap_lead' : fields.function(_gap_lead,string='Gap Lead',type='float'),
		'gap_senior' : fields.function(_gap_senior,string='Gap Senior',type='float'),
		'gap_junior' : fields.function(_gap_junior,string='Gap Junior',type='float'),
		'remaining_duration' : fields.integer('Remaining duration of the project (in mos)'),
	}

class electronic(osv.Model):
	_name = "electronic"

	def _gap_lead(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_lead - i.x_lead_ee_load
		return res

	def _gap_senior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_senior - i.optimal_senior
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'project_complexity' : fields.selection([
			('High','High'),
			('Medium','Medium'),
			('Low','Low')],'Project functional complexity ',required=True),
		'x_lead_ee_load' : fields.related('project_id','x_lead_ee_load',type='float',readonly=True,string='Optimal Lead'),
		'optimal_senior' : fields.float('Optimal Senior'),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior'),
		'projected_junior' : fields.float('Projected Junior'),
		'gap_lead' : fields.function(_gap_lead,string='Gap Lead',type='float'),
		'gap_senior' : fields.function(_gap_senior,string='Gap Senior',type='float'),
		'gap_junior' : fields.function(_gap_junior,string='Gap Junior',type='float'),
		'remaining_duration' : fields.integer('Remaining duration of the project (in mos)'),
	}

class system(osv.Model):
	_name = "system"

	def _gap_lead(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_lead - i.x_lead_se_load
		return res

	def _gap_senior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_senior - i.optimal_senior
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'project_complexity' : fields.selection([
			('High','High'),
			('Medium','Medium'),
			('Low','Low')],'Project functional complexity ',required=True),
		'x_lead_se_load' : fields.related('project_id','x_lead_se_load',type='float',readonly=True,string='Optimal Lead'),
		'optimal_senior' : fields.float('Optimal Senior'),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior'),
		'projected_junior' : fields.float('Projected Junior'),
		'gap_lead' : fields.function(_gap_lead,string='Gap Lead',type='float'),
		'gap_senior' : fields.function(_gap_senior,string='Gap Senior',type='float'),
		'gap_junior' : fields.function(_gap_junior,string='Gap Junior',type='float'),
		'remaining_duration' : fields.integer('Remaining duration of the project (in mos)'),
	}

class software(osv.Model):
	_name = "software"

	def _gap_lead(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_lead - i.x_lead_swe_load
		return res

	def _gap_senior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_senior - i.optimal_senior
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'project_complexity' : fields.selection([
			('High','High'),
			('Medium','Medium'),
			('Low','Low')],'Project functional complexity ',required=True),
		'x_lead_swe_load' : fields.related('project_id','x_lead_swe_load',type='float',readonly=True,string='Optimal Lead'),
		'optimal_senior' : fields.float('Optimal Senior'),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior'),
		'projected_junior' : fields.float('Projected Junior'),
		'gap_lead' : fields.function(_gap_lead,string='Gap Lead',type='float'),
		'gap_senior' : fields.function(_gap_senior,string='Gap Senior',type='float'),
		'gap_junior' : fields.function(_gap_junior,string='Gap Junior',type='float'),
		'remaining_duration' : fields.integer('Remaining duration of the project (in mos)'),
	}

class tpl(osv.Model):
	_name = "tpl"

	def _gap_lead(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_lead - i.optimal_lead
		return res

	def _gap_senior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_senior - i.optimal_senior
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'project_complexity' : fields.selection([
			('High','High'),
			('Medium','Medium'),
			('Low','Low')],'Project functional complexity ',required=True),
		'optimal_lead' : fields.float('Optimal Lead'),
		'optimal_senior' : fields.float('Optimal Senior'),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior'),
		'projected_junior' : fields.float('Projected Junior'),
		'gap_lead' : fields.function(_gap_lead,string='Gap Lead',type='float'),
		'gap_senior' : fields.function(_gap_senior,string='Gap Senior',type='float'),
		'gap_junior' : fields.function(_gap_junior,string='Gap Junior',type='float'),
		'remaining_duration' : fields.integer('Remaining duration of the project (in mos)'),
	}

