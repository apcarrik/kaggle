def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 28, "metric_value": 0.9059, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[2]<=23:
				return 'False'
			elif obj[2]>23:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]<=12:
				return 'False'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[2]<=15:
			# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=1:
				return 'True'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[2]>15:
			return 'False'
		else: return 'False'
	else: return 'True'
