def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 67, "metric_value": 0.9986, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 51, "metric_value": 0.9864, "depth": 3}
			if obj[2]<=17:
				return 'True'
			elif obj[2]>17:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[2]>7:
				return 'False'
			elif obj[2]<=7:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 60, "metric_value": 0.9007, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 40, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=12:
				return 'True'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[2]>4:
				return 'True'
			elif obj[2]<=4:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
