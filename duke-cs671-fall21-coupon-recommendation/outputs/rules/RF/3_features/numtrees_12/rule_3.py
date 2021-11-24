def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=8:
		# {"feature": "Education", "instances": 57, "metric_value": 0.9348, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 54, "metric_value": 0.951, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]>8:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.8631, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 25, "metric_value": 0.9044, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
