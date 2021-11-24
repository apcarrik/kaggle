def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]<=20:
		# {"feature": "Coupon", "instances": 49, "metric_value": 0.9486, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 34, "metric_value": 0.8338, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>20:
		return 'False'
	else: return 'False'
