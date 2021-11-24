def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Education", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>12:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=10:
				return 'True'
			elif obj[2]>10:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
