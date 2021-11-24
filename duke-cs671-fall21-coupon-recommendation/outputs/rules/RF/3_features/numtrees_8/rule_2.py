def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9671, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 108, "metric_value": 0.9357, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 107, "metric_value": 0.9303, "depth": 3}
			if obj[1]<=4:
				return 'True'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=19:
				return 'False'
			elif obj[2]>19:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
