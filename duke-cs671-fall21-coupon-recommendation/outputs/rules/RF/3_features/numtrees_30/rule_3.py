def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9612, "depth": 2}
		if obj[2]<=16:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]>16:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]>3:
				return 'False'
			elif obj[2]<=3:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
