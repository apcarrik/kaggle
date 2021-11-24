def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>20:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
