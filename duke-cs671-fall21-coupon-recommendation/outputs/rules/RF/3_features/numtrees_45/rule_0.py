def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]>4:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=4:
		# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
