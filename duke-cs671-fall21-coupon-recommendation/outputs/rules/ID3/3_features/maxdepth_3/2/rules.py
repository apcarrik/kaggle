def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4734, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 5886, "metric_value": 0.4676, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 3339, "metric_value": 0.4766, "depth": 3}
			if obj[2]<=13.375765736941226:
				return 'True'
			elif obj[2]>13.375765736941226:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 2547, "metric_value": 0.4545, "depth": 3}
			if obj[2]<=19.23922327259529:
				return 'True'
			elif obj[2]>19.23922327259529:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2261, "metric_value": 0.4837, "depth": 2}
		if obj[2]>2.0328104328662784:
			# {"feature": "Education", "instances": 1794, "metric_value": 0.4892, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=2.0328104328662784:
			# {"feature": "Education", "instances": 467, "metric_value": 0.4388, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
