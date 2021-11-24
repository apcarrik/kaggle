def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[0]>2:
			return 'True'
		elif obj[0]<=2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 2}
		if obj[2]>5:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]>3:
				return 'True'
			elif obj[0]<=3:
				return 'True'
			else: return 'True'
		elif obj[2]<=5:
			return 'False'
		else: return 'False'
	else: return 'True'
