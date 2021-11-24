def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 62, "metric_value": 0.9236, "depth": 2}
		if obj[2]<=15:
			# {"feature": "Education", "instances": 59, "metric_value": 0.8874, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>15:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[2]>4:
			# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[2]<=4:
			return 'False'
		else: return 'False'
	else: return 'False'
