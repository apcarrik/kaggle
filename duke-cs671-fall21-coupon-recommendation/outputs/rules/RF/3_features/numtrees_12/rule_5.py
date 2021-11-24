def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[2]<=7:
		# {"feature": "Coupon", "instances": 47, "metric_value": 0.9252, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 32, "metric_value": 0.9887, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>7:
		# {"feature": "Education", "instances": 38, "metric_value": 0.9678, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.999, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[0]>2:
				return 'False'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
