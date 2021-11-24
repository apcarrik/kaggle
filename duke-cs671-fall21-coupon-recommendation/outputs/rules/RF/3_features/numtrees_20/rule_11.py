def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 39, "metric_value": 0.7793, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.6343, "depth": 3}
			if obj[2]<=7:
				return 'True'
			elif obj[2]>7:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=10:
				return 'False'
			elif obj[2]>10:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
