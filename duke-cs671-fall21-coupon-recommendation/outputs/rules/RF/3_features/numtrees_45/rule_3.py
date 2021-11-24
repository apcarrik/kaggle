def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>6:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>3:
		return 'False'
	else: return 'False'
