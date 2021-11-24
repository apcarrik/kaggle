def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.4751, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 5867, "metric_value": 0.4695, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 3831, "metric_value": 0.476, "depth": 3}
			if obj[2]<=19.12113309419569:
				return 'True'
			elif obj[2]>19.12113309419569:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 2036, "metric_value": 0.4536, "depth": 3}
			if obj[2]<=19.16456021452013:
				return 'True'
			elif obj[2]>19.16456021452013:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2281, "metric_value": 0.4847, "depth": 2}
		if obj[2]>2.070384793617607:
			# {"feature": "Education", "instances": 1816, "metric_value": 0.4893, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=2.070384793617607:
			# {"feature": "Education", "instances": 465, "metric_value": 0.4291, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
