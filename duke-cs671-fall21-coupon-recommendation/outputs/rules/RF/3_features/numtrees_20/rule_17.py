def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Coupon", "instances": 29, "metric_value": 0.9294, "depth": 3}
			if obj[0]>3:
				return 'False'
			elif obj[0]<=3:
				return 'False'
			else: return 'False'
		elif obj[2]>20:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=6:
				return 'False'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
