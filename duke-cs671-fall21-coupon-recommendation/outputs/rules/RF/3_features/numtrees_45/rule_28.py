def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>10:
			return 'False'
		else: return 'False'
	else: return 'False'
