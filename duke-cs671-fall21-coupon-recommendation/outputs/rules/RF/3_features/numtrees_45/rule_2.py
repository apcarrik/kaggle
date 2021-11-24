def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.65, "depth": 2}
		if obj[2]<=9:
			return 'True'
		elif obj[2]>9:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
