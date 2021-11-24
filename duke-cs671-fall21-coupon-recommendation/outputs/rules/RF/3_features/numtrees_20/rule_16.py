def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 37, "metric_value": 0.9353, "depth": 2}
		if obj[2]<=21:
			# {"feature": "Coupon", "instances": 36, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[2]>21:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[2]>5:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[0]>2:
				return 'False'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		elif obj[2]<=5:
			return 'True'
		else: return 'True'
	else: return 'False'
