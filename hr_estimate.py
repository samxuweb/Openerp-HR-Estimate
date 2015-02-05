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
			res[i.id] = i.projected_senior - i.x_system_me_load
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	def _project_complexity(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_process_type == 'A':
				i.project_complexity = 'High'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'B':
				i.project_complexity = 'Medium'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'C':
				i.project_complexity = 'Low'
				res[i.id] = str(i.project_complexity)
		return res 

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'x_process_type' : fields.related('project_id','x_process_type',type='selection',selection=[('A','A'),('B','B'),('C','C')],string="Process Type"),
		'project_complexity' : fields.function(_project_complexity,type='char',string="Project Functional Complexity"),
		'x_lead_system_me_load' : fields.related('project_id','x_lead_system_me_load',type='float',string='Optimal Lead',readonly=True),
		'x_system_me_load' : fields.related('project_id','x_system_me_load', readonly=True, type='float', string="Optimal Senior"),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior',),
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
			res[i.id] = i.projected_senior - i.x_ee_load
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	def _project_complexity(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_process_type == 'A':
				i.project_complexity = 'High'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'B':
				i.project_complexity = 'Medium'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'C':
				i.project_complexity = 'Low'
				res[i.id] = str(i.project_complexity)
		return res 

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'x_process_type' : fields.related('project_id','x_process_type',type='selection',selection=[('A','A'),('B','B'),('C','C')],string="Process Type"),
		'project_complexity' : fields.function(_project_complexity,type='char',string="Project Functional Complexity"),
		'x_lead_ee_load' : fields.related('project_id','x_lead_ee_load',type='float',readonly=True,string='Optimal Lead'),
		'x_ee_load' : fields.related('project_id','x_ee_load', readonly=True, type='float', string="Optimal Senior"),
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
			res[i.id] = i.projected_senior - i.x_se_load
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	def _project_complexity(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_process_type == 'A':
				i.project_complexity = 'High'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'B':
				i.project_complexity = 'Medium'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'C':
				i.project_complexity = 'Low'
				res[i.id] = str(i.project_complexity)
		return res 

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'x_process_type' : fields.related('project_id','x_process_type',type='selection',selection=[('A','A'),('B','B'),('C','C')],string="Process Type"),
		'project_complexity' : fields.function(_project_complexity,type='char',string="Project Functional Complexity"),
		'x_lead_se_load' : fields.related('project_id','x_lead_se_load',type='float',readonly=True,string='Optimal Lead'),
		'x_se_load' : fields.related('project_id','x_se_load', readonly=True, type='float', string="Optimal Senior"),
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
			res[i.id] = i.projected_senior - i.x_swe_load
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	def _project_complexity(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_process_type == 'A':
				i.project_complexity = 'High'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'B':
				i.project_complexity = 'Medium'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'C':
				i.project_complexity = 'Low'
				res[i.id] = str(i.project_complexity)
		return res 

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'x_process_type' : fields.related('project_id','x_process_type',type='selection',selection=[('A','A'),('B','B'),('C','C')],string="Process Type"),
		'project_complexity' : fields.function(_project_complexity,type='char',string="Project Functional Complexity"),
		'x_lead_swe_load' : fields.related('project_id','x_lead_swe_load',type='float',readonly=True,string='Optimal Lead'),
		'x_swe_load' : fields.related('project_id','x_swe_load', readonly=True, type='float', string="Optimal Senior"),
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
			res[i.id] = i.projected_senior - i.x_lead_se_load
		return res

	def _gap_junior(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = i.projected_junior - i.optimal_junior
		return res

	def _project_complexity(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr, uid, ids, context=context):
			if i.x_process_type == 'A':
				i.project_complexity = 'High'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'B':
				i.project_complexity = 'Medium'
				res[i.id] = str(i.project_complexity)
			if i.x_process_type == 'C':
				i.project_complexity = 'Low'
				res[i.id] = str(i.project_complexity)
		return res 

	_columns = {
		'project_id' : fields.many2one('project.project','Project',required=True),
		'x_process_type' : fields.related('project_id','x_process_type',type='selection',selection=[('A','A'),('B','B'),('C','C')],string="Process Type"),
		'project_complexity' : fields.function(_project_complexity,type='char',string="Project Functional Complexity"),
		'optimal_lead' : fields.float('Optimal Lead'),
		'x_lead_se_load' : fields.related('project_id','x_lead_se_load', readonly=True, type='float', string="Optimal Senior"),
		'optimal_junior' : fields.float('Optimal Junior'),
		'projected_lead' : fields.float('Projected Lead'),
		'projected_senior' : fields.float('Projected Senior'),
		'projected_junior' : fields.float('Projected Junior'),
		'gap_lead' : fields.function(_gap_lead,string='Gap Lead',type='float'),
		'gap_senior' : fields.function(_gap_senior,string='Gap Senior',type='float'),
		'gap_junior' : fields.function(_gap_junior,string='Gap Junior',type='float'),
		'remaining_duration' : fields.integer('Remaining duration of the project (in mos)'),
	}

